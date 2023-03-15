Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for file sizes in HDFS. Here is one possible solution:

#### file sizes in HDFS
```python
# Import the hdfs module
from hdfs import InsecureClient

# Create a client object with the HDFS URL
client = InsecureClient('http://namenode:50070')

# Define a function to get the file size in bytes
def get_file_size(path):
  # Get the file status from the client
  status = client.status(path)
  # Return the file size attribute
  return status['length']

# Test the function with some example paths
print(get_file_size('/user/hadoop/file1.txt')) # Prints 1024
print(get_file_size('/user/hadoop/file2.csv')) # Prints 2048
print(get_file_size('/user/hadoop/file3.parquet')) # Prints 4096
```