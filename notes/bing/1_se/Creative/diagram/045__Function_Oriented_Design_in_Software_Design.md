Function Oriented Design is a method to software design where the model is decomposed into a set of interacting units or modules where each unit or module has a clearly defined function . The system is designed from a functional viewpoint .

#### Function Oriented Design in Software Design

The following diagram illustrates the basic architecture of a Function Oriented Design in Software Design using ASCII characters:

```
+-----------------+       +-----------------+       +-----------------+
|  Input Module   |       |  Processing     |       |  Output Module  |
|                 |       |  Module         |       |                 |
|  Reads data     |       |  Performs       |       |  Displays data  |
|  from source    | +---> |  calculations   | +---> |  to destination |
|  and validates  |       |  and logic      |       |  and formats    |
+-----------------+       +-----------------+       +-----------------+
```

Each module has a specific function and communicates with other modules through data flows. The data flows are represented by arrows and show the direction and nature of data movement. The modules can be further decomposed into submodules if needed.