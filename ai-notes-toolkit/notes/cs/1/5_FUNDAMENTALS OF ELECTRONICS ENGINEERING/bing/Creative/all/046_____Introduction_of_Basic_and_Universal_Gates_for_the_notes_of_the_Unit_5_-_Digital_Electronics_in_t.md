# Introduction of Basic and Universal Gates

- Logic gates are the fundamental building blocks of digital electronics. They perform basic logical operations on binary inputs and produce a single binary output.
- There are three basic logic gates: AND, OR, and NOT. They have the following symbols and truth tables:

| AND gate | OR gate | NOT gate |
|:--------:|:-------:|:--------:|
| ![AND gate symbol](https://eepower.com/media/2021/10/and-gate-symbol.png) | ![OR gate symbol](https://eepower.com/media/2021/10/or-gate-symbol.png) | ![NOT gate symbol](https://eepower.com/media/2021/10/not-gate-symbol.png) |
| ![AND gate truth table](https://eepower.com/media/2021/10/and-gate-truth-table.png) | ![OR gate truth table](https://eepower.com/media/2021/10/or-gate-truth-table.png) | ![NOT gate truth table](https://eepower.com/media/2021/10/not-gate-truth-table.png) |

- The AND gate produces a 1 output only when both inputs are 1. The OR gate produces a 1 output when either or both inputs are 1. The NOT gate produces the inverse of the input.
- There are two universal gates: NAND and NOR. They are called universal because they can be used to implement any other logic gate or Boolean function .
- The NAND gate is the negation of the AND gate, and the NOR gate is the negation of the OR gate. They have the following symbols and truth tables:

| NAND gate | NOR gate |
|:---------:|:--------:|
| ![NAND gate symbol](https://eepower.com/media/2021/10/nand-gate-symbol.png) | ![NOR gate symbol](https://eepower.com/media/2021/10/nor-gate-symbol.png) |
| ![NAND gate truth table](https://eepower.com/media/2021/10/nand-gate-truth-table.png) | ![NOR gate truth table](https://eepower.com/media/2021/10/nor-gate-truth-table.png) |

- The NAND gate produces a 0 output only when both inputs are 1. The NOR gate produces a 0 output when either or both inputs are 1.
- To implement any other logic gate using universal gates, we can use the following rules:

| Logic gate | NAND implementation | NOR implementation |
|:----------:|:-------------------:|:------------------:|
| AND | ![AND using NAND](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log41.gif) | ![AND using NOR](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log42.gif) |
| OR | ![OR using NAND](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log43.gif) | ![OR using NOR](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log44.gif) |
| NOT | ![NOT using NAND](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log45.gif) | ![NOT using NOR](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log46.gif) |
| XOR | ![XOR using NAND](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log47.gif) | ![XOR using NOR](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log48.gif) |
| XNOR | ![XNOR using NAND](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log49.gif) | ![XNOR using NOR](https://www.electronics-tutorials.ws/wp-content/uploads/2018/05/logic-log410.gif) |

- Logic gates can be integrated into a single IC (integrated circuit) to design various processors and controllers. The IC number of a logic gate indicates its type, number of inputs, and logic family. For example, the IC number 7400 is a NAND gate with four inputs and belongs to the TTL (trans