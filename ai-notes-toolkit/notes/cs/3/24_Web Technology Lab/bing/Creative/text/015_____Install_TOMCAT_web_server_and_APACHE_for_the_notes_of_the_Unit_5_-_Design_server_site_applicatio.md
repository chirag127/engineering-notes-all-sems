### Install TOMCAT web server and APACHE

- Tomcat is an open source web server and servlet container that supports Java applications.
- Apache is a popular web server that can work with Tomcat to serve dynamic web pages.
- To install Tomcat and Apache on a Linux system, follow these steps:

  1. Install Java
     - Tomcat requires Java to run, so you need to install a Java Development Kit (JDK) on your system.
     - You can use the following command to install the default JDK package from the repository:

       ```bash
       sudo apt update
       sudo apt install default-jdk
       ```

     - You can verify the installation by checking the Java version:

       ```bash
       java -version
       ```

  2. Create Tomcat System User
     - Running Tomcat as the root user is not recommended for security reasons.
     - You can create a dedicated system user and group for Tomcat with the following command:

       ```bash
       sudo useradd -r -m -U -d /opt/tomcat -s /bin/false tomcat
       ```

     - This command creates a user named tomcat, with a home directory at /opt/tomcat, and a disabled login shell.

  3. Install and Configure Apache Tomcat
     - You can download the latest version of Tomcat from the official website:

       ```bash
       wget https://downloads.apache.org/tomcat/tomcat-10/v10.0.14/bin/apache-tomcat-10.0.14.tar.gz -P /tmp
       ```

     - You can extract the downloaded archive to the /opt/tomcat directory:

       ```bash
       sudo tar xf /tmp/apache-tomcat-*.tar.gz -C /opt/tomcat
       ```

     - You can create a symbolic link to the Tomcat installation directory for easier management:

       ```bash
       sudo ln -s /opt/tomcat/apache-tomcat-10.0.14 /opt/tomcat/latest
       ```

     - You can change the ownership of the Tomcat files to the tomcat user and group:

       ```bash
       sudo chown -RH tomcat: /opt/tomcat/latest
       ```

     - You can make the Tomcat scripts executable:

       ```bash
       sudo sh -c 'chmod +x /opt/tomcat/latest/bin/*.sh'
       ```

  4. Create a Tomcat Systemd Service
     - To run Tomcat as a service, you need to create a systemd unit file for it.
     - You can use the following command to create a file named tomcat.service in the /etc/systemd/system directory:

       ```bash
       sudo nano /etc/systemd/system/tomcat.service
       ```

     - You can paste the following content into the file:

       ```ini
       [Unit]
       Description=Tomcat 10 servlet container
       After=network.target

       [Service]
       Type=forking

       User=tomcat
       Group=tomcat

       Environment="JAVA_HOME=/usr/lib/jvm/default-java"
       Environment="JAVA_OPTS=-Djava.security.egd=file:///dev/urandom -Djava.awt.headless=true"

       Environment="CATALINA_BASE=/opt/tomcat/latest"
       Environment="CATALINA_HOME=/opt/tomcat/latest"
       Environment="CATALINA_PID=/opt/tomcat/latest/temp/tomcat.pid"
       Environment="CATALINA_OPTS=-Xms512M -Xmx1024M -server -XX:+UseParallelGC"

       ExecStart=/opt/tomcat/latest/bin/startup.sh
       ExecStop=/opt/tomcat/latest/bin/shutdown.sh

       [Install]
       WantedBy=multi-user.target
       ```

     - You can save and close the file by pressing Ctrl+O and Ctrl+X.
     - You can reload the systemd daemon to apply the changes:

       ```bash
       sudo systemctl daemon-reload
       ```

     - You can start the Tomcat service with the following command:

       ```bash
       sudo systemctl start tomcat
       ```

     - You can check the status of the service with the following command:

       ```bash
       sudo systemctl status tomcat
       ```

     - You can enable the service to start on boot with the following command:

       ```bash
       sudo systemctl enable tomcat
       ```

  5. Install Apache HTTP Server