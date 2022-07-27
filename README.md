# cumulated-net-conn

## Overview

The repository `cumulated-net-conn` contains the Python codes designed to compute cumulated explicit and implicit connectivity probabilities given a generic  directed, weighted & temporal network. When using this code, please acknowledge the authors by citing  [Ser-Giacomi et al. (2021)](#references).



## Index
This documentation is organized as follows:

- [Cumulated connectivity code](#cumulated-connectivity-code)
	- [Description](#description)
	- [Inputs](#inputs)
	- [Outputs](#outputs)
	
- [References](#references)



## Cumulated connectivity code

#### Description

- The codes called `cumulated_multistep_explicit_connectivity.py` and `cumulated_multistep_implicit_connectivity.py` provide cumulated explicit and implicit connectivity probabilities for every pair of nodes in any temporal, directed weighted network. For the mathematical derivation refer to [Ser-Giacomi et al. (2021)](#references). The calculation is performed as a sequence of sparse matrix products using the `scipy.sparse` library. 
- The file `toy_net_right.dat` is the adjacency matrix of the toy network of Figure 5 (panel b) of [Ser-Giacomi et al. (2021)](#references). 

#### Inputs

The main inputs to run the code are:

- A sequence of adjacency matrices file-names `finname` describing the snapshots of the temporal network analyzed. The format for any input matrix should be a list omitting null weights (as in `toy_net_right.dat`). In detail:
	- Each row of the list correspond to a link with non-zero weight.
	- The first element of a row is the origin node, the second is the destination node, the third is the weight of the link between them.
	- For the proper normalization of the weights (that should correspond to probabilities) refer to [Ser-Giacomi et al. (2021)](#references) and to the toy matrix `toy_net_right.dat` .
- The number of nodes `N` in the network.
- The maximum number of steps `M` considered (the minimum number is by default equal to 1).


#### Outputs

The output file is a single matrix expressed as a list (omitting null weights) in which each element *i,j* correspond to the connectivity probability from node *i* to node *j*.



## References

[[Ser-Giacomi et al. 2021]](https://journals.aps.org/pre/abstract/10.1103/PhysRevE.103.042309) Ser-Giacomi, E., et al. Explicit and implicit network connectivity: Analytical formulation and application to transport processes. *Physical Review E* 103, 042309 (2021)




