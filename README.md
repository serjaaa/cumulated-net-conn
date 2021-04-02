# cumulated-net-conn

## Overview

The repository `cumulated-net-conn` contains the Python codes designed to compute explicit and implicit cumulated connectivity probabilities given a generic temporal weighted network. When using this code, please acknowledge the authors by citing  [Ser-Giacomi et al. (2021)](#references).



## Index
This documentation is organized as follows:

- [Cumulated connectivity code](#cumulated-connectivity-code)
	- [Description](#description)
	- [Inputs](#inputs)
	- [Outputs](#outputs)
	
- [References](#references)



## Cumulated connectivity code

#### Description

The codes called `cumulated_multistep_explicit_connectivity.py` and `cumulated_multistep_implicit_connectivity.py` provides cumulated explicit and implicit connectivity probabilities for every pair of nodes in a temporal network. The calculation is performed as a sequence of sparse matrix products using the `scipy.sparse` library. 


#### Inputs

The main input files are:

- A sequence of adjacency matrices file names `finname` (matrices are written in list format) describing the snapshots of the temporal network analyzed.
- Then number of nodes `N` in the network.
- The maximum number of steps `M` allowed.


#### Outputs

The output file is a simple matrix expressed as a list (omitting null weights) in which each element *i,j* correspond to the connectivity probability from node *i* to node *j*.



## References

[[Ser-Giacomi et al. 2021]](https://www.nature.com/articles/s41559-018-0587-2) Ser-Giacomi, E.,  (2021). Explicit and implicit network connectivity: analytical formulation and application to transport processes. *Physical Review E*




