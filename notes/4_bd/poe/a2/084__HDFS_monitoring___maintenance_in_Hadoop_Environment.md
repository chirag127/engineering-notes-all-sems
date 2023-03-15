 Here is the content in markdown format with formal tone and without emojis:

#### HDFS monitoring & maintenance in Hadoop Environment.

1. HDFS space usage monitoring
- Use df -h command to check total space and used space on HDFS.
- Use du -sh /* to check space used by each directory.
- Check for files with 0 bytes and delete them.
- Check for large files and determine if they are required. Delete if not needed.

2. HDFS capacity planning
- Monitor growth rate of data and compute required space for next 6-12 months.
- Add more nodes or replace with high capacity nodes if needed.
- Use compression and data tiering to optimize space.

3. HDFS maintenance
- Run balancer to distribute blocks evenly and optimise performance.
- Remove corrupted blocks using e.g. fsck command.
- Use trash feature to backup deleted files/folders before permanent delete.
- Use snapshots to take backups and rollback if needed.
- Upgrade Hadoop version and patch security vulnerabilities and other bugs when releases are made available.
- Tune HDFS parameters like replication factor, block size etc. based on data and workload patterns.

The above points cover key aspects of monitoring usage and planning capacity as well as ongoing maintenance activities required for HDFS in a Hadoop environment. Regular monitoring and maintenance helps optimise HDFS storage, performance and security.