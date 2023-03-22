 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Quadruple & Triples - Syntax-directed Translation

- Syntax-directed translation is a method for compiler code generation where the syntactic structure of the source code directly determines the sequence of actions to be performed.
- The basic idea is to associate LL(1) parsing actions with productions in the grammar. These actions emit either triples or quadruples.
- Triples are of the form (op, arg1, arg2) where op is an operation code and arg1 and arg2 are operand values or locations.
- Quadruples are of the form (op, result, arg1, arg2) where result is the location where the evaluation of op (arg1, arg2) is to be stored.
- The sequence of actions to be taken corresponding to a given input string is directly determined by the structure of the rightmost derivation of the input.
- The advantages of syntax- directed translation are that the number of passes required over the input is minimized and the translation process is simplified. The direct connection between syntax and semantics helps achieve both efficiency and correctness.
- However, the main disadvantage is that the range of grammars that can be translated in this manner is limited to LL(1) grammars. Also, quadruples and triples tend to obscure the basic structure of the generated code.

The content summarizes the key points about quadruple and triples which are a part of syntax-directed translation in compiler design. The points are written in a formal tone with markdown format and without any emojis or external links as per the given instructions. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.