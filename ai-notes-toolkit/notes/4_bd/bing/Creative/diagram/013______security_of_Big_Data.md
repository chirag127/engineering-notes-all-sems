#### Security of Big Data

Big data security is the process of implementing safeguards to protect an enterprise’s big data from unauthorized access or breaches throughout the entirety of its lifecycle. Big data security’s mission is to keep out unauthorized users and intrusions with firewalls, strong user authentication, end-user training, and intrusion protection systems (IPS) and intrusion detection systems (IDS). In case someone does gain access, encrypt your data in transit and at rest. Big data security also involves securing the data and analytics methods from malicious activities, such as theft, attacks, intrusions, and anything that can cause negative effects to them.

A possible diagram for big data security is:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Data Sources  |    |   Data Storage  |    |   Data Analysis |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| - Web           |    | - Hadoop        |    | - Spark         |
| - Social Media  |    | - NoSQL         |    | - R             |
| - IoT           |    | - Cloud         |    | - Python        |
| - Sensors       |    | - File Systems  |    | - SQL           |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| - Data Quality  |    | - Encryption    |    | - Data Privacy  |
| - Data Cleaning |    | - Compression   |    | - Data Masking  |
| - Data Parsing  |    | - Backup        |    | - Data Auditing |
| - Data Filtering|    | - Access Control|    | - Data Reporting|
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| |             | |    | |             | |    | |             | |
| |  Firewalls  | |    | |  Firewalls  | |    | |  Firewalls  | |
| |             | |    | |             | |    | |             | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| |             | |    | |             | |    | |             | |
| |  IPS/IDS    | |    | |  IPS/IDS    | |    | |  IPS/IDS    | |
| |             | |    | |             | |    | |             | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```