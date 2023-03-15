
#### Built-in Control Structures in Scala

1. `if`/`else`: These are the two most fundamental control structures in Scala, and they work as you'd expect. `if` lets you execute a block of code if a certain condition is true, while `else` lets you execute a different block of code if the condition is false.

2. `match`: This control structure is similar to a switch statement in other programming languages. It lets you execute different blocks of code depending on the value of a given expression.

3. `while`: This control structure lets you execute a block of code while a certain condition is true.

4. `do`/`while`: This control structure lets you execute a block of code at least once, and then continue to execute it while a certain condition is true.

5. `for`: This control structure lets you execute a block of code for each element in a given collection.

6. `break`: This control structure lets you exit a loop (`while`, `do`/`while`, or `for`) at any time.

7. `continue`: This control structure lets you skip the rest of the current iteration of a loop (`while`, `do`/`while`, or `for`) and start the next one.

Mnemonics and Learning Tricks:

- To remember the order of the built-in control structures in Scala, use the mnemonic "WDDFBC": `while`, `do`/`while`, `for`, `break`, `continue`.
- When using `if`/`else` statements, always use `else` as the default option. That way, the code will always execute something.
- When using `match` statements, always include a `case _` statement as the default option. That way, the code will always execute something, even if the expression doesn't match any of the cases.