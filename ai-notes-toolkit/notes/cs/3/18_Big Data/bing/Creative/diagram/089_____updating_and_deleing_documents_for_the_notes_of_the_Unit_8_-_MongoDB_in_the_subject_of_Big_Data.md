### Updating and Deleting Documents

- MongoDB provides various methods to update and delete documents from a collection.
- To update a document, MongoDB provides update operators, such as `$set`, to modify field values. To use the update operators, pass to the update methods an update document of the form: `{<operator1>: { <field1>: <value1>, ... }, ...}`.
- To delete a document, MongoDB provides delete operators, such as `$deleteOne`, to remove a single document from a collection. To use the delete operators, pass to the delete methods a filter document that matches the document to delete.
- Some of the methods for updating and deleting documents are:

  - `db.collection.updateOne()`: Updates a single document that matches the filter.
  - `db.collection.updateMany()`: Updates all documents that match the filter.
  - `db.collection.replaceOne()`: Replaces the content of a single document that matches the filter with the specified replacement document.
  - `db.collection.deleteOne()`: Deletes a single document that matches the filter.
  - `db.collection.deleteMany()`: Deletes all documents that match the filter.
  - `db.collection.remove()`: Removes documents from a collection by matching the filter. This method is deprecated in MongoDB 4.0.

- Examples of updating and deleting documents:

  - To update the `quantity` field of the document with `_id` value `100` in the `inventory` collection, use the following command:

    ```js
    db.inventory.updateOne(
      { _id: 100 },
      { $set: { quantity: 500 } }
    )
    ```

  - To update the `status` field of all documents in the `orders` collection with `status` value `pending` to `completed`, use the following command:

    ```js
    db.orders.updateMany(
      { status: "pending" },
      { $set: { status: "completed" } }
    )
    ```

  - To replace the entire document with `_id` value `101` in the `products` collection with a new document, use the following command:

    ```js
    db.products.replaceOne(
      { _id: 101 },
      { name: "Laptop", price: 999, category: "Electronics" }
    )
    ```

  - To delete the document with `_id` value `102` in the `customers` collection, use the following command:

    ```js
    db.customers.deleteOne(
      { _id: 102 }
    )
    ```

  - To delete all documents in the `logs` collection, use the following command:

    ```js
    db.logs.deleteMany(
      {}
    )
    ```