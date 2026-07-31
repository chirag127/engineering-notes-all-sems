#### Hadoop in the cloud in Hadoop Environment

Hadoop is an open-source framework that allows for the distributed storage and processing of large datasets across clusters of computers using simple programming models. Running Hadoop in the cloud environment has several advantages:

1. **Low capacity investment**: For companies still testing the waters with Hadoop, the low capacity investment in the cloud is a no-brainer. The cloud also makes sense for a quick, one-time use case involving big data computation.

2. **Simplifying Hadoop Operations**: As cluster consolidation happens in the enterprise, one thing that gets lost is the isolation of resources for different sets of users. Running Hadoop clusters in the same cloud environment is an obvious solution to this problem. This is, in a way, applying Hadoop’s principle of data locality at the macro level.

3. **Ephemeral clusters**: The biggest shift in your approach between running an on-premises Hadoop workflow and running the same workflow on Google Cloud is the shift away from monolithic, persistent clusters to specialized, ephemeral clusters. You spin up a cluster when you need to run a job and then delete it when the job completes.

4. **Security**: In a traditional on-premises Hadoop environment, the four pillars of Hadoop security (authentication, authorization, encryption, and audit) are integrated and handled by different components. On Google Cloud, they are handled by different Google Cloud components external to both Dataproc and Hadoop on Compute Engine.