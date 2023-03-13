The following diagram illustrates the basic architecture of a system that can measure the viscosity, conductance of solution, chloride and iron content in the water.

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Water sample   |      | Viscosity      |      | Viscosity      |
|                +----->+ sensor         +----->+ data           |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Conductance    |      | Conductance    |      | Conductance    |
| sensor         +----->+ data           +----->+ analyzer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Chloride and   |      | Chloride and   |      | Chloride and   |
| iron sensor    +----->+ iron data      +----->+ analyzer       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The water sample is collected from the source and passed through three sensors: a viscosity sensor, a conductance sensor, and a chloride and iron sensor. The sensors measure the respective properties of the water and send the data to the corresponding data modules. The data modules store and process the data and send it to the analyzers. The analyzers compare the data with the standard values and determine the quality of the water. The analyzers can also display the results on a screen or print a report.