

#### Capped Collections in MongoDB

- Capped collections are a special type of collection in MongoDB which have a fixed size and a fixed order.
- They are used to store data in a more efficient manner than normal collections.
- Capped collections are created with a size limit and once the limit is reached, the oldest documents are automatically removed to make room for new documents.
- Capped collections have a few advantages over regular collections:
  - They are faster to read and write from, as they are stored in a fixed order.
  - They are more space efficient, as they only store the documents that fit within the size limit.
  - They are more secure, as documents cannot be removed or modified once they have been added.
- Capped collections are best used for storing data that needs to be accessed quickly and is not expected to change often.
- They are often used for logging and auditing, as they can store a fixed amount of data and provide an easy way to retrieve the latest documents.
- Mnemonics and learning tricks for capped collections in MongoDB include:
  - C for Capped: Capped collections are collections with a fixed size and order.
  - F for Faster: Capped collections are faster to read and write from than regular collections.
  - S for Secure: Capped collections are more secure than regular collections, as documents cannot be removed or modified once they have been added.
  - L for Logging: Capped collections are often used for logging and auditing, as they can store a fixed amount of data and provide an easy way to retrieve the latest documents.