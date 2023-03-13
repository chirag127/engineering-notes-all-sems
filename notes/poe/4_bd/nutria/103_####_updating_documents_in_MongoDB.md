
#### Updating Documents in MongoDB

1. To update a document in MongoDB, you need to use the `update()` method. This method takes two parameters: the filter object and the update object. 
2. The filter object is used to specify which documents should be updated. This object can contain any valid MongoDB query. 
3. The update object is used to specify what should be updated in the documents that match the filter. This object can contain any valid MongoDB update operators. 
4. To update a single document, use the `updateOne()` method. This method takes two parameters: the filter object and the update object. 
5. To update multiple documents, use the `updateMany()` method. This method takes two parameters: the filter object and the update object. 
6. To update all documents, use the `replaceOne()` method. This method takes two parameters: the filter object and the update object. 
7. To update a document and return the updated document, use the `findOneAndUpdate()` method. This method takes three parameters: the filter object, the update object and the options object. 
8. To update multiple documents and return the updated documents, use the `bulkWrite()` method. This method takes two parameters: the filter object and the update object. 
9. To update a document and return the original document, use the `findOneAndReplace()` method. This method takes three parameters: the filter object, the update object and the options object. 
10. To update multiple documents and return the original documents, use the `bulkWrite()` method. This method takes two parameters: the filter object and the update object. 
11. To update a document atomically, use the `findOneAndUpdate()` method. This method takes three parameters: the filter object, the update object and the options object. The `options` object should contain the `upsert` and `returnOriginal` fields set to `true`. 
12. To update multiple documents atomically, use the `bulkWrite()` method. This method takes two parameters: the filter object and the update object. The `update` object should contain the `upsert` and `returnOriginal` fields set to `true`.