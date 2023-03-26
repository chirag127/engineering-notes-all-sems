## Installation of HBase, Installing Thrift, and Practice Examples for the Notes of the Big Data and Analytics Lab

This guide provides step-by-step instructions for installing HBase, Thrift, and practicing examples for the Big Data and Analytics Lab. This guide assumes that you have already set up a Hadoop cluster and have installed Hadoop on all nodes in the cluster.

### Installing HBase

1. Download the latest stable release of HBase from the official Apache website.
2. Extract the downloaded archive and move it to the desired location on your file system.
3. Navigate to the HBase installation directory and modify the `hbase-env.sh` file to set the `JAVA_HOME` environment variable to the location of your Java installation.
4. Modify the `hbase-site.xml` configuration file to set the necessary properties such as `hbase.rootdir`, `hbase.zookeeper.quorum`, and `hbase.zookeeper.property.dataDir`.
5. Start the HBase server by running the command `./bin/start-hbase.sh`.

### Installing Thrift

Thrift is a software framework for scalable cross-language services development. It allows you to define data types and service interfaces in a simple language and generates code to implement them in various programming languages.

1. Download the latest stable release of Thrift from the official Apache website.
2. Extract the downloaded archive and move it to the desired location on your file system.
3. Navigate to the Thrift installation directory and run the following commands:
   ```
   ./configure
   make
   make install
   ```
4. Verify the installation by running the command `thrift --version`.

### Practice Examples

Here are some practice examples that you can use to familiarize yourself with HBase and Thrift:

1. Create a table in HBase and insert data using the HBase shell.
   ```
   create 'mytable', 'cf'
   put 'mytable', 'row1', 'cf:col1', 'value1'
   put 'mytable', 'row2', 'cf:col1', 'value2'
   scan 'mytable'
   ```
2. Use the HBase Java API to perform CRUD operations on the table created in the previous example.
   ```
   Configuration config = HBaseConfiguration.create();
   Connection connection = ConnectionFactory.createConnection(config);
   Table table = connection.getTable(TableName.valueOf("mytable"));
   
   Put put = new Put(Bytes.toBytes("row3"));
   put.addColumn(Bytes.toBytes("cf"), Bytes.toBytes("col1"), Bytes.toBytes("value3"));
   table.put(put);
   
   Get get = new Get(Bytes.toBytes("row1"));
   Result result = table.get(get);
   byte[] value = result.getValue(Bytes.toBytes("cf"), Bytes.toBytes("col1"));
   System.out.println("Value : " + Bytes.toString(value));
   
   Scan scan = new Scan();
   ResultScanner scanner = table.getScanner(scan);
   for (Result row : scanner) {
       byte[] value = row.getValue(Bytes.toBytes("cf"), Bytes.toBytes("col1"));
       System.out.println("Value : " + Bytes.toString(value));
   }
   
   table.close();
   connection.close();
   ```
3. Use Thrift to write a client application that interacts with the HBase server.
   ```
   thrift -r --gen java Hbase.thrift
   javac -classpath /path/to/hbase.jar:/path/to/thrift.jar gen-java/*.java
   java -classpath /path/to/hbase.jar:/path/to/thrift.jar:/path/to/generated/classes MyClient
   ```
   ```
   import org.apache.hadoop.conf.Configuration;
   import org.apache.hadoop.hbase.client.*;
   import org.apache.hadoop.hbase.thrift.generated.*;
   import org.apache.thrift.transport.*;
   
   public class MyClient {
       public static void main(String[] args) throws Exception {
           TTransport transport = new TSocket("localhost", 9090);
           transport.open();
           
           TProtocol protocol = new TBinaryProtocol(new TFramedTransport(transport));
           
           Hbase.Client client = new Hbase.Client(protocol);
           
           byte[] tableName = Bytes.toBytes("mytable");
           byte[] row = Bytes.toBytes("row1");
           byte[] family = Bytes.toBytes("cf");
           byte[] qualifier = Bytes.toBytes("col1");
           byte[] value = Bytes.toBytes("value1");
           
           Mutation mutation = new Mutation();
           mutation.setColumn(family, qualifier, value);
           
           ColumnPath columnPath = new ColumnPath();
           columnPath.setColumn(family);
           columnPath.setQualifier(qualifier);
           
           client.mutateRow(tableName, row, Collections.singletonList(mutation), null);
           
           List<TCell> cells = client.get(tableName, row, columnPath, null);
           for (TCell cell : cells) {
               System.out.println("Value : " + Bytes.toString(cell.getValue()));
           }
           
           transport.close();
       }
   }
