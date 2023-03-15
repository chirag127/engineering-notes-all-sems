#### How to build applications with Zookeeper

1. **Starting ZooKeeper and Application Builder**: After installing Application Builder in admin mode, on the server(s) where ZooKeeper is installed, execute the `/etc/init.d/zookeeper-service-default` command . If you have installed Application Builder in non-admin mode, start the ZooKeeper server before starting Application Builder. To start the ZooKeeper server on a Linux system, use the `Zookeeper/zookeeper/bin/zkServer.sh restart` command from your Watson Explorer installation directory .

2. **Running ZooKeeper on Kubernetes**: You can use the `kubectl apply` command to create the manifest. For example, `kubectl apply -f https://k8s.io/examples/application/zookeeper/zookeeper.yaml`. This creates the `zk-hs` Headless Service, the `zk-cs` Service, the `zk-pdb` PodDisruptionBudget, and the `zk` StatefulSet .

3. **Using ZooKeeper in Distributed Applications**: ZooKeeper is used by Apache HBase, HDFS, and other Apache Hadoop projects to provide highly-available services and to make distributed programming easier. You can use ZooKeeper to easily and safely implement important features in your distributed software .

4. **Setting up a ZooKeeper server in standalone mode**: The server is contained in a single JAR file, so installation consists of creating a configuration. Once you've downloaded a stable ZooKeeper release, unpack it and `cd` to the root. To start ZooKeeper, you need a configuration file .

5. **Getting a ZooKeeper distribution**: Download a recent stable release from one of the Apache Download Mirrors. Setting up a ZooKeeper server in standalone mode is straightforward. The server is contained in a single JAR file, so installation consists of creating a configuration .