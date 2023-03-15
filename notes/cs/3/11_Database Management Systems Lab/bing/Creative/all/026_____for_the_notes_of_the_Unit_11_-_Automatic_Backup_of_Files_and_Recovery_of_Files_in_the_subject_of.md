# Unit 11 - Automatic Backup of Files and Recovery of Files in Database Management Systems Lab

## Introduction

- Automatic backup is a process of creating copies of data and storing them in a separate location, without manual intervention.
- Recovery is a process of restoring data from backups in case of data loss or corruption.
- Automatic backup and recovery are essential for data protection, disaster recovery and business continuity in database management systems.

## Objectives

- To understand the concepts and benefits of automatic backup and recovery of files in database management systems.
- To learn how to configure and perform automatic backup and recovery of files in different database management systems, such as IBM DB2, Microsoft SQL Server and SAP HANA.
- To practice the backup and recovery procedures using lab exercises and scenarios.

## Topics

- Automatic backup and recovery concepts and benefits
- Automatic backup and recovery features and options in different database management systems
- Backup and recovery strategies and best practices
- Backup and recovery scenarios and exercises

## Automatic backup and recovery concepts and benefits

- Automatic backup and recovery can help to:

  - Ensure data availability and integrity in case of hardware failures, human errors, malicious attacks or natural disasters.
  - Maintain recovery point objectives (RPO) and recovery time objectives (RTO) agreed by management and users.
  - Reduce the risk of data loss and the cost of data recovery.
  - Simplify the backup and recovery operations and reduce human errors and efforts.

- Automatic backup and recovery can be enabled for either online or offline backup, depending on the recovery model of the database and the backup frequency and duration.

  - Online backup allows the database to remain accessible and operational during the backup process, but may require additional resources and affect the performance of the database.
  - Offline backup requires the database to be shut down or disconnected during the backup process, but may provide faster and more consistent backup results.

- Automatic backup and recovery can be configured and performed using various methods and tools, such as:

  - Built-in features and commands of the database management systems, such as IBM DB2 Automatic Database Backup, Microsoft SQL Server Backup and Restore, and SAP HANA Database Backup and Recovery.
  - Third-party backup software and hardware solutions, such as Veritas NetBackup, IBM Spectrum Protect, and Dell EMC Data Domain.
  - Cloud-based backup and recovery services, such as Amazon Web Services (AWS) Backup, Microsoft Azure Backup, and Google Cloud Platform (GCP) Cloud Storage.

## Automatic backup and recovery features and options in different database management systems

- IBM DB2 Automatic Database Backup

  - IBM DB2 Automatic Database Backup is a feature that enables the database to automatically perform full or incremental backups at regular intervals or based on certain events or conditions.
  - IBM DB2 Automatic Database Backup can be enabled for either online or offline backup, depending on the recovery mode of the database (archive logging or circular logging).
  - IBM DB2 Automatic Database Backup can be configured using the db2 update db cfg command or the IBM Data Studio graphical user interface (GUI).
  - IBM DB2 Automatic Database Backup can be monitored and managed using the db2 list history command or the IBM Data Studio GUI.

- Microsoft SQL Server Backup and Restore

  - Microsoft SQL Server Backup and Restore is a feature that enables the database to create and manage backups of the whole database, a file or filegroup, or a portion of the transaction log.
  - Microsoft SQL Server Backup and Restore can be performed using either the Transact-SQL (T-SQL) statements (BACKUP and RESTORE) or the SQL Server Management Studio (SSMS) GUI.
  - Microsoft SQL Server Backup and Restore supports various backup types, such as full, differential, transaction log, copy-only, file or filegroup, and partial backups.
  - Microsoft SQL Server Backup and Restore supports various backup destinations, such as disk, tape, or URL (Azure Blob Storage).

- SAP HANA Database Backup and Recovery

  - SAP HANA Database Backup and Recovery is a feature that enables the database to create and manage backups of the data and log volumes of the database.
  - SAP HANA Database Backup and Recovery can be performed using either the SQL statements (BACKUP and RECOVERY) or the SAP HANA Studio GUI.
  - SAP HANA Database Backup and Recovery supports various backup types, such as data backups, log backups, and data snapshots.
  - SAP HANA Database Backup and Recovery supports various backup destinations, such as file system, backup catalog, or third-party backup tools.

## Backup and recovery strategies and best practices

- Backup and recovery strategies and best practices can help to:

  - Define the backup and