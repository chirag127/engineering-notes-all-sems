The following diagram illustrates the basic architecture of a smart metering system for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things. The diagram is drawn using ASCII characters and does not include any links or URLs.

```
+-----------------+       +-----------------+       +-----------------+
| Smart Meter     |       | Gateway/Bridge  |       | IoT Central     |
|                 |       |                 |       |                 |
| - Records and   |       | - Connects smart|       | - Connects,     |
|   communicates  |<----->|   meters to IoT |<----->|   monitors, and |
|   energy data   |       |   Central       |       |   manages smart |
| - Supports      |       | - Supports      |       |   meters        |
|   commands and  |       |   various       |       | - Provides      |
|   updates       |       |   protocols     |       |   dashboards,   |
| - Supports      |       | - Can be a      |       |   rules, and    |
|   bidirectional |       |   physical or   |       |   analytics     |
|   communication |       |   cloud device  |       | - Exposes APIs  |
+-----------------+       +-----------------+       |   and data      |
                                                    |   export        |
                                                    +-----------------+
```