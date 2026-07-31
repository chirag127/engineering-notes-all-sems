 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Log-based Recovery

1. Transaction logs maintain a record of all data modifications made by transactions. These logs are used to recover the database in case of a system failure.
2. There are two types of logs:
- Redo logs: Contains records of all changes made by transactions. Used to restore the database to a consistent state by re-applying all changes in the log.
- Undo logs: Contains records of original values before a change was made. Used to undo uncommitted changes and restore the database to a consistent state.
3. Recovery process:
- Analyze the log and determine which transactions committed and which aborted.
- For committed transactions, redo all changes recorded in the log. This ensures that all changes of completed transactions are reflected in the database.
- For aborted transactions, undo all changes recorded in the log. This undoes the changes made by incomplete transactions and restores original values.
- Once all log entries have been processed, the database is consistent and recovery is complete.

The above content summarizes the key points about log-based recovery in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.