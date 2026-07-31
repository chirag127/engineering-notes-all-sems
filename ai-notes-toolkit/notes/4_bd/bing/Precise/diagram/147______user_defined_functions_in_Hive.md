#### User Defined Functions in Hive

Hive user-defined functions, or UDFs, are custom functions that can be developed in Java, integrated with Hive, and built on top of a Hadoop cluster to allow for efficient and complex computation that would not otherwise be possible with simple SQL. They can be useful and very powerful, and yet online documentation is pretty weak.

In Hive, the users can define their own functions to meet certain client requirements. These are known as UDFs in Hive. User Defined Functions written in Java for specific modules. HIVE UDF (User Defined Functions) allow the user to extend HIVE Query Language. Once the UDF is added in the HIVE script, it works like a normal built-in function. To check which all UDFs are loaded in the current hive session, we use the SHOW command.

Basically, we can use two different interfaces for writing Apache Hive User Defined Functions. Simple API Complex API As long as our function reads and returns primitive types, we can use the simple API (org.apache.hadoop.hive.ql.exec.UDF). In other words, it means basic Hadoop & Hive writable types.

You can configure the cluster to find the JAR using the ADD JAR command on the Hive.