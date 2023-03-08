### Registers of 8085 microprocessor

- A register is a small memory unit that can store data temporarily and perform arithmetic and logical operations.
- The 8085 microprocessor has eight addressable 8-bit registers: A, B, C, D, E, H, L, F, and two 16-bit registers PC and SP .
- These registers can be classified as:

  - General Purpose Registers
  - Temporary Registers
  - Special Purpose Registers
  - Stack Pointer Register
  - Program Counter Register

#### General Purpose Registers

- The 8085 has six general-purpose registers to store 8-bit data; these are identified as- B, C, D, E, H, and L .
- They can be used individually or in pairs to store data, address or operands.
- The 16-bit pairs are BC, DE and HL, which are also called register pairs.
- The HL register pair is often used to store the address of a memory location, and hence it is also called a memory pointer.
- The general purpose registers are less important than the accumulator.

#### Temporary Registers

- The 8085 has two temporary registers that are not accessible to the programmer.
- They are:

  - Temporary Data Register: It is used to hold the data during an arithmetic or logical operation.
  - W and Z Registers: They are used to store the 8-bit data during the execution of some instructions, such as CALL, RET, RST, etc.

#### Special Purpose Registers

- The 8085 has two special purpose registers that are accessible to the programmer .
- They are:

  - Accumulator: It is an 8-bit register that is a part of the arithmetic and logic unit (ALU). It is used to store the result of an arithmetic or logical operation, or to hold one of the operands. It is also called register A.
  - Flag Register: It is an 8-bit register that is used to indicate the status of the microprocessor after an operation. It has five flags that are affected by the arithmetic and logical operations: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P) and Carry (CY). The other three bits are not used.

#### Stack Pointer Register

- The stack pointer (SP) is a 16-bit register that is used to store the address of the top of the stack .
- The stack is a section of memory that is used to store data temporarily, such as return addresses, parameters, etc.
- The stack grows from higher memory address to lower memory address, and the stack pointer is decremented when data is pushed onto the stack, and incremented when data is popped from the stack.

#### Program Counter Register

- The program counter (PC) is a 16-bit register that is used to store the address of the next instruction to be executed .
- The program counter is incremented by one or two bytes after each instruction is fetched, depending on the size of the instruction.
- The program counter can be modified by the jump, call and return instructions, which can change the sequence of execution.

Mnemonics are techniques that can help you remember new information by linking it to something you already know. They can be words, phrases, images, sounds, or actions that trigger your memory. Some examples of mnemonics are:

- **Acronyms**: Using the first letter of each word in a list or phrase to form a new word. For example, ROYGBIV is an acronym for the colors of the rainbow: red, orange, yellow, green, blue, indigo, and violet.
- **Rhymes**: Using words that sound alike to remember facts or concepts. For example, "In 1492, Columbus sailed the ocean blue" is a rhyme that helps you remember the year of his voyage.
- **Key words**: Using a word or phrase that sounds similar to the word or concept you want to remember. For example, to remember that the capital of Canada is Ottawa, you can use the key word "oatmeal" and imagine a bowl of oatmeal with a maple leaf on it.
- **Visuals**: Using images or drawings to represent the information you want to remember. For example, to remember the order of the planets in the solar system, you can use a visual mnemonic like this:

![image](https://www.thoughtco.com/thmb/9XZ3q7y0n8y7g0w0wZfY0ZnY8ZI=/768x0/filters:no_upscale():max_bytes(150000):strip_icc()/planet-mnemonic-58b8c8c35f9b58af5c9c4f0f.jpg)

The image shows a pizza with different toppings that correspond to the first letter of each planet: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, and Pluto.

To use mnemonics effectively, you should follow these guidelines:

- Choose the appropriate mnemonic for your situation. For example, if your goal is to learn how to spell a word, you may want to use the spelling mnemonic technique.
- Practice the technique. You may want to practice your mnemonic several times to help you remember it.
- Repeat the mnemonic to others. Sharing your mnemonic with someone else can help you reinforce it and get feedback on it.
- Review the mnemonic periodically. To prevent forgetting, you should review your mnemonic from time to time.

Mnemonics and learning tricks can be very helpful for the topic, as long as they are easy to remember and relevant to the information. You can create your own mnemonics or use existing ones that work for you. The more you use mnemonics, the more you will improve your memory and learning.