### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer, which is the recommended way to install and configure MySQL on Microsoft Windows .

- Download MySQL Installer from https://dev.mysql.com/downloads/installer/ and execute it.
- On the welcome screen, choose the first option: Install MySQL Products.
- On the license agreement screen, read the terms and conditions and select the checkbox to accept them. Then click Next.
- On the choosing a setup type screen, select the type of installation that suits your needs. For example, you can choose Developer Default, which includes the MySQL server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL for Visual Studio, and Connector/NET. Then click Next.
- On the checking requirements screen, the installer will check if your system meets the requirements for the selected setup type. If there are any missing requirements, the installer will download and install them for you. Then click Next.
- On the installation screen, the installer will show you the list of products that will be installed. Click Execute to start the installation process.
- On the product configuration screen, the installer will guide you through the configuration steps for each product. For example, for the MySQL server, you will need to choose the type and networking options, set the root password, create user accounts, and configure advanced options. Then click Next.
- On the installation complete screen, the installer will show you the status of the installation and configuration. Click Finish to complete the process.
- On the dashboard screen, you can see the list of installed products and their status. You can also launch the MySQL Shell or the MySQL Workbench to connect to the MySQL server and start working with it.

To verify the MySQL installation, you can open the MySQL Command Line Client from cmd and enter the root password. You should see a prompt like this:

```
mysql>
```

You can then run some basic commands to check the server version, the databases, and the tables. For example:

```
mysql> SELECT VERSION();
+-----------+
| VERSION() |
+-----------+
| 8.0.23    |
+-----------+
1 row in set (0.00 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)

mysql> USE mysql;
Database changed
mysql> SHOW TABLES;
+---------------------------+
| Tables_in_mysql           |
+---------------------------+
| columns_priv              |
| component                 |
| db                        |
| default_roles             |
| engine_cost               |
| func                      |
| general_log               |
| global_grants             |
| gtid_executed             |
| help_category             |
| help_keyword              |
| help_relation             |
| help_topic                |
| innodb_index_stats        |
| innodb_table_stats        |
| password_history          |
| plugin                    |
| procs_priv                |
| proxies_priv              |
| role_edges                |
| server_cost               |
| servers                   |
| slave_master_info         |
| slave_relay_log_info      |
| slave_worker_info         |
| slow_log                  |
| tables_priv               |
| time_zone                 |
| time_zone_leap_second     |
| time_zone_name            |
| time_zone_transition      |
| time_zone_transition_type |
| user                      |
+---------------------------+
34 rows in set (0.00 sec)
```

You have successfully installed and verified the MySQL database on Windows. You can now use it to design server site applications using JDDC, ODBC and section tracking API in the subject of Web Technology Lab.