

### Concepts in Backward and Forward Recovery for the Notes of the Unit 6 - Failure Recovery in Distributed Systems in the Subject of DISTRIBUTED SYSTEM

1. **Backward Recovery**: Backward recovery involves restoring the system to a previous state before a failure occurs. This is done by using a log or record of transactions that have been completed, which allows the system to undo any changes that have been made since the last backup. This type of recovery is often used for databases, as it allows for the data to be restored to its original state.

2. **Mnemonic for Backward Recovery**: The acronym B.A.C.K.U.P. stands for Backup All Completed Transactions, Unfinished Transactions, and Previous States.

3. **Forward Recovery**: Forward recovery involves restoring the system to a state after a failure has occurred. This is done by using a log or record of transactions that have been completed, which allows the system to redo any changes that have been made since the last backup. This type of recovery is often used for databases, as it allows for the data to be restored to its most recent state.

4. **Mnemonic for Forward Recovery**: The acronym F.O.R.W.A.R.D. stands for Fixing Outdated Records, Wiping Away Redundant Data, and Doing the Actions Again.

5. **Advantages of Recovery**: Recovery techniques can be used to restore data that has been lost due to hardware or software failures, as well as to prevent data loss due to malicious attacks. Recovery techniques can also be used to restore data that has been corrupted due to human error.

6. **Disadvantages of Recovery**: Recovery techniques can be time-consuming and costly, as they require the system to be taken offline while the recovery process is being performed. Additionally, recovery techniques may not be able to restore all of the data that has been lost or corrupted.

7. **Examples of Recovery**: 
  - Backward recovery can be used to restore a database to its original state before a failure occurred. 
  - Forward recovery can be used to restore a database to its most recent state after a failure occurred. 
  - Recovery techniques can be used to restore data that has been lost due to hardware or software failures, as well as to prevent data loss due to malicious attacks.

8. **Applications of Recovery**: Recovery techniques can be used in many different applications, such as databases, file systems, and operating systems. Recovery techniques can also be used to restore data that has been corrupted due to human error.