#### File sizes in HDFS

Here is an example of how to get the file sizes in HDFS using Python and the `hdfs` library:

```python
from hdfs import InsecureClient

# Connect to HDFS
client = InsecureClient('http://namenode:50070', user='hdfs')

# Get the file status
status = client.status('/path/to/file')

# Get the file size
file_size = status['length']

# Print the file size
print(f'File size: {file_size} bytes')
```
