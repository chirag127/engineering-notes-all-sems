#### Deleting Documents in MongoDB

MongoDB is a NoSQL database that stores data in collections. In MongoDB, documents can be deleted using various methods. Here are some ways to delete documents in MongoDB:

1. Using the `deleteOne()` method: This method is used to delete a single document that matches a specified filter.

   ```javascript
   db.collection.deleteOne(filter, options)
   ```

   - `filter`: A document that specifies the criteria used to select the document to delete.
   - `options`: An optional document that specifies additional options.

2. Using the `deleteMany()` method: This method is used to delete multiple documents that match a specified filter.

   ```javascript
   db.collection.deleteMany(filter, options)
   ```

   - `filter`: A document that specifies the criteria used to select the documents to delete.
   - `options`: An optional document that specifies additional options.

3. Using the `remove()` method: This method is used to delete a single document that matches a specified filter.

   ```javascript
   db.collection.remove(filter, options)
   ```

   - `filter`: A document that specifies the criteria used to select the document to delete.
   - `options`: An optional document that specifies additional options.

   **Note:** The `remove()` method is deprecated and may be removed in future versions of MongoDB.

4. Using the `drop()` method: This method is used to delete an entire collection.

   ```javascript
   db.collection.drop()
   ```

   **Note:** The `drop()` method is irreversible and permanently deletes the collection and its data.

5. Using the `dropDatabase()` method: This method is used to delete an entire database.

   ```javascript
   db.dropDatabase()
   ```

   **Note:** The `dropDatabase()` method is irreversible and permanently deletes the database and its data.

It is important to exercise caution when deleting documents in MongoDB. Always make sure to have a backup of your data before performing any deletions.