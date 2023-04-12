### Install TOMCAT web server and APACHE

Tomcat is an open source web server and servlet container that supports Java applications. Apache is a popular web server that can work with Tomcat to serve dynamic web pages. To install and configure Tomcat and Apache, follow these steps:

1. Install Java. Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system. You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/ and follow the installation instructions for your operating system.
2. Create a Tomcat system user. It is not recommended to run Tomcat as the root user, as it poses a security risk. You can create a dedicated user and group for Tomcat with the following commands:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

3. Install and configure Tomcat. You can download the latest version of Tomcat from https://tomcat.apache.org/download-10.cgi and extract the files to a suitable location, such as /opt/tomcat. You can also change the ownership and permissions of the Tomcat files to the tomcat user and group with the following commands:

```bash
sudo chown -R tomcat:tomcat /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
```

You can also edit the Tomcat configuration file (/opt/tomcat/conf/server.xml) to change the default port number, enable HTTPS, or add virtual hosts. For more details, see https://tomcat.apache.org/tomcat-10.0-doc/config/index.html.
4. Create a Tomcat systemd service. To start and stop Tomcat as a service, you need to create a systemd unit file for Tomcat. You can create a file named /etc/systemd/system/tomcat.service with the following content:

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

You can also modify the environment variables according to your Java and Tomcat settings. After creating the file, you need to reload the systemd daemon and enable the Tomcat service with the following commands:

```bash
sudo systemctl daemon-reload
sudo systemctl enable tomcat
```

You can then start, stop, or check the status of the Tomcat service with the following commands:

```bash
sudo systemctl start tomcat
sudo systemctl stop tomcat
sudo systemctl status tomcat
```

5. Install Apache HTTP Server. You can install Apache from the official repositories of your operating system using the package manager. For example, on Ubuntu, you can use the following command:

```bash
sudo apt install apache2
```

You can also configure Apache according to your needs, such as changing the document root, enabling SSL, or adding virtual hosts. For more details, see https://httpd.apache.org/docs/2.4/.
6. Configure Tomcat to work with Apache. To connect Tomcat and Apache, you need to use a connector module called mod_jk. You can download the latest version of mod_jk from https://tomcat.apache.org/download-connectors.cgi and compile it from source. Alternatively, you can install it from the official repositories of your operating system using the package manager. For example, on Ubuntu, you can use the following command:

```bash
sudo apt install libapache2-mod-jk
```

You also need to configure mod_jk to communicate with Tomcat. You can create a file named /etc/apache2/workers.properties with the following content:

```ini
worker.list=worker1
worker.worker1.type=ajp13
worker

```
