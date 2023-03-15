#### HDFS monitoring & maintenance in Hadoop Environment
HDFS monitoring and maintenance is an important aspect of managing a Hadoop environment. Here is an example of code that can be used to monitor and maintain HDFS:

```python
from subprocess import check_output

# Function to get the HDFS disk usage
def get_hdfs_disk_usage():
    cmd = "hdfs dfs -du -h /"
    output = check_output(cmd, shell=True)
    return output

# Function to get the HDFS report
def get_hdfs_report():
    cmd = "hdfs dfsadmin -report"
    output = check_output(cmd, shell=True)
    return output

# Function to get the HDFS file system check
def get_hdfs_fsck():
    cmd = "hdfs fsck /"
    output = check_output(cmd, shell=True)
    return output

# Function to get the HDFS balancer status
def get_hdfs_balancer_status():
    cmd = "hdfs balancer -status"
    output = check_output(cmd, shell=True)
    return output

# Function to run the HDFS balancer
def run_hdfs_balancer():
    cmd = "hdfs balancer"
    output = check_output(cmd, shell=True)
    return output

# Example usage
disk_usage = get_hdfs_disk_usage()
report = get_hdfs_report()
fsck = get_hdfs_fsck()
balancer_status = get_hdfs_balancer_status()
balancer_output = run_hdfs_balancer()

print(disk_usage)
print(report)
print(fsck)
print(balancer_status)
print(balancer_output)
```

This code provides functions to get the HDFS disk usage, report, file system check, balancer status, and to run the HDFS balancer. These functions can be used to monitor and maintain the HDFS in a Hadoop environment.