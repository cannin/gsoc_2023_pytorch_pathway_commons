import os
from typing import Callable, Optional, Tuple

import numpy as np
import pandas as pd
import torch
from torch_geometric.data import (Data, InMemoryDataset, download_url,
                                  extract_zip)

"""InMemoryDataset Class with brca_tcga.ipynb

This notebook shows how the data was created
"""
"""Importing Data and Libraries"""


class brca_tcga(InMemoryDataset):
    '''
      This is a dataset that was gotten by integrating the breast cancer
      (BRCA TCGA) dataset from the cBioPortal and data that shows
      node connections from Pathway Commons.
      They were preprocessed together to form one huge dataset that could be
      converted to Pytorch geometric data objects.
      This data is in the CSV format and can be downloaded, then processed to
      form a graph dataset comprising different graphs for training
      Graph Neural Networks (GNN).
      It could also be used as is for training Deep Neural Networks (DNN).
      The dataset contains the gene features of each patient in graph_features
      and the overall survival time (in months) of each patient,
      which are the labels.
    '''

    # Base URL to download the files
    url = 'https://zenodo.org/record/8179187/files/brca_tcga.zip?download=1'

    def __init__(
        self,
        root: str,
        transform: Optional[Callable] = None,
        pre_transform: Optional[Callable] = None,
        pre_filter: Optional[Callable] = None,
    ):
        super().__init__(root, transform, pre_transform, pre_filter=None)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        # List of the raw files
        return ['graph_idx.csv', 'graph_labels.csv', 'edge_index.pt']

    @property
    def processed_file_names(self):
        return 'breast_data.pt'

    def download(self):
        # Download the file specified in self.url and store
        # it in self.raw_dir
        path = download_url(self.url, self.raw_dir)
        extract_zip(path, self.raw_dir)
        # The zip file is removed
        os.unlink(path)

    def process(self):
        # Load features from CSV file
        graph_features = pd.read_csv(os.path.join(self.raw_dir, 'brca_tcga',
                                                  'graph_idx.csv'),
                                     index_col=0)

        # Load labels from CSV file
        graph_labels = np.loadtxt(os.path.join(self.raw_dir, 'brca_tcga',
                                               'graph_labels.csv'),
                                  delimiter=',')

        # Load the edge_index from the file
        file_path = os.path.join(self.raw_dir, 'brca_tcga', 'edge_index.pt')
        edge_index = torch.load(file_path)

        # Convert features to NumPy array
        graph_features = graph_features.values

        # Get the number of patients
        num_patients = graph_features.shape[0]

        # Create patient-specific graphs
        graphs = []
        for i in range(num_patients):
            node_features = graph_features[
                i]  # Node features for the i-th patient
            target = graph_labels[i]  # Target label for the i-th patient
            graph = (node_features, edge_index, target)
            graphs.append(graph)

        # Convert graphs to a list of Data objects
        data = [
            Data(x=torch.tensor(graph[0].reshape(len(graphs[0][0]), 1)),
                 edge_index=graph[1],
                 y=torch.tensor(graph[2])) for graph in graphs
        ]

        data, slices = self.collate(data)

        # Save the processed data
        torch.save((data, slices), self.processed_paths[0])

    def predefined_split(
            self, train_index, test_index,
            val_index) -> Tuple['brca_tcga', 'brca_tcga', 'brca_tcga']:
        # method to define custom split
        train_dataset = self.index_select(train_index)
        test_dataset = self.index_select(test_index)
        val_dataset = self.index_select(val_index)

        return train_dataset, test_dataset, val_dataset
