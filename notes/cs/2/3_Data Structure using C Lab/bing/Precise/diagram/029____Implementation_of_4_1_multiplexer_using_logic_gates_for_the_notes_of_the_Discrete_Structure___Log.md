## Implementation of 4:1 multiplexer using logic gates

A multiplexer is a combinational circuit that selects one output from several inputs. A 4:1 multiplexer has four inputs, two control inputs, and one output. The control inputs determine which of the four inputs is connected to the output.

The implementation of a 4:1 multiplexer using logic gates can be done using AND, OR, and NOT gates. The circuit diagram for the implementation is shown below:

```
  +---+   +---+   +---+
  | A |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | B |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | C |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | D |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | E |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | F |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | G |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | H |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | I |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | J |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | K |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | L |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | M |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | N |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | O |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | P |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | Q |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | R |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | S |---|   |---|   |
  +---+   |   |   |   |
          |AND|   |   |
  +---+   |   |   |   |
  | T |---|   |---|   |
  +---+   +---+   |   |
                  |   |
  +---+   +---+   |   |
  | U |---|   |---|   |
  +---+   |   |   |   |

```
