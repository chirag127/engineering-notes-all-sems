### Zookeeper

A zookeeper is a term that can refer to two different things:

- A person who manages zoo animals that are kept in captivity for conservation or to be displayed to the public. 
- An open source Apache project that provides a centralized service for providing configuration information, naming, synchronization and group services over large clusters in distributed systems.   

Some points to know about zookeepers are:

- Zookeepers who work with animals are usually responsible for the feeding and daily care of the animals. They may also clean the exhibits and report health problems. 
- Zookeepers who work with distributed systems use a hierarchical key-value store, which is used to provide a distributed configuration service, synchronization service, and naming registry for large distributed systems. 
- ZooKeeper's architecture supports high availability through redundant services. The clients can thus ask another ZooKeeper leader if the first fails to answer. 
- ZooKeeper nodes store their data in a hierarchical name space, much like a file system or a tree data structure. Clients can read from and write to the nodes and in this way have a shared configuration service. 
- ZooKeeper is especially fast in "read-dominant" workloads (i.e. workloads in which reads are much more common than writes). 
- ZooKeeper is modeled after Google's Chubby lock service and was originally developed at Yahoo! for streamlining the processes running on big-data clusters by storing the status in local log files on the ZooKeeper servers. 
- ZooKeeper is used by companies including Yelp, Rackspace, Yahoo!, Odnoklassniki, Reddit, NetApp SolidFire, Meta, Twitter and eBay as well as open source enterprise search systems like Solr.