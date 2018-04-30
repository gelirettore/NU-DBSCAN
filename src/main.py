import numpy as np


class NUDBSCAN:

    def __init__(self, eps, min_samples):
        self.eps = eps
        self.min_samples = min_samples

        self.labels = []
        self.corepoints = []

    def fit(self, X):
        # Initially all labels are 0.
        self.labels = np.zeros(len(X), dtype=int)
        self.corepoints = np.zeros(len(X), dtype=int)

        # C is the id of the current cluster.
        C = 0

        # For each point P (index) in the dataset ...
        for P in range(0, len(X)):

            # If its label is not 0, skip this point.
            if self.labels[P] != 0:
                continue

            # Overwise find all of neighboring points.
            N = self.__get_neigbors(X, P)

            # If number of neigbhors < min_samples, point is noise.
            if len(N) < self.min_samples:
                self.labels[P] = -1

            # Else, it's a core point -> create new cluster and make it grow
            else:
                C += 1
                self.corepoints[P] = 1
                self.labels[P] = C
                self.__grow_cluster(X, N, C)

    def __grow_cluster(self, X, N, C):
        # For each point in neigbhors list...
        i = 0
        while i < len(N):

            # Get the next point.
            P = N[i]

            # If point labelled as noise, add it in cluster.
            if self.labels[P] == -1:
                self.labels[P] = C

            # Else if point has not been labelled ...
            elif self.labels[P] == 0:

                # Add point to cluster.
                self.labels[P] = C

                # Find all its neighbors.
                new_neighbors = self.__get_neigbors(X, P)

                # If point is a core point -> concatenate neighbors
                if len(new_neighbors) >= self.min_samples:
                        self.corepoints[P] = 1
                        N = np.concatenate([N, new_neighbors])

            # Go to next neighbour
            i += 1

    def __get_neigbors(self, X, P):
        # Return indexs where points are reachable by P
        mask = np.sqrt((X[P] - X)**2) < self.eps

        return np.where(mask.all(axis=1))[0]
