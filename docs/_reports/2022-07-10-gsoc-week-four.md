---
layout: post
title:  "Week four | retrain model with rcellminer's drug data"
tags: gsoc
author: Yoshitaka Inoue
---

## GSoC Project

- [GSoC Project URL](https://summerofcode.withgoogle.com/programs/2022/projects/ylOolPrk)
- [Work Repository](https://github.com/cannin/graph_neural_network_drug_response)

Mentor:
**Augustin Luna** ([@cannin](https://github.com/cannin))

## Tasks

1. [Re-train DrugCell model](https://github.com/cannin/graph_neural_network_drug_response/issues/13).  
    Status: **Done**.   
    Branch: **[6-drugcell-test](https://github.com/cannin/graph_neural_network_drug_response/tree/6-drugcell-test)**.  
    PR: **None**.
    
    I did retraining again.

    
## Comments

I tried to tune this model but it takes over 30 hours and need to hyper parameter tuning (layer), this is not enough to use colab.  
So from next week, I plan to use the other GPU machine to tune and try to run over 2 or 3 days.  
I still don't understand model completely and probably this model looks complicated.  
So, I think it takes 2 or more weeks to get good results. (I hope to get good result asap though.)

## Next Step

- train new model
- read this paper carefully and tune model
