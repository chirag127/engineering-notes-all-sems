Networking in Scripting is the process of using scripts to automate various network administration tasks, such as mapping network drives, configuring network devices, monitoring network performance, and troubleshooting network issues. Scripts are written in different languages, such as shell, Python, PowerShell, Perl, and Ruby, and can be executed on different platforms, such as Windows, Linux, and macOS.

The following diagram illustrates the basic architecture of a network script:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Script Host    |        |  Network Device |        |  Network Device |
|                 |        |                 |        |                 |
|  +-----------+  |        |  +-----------+  |        |  +-----------+  |
|  |           |  |        |  |           |  |        |  |           |  |
|  |  Script   |  |        |  |  Config   |  |        |  |  Config   |  |
|  |           |  |        |  |           |  |        |  |           |  |
|  +-----+-----+  |        |  +-----+-----+  |        |  +-----+-----+  |
|        |        |        |        |        |        |        |        |
+--------+--------+        +--------+--------+        +--------+--------+
         |                         |                         |
         |                         |                         |
         +-------------------------+-------------------------+
                               |
                               |
                               v
                        +-----------------+
                        |                 |
                        |  Network Script |
                        |                 |
                        |  +-----------+  |
                        |  |           |  |
                        |  |  Logic    |  |
                        |  |           |  |
                        |  +-----+-----+  |
                        |        |        |
                        +--------+--------+
                                 |
                                 |
                                 v
                        +-----------------+
                        |                 |
                        |  Script Output  |
                        |                 |
                        +-----------------+
```

The script host is the machine where the script is executed. It can be a local or remote computer, depending on the script language and the network protocol used. The script host communicates with the network devices through the network script, which contains the logic and commands to perform the network administration tasks. The network script can use different protocols, such as SSH, Telnet, SNMP, REST, or NETCONF, to interact with the network devices. The network devices are the routers, switches, firewalls, or other devices that are configured, monitored, or troubleshooted by the script. The network devices have their own configuration files, which store the settings and parameters of the device. The script output is the result of the script execution, which can be displayed on the screen, saved to a file, or sent to a database or a monitoring system. The script output can show the status, performance, or configuration of the network devices, or any errors or warnings that occurred during the script execution.