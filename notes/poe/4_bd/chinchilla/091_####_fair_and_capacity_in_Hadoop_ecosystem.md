#### Fair and Capacity in Hadoop Ecosystem

In the Hadoop ecosystem, the concepts of Fair and Capacity scheduling are used to allocate resources to different applications and ensure that the resources are utilized efficiently. These concepts are crucial for optimizing the performance of Hadoop clusters and ensuring that all applications are given a fair share of resources.

**Fair Scheduling**

Fair scheduling is a scheduling algorithm that ensures that all applications running on a Hadoop cluster get an equal share of resources. This means that no single application can hog all the resources, and all applications are given a fair chance to run.

- The fair scheduler divides the cluster resources into pools and allocates resources to each pool based on the number of running tasks and the priority of the tasks.
- The fair scheduler maintains a pool of tasks for each application and allocates resources to each pool based on the pool's share of the total cluster resources.
- The fair scheduler ensures that each pool gets a fair share of the resources, even if some pools have more tasks than others.

Mnemonic: "Fair scheduling is like dividing a cake into equal pieces, so everyone gets a fair share."

**Capacity Scheduling**

Capacity scheduling is a scheduling algorithm that ensures that each application running on a Hadoop cluster gets a fixed share of resources. This means that each application is guaranteed a certain amount of resources, regardless of how many other applications are running on the cluster.

- The capacity scheduler allocates a fixed amount of resources to each application based on its configured capacity.
- The capacity scheduler ensures that each application gets its allocated resources, even if other applications are not using their full capacity.
- The capacity scheduler is useful for scenarios where some applications require a fixed amount of resources and cannot run if they do not get their allocated resources.

Mnemonic: "Capacity scheduling is like reserving seats on a plane. Each application gets their reserved seat, even if other seats are empty."

**Advantages of Fair and Capacity Scheduling**

- Both fair and capacity scheduling algorithms ensure that resources are allocated efficiently, and all applications get a fair share of resources.
- Fair scheduling ensures that no application can hog all the resources, while capacity scheduling ensures that each application gets its allocated resources.
- Fair scheduling is useful for scenarios where applications have varying resource requirements, while capacity scheduling is useful for scenarios where some applications require a fixed amount of resources.

**Disadvantages of Fair and Capacity Scheduling**

- Fair scheduling can result in longer wait times for applications with low priority, as they may have to wait for higher priority applications to finish.
- Capacity scheduling can result in unused resources if applications do not use their full allocated capacity.

**Examples of Fair and Capacity Scheduling**

- Fair scheduling is used by default in Hadoop 2.x, and it is used by several big data platforms, such as Spark, Flink, and HBase.
- Capacity scheduling is used by several Hadoop distributions, such as Cloudera and Hortonworks.

**Applications of Fair and Capacity Scheduling**

- Fair and capacity scheduling are used in Hadoop clusters to ensure that all applications get a fair share of resources and that resources are utilized efficiently.
- Fair and capacity scheduling are also used in other big data platforms, such as Spark and Flink, to allocate resources to different applications.