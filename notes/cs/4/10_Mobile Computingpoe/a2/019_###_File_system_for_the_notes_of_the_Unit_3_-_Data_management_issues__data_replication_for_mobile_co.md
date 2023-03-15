 Here is the content in Markdown format:

### File system for the notes of the Unit 3 - Data management issues, data replication for mobile computers, adaptive clustering for mobile in the subject of Mobile Computing

**Mnemonics:**
- Mobile File System (MoFS) - remembers that the file system is for mobile computing to handle issues like limited storage, disconnections, etc.

**Points:**
1. Specialized file system required for mobile devices due to limited storage and possibility of disconnections.
2. File system should handle caching, prefetching, and replication of data to enable offline access and faster access.
3. **MoFS (Mobile File System)** - export parts of file hierarchy based on access patterns and prefetch files to be accessed.
4. **UbiCache file system** - separates file metadata and data and replicates metadata on mobile device for access during disconnections. Data cached based on usage.
5. **Coda file system** - disconnected operation supported. Updates cached and synced when connection is available. Conflicts resolved using policies.
6. **MTCI file system** - based on NFS and supports disconnections via caching and update propagation. Updates take precedence over caches.

**Diagrams:**
[Include diagrams to show the working of MoFS or any other mobile file system and its components]

**Advantages:**
- Enable offline access and faster access via caching and prefetching
- Changes synchronized when connected preserving consistency
- Limited storage optimized via exporting parts of file hierarchy or separation of metadata and data

**Disadvantages:**
- Complex as compared to traditional file systems due to additional components and logic to handle disconnections and limited storage
- Prefetching and caching can lead to unused data occupying space if access patterns change
- Additional overhead of propagating updates and resolving conflicts when devices connect

**Applications:** Mobile computing and devices like laptops, tablets, smartphones, etc.