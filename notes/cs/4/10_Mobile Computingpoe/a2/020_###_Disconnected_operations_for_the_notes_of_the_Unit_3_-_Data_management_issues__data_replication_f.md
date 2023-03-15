 Here is the content in markdown format for the topic ### Disconnected operations for the notes of the Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile in the subject of Mobile Computing:

### Disconnected operations

- Mobile devices may move in and out of connectivity resulting in disconnected operations. Data needs to be synchronized when connectivity is available again.
- Some ways to handle disconnected operations:
    - Data replication: Copying data from central database to local database on mobile device. Allows operations on local data and syncing later.
    - Data sharing: Sharing data among nearby mobile devices and synchronizing with central database later. Uses short range communication technologies like Bluetooth or Wi-Fi ad-hoc networks.
    - Accepting writes locally and syncing later: Allowing updates on local database and syncing to central database later. Conflicts can occur and need to be resolved.
- Mnemonic: Replicate or share data locally and sync later when connectivity is available to handle disconnected operations.

### Data management issues

- Managing data on mobile devices and synchronization with central database leads to some issues:
    - Limited storage on mobile devices: Need to selectively replicate data.
    - Bandwidth constraints: Need efficient synchronization techniques.
    - Security: Need to protect data on mobile devices and during transmission.
    - Conflicts: Need automatic or manual resolution of conflicts during synchronization.
- Examples of data management issues and solutions:
    - Caching data on mobile devices: Replicate selective data and update caches efficiently.
    - Differential synchronization: Sync only changed data to save bandwidth.
    - Data encryption: Protect data using encryption techniques.
    - Timestamp based conflict resolution: Choose latest updates as final values to resolve conflicts.

[Detailed diagrams and examples can be added here if required to help understand the concepts better.]