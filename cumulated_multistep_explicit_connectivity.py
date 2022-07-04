import scipy.sparse
import numpy as np
from scipy.sparse import csc_matrix
import scipy.io



# ############################ INPUT PARAMETERS AND DEFINITIONS

# name input directory
findir = ''

# The list finname is the sequence of matrices we need (for M steps we should have M matrices in this sequence), they should be properly normalized as in the paper.
#
# FORWARD IN TIME (use F matrices, defined and normalized as in the paper):
# the first matrix on the finname list (ie. finname[0]) should be the one representing the dynamics from t_{0} to t_{1}. The second (ie. finname[1]) from t_{1} to t_{2}, etc.
#
# BACKWARD IN TIME (use B matrices, defined and normalized as in the paper):
# the first matrix on the finname list (ie. finname[0]) should be the one representing the dynamics from t_{M} to t_{M-1}. The second (ie. finname[1]) from t_{M-1} to t_{M-2}, etc.

finname = []


# Output path
foutpath = ''

# number nodes (we have to use the notation for which the first node is the 0, the second is the 1, etc.)
N = #insert

# number of steps
M = #insert

# L matrix sparse version (our definition)
L_s = csc_matrix(np.ones((N,N))-np.identity(N))

# verbose
verb = False



# ############################ READING AND ADDING FIRST MATRIX

print('READING AND SUMMING FIRST MATRIX \n')

# reading the first matrix as a list (the first matrix is the element [0] of the finname list)
list_mat0 = np.loadtxt(findir + finname[0], delimiter=" ")
num_links0 = np.shape(list_mat0)[0]

# converting from list to an initialized dense matrix the first matrix of our sequence 
mat0 = np.zeros((N,N))
for i in range(0,num_links0):
        mat0[int(list_mat0[i][0]),int(list_mat0[i][1])]=list_mat0[i][2]

# adding the first matrix to a sparse sum matrix  (corresponding to the sum of terms in the probability union)
sum_mat_s = csc_matrix(mat0)



# ############################ LOOPS FOR THE CALCULATION OF THE PROBABILITY UNION

# external loop over elements of the sum in the probability union (start from two because the first term is already summed)
for count_sum in range(2,M+1,1):

        if (verb==True):
                print( str(count_sum) + ' ==================================================== outer counter on the terms of the sum  \n')

        # product matrix (corresponds to the products of transition matrices and L matrices inside each term of the sum) initialized to identity
        prod_mat_s = csc_matrix(np.identity(N))

        # internal loop to make products for a single term of the sum (the last product is done out of the loop)
        for count_prod in range(count_sum,1,-1):

                if (verb==True):
                        print( str(count_prod) + ' ---------------------------- inner counter on the terms of the product \n')

                # reading the count_prod matrix as a list
                list_mat = np.loadtxt(findir + finname[count_prod-1], delimiter=" ")
                num_links = np.shape(list_mat)[0]
                
                # converting from list to an initialized dense matrix
                mat = np.zeros((N,N))
                for i in range(0,num_links):
                        mat[int(list_mat[i][0]),int(list_mat[i][1])]=list_mat[i][2]

                if (verb==True):
                        print('performing products \n')
                        
                # sparsing the matrix
                mat_s = csc_matrix(mat)
                                
                # row-column product among the mat and the previous product (i.e. prod_mat)
                prod_mat_s = mat_s * prod_mat_s
                
                # hadamard product among the L matrix and the last product
                prod_mat_s = L_s.multiply(prod_mat_s)

                if (verb==True):
                        print('products done, end inner loop \n')
                        
                                
        # performing the last row-column product with the first matrix (the first matrix is the element [0] of the finname list)
        prod_mat_s = csc_matrix(mat0) *  prod_mat_s
        
        # summing the final product to the sum_mat
        sum_mat_s = sum_mat_s +  prod_mat_s

        if (verb==True):
              print('sum to final matrix, end outer loop \n')
                        
        

# ############################ WRITE OUTPUT

print('DENSIFY FINAL MATRIX \n')

# dense version of sum_mat_s
sum_mat = sum_mat_s.todense()

print('WRITING OUTPUT \n')
        
# writing matrix sum_mat_s (i.e. the forward-in-time integrated multistep connectivity matrix for M steps)
f=open(foutpath,'w')
for i in range (0,N):
        for j in range (0,N):
                if sum_mat[i,j] > 0. :
                        f.write(str(i) + ' ' + str(j) + ' ' + str(sum_mat[i,j]) + '\n')
f.close()










                        
