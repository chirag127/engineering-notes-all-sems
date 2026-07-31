 Here is the markdown content in formal tone without emojis or external links:

### Resource Provisioning Methods

1. Manual Provisioning: Here, the resources are provisioned manually by the administrator. The admin provisions the resources as and when requested by the users. This method has some disadvantages like it is time-consuming, prone to human errors, and cannot handle the scalability requirements of the cloud.
2. Dynamic Provisioning: In this method, the resources are provisioned dynamically based on the actual demands of the workload. The resources are automatically scaled up or down by the cloud platform based on metrics like CPU utilization, memory usage, etc. This method effectively meets the scalability requirements but can lead to overprovisioning or under-provisioning of resources. Some examples are AWS Auto Scaling groups and Google Compute Engine Autoscalers.
3. Spot Provisioning: In this method, the spare resources that are left unused by the cloud provider are offered at a discounted price. This enables cost-effectiveness but there is a risk of losing resources at short notice. AWS Spot instances and Google Preemptible VMs are examples of spot provisioning.
4. Queuing based Provisioning: In this approach, the user requests are queued and provisioned once resources are available. This approach ensures no wastage of resources but can lead to unpredictable wait times and latency.

The above points summarize the key resource provisioning methods in cloud computing. The selection of an appropriate method depends on the use case, workload patterns, budget, latency requirements, etc. A combination of multiple methods is also commonly employed to reap their respective benefits.