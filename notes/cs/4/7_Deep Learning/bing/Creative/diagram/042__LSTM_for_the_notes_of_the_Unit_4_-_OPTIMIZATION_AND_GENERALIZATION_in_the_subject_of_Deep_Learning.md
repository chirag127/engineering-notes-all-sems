The following diagram illustrates the basic architecture of a LSTM unit for the notes of the Unit 4 - OPTIMIZATION AND GENERALIZATION in the subject of Deep Learning.

```
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
|     Input      |   |     Input      |   |     Input      |
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
+----------------+   +----------------+   +----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       v                    v                    v
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
|     LSTM       |   |     LSTM       |   |     LSTM       |
|     Unit       |   |     Unit       |   |     Unit       |
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
+----------------+   +----------------+   +----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       v                    v                    v
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
|     Output     |   |     Output     |   |     Output     |
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
+----------------+   +----------------+   +----------------+
```

Each LSTM unit consists of a cell, an input gate, an output gate, and a forget gate. The cell stores the long-term memory, while the gates regulate the flow of information into and out of the cell. The input gate decides which values from the input to update the memory state. The output gate determines what to output based on the input and the memory. The forget gate decides what to erase from the memory. The following diagram shows the internal structure of a LSTM unit.

```
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
|     Input      |   |     Input      |   |     Input      |
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
+----------------+   +----------------+   +----------------+
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       |                    |                    |
       v                    v                    v
+----------------+   +----------------+   +----------------+
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
|     LSTM       |   |     LSTM       |   |     LSTM       |
|     Unit       |   |     Unit       |   |     Unit       |
|                |   |                |   |                |
|                |   |                |   |                |
|                |   |                |   |                |
+----------------+   +----------------+