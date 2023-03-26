 Here is the formal content in Markdown format without emojis and external links:

## Installation of Hive along with practice examples.

1. Download Apache Hive from http://hive.apache.org/downloads.html. Extract the archive file to a suitable location.

2. Set the HIVE_HOME environment variable to point to the installation location. For example, if Hive is installed in /usr/local/hive, add the following line to .bashrc:

export HIVE_HOME=/usr/local/hive

3. Add $HIVE_HOME/bin to the PATH environment variable. This is required to run Hive commands from any location.

4. Download and install a MySQL or PostgreSQL database. Create a database and user for Hive metastore. Note down the database name, hostname, port, and user credentials which will be used during Hive configuration.

5. Copy hive-default.xml.template to hive-site.xml. Update the following properties in hive-site.xml:

<property>
  <name>javax.jdo.option.ConnectionURL</name>
  <value>jdbc:mysql://localhost:3306/metastore_db?createDatabaseIfNotExist=true</value>
</property>
<property>
  <name>javax.jdo.option.ConnectionDriverName</name>
  <value>com.mysql.jdbc.Driver</value>
</property>
<property>
  <name>javax.jdo.option.ConnectionUserName</name>
  <value>hiveuser</value>
</property>
<property>
  <name>javax.jdo.option.ConnectionPassword</name>
  <value>hivepassword</value>
</property>

6. Start the Hive metastore service by running the following command:

hive --service metastore

7. Start the Hive server by running the following command:

hive --service hiveserver2

8. Open Beeline or Hive CLI and run some sample queries to test the installation.

For example:

SHOW TABLES;
CREATE TABLE students (name STRING, age INT);
SELECT * FROM students;