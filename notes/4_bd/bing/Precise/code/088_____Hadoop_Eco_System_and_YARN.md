### Hadoop Eco System and YARN

Hadoop is an open-source software framework for storing and processing large datasets. The Hadoop ecosystem consists of several components, including Hadoop Distributed File System (HDFS), MapReduce, and Yet Another Resource Negotiator (YARN).

YARN is the resource management layer of Hadoop. It is responsible for managing and allocating resources to applications running on the Hadoop cluster. YARN separates the resource management and scheduling functions from the data processing component, allowing for more efficient and scalable processing of data.

Here is an example of how YARN works in the Hadoop ecosystem:

```python
from hadoop.yarn import api

# Create a YARN client
client = api.YarnClient()

# Submit a new application to the YARN cluster
app = client.submit_application(
    name="my-app",
    queue="default",
    memory=1024,
    vcores=1,
    command="my-command"
)

# Monitor the application's progress
while app.state not in ["FINISHED", "FAILED", "KILLED"]:
    app = client.get_application(app.id)
    print("Application state:", app.state)
    time.sleep(1)

# Get the final application report
report = client.get_application_report(app.id)
print("Application report:", report)
```

This code creates a YARN client, submits a new application to the YARN cluster, monitors the application's progress, and retrieves the final application report. This is just one example of how YARN can be used in the Hadoop ecosystem to manage resources and run applications.