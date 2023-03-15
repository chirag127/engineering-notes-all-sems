##### Halestead’s Software Science in software design

Here is an ASCII diagram for Halstead's Software Science in software design:

```
+------------------------+
|                        |
|   Halstead's Metrics   |
|                        |
+------------------------+
|                        |
|  n1 = unique operators |
|  n2 = unique operands  |
|  N1 = total operators  |
|  N2 = total operands   |
|                        |
+------------------------+
|                        |
|  Vocabulary = n1 + n2  |
|  Length = N1 + N2      |
|  Volume = Length *     |
|           log2(Vocab)  |
|                        |
+------------------------+
|                        |
|  Difficulty = (n1/2) * |
|              (N2/n2)   |
|  Effort = Difficulty * |
|           Volume       |
|                        |
+------------------------+
```
