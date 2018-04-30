import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN

centers = [[5, 6], [5, 4]]
X = np.array([
    [np.random.uniform(c[0] - 4, c[0] + 4),
     np.random.uniform(c[1] - .5, c[1] + .5)]
    for c in centers
    for i in range(0, 50)
])

print(X)
def cluster(eps):
    db = DBSCAN(eps=eps, min_samples=10).fit(X)
    core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
    core_samples_mask[db.core_sample_indices_] = True
    labels = db.labels_
    
    unique_labels = set(labels)

    colors = [plt.cm.get_cmap('plasma')(each)
              for each in np.linspace(0, 1, len(unique_labels))]

    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    ax.scatter(X[:, 0], X[:, 1])

    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    for k, col in zip(unique_labels, colors):
        if k == -1:
            # Black used for noise.
            col = [0, 0, 0, 1]

        class_member_mask = (labels == k)

        xy = X[class_member_mask & core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=14)

        xy = X[class_member_mask & ~core_samples_mask]
        plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
                 markeredgecolor='k', markersize=6)

    plt.show()
