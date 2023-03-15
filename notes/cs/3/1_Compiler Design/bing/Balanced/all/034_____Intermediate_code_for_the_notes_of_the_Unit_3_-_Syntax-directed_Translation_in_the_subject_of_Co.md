# Intermediate Code Generation

Intermediate code generation is a phase in the compiler design that produces an intermediate representation of the source program. The intermediate code is independent of the source language and the target machine, and it can be easily translated into the machine code. Intermediate code can also be used for code optimization and analysis.

The following are some of the advantages of intermediate code generation:

- It simplifies the task of the compiler by separating the analysis and synthesis phases.
- It eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The synthesis portion can be changed according to the target machine.
- It allows portability of the compiler across different machines and platforms.
- It facilitates the implementation of code-improving transformations on the intermediate code.

The following are some of the commonly used intermediate code representations:

- Postfix notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between, as in a + b. In postfix notation, the operator follows the operands, as in a b +. Postfix notation does not require parentheses or precedence rules to indicate the order of evaluation.
- Prefix notation: Also known as Polish notation or prefix notation. The operator precedes the operands, as in + a b. Prefix notation also does not require parentheses or precedence rules.
- Three-address code: A sequence of instructions of the form x = y op z, where x, y, and z are names, constants, or compiler-generated temporaries, and op is an operator. Each instruction has at most three operands and can be thought of as a computation that applies op to y and z and stores the result into x.
- Quadruples: A table of four columns, where each row represents an instruction. The first column contains the operator, the second and third columns contain the operands, and the fourth column contains the result. For example, the instruction x = y + z can be represented as a row [+ | y | z | x] in the quadruples table.
- Triples: A table of three columns, where each row represents an instruction. The first column contains the operator, and the second and third columns contain the operands. The result is implicitly represented by the row number. For example, the instruction x = y + z can be represented as a row [+ | y | z] in the triples table, and the result can be referred to as (0), where 0 is the row number.
- Indirect triples: A variation of triples, where the result is explicitly represented by a pointer to the row number. For example, the instruction x = y + z can be represented as a row [+ | y | z | 0] in the indirect triples table, and the result can be referred to as *0, where 0 is the pointer to the row number.
- Abstract syntax tree: A tree representation of the syntactic structure of the source program. Each node in the tree corresponds to a construct in the source language. The leaves are atomic symbols, such as identifiers, constants, or operators. The internal nodes are non-terminal symbols, such as expressions, statements, or declarations. The root of the tree is the start symbol of the grammar.
- Directed acyclic graph: A graph representation of the expressions in the source program. Each node in the graph corresponds to an operator or an operand. The edges represent the flow of values from operands to operators. The graph is acyclic, meaning that there are no cycles or loops in the graph. The graph is directed, meaning that the edges have a direction from source to destination. A directed acyclic graph can eliminate common subexpressions and redundant calculations.
- Bytecode: A low-level, compact, and platform-independent representation of the source program. Bytecode is typically generated for interpreted languages, such as Java or Python. Bytecode consists of a sequence of instructions that can be executed by a virtual machine. Each instruction is encoded as a byte or a sequence of bytes. Bytecode can be easily translated into the machine code of the target machine.