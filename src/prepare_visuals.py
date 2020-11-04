#Author: Gentry Atkinson
#Organization: Texas University
#Data: 04 November, 2020
#Create visualizations of 6 instances each from 2 UniMiB sets and the UCI set
#  using 3 methods of feature extraction

import random as rand
from tsar import get_supervised_features, get_unsupervised_features, print_graph_for_instance, get_NN_for_dataset
from utils.ts_feature_toolkit import get_features_for_set
from import_datasets import get_unimib_data, get_uci_data
from sklearn.manifold import TSNE as tsne

if __name__ == "__main__":
    print("Preparing 45 instance visualizations...")
    print("UniMiB Traditional")
    for s in ["adl", "two_classes"]:
        X, y, labels = get_unimib_data(s)
        NUM_INSTANCES = len(X)

        feat_x = get_features_for_set(X[:,0,:], num_samples=NUM_INSTANCES)
        feat_y = get_features_for_set(X[:,1,:], num_samples=NUM_INSTANCES)
        feat_z = get_features_for_set(X[:,2,:], num_samples=NUM_INSTANCES)
        NUM_FEATURES = feat_x.shape[1]
        feat = np.zeros((NUM_INSTANCES,3*NUM_FEATURES))
        feat[:, 0:NUM_FEATURES] = feat_x[:,:]
        feat[:, NUM_FEATURES:2*NUM_FEATURES] = feat_y[:,:]
        feat[:, 2*NUM_FEATURES:3*NUM_FEATURES] = feat_z[:,:]

        vis = tsne(n_components=2, n_jobs=8).fit_transform(feat)
        neighbors = get_NN_for_dataset(feat)
        print("Correct Labels")
        for i in range(3):
            print(i)
            instance = rand.randint(len(X))
            print_graph_for_instance(X, y, labels, instance, feat, neighbors, vis, False, True, "imgs/unimib_"+s+"_trad_correct_"+str(i)+".pdf")
