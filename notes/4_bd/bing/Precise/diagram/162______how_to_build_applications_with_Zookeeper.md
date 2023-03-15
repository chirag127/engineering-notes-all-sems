#### How to build applications with Zookeeper

Zookeeper is a distributed system coordinator that is used to provide highly-available services and to make distributed programming easier. It is used by Apache HBase, HDFS, and other Apache Hadoop projects .

1. **Starting ZooKeeper and Application Builder**: After installing Application Builder in admin mode, execute the `/etc/init.d/zookeeper-service-default` on the server where ZooKeeper is installed . In non-admin mode, start the ZooKeeper server before starting Application Builder. To start the ZooKeeper server on a Linux system, use the `Zookeeper/zookeeper/bin/zkServer.sh restart` command from your Watson Explorer installation directory .

2. **Running ZooKeeper on Kubernetes**: Open a terminal, and use the `kubectl apply` command to create the manifest. `kubectl apply -f https://k8s.io/examples/application/zookeeper/zookeeper.yaml`. This creates the `zk-hs` Headless Service, the `zk-cs` Service, the `zk-pdb` PodDisruptionBudget, and the `zk` StatefulSet .

3. **Setting up a ZooKeeper server in standalone mode**: The server is contained in a single JAR file, so installation consists of creating a configuration. Once you've downloaded a stable ZooKeeper release, unpack it and `cd` to the root. To start ZooKeeper you need a configuration file .