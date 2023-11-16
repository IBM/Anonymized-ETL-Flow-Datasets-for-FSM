# Anonymized ETL Flow Datasets for Frequent Subgraph Mining
## Datasets Overview
This repository consists an anonymized version of six datasets taken from IBM's [DataStage™](https://www.ibm.com/products/datastage) production systems and used for frequent subgraph mining in the paper [Refactoring ETL Flows in The Wild](paper-placeholder).

If you are using this datasets in publications, please cite:
> Dolev Adas, Ohad Eytan, Guy Khazma, Josep Sampé, and Paula Ta-Shma 
> 
> "Refactoring ETL Flows in The Wild"
> 
> 2023 IEEE International Conference on Big Data (Big Data), Sorrento, Italy, 2023

## Dataset Format
Similar to the format used [here](https://github.com/TonyZZX/gSpan.Java) and [here](https://github.com/betterenvi/gSpan), each dataset is a text file, where each line contains one of three options:
1. `t # n` - represents the start of flow number `n`.
2. `v x l` - represents vertex with id `x` and label of `l` (below we explain the process of deriving `l`).
3. `e x y l` - represents an edge from vertex `x` to vertex `y` with label `l` (in our case, all the labels are `1`).

## The Lifting and Anonimazion Proccess
As we explained in more detail in the paper, each stage in a flow of DataStage™ has parameters, and we have different options for deriving the label of the stage depending on which patterns we are looking for. We call this process lifting.

Here, we are publishing two types of lifting:
1. *Simple:* We only take the stage type as the label. This could be used to find general patterns and help create tools to help flow authoring.  
2. *Detailed*: Take parameters into account, aiming to take all the parameters that would provide an option to refactor flows to use common subflows. Notice that as this is a WIP prototype, this might not be completely accurate (e.g., we take parameters that we shouldn't or vice versa). 

These values hashed into unique integers to preserve our users' anonymity while keeping the structure of the flows and the ability to find common subgraphs using FSM algorithms. The hashes are *not* consistent between different datasets.

## Acknowledgment 
We thank the DataStage™ team for providing us the data and allowing us to share it with the community.

## License
Although this Github repository is under the `Apache-2.0 license`, the actual datasaets are released under the [CDLA-Sharing-1.0 license](https://cdla.dev/sharing-1-0/). By downloading or using them, you agree to the terms of this license.
