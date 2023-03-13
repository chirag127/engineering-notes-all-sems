 Here is the content in markdown format for the topic ### Cloud Storage for the notes of the Unit 3 - Cloud Architecture, Services And Storage in the subject of Cloud Computing:

### Cloud Storage

- Cloud storage refers to a model of storing and accessing data over the internet instead of on a local device. The data is stored in logical pools, typically referred to as object storage or blob storage.
- The three main types of cloud storage are:
    - Object storage - Data is stored as objects/blobs with metadata. Example - Amazon S3, Azure Blob Storage.
    - File storage - Data is stored in a hierarchical file system. Example - Azure Files, Amazon EFS.
    - Block storage - Data is stored in block storage devices. Example - Amazon EBS, Azure Disks.
- Advantages:
    - Scalability - Storage capacity can be easily scaled up/down as per requirements.
    - Durability - Data is redundantly stored across multiple servers/locations to prevent loss.
    - Availability - Data can be accessed from anywhere on any device.
    - Low cost - Pay only for what you use.
- Disadvantages:
    - Dependency - Reliance on internet connectivity and cloud provider.
    - Vendor lock-in - Difficult to migrate data between cloud providers.
    - Security - Responsibility of the customer to enable appropriate security controls.
- Use cases:
    - Backup and archival storage.
    - Web hosting.
    - Mobile application data storage.
    - Analytics and big data storage.

- Mnemonics:
    - C - Scalable, cheap
    - L - Accessible from anywhere
    - O - Object, file, block storage types
    - U - Durability and availability

- Code example:
// Upload an object to Amazon S3
s3.putObject({
    Bucket: 'mybucket',
    Key: 'mykey',
    Body: 'Hello World!'
});

- Diagrams and detailed explanations can be added if required. The content can be modified as needed to best suit learning and exam preparation.