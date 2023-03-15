### Control Flow Graphs

- A control flow graph (CFG) is a graphical representation of the control flow or computation during the execution of a program or application .
- A CFG consists of nodes and edges, where nodes represent basic blocks and edges represent the possible paths of execution .
- A basic block is a maximal length sequence of straightline, or branch-free, code that always executes together, unless an operation raises an exception.
- A CFG has a single entry node and a single exit node, which are the start and end points of the program or application .
- A CFG can be used for various purposes, such as static analysis, compiler optimization, testing, debugging, and program slicing .

#### Symbols and Example

- The following symbols are commonly used to draw a CFG:

  - A rectangle represents a basic block that contains one or more statements or operations.
  - A diamond represents a decision point that has two or more outgoing edges based on a condition or a predicate.
  - A circle represents the entry or exit node of the CFG.
  - An arrow represents the direction of the control flow from one node to another.

- For example, consider the following pseudocode of a program that calculates the factorial of a given number n:

  ```
  begin
    read n
    if n < 0 then
      print "Invalid input"
      stop
    else
      f = 1
      i = 1
      while i <= n do
        f = f * i
        i = i + 1
      end while
      print f
      stop
    end if
  end
  ```

- The CFG of this program can be drawn as follows:

  ```
  +-----+
  |     |
  |begin|
  |     |
  +-----+
    |
    v
  +-----+
  |     |
  |read n|
  |     |
  +-----+
    |
    v
  +-----+
  |     |
  |n < 0|
  |     |
  +-----+
   / \
  /   \
 /     \
v       v
+-----+ +-----+
|     | |     |
|print| |f = 1|
|stop | |i = 1|
|     | |     |
+-----+ +-----+
        |
        v
      +-----+
      |     |
      |i <= n|
      |     |
      +-----+
       / \
      /   \
     /     \
    v       v
  +-----+ +-----+
  |     | |     |
  |f = f| |print|
  |* i  | |f    |
  |i = i| |stop |
  |+ 1  | |     |
  |     | +-----+
  +-----+
    |
    v
    |
    +-----+
    |     |
    |end  |
    |     |
    +-----+
  ```