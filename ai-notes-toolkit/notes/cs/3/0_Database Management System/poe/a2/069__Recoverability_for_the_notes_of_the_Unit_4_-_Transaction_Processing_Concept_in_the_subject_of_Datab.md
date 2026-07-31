 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Recoverability for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

1. Recovery Manager - The recovery manager is responsible for restoring the database to a correct state in case of failures. It uses the log records to undo the partial effects of incomplete transactions and redo the effects of completed transactions that may not have been permanently recorded yet.
2. Checkpoint - A checkpoint is a designated place in the log at which database recovery can begin, instead of beginning recovery at the start of the log. Databases periodically write a checkpoint record to the log.
3. Shadow Paging - Shadow paging keeps old versions of pages until transactions complete. In case of a failure, these old versions can be used to roll back incomplete transactions. Shadow paging requires substantial storage for maintaining old page versions.
4. ARIES (AlgoRithm for Recovery and Isolation Exploiting Semantics) - ARIES is a recovery technique that uses write-ahead logging along with other strategies to minimize recovery time. Some of the key techniques used by ARIES are:
- Log records are written before the actual data is updated.
- Maintaining before and after images of data
- Use of fuzzy checkpoints
- Analysis of transaction semantics to determine safe recovery point

The points are written in a formal tone with no emojis or external links as per the given instructions. Please let me know if you would like me to modify or expand the answer.