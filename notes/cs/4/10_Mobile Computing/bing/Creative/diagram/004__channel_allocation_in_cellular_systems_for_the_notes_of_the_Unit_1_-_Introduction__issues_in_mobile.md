Channel allocation in cellular systems is the process of assigning the available channels to the cells in a cellular network. Channel allocation strategies aim to maximize the system capacity and minimize the interference among the cells that share the same frequency band. There are two main types of channel allocation schemes: fixed and dynamic. Fixed channel allocation (FCA) assigns a predetermined set of channels to each cell manually, while dynamic channel allocation (DCA) assigns channels to cells based on the current traffic demand and interference conditions. A simple example of FCA is shown in the following diagram, where each cell is assigned a set of three channels out of a total of seven channels available in the system. The channels are reused in a pattern that ensures a minimum distance between the cells that use the same channel.

```
    A   B   A   B   A
   / \ / \ / \ / \ / \
  C   D   C   D   C   D
 / \ / \ / \ / \ / \ / \
A   B   A   B   A   B   A
 \ / \ / \ / \ / \ / \ /
  D   C   D   C   D   C
   \ / \ / \ / \ / \ /
    B   A   B   A   B
```