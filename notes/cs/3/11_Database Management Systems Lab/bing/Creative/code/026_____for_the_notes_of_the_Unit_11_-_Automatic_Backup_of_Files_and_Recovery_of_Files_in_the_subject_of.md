# Unit 11 - Automatic Backup of Files and Recovery of Files in Database Management Systems Lab

- Automatic backup is a feature that allows the database system to perform regular backups of the data and log files without manual intervention.
- Automatic backup can help improve data protection, disaster recovery, and business continuity by reducing the risk of data loss, corruption, or human error.
- Automatic backup can be configured to run at specific intervals, events, or conditions, depending on the database system and the backup strategy.
- Automatic backup can be performed online (while the database is operational) or offline (while the database is shut down), depending on the recovery model of the database.
- Recovery model is a property of the database that determines how the transaction log is maintained and how the database can be restored.
- Recovery model can be either simple, full, or bulk-logged, depending on the level of data protection and point-in-time recovery required.
- Simple recovery model does not support point-in-time recovery and requires only full backups and differential backups.
- Full recovery model supports point-in-time recovery and requires full backups, differential backups, and transaction log backups.
- Bulk-logged recovery model supports point-in-time recovery, except for bulk operations, and requires full backups, differential backups, and transaction log backups.
- Recovery is a process that restores the database to a consistent state by applying the data and log pages from the backups and rolling forward or backward the transactions that are logged in the backups.
- Recovery can be performed to the most recent state or to a specific point-in-time, depending on the backup strategy and the recovery model of the database.
- Recovery can be performed to a specific data backup or data snapshot, which is a point-in-time copy of the database that can be created and restored quickly.
- Recovery can be performed using various tools and commands, depending on the database system and the backup format.