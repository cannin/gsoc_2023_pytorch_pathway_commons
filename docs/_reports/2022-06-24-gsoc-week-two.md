---
layout: post
title:  "Week two | retrain model"
tags: gsoc
author: Yoshitaka Inoue
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2022/projects/ylOolPrk)
- [Work Repository](https://github.com/cannin/graph_neural_network_drug_response)

Mentor:
**Augustin Luna** ([@cannin](https://github.com/cannin))

## Tasks

1. [Document Project Dependencies](https://github.com/cannin/graph_neural_network_drug_response/issues/8).  
    Status: **In progress**.  
    Branch: **None**.       
    PR: **None**.  
   
    I was able to create R and Python environment respectively.
    So, I'll add them.

2. [Reformat CellMinerCDB Data for DrugCell ](https://github.com/cannin/graph_neural_network_drug_response/issues/2).  
    Status: **Done**.  
    Branch: **[6-drugcell-test](https://github.com/cannin/graph_neural_network_drug_response/tree/6-drugcell-test)**.       PR: **None**.  
    
    I can extract from rcellminer and reformat for DrugCell.

3. [Run DrugCell Model on CellMinerCDB Data](https://github.com/cannin/graph_neural_network_drug_response/issues/6).  
    Status: **Done**.   
    Branch: **[6-drugcell-test](https://github.com/cannin/graph_neural_network_drug_response/tree/6-drugcell-test)**.  
    PR: **None**.   
    
    I can run DrugCell with rcellminer data.
    
4. [Need to replace SMILES from rcellminer to DrugCell](https://github.com/cannin/graph_neural_network_drug_response/issues/11).  
    Status: **Done**.   
    Branch: **[6-drugcell-test](https://github.com/cannin/graph_neural_network_drug_response/tree/6-drugcell-test)**.  
    PR: **None**.
    
    I did replace cell line name and SMILES from rcellminer to DrugCell
    
5. [Re-train DrugCell model](https://github.com/cannin/graph_neural_network_drug_response/issues/13).  
    Status: **Done**.   
    Branch: **[6-drugcell-test](https://github.com/cannin/graph_neural_network_drug_response/tree/6-drugcell-test)**.  
    PR: **None**.
    
    I train the DrugCell model with rcellminer data.

## Comments

Today, I trained the new DrugCell model using rcellminer data. The result was not so bad (Peason corr was 0.29) but not so good like original's one (Peason corr was 0.8). In my opinion, this is caused by the number of dataset. For training, I only use around 1000 entries. But we have more data but not so easy to use it for new model. Anyway, we ca n get knowledge how to train the model. Using this, I hope to explore more data and get good results.

## Next Step

- Share today's progress with Augustin.
- Analyse results in detail.
