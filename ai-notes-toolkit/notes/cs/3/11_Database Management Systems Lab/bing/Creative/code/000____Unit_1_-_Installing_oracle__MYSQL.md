## Unit 1 - Installing Oracle/MySQL

Oracle and MySQL are two popular relational database management systems (RDBMS) that can be used to store, manage and manipulate data. In this unit, we will learn how to install Oracle and MySQL on Windows and Linux operating systems.

### Installing Oracle on Windows

To install Oracle on Windows, you need to follow these steps:

1. Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
2. Choose the edition and version of Oracle that suits your needs and system requirements. For example, you can choose Oracle Database 19c Standard Edition 2 for Windows x64.
3. Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement, choose the installation type (typical or custom), specify the installation location, create an Oracle home user and password, and configure the database options.
4. Wait for the installation to complete and verify that the Oracle services are running in the Windows Services console. You can also launch the Oracle Database Configuration Assistant to create and manage databases.
5. To connect to the Oracle database, you can use tools such as SQL Developer, SQL*Plus, or Oracle Net Manager.

### Installing Oracle on Linux

To install Oracle on Linux, you need to follow these steps:

1. Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
2. Choose the edition and version of Oracle that suits your needs and system requirements. For example, you can choose Oracle Database 19c Enterprise Edition for Linux x86-64.
3. Transfer the installer files to the Linux server and unzip them in a directory of your choice. You will need to have enough disk space and memory to install Oracle.
4. Log in as the root user and run the oracle-database-preinstall-19c package to install the required dependencies and create the oracle user and groups. You can also manually perform these tasks by following the instructions in the Oracle documentation: https://docs.oracle.com/en/database/oracle/oracle-database/19/ladbi/index.html
5. Log in as the oracle user and run the runInstaller script to launch the installer. You will need to accept the license agreement, choose the installation type (typical or custom), specify the installation location, create an Oracle inventory, and configure the database options.
6. Wait for the installation to complete and verify that the Oracle services are running in the Linux Services console. You can also launch the Oracle Database Configuration Assistant to create and manage databases.
7. To connect to the Oracle database, you can use tools such as SQL Developer, SQL*Plus, or Oracle Net Manager.

### Installing MySQL on Windows

To install MySQL on Windows, you need to follow these steps:

1. Download the MySQL Installer from the official website: https://dev.mysql.com/downloads/installer/
2. Choose the edition and version of MySQL that suits your needs and system requirements. For example, you can choose MySQL Installer 8.0.26 for Windows.
3. Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement, choose the setup type (developer default, server only, client only, or custom), specify the installation location, configure the MySQL server, create a root password, and configure the MySQL products.
4. Wait for the installation to complete and verify that the MySQL services are running in the Windows Services console. You can also launch the MySQL Workbench to create and manage databases.
5. To connect to the MySQL database, you can use tools such as MySQL Workbench, MySQL Shell, or MySQL Connector.

### Installing MySQL on Linux

To install MySQL on Linux, you need to follow these steps:

1. Download the MySQL repository package from the official website: https://dev.mysql.com/downloads/repo/
2. Choose the repository package that matches your Linux distribution and version. For example, you can choose MySQL 8.0 Community Server for Ubuntu 20.04.
3. Transfer the repository package to the Linux server and install it using the appropriate package manager. For example, you can use the dpkg command for Debian-based distributions or the rpm command for Red Hat-based distributions.
4. Update the package information and install the MySQL server and client packages using the appropriate package manager. For example, you can use the apt command for Debian-based distributions or the yum command for Red Hat-based distributions.
5. Start the MySQL service and verify that it is running in the Linux Services console. You can also launch the mysql_secure_installation script to set a root password and secure the MySQL installation.
6. To connect to the MySQL database,