## Unit 1 - Installing Oracle/MySQL

Oracle and MySQL are two popular relational database management systems (RDBMS) that can store, manipulate, and retrieve data. To use them, you need to install them on your computer or server. Here are the steps to install Oracle and MySQL on Windows and Linux platforms.

### Installing Oracle on Windows

- Download the Oracle Database installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Run the installer as an administrator and follow the instructions on the screen. You will need to provide a password for the system and sys accounts, which are the default administrative users for Oracle.
- Choose the type of installation you want: typical, custom, or advanced. Typical installation will install the most common components and features, while custom and advanced installation will allow you to select the components and features you want to install.
- Choose the location where you want to install Oracle. The default location is C:\app\username\product\version\dbhome_1.
- Wait for the installation to complete. You can check the progress and status of the installation on the screen.
- After the installation is done, you can launch the Oracle Database Configuration Assistant to create and configure a database. You can also use the Oracle Enterprise Manager Database Express to manage and monitor your database.

### Installing Oracle on Linux

- Download the Oracle Database installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Transfer the installer to your Linux machine using a secure method, such as SCP or SFTP. You can also use a USB drive or a CD-ROM to copy the installer to your Linux machine.
- Log in to your Linux machine as the root user or a user with sudo privileges. Create a new user and group for Oracle, such as oracle and oinstall. You will use this user and group to install and run Oracle.
- Create a directory where you want to install Oracle, such as /u01/app/oracle. Change the ownership and permissions of this directory to the oracle user and oinstall group.
- Install the required packages and dependencies for Oracle. You can use the yum or apt-get commands to install them. Some of the packages and dependencies are: binutils, gcc, glibc, libaio, libnsl, libstdc++, make, and unzip.
- Set the environment variables for Oracle, such as ORACLE_BASE, ORACLE_HOME, ORACLE_SID, and PATH. You can use the export command to set them in the .bash_profile file of the oracle user.
- Run the installer as the oracle user and follow the instructions on the screen. You will need to provide a password for the system and sys accounts, which are the default administrative users for Oracle.
- Choose the type of installation you want: typical, custom, or advanced. Typical installation will install the most common components and features, while custom and advanced installation will allow you to select the components and features you want to install.
- Choose the location where you want to install Oracle. The default location is /u01/app/oracle/product/version/dbhome_1.
- Wait for the installation to complete. You can check the progress and status of the installation on the screen.
- After the installation is done, you can launch the Oracle Database Configuration Assistant to create and configure a database. You can also use the Oracle Enterprise Manager Database Express to manage and monitor your database.

### Installing MySQL on Windows

- Download the MySQL installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement and choose the type of setup you want: developer default, server only, client only, or custom. Developer default will install the most common components and features, while custom will allow you to select the components and features you want to install.
- Choose the location where you want to install MySQL. The default location is C:\Program Files\MySQL.
- Configure the MySQL server. You will need to provide a password for the root user, which is the default administrative user for MySQL. You will also need to choose the authentication method, the network configuration, the Windows service name, and the advanced options for your MySQL server.
- Wait for the installation and configuration to complete. You can check the progress and status of the installation on the screen.
- After the installation and configuration is done, you can launch the MySQL Workbench to manage and monitor your MySQL server. You can also use the MySQL Shell or the MySQL Command-Line Client to interact with your MySQL server.

### Installing MySQL on Linux

- Download the MySQL installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Transfer the installer to