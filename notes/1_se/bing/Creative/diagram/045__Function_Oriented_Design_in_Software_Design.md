Function Oriented Design is an approach to software design where the design is decomposed into a set of interacting units or modules where each unit has a clearly defined function. The design can be represented graphically or mathematically by the following notations:

- Data Flow Diagram (DFD): A data flow diagram (DFD) maps out the flow of information for any process or system. It uses defined symbols like rectangles, circles and arrows, plus short text labels, to show data inputs, outputs, storage points and the routes between each destination.
- Data Dictionaries: Data dictionaries are simply repositories to store information about all data items defined in DFDs. At the requirement stage, data dictionaries contains data items. Data dictionaries include Name of the item, Aliases (Other names for items), Description / purpose, Related data items, Range of values, Data structure definition / form.
- Structure Charts: Structure charts are the hierarchical representation of system which partitions the system into black boxes (functionality is known to users but inner details are unknown). Components are read from top to bottom and left to right. When a module calls another, it views the called module as black box, passing required parameters and receiving results.
- Pseudo Code: Pseudo code is system description in short English like phrases describing the function. It use keyword and indentation. Pseudo codes are used as replacement for flow charts. It decreases the amount of documentation required.

#### Function Oriented Design in Software Design

The following diagram illustrates the basic architecture of a function oriented design in software design using the DFD notation:

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Input Module  |------>|  Process Module|------>|  Output Module |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
     |  ^                      |  ^                      |  ^
     |  |                      |  |                      |  |
     v  |                      v  |                      v  |
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|  Input Data    |       |  Process Data  |       |  Output Data   |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
```

The input module is responsible for reading the data from the source and validating it. The process module is responsible for applying the logic and algorithms to the data and producing the desired output. The output module is responsible for formatting and displaying the output to the user or the destination. The data flows between the modules and the data stores are represented by arrows. The data stores are represented by rectangles with two parallel lines. The modules are represented by rectangles with rounded corners. The data items are represented by short text labels.