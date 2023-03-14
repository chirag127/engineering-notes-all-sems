Various size oriented measures are derived by normalizing quality and/or productivity measures by considering the size of the software that has been produced. The size of the software is usually expressed as kilo lines of code (KLOC), which is the number of lines of code in thousands. However, different programming languages and coding styles may affect the number of lines of code, so this measure is not very reliable or consistent.

Some examples of size oriented measures are:

- Effort = person-months / KLOC
- Productivity = KLOC / person-months
- Quality = number of faults / KLOC
- Cost = dollars / KLOC
- Documentation = pages of documentation / KLOC

The following diagram illustrates the basic architecture of a size oriented measure:

```
+-----------------+     +-----------------+     +-----------------+
| Quality Measure |     | Productivity    |     | Cost Measure    |
+-----------------+     | Measure         |     +-----------------+
| Number of faults|     | KLOC            |     | Dollars         |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
| Size Measure    |     | Effort Measure  |     | Documentation   |
+-----------------+     +-----------------+     | Measure         |
| KLOC            |     | Person-months   |     +-----------------+
+-----------------+     +-----------------+     | Pages of        |
                                                 | documentation   |
                                                 +-----------------+
```