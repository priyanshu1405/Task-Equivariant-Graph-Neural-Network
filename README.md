# Investigating Task Equivariant Graph Performance on Diverse Tasks

<p align="center">   
    <a href="https://pytorch.org/" alt="PyTorch">
      <img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?e&logo=PyTorch&logoColor=white" /></a>
</p>

The official model code for [**Task-Equivariant Graph Few-shot Learning**](https://arxiv.org/abs/2305.18758).
<br>
The official repository for [**Investigating Task Equivariant Graph Performance on Diverse Tasks**](https://github.com/priyanshu1405/Task-Equivariant-Graph-Neural-Network).

## Abstract 
 Few-shot node classification is an emerging challenge, where labelled data
 is scarce for each class and poses a major hurdle for current Graph Neural
 Networks. For real-world applications, traditional meta-learning techniques
 frequently call for enormous volumes of diverse training data, which is unfea
sible. This work investigates the Task-Equivariant Graph (TEG) framework
 for few-shot node categorization. Our aim is to identify and explain TEG’s
 limitations on a diverse set of datasets, thus building upon its already strong
 generalization capabilities. TEG is extremely suitable for real-world scenar
ios with minimal labeled data, achieving state-of-the-art performance even
 with limited training data. We extensively investigate TEG’s generalizabil
ity and robustness on a wide variety of benchmark datasets to investigate its
 effectiveness in a wide range of applications.

    
## Requirements
- python=3.8.13
- pytorch=1.10.1
- numpy=1.23.4
- torch-geometric=2.0.3

## Datasets
You can download the datasets, "coauthorCS", "ogbn-arxiv", "citeseer", "squirrel" from web. All the datasets are openly available. 


## How to run
```
python main.py --dataset coauthorCS --way 5 --shot 3
```
### Flags
`dataset` : coauthorCS, ogbn-arxiv, citeseer, squirrel  
`way` : N-way  
`shot` : K-shot  
`qry` : M-query 

