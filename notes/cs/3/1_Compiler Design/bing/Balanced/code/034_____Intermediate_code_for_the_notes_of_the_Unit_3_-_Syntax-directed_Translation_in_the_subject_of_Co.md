# Intermediate code for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design

- Intermediate code is a form of representation of the source program that is easier to translate into the target machine code.
- Intermediate code eliminates the need of a new full compiler for every unique machine by keeping the analysis portion same for all the compilers. The second part of compiler, synthesis, is changed according to the target machine.
- Intermediate code can be either language-specific (e.g., Bytecode for Java) or language-independent (three-address code).
- The following are commonly used intermediate code representations:
  - Postfix Notation: Also known as reverse Polish notation or suffix notation. The ordinary (infix) way of writing the sum of a and b is with an operator in between: a + b. In postfix notation, the operator comes after the operands: a b +. This notation eliminates the need for parentheses and precedence rules.
  - Syntax Trees: A syntax tree is a graphical representation of the abstract syntax of the source program. The leaves of the tree are the operands and the interior nodes are the operators. The order of evaluation is determined by the structure of the tree.
  - Three-Address Code: A three-address code is a linearized representation of a syntax tree, where each statement has at most one operator and three operands. The operands can be constants, variables, or temporary names. A temporary name is a compiler-generated name that holds an intermediate value. For example, the statement x = y + z * w can be translated into the following three-address code:

    ```
    t1 = z * w
    t2 = y + t1
    x = t2
    ```

- Intermediate code generation is a phase in the compiler that takes the output of the syntax analysis phase (parse tree or abstract syntax tree) and applies semantic rules to generate an intermediate code.
- The intermediate code generator can use various techniques to generate the intermediate code, such as:
  - Syntax-directed translation: A method of translating the parse tree or abstract syntax tree into intermediate code by attaching semantic actions to the grammar rules. The semantic actions are executed during the parsing process and produce the intermediate code as a side effect.
  - Translation schemes: A notation for specifying syntax-directed translation that combines the grammar rules and the semantic actions in one place. The semantic actions are written within curly braces and are inserted at arbitrary positions in the right-hand side of the grammar rules. For example, the following translation scheme generates three-address code for arithmetic expressions:

    ```
    E -> E1 + T { E.place = newtemp();
                  gen(E.place = E1.place + T.place); }
      | T { E.place = T.place; }
    T -> T1 * F { T.place = newtemp();
                  gen(T.place = T1.place * F.place); }
      | F { T.place = F.place; }
    F -> (E) { F.place = E.place; }
      | id { F.place = id.place; }
    ```

  - Intermediate representation languages: A formal language for defining the syntax and semantics of the intermediate code. The intermediate representation language can be either textual or graphical. For example, the following is a textual intermediate representation language for arithmetic expressions:

    ```
    expr -> expr + term | term
    term -> term * factor | factor
    factor -> (expr) | id
    ```

    The following is a graphical intermediate representation language for arithmetic expressions:

    ```
    expr -> expr + term
          /        \
       expr       term
       /  \       /  \
    expr term  term factor
    /  \  /  \  /  \   |
    id  + id * id *  id
    ```