
### Capped Collections for the Notes of the Unit 8 - MongoDB in the Subject of Big Data

* MongoDB is a document-oriented database that uses a data model comprised of collections and documents. 
* Capped collections are a type of MongoDB collection that have a fixed size and a set number of documents. 
* Capped collections are ideal for handling data that needs to be stored in a fixed order and accessed quickly.
* Capped collections are created using the `createCollection()` method with the `capped` option set to `true`.
* The `max` option specifies the maximum size of the collection in bytes and the `size` option specifies the initial size of the collection in bytes.
* MongoDB will automatically delete documents from the collection when it reaches its maximum size.
* Capped collections are ideal for storing data such as log files or audit trails.