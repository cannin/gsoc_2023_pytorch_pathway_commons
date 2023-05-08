---
layout: post
title:  "Week Three | retrain model with rcellminer's drug data"
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
    
    It takes 24 hour to run this model and also I need to tune the paramters.

    
## Comments

I trained new model using rcellminer's all drugs. But it takes around 20 hours. So, I'll try it on my GPU machine next week. 
This is ongoing result. It looks like around 0.324294 correration for validation.
![Screen Shot 2022-07-01 at 23 25 21](https://user-images.githubusercontent.com/8393063/176986423-ad39457a-bb28-414d-98a6-74caa02424ee.png)
Um, looks not super good. Probably I need to tune params for that. I'm not familier this model. So, I'll read this paper in detail and try to do that.

## Next Step

- train new model
- read this paper carefully and tune model
