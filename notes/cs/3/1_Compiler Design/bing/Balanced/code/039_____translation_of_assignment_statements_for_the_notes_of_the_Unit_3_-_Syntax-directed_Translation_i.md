### Translation of Assignment Statements

- An assignment statement is a statement that assigns a value to a variable or a data structure.
- In compiler design, translation of assignment statements involves generating intermediate code or target code that performs the same operation as the source code.
- Translation of assignment statements depends on the type and structure of the expressions involved, such as real, integer, array, record, etc.
- Translation of assignment statements also depends on the syntax and semantics of the source language and the target language.
- Some common techniques for translation of assignment statements are:

  - **Syntax-directed translation**: This technique uses a context-free grammar (CFG) and a set of semantic rules to generate intermediate code or target code for each production of the grammar. The semantic rules are associated with the grammar symbols and are executed during parsing. The semantic rules can use attributes and actions to store and manipulate information about the grammar symbols. Syntax-directed translation can be implemented using either a top-down parser or a bottom-up parser. 
  - **Three-address code**: This technique uses a linear representation of intermediate code that consists of a sequence of instructions, each of which has at most three operands. The operands can be constants, variables, or temporary names. The instructions can perform arithmetic, logical, or control operations. Three-address code can be easily translated into target code by using a one-to-one mapping or by applying some optimization techniques.  
  - **Postfix notation**: This technique uses a stack-based representation of intermediate code that consists of a sequence of operands and operators. The operands are pushed onto the stack and the operators are applied to the topmost operands on the stack. Postfix notation can be easily obtained from the parse tree or the abstract syntax tree of the source code by using a depth-first traversal. Postfix notation can be easily translated into target code by using a stack machine or by applying some optimization techniques.  

- Some examples of translation of assignment statements are:

  - **Example 1**: Consider the following assignment statement in C:

    ```c
    x = y + z * 2;
    ```

    The translation of this statement into three-address code can be:

    ```c
    t1 = z * 2;
    t2 = y + t1;
    x = t2;
    ```

    The translation of this statement into postfix notation can be:

    ```c
    z 2 * y + x =
    ```

  - **Example 2**: Consider the following assignment statement in Pascal:

    ```pascal
    a[i] := b[i] + c;
    ```

    The translation of this statement into three-address code can be:

    ```pascal
    t1 = i * 4; // assuming integer size is 4 bytes
    t2 = a + t1; // assuming a is the base address of the array
    t3 = i * 4;
    t4 = b + t3;
    t5 = *t4; // dereferencing the address
    t6 = t5 + c;
    *t2 = t6; // dereferencing and assigning the value
    ```

    The translation of this statement into postfix notation can be:

    ```pascal
    i 4 * a + i 4 * b + * c + =
    ```