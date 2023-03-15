### Install TOMCAT web server and APACHE for the notes of the Unit 5 - Design server site applications using JDDC,ODBC and section tracking API in the subject of Web Technology Lab

- TOMCAT is an open source web server and servlet container that supports Java Servlet and JavaServer Pages (JSP) technologies.
- APACHE is an open source web server that can handle requests from various protocols, such as HTTP, HTTPS, FTP, and SMTP.
- To install TOMCAT and APACHE on a Windows system, follow these steps:

  1. Download the latest version of TOMCAT from https://tomcat.apache.org/download-10.cgi and extract the zip file to a desired location, such as C:\tomcat.
  2. Download the latest version of APACHE from https://httpd.apache.org/download.cgi and run the installer. Follow the instructions and choose the default options, such as the installation directory (C:\Apache24) and the server name (localhost).
  3. To configure APACHE to work with TOMCAT, open the file C:\Apache24\conf\httpd.conf in a text editor and add the following lines at the end of the file:

```
# Load the proxy modules
LoadModule proxy_module modules/mod_proxy.so
LoadModule proxy_http_module modules/mod_proxy_http.so
LoadModule proxy_ajp_module modules/mod_proxy_ajp.so

# Proxy requests to TOMCAT
ProxyPass /tomcat http://localhost:8080/
ProxyPassReverse /tomcat http://localhost:8080/
```

  4. To test the installation, start both TOMCAT and APACHE by running the files C:\tomcat\bin\startup.bat and C:\Apache24\bin\httpd.exe respectively. Then open a web browser and go to http://localhost/tomcat. You should see the TOMCAT welcome page.
  5. To stop both TOMCAT and APACHE, run the files C:\tomcat\bin\shutdown.bat and C:\Apache24\bin\httpd.exe -k stop respectively.