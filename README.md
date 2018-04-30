# NU-DBSCAN

**DBSCAN implementation for Non Uniform cluster density.**

This DBSCAN implementation lets you set an epsilon as a vector
and so define a reachability value for each dimension of the dataset.

The only difference from the classic DSCAN is the way neighbors points are found.

Dependencies
---

```bash
    pip install numpy
```

Examples of use & Results
---

```python
    # Dataset composed of 2 non-circular clusters of 50 points.
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
    # Best result get with DBSCAN.
    clusterer = DBSCAN(eps=1, min_samples=10).fit(X)
```
![Dataset](/img/dbscan.png)

```python
    # Result get with NU-DBSCAN.
    clusterer = NUDBSCAN(eps=(4, .5), min_samples=10).fit(X)
```
![Dataset](/img/nudbscan.png)
