
### Installing Tomcat and Apache for Unit 5 - Designing Server-Side Applications Using JDDC, ODBC and Session Tracking API

This section of the Web Technology Lab will provide instructions on how to install Tomcat and Apache for use in server-side applications.

#### Installing Tomcat

1. Download the latest version of Tomcat from [Apache Tomcat](https://tomcat.apache.org/download-90.cgi).
2. Extract the downloaded zip file to a directory of your choice.
3. Open the Tomcat installation directory and run the **startup.bat** file.
4. Once the Tomcat server has started, open a web browser and enter the following URL: `http://localhost:8080` to access the Tomcat home page.

#### Installing Apache

1. Download the latest version of Apache from [Apache HTTP Server](https://httpd.apache.org/download.cgi).
2. Extract the downloaded zip file to a directory of your choice.
3. Open the Apache installation directory and run the **httpd.exe** file.
4. Once the Apache server has started, open a web browser and enter the following URL: `http://localhost:80` to access the Apache home page.

#### Configuring Tomcat and Apache

1. Open the Tomcat installation directory and navigate to the `conf` directory.
2. Open the **server.xml** file and add the following line: `<Connector port="80" protocol="HTTP/1.1" connectionTimeout="20000" redirectPort="8443" />`
3. Open the Apache installation directory and navigate to the `conf` directory.
4. Open the **httpd.conf** file and add the following line: `ProxyPass / http://localhost:8080/`

Once Tomcat and Apache have been installed and configured, you can begin developing server-side applications using JDDC, ODBC, and session tracking API.