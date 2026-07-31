## Implementing 4x1 and 8x1 MULTIPLEXERS

- A multiplexer (MUX) is a digital device that selects one of its inputs and forwards it to the output based on some selection lines.
- A 4x1 MUX has 4 data inputs, 2 selection lines and one output. A 8x1 MUX has 8 data inputs, 3 selection lines and one output.
- To implement a 8x1 MUX using lower order MUXes, we can use two 4x1 MUXes and one 2x1 MUX as follows:

```
    +---+       +---+
    | A |       | E |
    +---+       +---+
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           |
      |           +-------------------+
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      |                               |
      +-------------------+           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          |           |
                          +-----------+-----------+
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      |           |
                                      +-----------+-----------+
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      +-----------+-----------+
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      +-----------+-----------+
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      +-----------+-----------+
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      +-----------+-----------+
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |           |           |
                                      |

```
