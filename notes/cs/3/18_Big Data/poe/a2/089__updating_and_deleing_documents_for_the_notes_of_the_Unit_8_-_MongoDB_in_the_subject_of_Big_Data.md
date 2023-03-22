 Here is the content in markdown format without any emojis or external links:

### Updating and Deleting Documents

Some key points on updating and deleting documents in MongoDB:

1. Updating Documents:
- Use the update_one() or update_many() methods to update documents.
- Specify the filter criteria to select the document to update.
- Pass the updated data to be replaced/updated in the document.
- Use operators like $set to update only specific fields and prevent overriding entire document.

2. Deleting Documents:
- Use the delete_one() or delete_many() methods to delete documents.
- Specify the filter criteria to select the document(s) to delete.
- Deleted documents are removed instantly.

3. Other Considerations:
- MongoDB updates and deletes are atomic at the document level.
- If the update/delete does not match any documents, no errors are returned (update_one returns nModified= 0).
- Updates and deletes do not support rollbacks - be careful when implementing these operations.

The content here is formal and written in points without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.