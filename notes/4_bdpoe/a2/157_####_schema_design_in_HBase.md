 Here is the content in markdown format on the topic #### schema design in HBase:

#### Schema Design in HBase

- Decide on row key design:
-- Row key should be unique and sortable.
-- Choose a design that suites your access patterns (sequential, random, indexed). For e.g. timestamp, alphanumeric etc.
-- Avoid hotspots by salting/hashing row keys.
- Choose column families:
-- Group related columns into column families.
-- Ideally keep column families < 4-5.
-- Choose a compact design: have similar access/update patterns in one CF.
-- Choose appropriate compression for each CF.
- Deal with versioning:
-- Don't use excessively high max versions if not required. It wastes space.
-- Use TTL to auto-delete old versions if timeline based data.
- Data modeling:
-- Denormalize and store duplicate data if fast read speed is priority.
-- Normalize if you can't store duplicates (less storage but slower reads).
-- If both speed and storage are priority, hybrid approach.

Some Mnemonics/Tips:
- Rowkey: Timeseries data -> timestamp, User data -> uid
- CFs: Related data together, keep < 5
- Versions: Low unless needed, use TTL for old data
- Data modeling: Denormalize for fast reads, Normalize for less storage

[Detailed diagrams, examples, codes, pros/cons, applications can be added here if helpful for learning.]

The content is written in points and in a formal tone as requested. I have included some Mnemonics/tips where applicable. Please let me know if you would like me to modify or add any other details to the content.