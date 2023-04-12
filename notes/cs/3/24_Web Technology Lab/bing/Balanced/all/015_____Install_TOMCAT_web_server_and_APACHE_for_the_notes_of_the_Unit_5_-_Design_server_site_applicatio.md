# Install TOMCAT web server and APACHE

- Apache Tomcat is an open source web server and servlet container that supports Java applications.
- Apache HTTP Server is a web server that can work with Tomcat to serve static and dynamic web content.
- To install and configure Tomcat and Apache, follow these steps:

## 1. Install Java
- Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system.
- You can download the latest JDK from https://www.oracle.com/java/technologies/javase-downloads.html and follow the installation instructions for your operating system.
- You also need to set the JAVA_HOME environment variable to point to the JDK installation directory.

## 2. Create Tomcat System User
- Running Tomcat as the root user is not recommended for security reasons, so you should create a dedicated system user for Tomcat.
- On Linux, you can use the following commands to create a tomcat user and group:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

- On Windows, you can use the User Accounts tool in the Control Panel to create a tomcat user and assign it a password.

## 3. Install and Configure Apache Tomcat
- You can download the latest Tomcat binary distribution from https://tomcat.apache.org/download-10.cgi and choose the appropriate package for your operating system.
- On Linux, you can extract the downloaded file to /opt/tomcat and change the ownership and permissions of the files to the tomcat user and group:

```bash
sudo tar xvf apache-tomcat-10.0.13.tar.gz -C /opt/tomcat
sudo chown -R tomcat:tomcat /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
```

- On Windows, you can run the downloaded installer and follow the wizard to install Tomcat to a desired location, such as C:\Tomcat.
- You also need to configure Tomcat to work with Apache by editing the server.xml file in the conf directory of the Tomcat installation.
- You need to add a Connector element inside the Service element with the following attributes:

```xml
<Connector port="8009" protocol="AJP/1.3" redirectPort="8443" />
```

- This will enable the AJP protocol on port 8009, which is used by Apache to communicate with Tomcat.
- You also need to add an Engine element inside the Host element with the following attribute:

```xml
<Engine name="Catalina" defaultHost="localhost" jvmRoute="tomcat1">
```

- This will assign a unique name to the Tomcat instance, which is used by Apache to load balance requests among multiple Tomcat servers.

## 4. Create a Tomcat Systemd Service
- On Linux, you can create a systemd service file to manage the Tomcat service.
- You can create a file named tomcat.service in the /etc/systemd/system directory with the following content:

```ini
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

Environment=JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
Environment=CATALINA_PID=/opt/tomcat/temp/tomcat.pid
Environment=CATALINA_HOME=/opt/tomcat
Environment=CATALINA_BASE=/opt/tomcat
Environment='CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC'
Environment='JAVA_OPTS=-Djava.awt.headless=true -Djava.security.egd=file:/dev/./urandom'

ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

User=tomcat
Group=tomcat
UMask=0007
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target
```

- You need to adjust the JAVA_HOME and CATALINA_HOME variables according to your Java and Tomcat installation paths.
- You also need to reload the systemd daemon and enable the Tomcat service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
```

- You can then start, stop, and check the status of the Tomcat service using the following commands:

```bash
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl status tom

```
