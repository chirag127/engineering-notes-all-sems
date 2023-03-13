The following diagram illustrates the basic architecture of a path-pushing algorithm for distributed deadlock detection. The diagram is drawn using ASCII characters.

### Path-pushing algorithm for distributed deadlock detection

    +--------+     +--------+     +--------+
    | Site 1 |     | Site 2 |     | Site 3 |
    +--------+     +--------+     +--------+
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
    +--------+     +--------+     +--------+
    | Local  |     | Local  |     | Local  |
    | WFG    |     | WFG    |     | WFG    |
    +--------+     +--------+     +--------+
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
    +--------+     +--------+     +--------+
    | Dead-  |     | Dead-  |     | Dead-  |
    | lock   |     | lock   |     | lock   |
    | compu- |     | compu- |     | compu- |
    | tation |     | tation |     | tation |
    +--------+     +--------+     +--------+
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        |              |              |
        +--------------+--------------+
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               |              |
               +--------------+
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |
                      |