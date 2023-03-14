The following diagram illustrates the classification of distributed mutual exclusion algorithms based on the information from the search results   :

```
+----------------------------------------+
| Distributed Mutual Exclusion Algorithms |
+----------------------------------------+
|                                        |
+----------------+-----------------------+
| Token-based   | Non-token-based       |
+----------------+-----------------------+
|               |                       |
+-------+-------+-------+---------------+
| Ring  | Tree  | Other | Permission-   |
| based | based | based | based         |
+-------+-------+-------+---------------+
|       |       |       |               |
+-------+-------+-------+-------+-------+
|       |       |       | Quorum| Other |
|       |       |       | based |       |
+-------+-------+-------+-------+-------+
```