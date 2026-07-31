# Unit 1 - Installing Oracle/MySQL in the subject of Database Management Systems Lab

## Oracle Installation

- Oracle is a relational database management system (RDBMS) that supports the creation and management of data, applications, and information.
- Oracle can be installed on various operating systems, such as Windows, Linux, Mac OS, etc.
- To install Oracle on Windows, the following steps are required:

  - Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
  - Choose the appropriate edition and version of Oracle Database for your system and download the zip file.
  - Extract the zip file to a folder and run the setup.exe file as administrator.
  - Follow the instructions on the installation wizard and choose the installation type, destination folder, database configuration, etc.
  - Wait for the installation to complete and verify that the Oracle Database service is running on your system.

- To install Oracle on Linux, the following steps are required:

  - Download the Oracle Database installer from the official website: https://www.oracle.com/database/technologies/oracle-database-software-downloads.html
  - Choose the appropriate edition and version of Oracle Database for your system and download the zip file.
  - Transfer the zip file to your Linux system and extract it to a folder.
  - Run the runInstaller script as root user and follow the instructions on the installation wizard.
  - Choose the installation type, destination folder, database configuration, etc.
  - Wait for the installation to complete and verify that the Oracle Database service is running on your system.

## MySQL Installation

- MySQL is an open-source relational database management system (RDBMS) that supports the creation and management of data, applications, and information.
- MySQL can be installed on various operating systems, such as Windows, Linux, Mac OS, etc.
- To install MySQL on Windows, the following steps are required:

  - Download the MySQL installer from the official website: https://dev.mysql.com/downloads/installer/
  - Choose the appropriate edition and version of MySQL for your system and download the exe file.
  - Run the exe file as administrator and follow the instructions on the installation wizard.
  - Choose the installation type, destination folder, database configuration, etc.
  - Wait for the installation to complete and verify that the MySQL service is running on your system.

- To install MySQL on Linux, the following steps are required:

  - Download the MySQL installer from the official website: https://dev.mysql.com/downloads/repo/yum/
  - Choose the appropriate edition and version of MySQL for your system and download the rpm file.
  - Transfer the rpm file to your Linux system and install it using the command: sudo rpm -ivh mysql-<version>.rpm
  - Run the command: sudo yum install mysql-server to install the MySQL server package.
  - Start the MySQL service using the command: sudo systemctl start mysqld
  - Verify that the MySQL service is running on your system using the command: sudo systemctl status mysqld