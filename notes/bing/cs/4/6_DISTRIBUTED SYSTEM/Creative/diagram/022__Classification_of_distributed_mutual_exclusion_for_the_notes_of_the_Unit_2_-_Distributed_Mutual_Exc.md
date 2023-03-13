The following is a detailed ASCII diagram for the classification of distributed mutual exclusion algorithms for the notes of the Unit 2 - Distributed Mutual Exclusion in the subject of DISTRIBUTED SYSTEM.

### Classification of distributed mutual exclusion algorithms

```
+--------------------------------------------+
|                                            |
| Distributed mutual exclusion algorithms    |
|                                            |
+--------------------------------------------+
|                                            |
+----------------+---------------------------+
|                |                           |
| Token-based   | Non-token-based           |
|                |                           |
+----------------+---------------------------+
|                |                           |
| +------------+ | +-----------------------+ |
| | Centralized| | | Centralized           | |
| +------------+ | +-----------------------+ |
|                |                           |
| +------------+ | +-----------------------+ |
| | Distributed| | | Distributed           | |
| +------------+ | +-----------------------+ |
|                |                           |
| +------------+ | +-----------------------+ |
| | Ring       | | | Ricart-Agrawala      | |
| +------------+ | +-----------------------+ |
|                |                           |
+----------------+---------------------------+
|                                            |
+----------------+---------------------------+
|                |                           |
| Quorum-based  | Hybrid                    |
|                |                           |
+----------------+---------------------------+
|                |                           |
| +------------+ | +-----------------------+ |
| | Maekawa    | | | Suzuki-Kasami        | |
| +------------+ | +-----------------------+ |
|                |                           |
| +------------+ | +-----------------------+ |
| | Tree-based | | | Raymond's tree-based | |
| +------------+ | +-----------------------+ |
|                |                           |
+----------------+---------------------------+
```