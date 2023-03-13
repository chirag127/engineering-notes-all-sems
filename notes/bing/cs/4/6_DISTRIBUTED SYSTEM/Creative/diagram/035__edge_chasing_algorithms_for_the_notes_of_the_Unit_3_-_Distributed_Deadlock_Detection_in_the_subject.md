The edge chasing algorithm for distributed deadlock detection is based on the Chandy-Misra-Haas's algorithm for the AND request model. It uses a special message called probe, which is a triplet (i, j, k), denoting that it belongs to a deadlock detection initiated by process Pi and it is being sent by the home site of process Pj to the home site of process Pk .

The following diagram illustrates the basic architecture of an edge chasing algorithm for distributed deadlock detection using ASCII characters:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     Site 1     |      |     Site 2     |      |     Site 3     |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     P1         |      |     P2         |      |     P3         |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|     P4         |      |     P5         |      |     P6         |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+

P1 -> P2: request
P2 -> P3: request
P3 -> P1: request
P1 -> P4: request
P4 -> P5: request
P5 -> P6: request
P6 -> P4: request

P1 initiates deadlock detection and sends probe (1, 1, 2) to site 2
Site 2 forwards probe (1, 1, 2) to P2
P2 forwards probe (1, 2, 3) to site 3
Site 3 forwards probe (1, 2, 3) to P3
P3 forwards probe (1, 3, 1) to site 1
Site 1 detects a cycle and informs P1 of deadlock
```