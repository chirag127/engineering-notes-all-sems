Design strategies in software design are the approaches that are taken to design a software system. There are several strategies that can be used to design software systems, such as top-down design, bottom-up design, structured design, function-oriented design, and object-oriented design .

The following diagram illustrates the basic architecture of a software system using the top-down design strategy:

```
+-------------------+
|   Software System |
+-------------------+
        /|\
       / | \
      /  |  \
     /   |   \
    /    |    \
+-----+ +-----+ +-----+
|Sub-1| |Sub-2| |Sub-3|
+-----+ +-----+ +-----+
  /|\    /|\    /|\
 / | \  / | \  / | \
+---+ +---+ +---+ +---+ +---+
|A1| |A2| |B1| |B2| |C1| |C2|
+---+ +---+ +---+ +---+ +---+
```

The following diagram illustrates the basic architecture of a software system using the bottom-up design strategy:

```
+---+ +---+ +---+ +---+ +---+
|A1| |A2| |B1| |B2| |C1| |C2|
+---+ +---+ +---+ +---+ +---+
 \ /    \ /    \ /    \ /
  X      X      X      X
+-----+ +-----+ +-----+ +-----+
|Sub-1| |Sub-2| |Sub-3| |Sub-4|
+-----+ +-----+ +-----+ +-----+
    \      |      /     /
     \     |     /     /
      \    |    /     /
       \   |   /     /
        \  |  /     /
         \ | /     /
          \|/     /
+-------------------+
|   Software System |
+-------------------+
```

The following diagram illustrates the basic architecture of a software system using the structured design strategy:

```
+-------------------+
|   Software System |
+-------------------+
        /|\
       / | \
      /  |  \
     /   |   \
    /    |    \
+-----+ +-----+ +-----+
|Mod-1| |Mod-2| |Mod-3|
+-----+ +-----+ +-----+
  /|\    /|\    /|\
 / | \  / | \  / | \
+---+ +---+ +---+ +---+ +---+
|F1| |F2| |F3| |F4| |F5| |F6|
+---+ +---+ +---+ +---+ +---+
```

The following diagram illustrates the basic architecture of a software system using the function-oriented design strategy:

```
+-------------------+
|   Software System |
+-------------------+
        /|\
       / | \
      /  |  \
     /   |   \
    /    |    \
+-----+ +-----+ +-----+
|Fun-1| |Fun-2| |Fun-3|
+-----+ +-----+ +-----+
  /|\    /|\    /|\
 / | \  / | \  / | \
+---+ +---+ +---+ +---+ +---+
|D1| |D2| |D3| |D4| |D5| |D6|
+---+ +---+ +---+ +---+ +---+
```

The following diagram illustrates the basic architecture of a software system using the object-oriented design strategy:

```
+-------------------+
|   Software System |
+-------------------+
        /|\
       / | \
      /  |  \
     /   |   \
    /    |    \
+-----+ +-----+ +-----+
|Obj-1| |Obj-2| |Obj-3|
+-----+ +-----+ +-----+
  /|\    /|\    /|\
 / | \  / | \  / | \
+---+ +---+ +---+ +---+ +---+
|A1| |A2| |B1| |B2| |C1| |C2|
+---+ +---+ +---+ +---+ +---+
```

: Software Engineering | System