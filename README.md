If you make use of the brca_tcga code, please cite the Zenodo DOI: https://zenodo.org/record/8251328

If you make use of the acc_tcga code, please cite the Zenodo DOI: https://zenodo.org/record/8286179

This is a project that was carried out during Google Summer of Code(GSoC'23).

# PyTorch Geometric Example Dataset using Pathway Commons and cBioPortal

The aim of the project is to develop an example dataset that will be compatible with Pytorch Geometric. This dataset will be created by integrating datasets gotten from cBIo datahub and Pathway Commons. The data integration process will require combining the two datasets to create a single, comprehensive dataset. The integrated dataset will then be used to train GNN models for downstream tasks. 

The proposed solution involves a three-stage process: retrieving and preprocessing data from the datasets, integrating the data, and developing and training Graph Neural Network(GNN) models on the integrated dataset.

WorkFlow Image;

![gsoc_cbioportal](https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/assets/63251266/ed1b185e-0b41-4498-9938-f9484f7a30b2)

During the phase of this project, two main cancer types were considered which includes:
1. Adrenocortical Carcinoma
2. Breast Invasive Carcinoma

#  Pipeline From Data Collection to Model Building

This is a set of notebooks that shows how data was collected, preprocessed and integrated, then converted to PyTorch Geometric Dataset

## Overview of Repository
1. Data Collection: The Datasets that were collected from cbioportal and Pathway Commons are:
   
   - Reactome subset from Pathway Commons: https://www.pathwaycommons.org/archives/PC2/v12/PathwayCommons12.reactome.hgnc.sif.gz
     
   - brca_tcga_pan_can_atlas_2018(data_clinical_patient.txt, data_clinical_patient.txt and data_mrna_seq_v2_rsem.txt): 
     https://github.com/cBioPortal/datahub/tree/master/public/brca_tcga_pan_can_atlas_2018
     
   - acc_tcga_pan_can_atlas_2018(data_clinical_patient.txt, data_clinical_patient.txt and data_mrna_seq_v2_rsem.txt): 
     https://github.com/cBioPortal/datahub/tree/master/public/acc_tcga_pan_can_atlas_2018
     
   To have access to these datasets without having to go through the process needed to download datasets from cBioportal, you can access 
   them on Zenodo: https://zenodo.org/record/8251328

   NB: If you want to do these steps for a different dataset, then you have to download the required data from the sites. You can see how to download from cBioportal here: 
   https://github.com/cBioPortal/datahub/tree/master

1. Data Preprocessing: For the creation of this sample dataset, the data_clinical_patient.txt and data_clinical_patient.txt were merged based on the patient identifier.
   After which, the only columns kept were the sample identifier, patient identifier and overall survival(months) of each patient.
   Next, the merged dataset was merged with the data_mrna_seq_v2_rsem.txt on the sample identifiers. 
   Then this new dataset was splitted into X and y which represents features and labels.
   In this stage, work was also done on creating training, test and validation splits for modelling using the 60:20:20 rule for the brca_tcga and the 70:30 rule for acc_tcga

   The final results gotten from these steps include:
   For brca_tcga:
   - X_train, y_train, X_val, y_val, X_test, y_test.
   
   - Gene features: graph_idx
     
   - Labels: graph_labels
     
   - edges: edge_index
  
   For acc_tcga:
   - X_train, y_train, X_test, y_test.
   
   - Gene features: graph_idx
     
   - Labels: graph_labels
     
   - edges: edge_index

   All the datasets can be accessed here: https://zenodo.org/record/8251328

   The steps that were followed after downloading the required datasets are shown in the notebooks below.
   https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/breast_cancer_preprocesing.ipynb
   https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/acc_data_processing.ipynb
   

4. Data Integration: To convert to a PyG Dataset, a list of graphs were created from the preprocessed dataset first.
   Then these graphs were converted to data objects. These steps are shown in the provided notebook.

   You can view the datatsets final statistics here: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/docs/dataset_statistics.csv

   Notebook for brca_tcga Integration: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Noteboooks/InMemoryDataset_Class_with_brca_tcga.ipynb

   Notebook for acc_tcga Integration: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/pyg_sample_data_with_inmemorydataset_class.ipynb

  
6. Modelling: The two datasets were then used for modelling. First a baseline model was created using FLAML, then a Graph Neural Network(GNN) model was built using GCNConv.
   For the brca_tcga dataset, another GNN model technique known as Graph Attention Network(GAT) was used for modeliing too.
   The notebooks below show the modelling steps that was carried out.

   For brca_tcga: 
   Baseline model: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/baseline_model_with_brca_data.ipynb

   GNN model: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/gnn_modelling_with_breast_cancer_data.ipynb

   GAT model: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/gat_modelling_with_breast_cancer_data.ipynb

   For acc_tcga:
   Baseline model: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/baseline_model_with_acc_data.ipynb

   GNN model: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/Notebooks/gnn_modelling_with_acc_data.ipynb

   View the modelling statistics here: https://github.com/cannin/gsoc_2023_pytorch_pathway_commons/blob/main/docs/modelling_statistics.csv




