### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer, which is the recommended method . MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.

The following are the steps to install MySQL database on Windows:

- Download MySQL Installer from https://dev.mysql.com/downloads/installer/ and execute it. You can choose either the web-community version or the full version depending on your needs  .
- On the welcome screen, choose the first option: Install MySQL Products.
- On the license agreement screen, read the terms and conditions and accept them if you agree.
- On the choosing a setup type screen, select the type of installation that suits your requirements. You can choose either Developer Default, Server Only, Client Only, or Custom . For this tutorial, we will choose Developer Default, which includes MySQL Server, MySQL Workbench, MySQL Connector/ODBC, and other tools.
- On the checking requirements screen, the installer will check if your system meets the prerequisites for the selected products. If any requirements are missing, the installer will download and install them for you .
- On the installation screen, the installer will show the progress of installing the selected products. You can click Show Details to see more information .
- On the product configuration screen, the installer will guide you through the configuration of MySQL Server and other products. You can click Next to accept the default options or change them as per your preferences . Some of the options include:
  - Type and Networking: You can choose the configuration type (Development, Server, or Custom) and the network port and protocol for MySQL Server .
  - Authentication Method: You can choose the authentication method (Strong Password Encryption or Legacy Authentication) for MySQL Server .
  - Accounts and Roles: You can create a root password and add other user accounts and roles for MySQL Server .
  - Windows Service: You can configure the Windows service name, start type, and account for MySQL Server .
  - Apply Configuration: The installer will apply the configuration settings and start the MySQL Server service .
- On the installation complete screen, the installer will show the status of the installation and configuration. You can click Finish to exit the installer .

To verify the installation of MySQL database, you can open the MySQL Command Line Client from the Start menu or the cmd and enter the root password. You should see a prompt like this:

```sql
mysql>
```

You can then enter SQL commands to interact with the MySQL database .

: https://www.w3schools.com/mysql/mysql_install_windows.asp
: https://dev.mysql.com/doc/mysql-getting-started/en/
: https://www.mysqltutorial.org/install-mysql/
: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html
: https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/