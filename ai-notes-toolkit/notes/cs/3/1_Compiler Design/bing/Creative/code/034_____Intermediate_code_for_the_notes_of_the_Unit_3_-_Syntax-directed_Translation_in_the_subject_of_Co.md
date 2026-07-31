# Intermediate Code Generation

Intermediate code generation is a phase in the compiler design that produces an intermediate representation of the source program. The intermediate code is independent of the source language and the target machine, and it can be easily translated into the machine code. Intermediate code can also be used for code optimization and analysis.

The following are some of the advantages of intermediate code generation:

- It simplifies the task of the compiler by separating the analysis and synthesis phases.
- It eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers.
- It allows the compiler to perform machine-independent optimizations on the intermediate code.
- It facilitates the portability of the compiler to different machines and platforms.

The following are some of the commonly used intermediate code representations:

- Postfix notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between, as in a + b. In postfix notation, the operator follows the operands, as in a b +. Postfix notation does not require parentheses or precedence rules to indicate the order of evaluation. For example, the expression (a + b) * c can be written as a b + c * in postfix notation.
- Prefix notation: Also known as Polish notation or prefix notation. The operator precedes the operands, as in + a b. Prefix notation also does not require parentheses or precedence rules. For example, the expression (a + b) * c can be written as * + a b c in prefix notation.
- Three-address code: A sequence of instructions, each of which has at most three operands. An operand can be a constant, a variable, a temporary variable, or a label. A label is used to mark the target of a jump instruction. An instruction can have one of the following forms:

  - x = y op z, where op is a binary arithmetic or logical operator.
  - x = op y, where op is a unary arithmetic or logical operator.
  - x = y, where y is assigned to x.
  - goto L, where L is a label.
  - if x goto L, where the control jumps to L if x is true.
  - ifFalse x goto L, where the control jumps to L if x is false.
  - param x, where x is passed as a parameter to a procedure.
  - call p, n, where p is the name of a procedure and n is the number of parameters.
  - return, where the control returns from a procedure.
  - return x, where the control returns from a procedure with x as the return value.

  For example, the expression x = (a + b) * c can be translated into the following three-address code:

  - t1 = a + b
  - t2 = t1 * c
  - x = t2

- Quadruples: A list of four-tuples, each of which represents an instruction with four fields: op, arg1, arg2, and result. The op field specifies the operator, and the arg1 and arg2 fields specify the operands. The result field specifies where the result of the operation is stored. A field can be empty if it is not needed. For example, the expression x = (a + b) * c can be translated into the following quadruples:

  - ( + , a , b , t1 )
  - ( * , t1 , c , t2 )
  - ( = , t2 ,   , x )

- Triples: A list of three-tuples, each of which represents an instruction with three fields: op, arg1, and arg2. The op field specifies the operator, and the arg1 and arg2 fields specify the operands. The result of each operation is stored in a temporary variable, which is implicitly defined by the position of the triple in the list. The temporary variables are denoted by (i), where i is the index of the triple. For example, the expression x = (a + b) * c can be translated into the following triples:

  - ( + , a , b )
  - ( * , (0) , c )
  - ( = , (1) , x )

- Indirect triples: A variation of triples, where each triple is assigned a label, and the operands are either constants, variables, or labels. The labels are used to refer to the results of other triples. For example, the expression x = (a + b) * c can be translated into the following indirect triples: