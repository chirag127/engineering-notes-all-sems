#### Querying documents in MongoDB

- MongoDB is a document-oriented database that stores data in collections of JSON-like documents.
- To query data from a collection, you can use the `db.collection.find()` method, which returns a cursor to the matching documents.
- The `find()` method accepts two optional parameters: a filter document and a projection document.
- The filter document specifies the query criteria, or the conditions to match documents in the collection.
- The projection document specifies the fields to include or exclude in the query result.
- You can use various query operators to specify complex conditions in the filter document, such as logical operators (`$and`, `$or`, `$not`, `$nor`), comparison operators (`$eq`, `$gt`, `$lt`, `$in`, `$nin`, etc.), array operators (`$all`, `$elemMatch`, `$size`, etc.), and element operators (`$exists`, `$type`, etc.).
- You can also query embedded documents and arrays using the dot notation (`field.subfield`) or the array index notation (`field.0`).
- You can use the `pretty()` method to format the query output in a readable way.
- You can use the `limit()`, `skip()`, and `sort()` methods to modify the cursor behavior and order the query result.

Here is an example of querying documents in MongoDB using the `find()` method:

```javascript
// Connect to the MongoDB shell as the administrative user
mongo -u admin -p password --authenticationDatabase admin

// Switch to the sample database
use sample

// Insert some documents into the mountains collection
db.mountains.insertMany([
  {
    name: "Mount Everest",
    height: 8848,
    location: "Nepal-China",
    first_ascent: {
      year: 1953,
      climbers: ["Edmund Hillary", "Tenzing Norgay"]
    }
  },
  {
    name: "K2",
    height: 8611,
    location: "Pakistan-China",
    first_ascent: {
      year: 1954,
      climbers: ["Achille Compagnoni", "Lino Lacedelli"]
    }
  },
  {
    name: "Kangchenjunga",
    height: 8586,
    location: "Nepal-India",
    first_ascent: {
      year: 1955,
      climbers: ["George Band", "Joe Brown"]
    }
  },
  {
    name: "Lhotse",
    height: 8516,
    location: "Nepal-China",
    first_ascent: {
      year: 1956,
      climbers: ["Fritz Luchsinger", "Ernst Reiss"]
    }
  },
  {
    name: "Makalu",
    height: 8485,
    location: "Nepal-China",
    first_ascent: {
      year: 1955,
      climbers: ["Jean Couzy", "Lionel Terray"]
    }
  }
])

// Query all documents in the collection
db.mountains.find()

// Query documents where the height is greater than 8500
db.mountains.find({height: {$gt: 8500}})

// Query documents where the location contains "Nepal"
db.mountains.find({location: /Nepal/})

// Query documents where the first ascent year is 1955
db.mountains.find({"first_ascent.year": 1955})

// Query documents where the first ascent climbers array has two elements
db.mountains.find({"first_ascent.climbers": {$size: 2}})

// Query documents where the name is "K2" or "Lhotse"
db.mountains.find({name: {$in: ["K2", "Lhotse"]}})

// Query documents and project only the name and height fields
db.mountains.find({}, {name: 1, height: 1, _id: 0})

// Query documents and sort them by height in descending order
db.mountains.find().sort({height: -1})

// Query documents and limit the result to 3 documents
db.mountains.find().limit(3)

// Query documents and skip the first 2 documents
db.mountains.find().skip(2)
```

Here is the output of the queries:

```javascript
> db.mountains.find()
{ "_id" : ObjectId("61c1c8f2f6a0a0a1a0c1c8f2"), "name" : "Mount Everest", "height" :