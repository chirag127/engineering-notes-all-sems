### Install a database (Mysql or Oracle) for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

This section will explain how to install MySQL database on Windows using the MySQL Installer . MySQL is a popular open-source relational database management system that can be used to store and manipulate data for web applications.

The steps to install MySQL database are as follows:

1. Download MySQL Installer for Windows from https://dev.mysql.com/downloads/installer/ and execute it. This will launch the MySQL Installer wizard that will guide you through the installation process.
2. On the welcome screen, choose the first option: Install MySQL Products. This will check for the latest updates and download them if available.
3. On the Choosing a Setup Type screen, select the setup type that suits your needs. You can choose from Developer Default, Server Only, Client Only, or Custom. For this tutorial, we will choose Developer Default, which will install the MySQL Server, MySQL Workbench, MySQL Shell, MySQL Router, MySQL Notifier, and other tools.
4. On the Check Requirements screen, review the list of software that will be installed or updated. If there are any missing prerequisites, the installer will download and install them for you. Click Next to continue.
5. On the Installation screen, click Execute to start the installation of the selected products. This may take some time depending on your internet speed and system performance. You can monitor the progress of each product on the screen.
6. On the Product Configuration screen, click Next to configure the MySQL Server. You will need to specify the following options:
   - Type and Networking: Choose the configuration type for your server. You can choose from Development Machine, Server Machine, or Dedicated Machine. For this tutorial, we will choose Development Machine, which will optimize the server for local development. You can also choose the port number and the network protocols for your server. The default port number is 3306 and the default protocol is TCP/IP. You can leave these as they are unless you have a specific reason to change them.
   - Authentication Method: Choose the authentication method for your server. You can choose from Strong Password Encryption for Authentication (recommended) or Use Legacy Authentication Method (Retain MySQL 5.x Compatibility). For this tutorial, we will choose the recommended option, which will use the caching_sha2_password plugin for password encryption and authentication.
   - Accounts and Roles: Set the password for the root user, which is the administrator account for your server. You can also create other user accounts and assign them roles and privileges. For this tutorial, we will only set the password for the root user and leave the rest as default.
   - Windows Service: Choose whether to run the MySQL Server as a Windows service or not. If you choose to run it as a service, you can also specify the service name, the start type, and the account that will run the service. For this tutorial, we will choose to run the MySQL Server as a service with the default options.
   - Apply Configuration: Click Execute to apply the configuration settings to your server. This will initialize the server, start the service, and test the connection. You can view the details of each step on the screen.
7. On the Installation Complete screen, click Next to finish the installation process. You can also choose to view the log file or the product manual if you want.
8. On the Finish screen, click Finish to exit the MySQL Installer wizard. You have successfully installed the MySQL database on your Windows machine.

You can verify the installation by opening the MySQL Command Line Client from cmd and entering the password for the root user. You should see a prompt like this:

```sql
mysql>
```

You can also use the MySQL Workbench, MySQL Shell, or any other tool to connect to and interact with your MySQL server.

: https://dev.mysql.com/doc/mysql-getting-started/en/
: https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html