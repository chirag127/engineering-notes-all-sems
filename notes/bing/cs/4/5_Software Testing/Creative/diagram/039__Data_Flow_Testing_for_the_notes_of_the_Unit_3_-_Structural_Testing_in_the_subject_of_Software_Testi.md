Data Flow Testing is a type of structural testing that is used to find the test paths of a program according to the locations of definitions and uses of variables in the program. It is based on selecting paths through the program's control flow graph in order to explore sequences of events related to the status of variables or data objects.

The following diagram illustrates the basic steps of Data Flow Testing:

```
+-----------------+      +------------------+      +-----------------+
| Identify the    |      | Construct the    |      | Select the test |
| variables and   |----->| control flow     |----->| paths based on  |
| their           |      | graph of the     |      | data flow       |
| definitions and |      | program          |      | criteria        |
| uses            |      |                  |      |                 |
+-----------------+      +------------------+      +-----------------+
```

The data flow criteria are the rules that determine which paths to select for testing. Some of the common data flow criteria are:

- All definitions: Every definition of a variable must be executed at least once.
- All uses: Every use of a variable must be executed at least once.
- All definition-use paths: Every path from a definition of a variable to a use of that variable must be executed at least once.
- All du-pairs: Every pair of a definition and a use of a variable must be executed at least once.

An example of Data Flow Testing is shown below:

```
int x, y, z;
x = 10; // Definition of x
y = 20; // Definition of y
z = x + y; // Use of x and y, definition of z
print(z); // Use of z
```

The control flow graph of this program is:

```
+---+     +---+     +---+     +---+
| x |---->| y |---->| z |---->| p |
+---+     +---+     +---+     +---+
```

The test paths based on the data flow criteria are:

- All definitions: x -> y -> z -> p
- All uses: x -> y -> z -> p
- All definition-use paths: x -> z -> p, y -> z -> p, z -> p
- All du-pairs: x -> z, y -> z, z -> p