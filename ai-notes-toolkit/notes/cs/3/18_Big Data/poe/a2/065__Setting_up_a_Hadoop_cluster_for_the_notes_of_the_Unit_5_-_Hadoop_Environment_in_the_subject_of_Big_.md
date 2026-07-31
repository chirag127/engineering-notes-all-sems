 Here is the content in markdown format without any emojis or external links in a formal tone:

### Setting up a Hadoop cluster for the notes of the Unit 5 - Hadoop Environment in the subject of Big Data.

1. Gather Hardware:
 - Master node: RAM: 16GB, CPU: Quad-core, Storage: 1TB HDD
 - Slave/Worker nodes: RAM: 8GB, CPU: Quad-core, Storage: 2TB HDD (Each)
 - Network: 1Gbps or above Ethernet switches
2. Install Ubuntu/ Linux operating system:
 - Master and slave nodes
 - Same operating system version for compatibility
3. Configure SSH:
 - Master node: Generate SSH keys and copy to slaves
 - Disable password login and allow only key-based login for security
4. Install Hadoop:
 - Use package manager to install Hadoop on all machines
 - Ensure the same Hadoop version and distributions across the cluster
5. Update Configuration files:
 - Edit `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml` with necessary configurations
 - Set unique IDs for each node
 - Set memory and CPU capacities
6. Form a cluster:
 - On master, format the filesystem
 - Start HDFS and YARN daemons on all machines
 - Test the setup by running sample MapReduce jobs

The above points cover the key steps to setup a basic Hadoop cluster. Further fine-tuning and optimizations can be done based on the system specifications and use-cases.