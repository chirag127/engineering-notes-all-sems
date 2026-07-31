 Here is the content in markdown format with formal tone and without emojis:

#### Updating Documents in MongoDB

1. Use the updateOne() method to update a single document that matches a filter.
- The filter specifies which document to update.
- The update specifies how to modify the document.
- Options can be passed to control the execution.

2. Use the updateMany() method to update all documents that match a filter.
- The filter specifies which documents to update.
- The update specifies how to modify the documents.
- Options can be passed to control the execution.

3. The update can be a replacement document or an update operator.
- A replacement document will replace the entire matching document.
- Update operators specify field and value changes to be made.
- Multiple update operators can be used in a single update to modify and increment values, append arrays, etc.

4. Upserts can be used to insert a document if it does not exist.
- If the filter does not match any documents, by default the update will have no effect.
- The upsert option can be used to create and insert a new document if no match is found.
- This ensures that a document matching the filter will exist after the update, either by updating an existing document or by inserting a new one.

5. Write concerns can be passed to control how MongoDB handles the write operation.
- Acknowledgement of the write can be specified.
- The durability of the write can be specified.
- The write concern can be configured on a per-operation or global basis.