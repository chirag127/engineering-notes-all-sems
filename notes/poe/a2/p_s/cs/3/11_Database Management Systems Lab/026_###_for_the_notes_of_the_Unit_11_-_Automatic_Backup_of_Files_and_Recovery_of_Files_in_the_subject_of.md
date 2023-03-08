 Here is the content in markdown format for the notes of Unit 11 - Automatic Backup of Files and Recovery of Files in Database Management Systems Lab:

### Automatic Backup of Files and Recovery of Files

- Regular backup of database files is necessary to prevent data loss in case of any failure or disaster.
- Automatic backup can be scheduled to run at regular intervals or specific times.
- The backup files can be stored in a separate system or in the same system at a different location.
- The backup files should be verified regularly to ensure the data is consistent and can be recovered properly if needed.
- In case of any failure or corruption of database files, the backup files can be used to recover the data and restart the database.
- The recovered files should be tested properly before putting the database into use again to check for any inconsistencies or issues.
- Depending on the criticality of the data and recovery requirements, the backup files can be full backup, differential backup or transaction log backup.
- Full backup backs up the entire database but takes more time and resources. Differential backup backs up only the changes since last full backup and is faster. Transaction log backups the transaction logs to enable point-in-time recovery but the log files should be managed properly to avoid issues.
- The backup and recovery process should be automated as much as possible to reduce manual efforts and chances of errors. Appropriate alerts should be setup to notify administrators of any failures or issues with the backup or recovery process.

[Diagrams, examples, codes, tables, advantages, disadvantages, and applications can be added here if required.]