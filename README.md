# NU-DBSCAN

**DBSCAN implementation for Non Uniforme cluster density.**

This DBSCAN implementation let you choose an epsilon value for each dimension of your
dataset.

It's usefull in case of your cluster have the same density but
points are non-uniform spreaded inside this cluster.

See the examples of use for more explenations.

Dependencies
---

```bash
    pip install numpy
```

Examples of use
---

```python
    # Dataset composed of 2 cluster of 50 points
    centers = [[5, 6], [5, 4]]
    X = np.array([
        [np.random.uniform(c[0] - 4, c[0] + 4),
         np.random.uniform(c[1] - .5, c[1] + .5)]
        for c in centers
        for i in range(0, 50)
    ])
```
![Dataset](/img/dataset.png)


```python
    # Best result get with DBSCAN
    clusterer = DBSCAN(eps=1, min_samples=10).fit(X)
```
![Dataset](/img/dbscan.png)

```python
    # Result get with NU-DBSCAN
    clusterer = DBSCAN(eps=(4, .5), min_samples=10).fit(X)
```
![Dataset](/img/nudbscan.png)
