#### Block Sizes in HDFS

In Hadoop Distributed File System (HDFS), the default block size is 128 MB. This can be changed by modifying the `dfs.blocksize` parameter in the `hdfs-site.xml` configuration file. Here is an example of how to change the block size to 256 MB:

```xml
<configuration>
  <property>
    <name>dfs.blocksize</name>
    <value>268435456</value>
    <description>Block size in bytes.</description>
  </property>
</configuration>
```

After changing the block size, the Hadoop cluster needs to be restarted for the changes to take effect. It is important to note that changing the block size will only affect new files that are added to HDFS. Existing files will still have the old block size.