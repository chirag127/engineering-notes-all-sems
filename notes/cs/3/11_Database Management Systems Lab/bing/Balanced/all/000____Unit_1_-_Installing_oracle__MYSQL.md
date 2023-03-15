## Unit 1 - Installing Oracle/MySQL

Oracle and MySQL are two popular relational database management systems (RDBMS) that can store, manage, and manipulate data. To use them, you need to install them on your computer or server. Here are the steps to install Oracle and MySQL on Windows and Linux platforms.

### Installing Oracle on Windows

- Download the Oracle Database installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Run the installer as an administrator and follow the instructions on the screen. You will need to provide a password for the SYS and SYSTEM accounts, which are the default administrative accounts for Oracle.
- Choose the installation type and the location for the Oracle home directory, where the software and data files will be stored.
- Review the summary and click Install to start the installation process. The installer will create and configure the database and the listener, which is a service that enables communication between the database and the clients.
- After the installation is complete, you can use the Oracle Database Configuration Assistant to create additional databases, modify the existing database, or delete the database.
- You can also use the Oracle SQL Developer, a graphical tool that allows you to interact with the database, execute SQL statements, and perform other tasks.

### Installing Oracle on Linux

- Download the Oracle Database installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Transfer the installer files to the Linux machine and unzip them in a directory of your choice.
- Log in as the root user or a user with sudo privileges and run the following commands to install the required packages and dependencies:

```bash
yum install -y oracle-database-preinstall-19c
yum install -y binutils
yum install -y compat-libcap1
yum install -y compat-libstdc++-33
yum install -y elfutils-libelf
yum install -y elfutils-libelf-devel
yum install -y gcc
yum install -y gcc-c++
yum install -y glibc
yum install -y glibc-devel
yum install -y ksh
yum install -y libaio
yum install -y libaio-devel
yum install -y libgcc
yum install -y libstdc++
yum install -y libstdc++-devel
yum install -y make
yum install -y sysstat
```

- Create a new user and group for the Oracle installation, such as oracle and oinstall, and assign the appropriate permissions and ownership to the installer directory and the Oracle home directory, where the software and data files will be stored.
- Log in as the oracle user and run the installer from the installer directory. Follow the instructions on the screen. You will need to provide a password for the SYS and SYSTEM accounts, which are the default administrative accounts for Oracle.
- Choose the installation type and the location for the Oracle home directory.
- Review the summary and click Install to start the installation process. The installer will create and configure the database and the listener, which is a service that enables communication between the database and the clients.
- After the installation is complete, you can use the Oracle Database Configuration Assistant to create additional databases, modify the existing database, or delete the database.
- You can also use the Oracle SQL Developer, a graphical tool that allows you to interact with the database, execute SQL statements, and perform other tasks.

### Installing MySQL on Windows

- Download the MySQL installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Run the installer as an administrator and follow the instructions on the screen. You will need to accept the license agreement and choose the setup type and the products to install. The installer will download and install the selected products.
- Configure the MySQL server by choosing the configuration type, the port number, the root password, and the authentication method. You can also create additional user accounts and enable or disable the MySQL service.
- After the configuration is complete, you can use the MySQL Workbench, a graphical tool that allows you to interact with the database, execute SQL statements, and perform other tasks.

### Installing MySQL on Linux

- Download the MySQL installer from the official website. Choose the edition and version that suits your needs and system requirements.
- Transfer the installer files to the Linux machine and unzip them in a directory of your choice.
- Log in as the root user or a user with sudo privileges and run the following commands to install the required packages and dependencies:

```bash
yum install -y libaio
yum install -y numactl
```

- Run the installer from the installer directory and follow the instructions on the screen. You will need to accept the license agreement and choose the installation type and the location for the MySQL home directory, where