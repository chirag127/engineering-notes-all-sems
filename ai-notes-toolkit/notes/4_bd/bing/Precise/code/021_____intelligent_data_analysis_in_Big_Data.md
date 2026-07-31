### Intelligent Data Analysis in Big Data

Here is an example of code for intelligent data analysis in Big Data using Python:

```python
import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

# Load the data
data = pd.read_csv('big_data.csv')

# Preprocess the data
data = preprocessing.scale(data)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

# Get the cluster labels
labels = kmeans.labels_
```
