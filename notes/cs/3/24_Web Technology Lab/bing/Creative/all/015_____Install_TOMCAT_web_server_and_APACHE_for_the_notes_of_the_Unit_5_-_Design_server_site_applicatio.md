# Install TOMCAT web server and APACHE

- Apache Tomcat is an open source web server and servlet container that supports Java applications.
- Apache HTTP Server is a web server that can work with Tomcat to serve static and dynamic web content.
- To install and configure Tomcat and Apache, follow these steps:

## 1. Install Java
- Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system.
- You can download the latest JDK from https://www.oracle.com/java/technologies/downloads/.
- Follow the instructions to install the JDK and set the JAVA_HOME environment variable to point to the installation directory.

## 2. Create Tomcat System User
- Running Tomcat as the root user is not recommended for security reasons.
- You can create a dedicated system user and group for Tomcat with the following commands:

```bash
sudo groupadd tomcat
sudo useradd -s /bin/false -g tomcat -d /opt/tomcat tomcat
```

- This will create a tomcat user and group with no login shell and a home directory at /opt/tomcat.

## 3. Install and Configure Apache Tomcat
- You can download the latest Tomcat binary distribution from https://tomcat.apache.org/download-10.cgi.
- Choose the tar.gz file under the Core section and save it to your system.
- Extract the file to the /opt/tomcat directory with the following commands:

```bash
sudo mkdir /opt/tomcat
sudo tar xzvf apache-tomcat-10*tar.gz -C /opt/tomcat --strip-components=1
```

- Change the ownership and permissions of the Tomcat files and directories with the following commands:

```bash
sudo chown -R tomcat: /opt/tomcat
sudo chmod +x /opt/tomcat/bin/*.sh
```

- Create a systemd service file for Tomcat with the following command:

```bash
sudo nano /etc/systemd/system/tomcat.service
```

- Paste the following content into the file and save it:

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

- Reload the systemd daemon and start the Tomcat service with the following commands:

```bash
sudo systemctl daemon-reload
sudo systemctl start tomcat
```

- Enable the Tomcat service to start on boot with the following command:

```bash
sudo systemctl enable tomcat
```

- Verify that Tomcat is running by accessing http://your_server_ip:8080 in your web browser. You should see the Tomcat default page.

## 4. Install Apache HTTP Server
- You can install Apache HTTP Server from the default repositories with the following command:

```bash
sudo apt install apache2
```

- Start and enable the Apache service with the following commands:

```bash
sudo systemctl start apache2
sudo systemctl enable apache2
```

- Verify that Apache is running by accessing http://your_server_ip in your web browser. You should see the Apache default page.

## 5. Configure Tomcat to Work with Apache
- To enable Apache to communicate with Tomcat, you need to install and configure a connector module called mod_jk.
- You can install mod_jk from the default repositories with the following command:

```bash
sudo apt install libapache2-mod-jk
```

- Create a workers.properties file for mod_jk with the following command:

```bash
sudo nano /etc/libapache2-mod-jk/workers.properties
```

- Paste the following content into the file and save it:

```ini
# Define 1 real worker using ajp13
worker