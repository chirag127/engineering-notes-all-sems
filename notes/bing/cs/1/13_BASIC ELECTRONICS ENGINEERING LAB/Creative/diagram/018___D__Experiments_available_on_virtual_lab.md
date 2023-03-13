There are many types of experiments available on virtual lab, depending on the subject and the level of difficulty. Some examples are:

- Chemistry experiments: These involve simulating chemical reactions, synthesis, analysis, and separation of substances using virtual lab equipment and tools. For example, you can perform a titration, a chromatography, or a synthesis of aspirin using virtual lab.
- Physics experiments: These involve simulating physical phenomena, such as motion, forces, energy, waves, and electricity using virtual lab instruments and models. For example, you can measure the speed of sound, the acceleration of gravity, or the resistance of a circuit using virtual lab.
- Biology experiments: These involve simulating biological processes, such as cell division, DNA replication, enzyme activity, and photosynthesis using virtual lab microscopes and animations. For example, you can observe the stages of mitosis, the structure of DNA, or the effect of temperature on enzyme activity using virtual lab.

The following diagram illustrates the basic architecture of a virtual lab:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|   User Device   |      |   Web Server    |      |   Virtual Lab   |
|                 |      |                 |      |                 |
|  - Web Browser  | <--> |  - Web Service  | <--> |  - Lab Engine   |
|  - User Input   |      |  - Lab Content  |      |  - Lab Model    |
|  - Lab Output   |      |                 |      |  - Lab Data     |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The user device is the device that the user uses to access the virtual lab, such as a computer, a tablet, or a smartphone. It has a web browser that can display the lab content and interact with the web server.

The web server is the server that hosts the web service and the lab content. It receives the user input from the web browser and sends it to the virtual lab. It also receives the lab output from the virtual lab and sends it to the web browser.

The virtual lab is the server that runs the lab engine and the lab model. It simulates the lab experiments using the lab data and the user input. It generates the lab output and sends it to the web server.