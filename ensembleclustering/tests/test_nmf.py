# test_nmf.py


import os
import numpy as np
from sklearn.metrics import normalized_mutual_info_score
from ensembleclustering import cluster_ensembles


def test_missing():
    base_clusters = np.array([
        [1, 1, 1, 2, 2, 3, 3],
        [2, 2, 2, 3, 3, 1, 1],
        [4, 4, 2, 2, 3, 3, 3],
        [1, 2, np.nan, 1, 2, np.nan, np.nan]
    ])
    label_true = np.array([1, 1, 1, 2, 2, 3, 3])
    label_pred = cluster_ensembles(base_clusters, solver='nmf', random_state=0)
    nmi_score = normalized_mutual_info_score(label_true, label_pred, average_method='geometric')
    assert nmi_score == 1.0


def test_performance():
    base_clusters = np.loadtxt(os.path.dirname(__file__) + '/data/base_clusters.csv', delimiter=',', dtype=int)
    label_true = np.loadtxt(os.path.dirname(__file__) + '/data/label_true.csv', delimiter=',', dtype=int)
    label_pred = cluster_ensembles(base_clusters, solver='nmf', random_state=0)
    nmi_score = normalized_mutual_info_score(label_true, label_pred, average_method='geometric')
    assert nmi_score == 1.0

