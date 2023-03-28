

### Multi Version Schemes

Multi version schemes are a type of concurrency control technique used in database management systems. This approach allows multiple users to access and modify the same data simultaneously, while also providing a way to maintain data integrity and consistency. 

The main idea behind multi version schemes is to create multiple versions of the same data. When a user attempts to modify the data, a new version is created. This version is then stored in the database and made available to other users. The original version is also stored, so that the user can revert back to it if needed.

The main advantages of multi version schemes include:

- Data integrity is maintained, as no user can overwrite another user’s changes.
- Data consistency is maintained, as all users will always be working with the same version of the data.
- Performance is improved, as multiple users can access and modify the same data simultaneously.
- Data is protected, as previous versions of the data are stored in the database.

The main disadvantage of multi version schemes is that they require a large amount of storage space, as multiple versions of the same data must be stored.