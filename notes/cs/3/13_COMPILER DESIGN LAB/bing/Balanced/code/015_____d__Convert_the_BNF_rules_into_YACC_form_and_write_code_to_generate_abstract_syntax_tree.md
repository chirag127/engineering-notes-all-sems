Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on how to convert BNF rules into YACC form and write code to generate abstract syntax tree:

- BNF (Backus-Naur form) is a notation for describing the syntax of a language using production rules. YACC (Yet Another Compiler Compiler) is a tool that generates a parser from a grammar written in BNF form.
- To convert BNF rules into YACC form, you need to follow some steps:
  - Identify the terminals and non-terminals of the grammar and declare them using %token and %type directives respectively.
  - Write the production rules in the format: non-terminal : symbol-sequence ;
  - Use curly braces { } to enclose the semantic actions that will be executed when a rule is matched. The semantic actions can be written in C code and can use the variables $$, $1, $2, ... to refer to the attributes of the non-terminal and the symbols in the rule.
  - Use the %start directive to specify the start symbol of the grammar.
  - Use the %union directive to define a union type that can hold the attributes of different symbols.
  - Use the %left, %right, and %nonassoc directives to specify the associativity and precedence of the operators in the grammar.
- To write code to generate abstract syntax tree (AST) for the mini language specified, you need to follow some steps:
  - Define a data structure that can represent the nodes of the AST. For example, you can use a struct with a tag field that indicates the type of the node and a union field that holds the data of the node.
  - Write a function that can create a new node of a given type and data. For example, you can use a function like node (type, data1, data2, ...) that allocates memory for a new node and initializes its fields.
  - In the semantic actions of the YACC rules, use the node function to create AST nodes and assign them to the $$ variable. For example, if you have a rule like expr : expr '+' expr ;, you can write { $$ = node ( '+', $1, $3 ); } to create a node with a '+' tag and two children nodes that are the attributes of the left and right expressions.
  - In the main function of the YACC program, call the yyparse function to parse the input and obtain the root of the AST. Then, you can traverse the AST and perform any operations on it, such as printing, evaluating, or generating machine code.