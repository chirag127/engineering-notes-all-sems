

## Course Outcome (CO) Bloom's Knowledge Level (KL)

- Course Outcome (CO) is a statement that describes what a learner should be able to do at the end of a course or a unit of instruction.
- Bloom's Knowledge Level (KL) is a classification of the cognitive skills that learners need to demonstrate in order to achieve a CO.
- Bloom's taxonomy is a framework that divides cognitive skills into six levels: remember, understand, apply, analyze, evaluate, and create.
- Each level of Bloom's taxonomy requires a higher degree of cognitive complexity and mastery than the previous one.
- A CO should be aligned with a specific KL that matches the intended learning outcome and the assessment method.
- For example, a CO that states "The learner will be able to explain the concept of inheritance in object-oriented programming" is aligned with the KL of understand, and can be assessed by asking the learner to write a short paragraph or answer multiple-choice questions.
- A CO that states "The learner will be able to design and implement a class hierarchy using inheritance and polymorphism" is aligned with the KL of create, and can be assessed by asking the learner to write a program or a pseudocode.
- A CO should be SMART: specific, measurable, achievable, relevant, and time-bound.
- A CO should be written using an action verb that indicates the observable behavior or performance of the learner, such as define, compare, solve, critique, or design.
- A CO should be written from the perspective of the learner, not the instructor, using phrases such as "The learner will be able to..." or "By the end of this course, the learner will..."
- A CO should be clear, concise, and consistent with the course objectives and the curriculum standards.



Hello, I am Sydney, your AI assistant. I am here to help you with any task or question you have.

Some possible responses for the topic are:

### At the end of the course, the student will be able to:

- Apply the fundamental concepts and principles of computer science to solve various problems.
- Design, implement, test, and debug programs using a high-level programming language such as Python, Java, or C++.
- Use data structures and algorithms to organize, manipulate, and analyze data efficiently and effectively.
- Understand the basic concepts of computer architecture, operating systems, networks, and databases.
- Communicate effectively and ethically with peers, instructors, and clients using oral, written, and graphical modes.
- Work collaboratively and independently on projects, assignments, and research.
- Demonstrate critical thinking, creativity, and problem-solving skills in various domains of computer science.



#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

- Lexical analysis is the process of converting a sequence of characters from a source program into a sequence of tokens that can be recognized by a compiler or an interpreter.
- A token is a basic unit of a source program, such as a keyword, an identifier, a constant, an operator, or a delimiter.
- A pattern is a rule that describes how to form a token from a sequence of characters. For example, a pattern for an identifier may be a letter followed by zero or more letters or digits.
- A regular expression is a notation for specifying patterns using symbols and operators. For example, the regular expression `[a-zA-Z][a-zA-Z0-9]*` specifies the pattern for an identifier.
- A regular expression can be represented by a finite automaton, which is a mathematical model of computation that consists of a finite set of states, a finite set of input symbols, a transition function that maps a state and an input symbol to a new state, a start state, and a set of final states.
- A finite automaton can be either deterministic or nondeterministic. A deterministic finite automaton (DFA) has exactly one transition for each state and input symbol, while a nondeterministic finite automaton (NFA) may have zero, one, or more transitions for each state and input symbol.
- A DFA can recognize a token by starting from the start state and following the transitions according to the input symbols until reaching a final state or an undefined transition. If the final state is reached, the token is accepted; otherwise, the token is rejected.
- An NFA can recognize a token by starting from the start state and following any possible transitions according to the input symbols until reaching a final state or no more transitions. If any final state is reached, the token is accepted; otherwise, the token is rejected.
- Every NFA can be converted to an equivalent DFA using the subset construction algorithm, which constructs a new state for each subset of states of the NFA and defines the transitions and final states accordingly.
- A regular expression can also be represented by a regular grammar, which is a formal grammar that consists of a finite set of nonterminal symbols, a finite set of terminal symbols, a start symbol, and a finite set of production rules that have the form A -> a or A -> aB, where A and B are nonterminals and a is a terminal. A regular grammar can generate a token by starting from the start symbol and applying the production rules until reaching a terminal symbol. The sequence of terminal symbols generated is the token.
- A regular grammar can be either left-linear or right-linear, depending on whether the nonterminal symbol in the production rule appears on the left or the right of the terminal symbol. A left-linear grammar can be converted to an equivalent right-linear grammar and vice versa by reversing the production rules and the terminal symbols.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

# CO 2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, which are the basic units of a language, such as keywords, identifiers, literals, operators, etc.
- LEX is a tool that generates a lexical analyzer from a set of regular expressions that define the tokens of a language.
- YACC is a tool that generates a parser from a set of context-free grammar rules that define the syntax of a language.
- C is a general-purpose programming language that can be used to implement the lexical analyzer and the parser generated by LEX and YACC.
- The steps to design a lexical analyzer for a given language using C and LEX /YACC tools are:

  - Define the tokens of the language using regular expressions and assign them names or codes.
  - Write the LEX specification file that contains the declarations, rules, and user subroutines sections.
  - Run the LEX tool on the specification file to generate the C source code for the lexical analyzer, which is usually named lex.yy.c.
  - Define the grammar rules of the language using context-free grammar and assign them names or codes.
  - Write the YACC specification file that contains the declarations, rules, and user subroutines sections.
  - Run the YACC tool on the specification file to generate the C source code for the parser, which is usually named y.tab.c.
  - Write the main function in C that invokes the parser function yyparse() and handles the errors and actions.
  - Compile and link the C source files generated by LEX and YACC and the main function to produce the executable program for the lexical analyzer and the parser.

- Here is an example of a LEX specification file for a simple language that has four tokens: ID, NUM, PLUS, and MINUS.

```
%{
#include "y.tab.h"
%}

%%

[a-zA-Z]+ { return ID; }
[0-9]+ { return NUM; }
"+" { return PLUS; }
"-" { return MINUS; }
[ \t\n] { /* ignore whitespace */ }
. { printf("Invalid character: %c\n", yytext[0]); exit(1); }

%%

int yywrap() {
  return 1;
}
```

- Here is an example of a YACC specification file for a simple language that has one grammar rule: expr -> expr PLUS expr | expr MINUS expr | ID | NUM.

```
%{
#include <stdio.h>
%}

%token ID NUM PLUS MINUS

%%

expr: expr PLUS expr { printf("Addition\n"); }
    | expr MINUS expr { printf("Subtraction\n"); }
    | ID { printf("Identifier: %s\n", yytext); }
    | NUM { printf("Number: %s\n", yytext); }
    ;

%%

int main() {
  yyparse();
  return 0;
}

int yyerror(char *s) {
  printf("Syntax error: %s\n", s);
  return 0;
}
```

- Here is an example of a main function in C that invokes the parser function yyparse() and handles the errors and actions.

```
#include <stdio.h>
#include "y.tab.h"

extern int yyparse();

int main() {
  if (yyparse() == 0) {
    printf("Parsing successful\n");
  } else {
    printf("Parsing failed\n");
  }
  return 0;
}
```

- To compile and link the C source files generated by LEX and YACC and the main function, use the following commands:

```
lex lex.l
yacc -d yacc.y
gcc lex.yy.c y.tab.c main.c -o parser
```

- To run the executable program for the lexical analyzer and the parser, use the following command:

```
./parser
```

- To test the program, enter some input that conforms to the language, such as:

```
a + b - 10
```

- The output of the program should be:

```
Identifier: a
Identifier: b
Addition
Number: 10
Subtraction
Parsing successful
```



#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- Top down and bottom up parsers are two types of parsers that are used to construct parse trees from a given input string and a grammar.
- A parse tree is a graphical representation of the syntactic structure of a sentence according to a grammar.
- A grammar is a set of rules that define the syntax of a language, i.e., how words and symbols can be combined to form valid sentences.
- A parser is a program that takes an input string and a grammar as input and outputs a parse tree or an error message if the input string is not syntactically correct.
- Top down and bottom up parsers differ in the direction and the order of applying the rules of grammar to construct the parse tree.

##### Top down parsing
- Top down parsing is a parsing technique that starts from the root of the parse tree and works down to the leaves by using the rules of grammar in a forward order.
- Top down parsing is based on leftmost derivation, i.e., it expands the leftmost non-terminal symbol in each step until it reaches the input string.
- Top down parsing can be implemented by two methods: recursive descent parsing and predictive parsing.
- Recursive descent parsing is a method that uses a set of recursive procedures, one for each non-terminal symbol, to parse the input string. Each procedure tries to match the input string with the right hand side of the production rule for that non-terminal symbol. If the match fails, the procedure backtracks and tries another alternative.
- Predictive parsing is a method that uses a data structure called a parsing table to guide the parsing process. A parsing table is a two-dimensional array that maps each pair of a non-terminal symbol and an input symbol to a production rule or an error. A predictive parser uses a stack to keep track of the non-terminal symbols that need to be expanded and a pointer to scan the input string. It consults the parsing table to determine which production rule to apply or whether to report an error.
- Advantages of top down parsing:
  - It is easy to implement and understand.
  - It can handle left factored grammars, i.e., grammars that do not have common prefixes in the right hand side of the production rules.
  - It can handle left recursive grammars, i.e., grammars that have production rules of the form A -> Aα, where A is a non-terminal symbol and α is a string of terminal and non-terminal symbols.
- Disadvantages of top down parsing:
  - It may perform unnecessary backtracking, which is inefficient and time-consuming.
  - It cannot handle left recursive grammars, i.e., grammars that have production rules of the form A -> Aα, where A is a non-terminal symbol and α is a string of terminal and non-terminal symbols.
  - It cannot handle ambiguous grammars, i.e., grammars that have more than one parse tree for the same input string.

##### Bottom up parsing
- Bottom up parsing is a parsing technique that starts from the leaves of the parse tree and works up to the root by using the rules of grammar in a reverse order.
- Bottom up parsing is based on rightmost derivation, i.e., it reduces the rightmost non-terminal symbol in each step until it reaches the start symbol.
- Bottom up parsing can be implemented by two methods: shift-reduce parsing and operator precedence parsing.
- Shift-reduce parsing is a method that uses a data structure called a stack to store the symbols that have been scanned from the input string. It performs two operations: shift and reduce. A shift operation moves the next input symbol to the top of the stack. A reduce operation applies a production rule in reverse to replace the right hand side of the rule with the left hand side of the rule on the top of the stack. The parsing process ends when the stack contains only the start symbol and the input string is empty.
- Operator precedence parsing is a method that uses a data structure called a precedence table to guide the parsing process. A precedence table is a two-dimensional array that maps each pair of terminal symbols to a precedence relation: less than, equal to, or greater than. A operator precedence parser uses a stack to store the symbols that have been scanned from the input string. It compares the top symbol of the stack with the next input symbol using the precedence table to determine whether to shift or reduce. It shifts if the top symbol is less than the next input symbol, and reduces if the top symbol is greater than or equal to the next input symbol. The parsing process ends when the stack contains only the start symbol and the



#### CO 4 Generate the intermediate code K4, K5

- Intermediate code is a representation of a program that is between the source code and the target code.
- Intermediate code can be used for various purposes, such as optimization, portability, analysis, and debugging.
- There are different forms of intermediate code, such as abstract syntax trees, three-address code, quadruples, triples, and indirect triples.
- K4 and K5 are two types of intermediate code that use quadruples and triples, respectively.
- A quadruple is a four-tuple that consists of an operator, two operands, and a result. For example, `(+, a, b, t1)` means `t1 = a + b`.
- A triple is a three-tuple that consists of an operator and two operands. The result is implicitly stored in a temporary variable. For example, `(+, a, b)` means `t = a + b`, where `t` is the next available temporary variable.
- K4 and K5 are intermediate code generators that use quadruples and triples to represent arithmetic expressions, assignment statements, conditional statements, and loops.
- K4 and K5 use the following rules to generate intermediate code:

  - For an arithmetic expression, generate a quadruple or a triple for each binary operator, using the operands as the source and a temporary variable as the destination. For example, for the expression `a + b * c`, generate `(*, b, c, t1)` and then `(+, a, t1, t2)` in K4, or `(*, b, c)` and then `(+, a, t)` in K5.
  - For an assignment statement, generate a quadruple or a triple that copies the value of the right-hand side expression to the left-hand side variable. For example, for the statement `x = a + b * c`, generate `(=, t2, _, x)` in K4, or `(=, t, _, x)` in K5, after generating the intermediate code for the expression `a + b * c`.
  - For a conditional statement, generate a quadruple or a triple that evaluates the condition and jumps to a label if it is false. Then, generate the intermediate code for the true branch, followed by a jump to the end label. Next, generate the intermediate code for the false branch, followed by the end label. For example, for the statement `if (a < b) then x = x + 1 else x = x - 1`, generate the following intermediate code in K4:

    ```
    (<, a, b, t1)
    (jfalse, t1, _, L1)
    (+, x, 1, t2)
    (=, t2, _, x)
    (jump, _, _, L2)
    L1:
    (-, x, 1, t3)
    (=, t3, _, x)
    L2:
    ```

    And the following intermediate code in K5:

    ```
    (<, a, b)
    (jfalse, t, _, L1)
    (+, x, 1)
    (=, t, _, x)
    (jump, _, _, L2)
    L1:
    (-, x, 1)
    (=, t, _, x)
    L2:
    ```

  - For a loop statement, generate a quadruple or a triple that evaluates the condition and jumps to the end label if it is false. Then, generate the intermediate code for the loop body, followed by a jump to the start label. Next, generate the end label. For example, for the statement `while (a < b) do x = x + 1`, generate the following intermediate code in K4:

    ```
    L1:
    (<, a, b, t1)
    (jfalse, t1, _, L2)
    (+, x, 1, t2)
    (=, t2, _, x)
    (jump, _, _, L1)
    L2:
    ```

    And the following intermediate code in K5:

    ```
    L1:
    (<, a, b)
    (jfalse, t, _, L2)
    (+, x, 1)
    (=, t, _, x)
    (jump, _, _, L1)
    L2:
    ```



#### CO 5 Generate machine code from the intermediate code forms K3, K4

- Machine code is the low-level binary representation of a program that can be directly executed by the target system.
- Intermediate code is a high-level or abstract representation of a program that is independent of the target system  .
- Intermediate code generation is the process of translating the source code into intermediate code by the compiler  .
- Machine code generation is the process of translating the intermediate code into machine code by the code generator  .
- The advantages of using intermediate code are:
  - It enhances the portability of the compiler, as the same intermediate code can be used for different target systems .
  - It simplifies the code generation and optimization phases, as the intermediate code is more structured and uniform than the source code .
- The challenges of generating machine code from intermediate code are:
  - The code generator has to deal with the limited number of registers and memory locations available in the target system .
  - The code generator has to map the intermediate code instructions to the corresponding machine code instructions, which may not have a one-to-one correspondence .
  - The code generator has to handle the differences in the instruction formats, operands, addressing modes, and control flow structures between the intermediate code and the machine code .
- The steps involved in generating machine code from intermediate code are:
  - Instruction selection: The code generator chooses the appropriate machine code instructions for each intermediate code instruction .
  - Register allocation: The code generator assigns the intermediate code operands to the available registers or memory locations in the target system .
  - Instruction scheduling: The code generator orders the machine code instructions to optimize the performance and reduce the stalls in the target system .
- The types of intermediate code forms are:
  - K3: Three-address code, which is a linear sequence of instructions, each having at most three operands .
  - K4: Quadruples, which is a table of four columns, each representing an operator, an argument, another argument, and a result .
- The examples of generating machine code from intermediate code forms are:

  | Intermediate code (K3) | Machine code |
  | ---------------------- | ------------ |
  | x = y + z              | ADD R1, y    |
  |                        | ADD R1, z    |
  |                        | MOV x, R1    |
  | if x < y goto L1       | CMP x, y     |
  |                        | JL L1        |
  | L1: x = x + 1          | L1: INC x    |

  | Intermediate code (K4) | Machine code |
  | ---------------------- | ------------ |
  | (+, y, z, t1)          | ADD R1, y    |
  |                        | ADD R1, z    |
  |                        | MOV t1, R1   |
  | (<, x, y, t2)          | CMP x, y     |
  |                        | SETL R2      |
  |                        | MOV t2, R2   |
  | (goto, t2, -, L1)      | TEST t2      |
  |                        | JNZ L1       |
  | (L1, =, t1, x)         | L1: MOV x, t1|



## DETAILED SYLLABUS

- A detailed syllabus is a document that outlines the topics, objectives, assignments, assessments, and policies of a course.
- A detailed syllabus can help students to understand the expectations and requirements of the course, as well as to plan their study time and workload accordingly.
- A detailed syllabus can also help instructors to organize and deliver the course content, as well as to communicate with students and provide feedback.
- A detailed syllabus typically includes the following sections:

  - Course information: This section provides basic information about the course, such as the course title, code, number, credits, prerequisites, instructor name and contact details, office hours, meeting times and locations, etc.
  - Course description: This section provides a brief overview of the course, such as the main topics, themes, goals, and outcomes of the course, as well as the relevance and importance of the course to the discipline or program.
  - Course objectives: This section provides a list of specific and measurable learning outcomes that students are expected to achieve by the end of the course, such as the knowledge, skills, and attitudes that students will acquire or demonstrate.
  - Course materials: This section provides a list of required and recommended texts, readings, resources, and materials that students will need to access and use for the course, such as books, articles, websites, software, etc.
  - Course schedule: This section provides a detailed breakdown of the course content and activities, such as the topics, subtopics, readings, assignments, quizzes, exams, projects, presentations, etc. that will be covered in each class session or week, as well as the due dates and deadlines for each component.
  - Course policies: This section provides a set of rules and guidelines that students are expected to follow and adhere to throughout the course, such as the attendance, participation, late submission, academic integrity, grading, feedback, communication, etc. policies of the course, as well as the consequences and penalties for violating them.
  - Course evaluation: This section provides a description and explanation of the methods and criteria that will be used to assess and grade students' performance and learning in the course, such as the weight, format, rubric, etc. of each assignment, quiz, exam, project, presentation, etc. that will contribute to the final grade of the course.



Hello, I am Sydney, your AI assistant. I can help you with your topic.

# Design and implement a lexical analyzer for given language using C and the lexical analyzer should ignore redundant

- A lexical analyzer is a program that takes a source code as input and produces a stream of tokens as output.
- A token is a meaningful unit of the source code, such as a keyword, an identifier, a constant, an operator, or a delimiter.
- A lexical analyzer should ignore redundant parts of the source code, such as comments, whitespaces, and newlines, as they do not affect the meaning of the program.
- To design and implement a lexical analyzer for a given language using C, the following steps are required:

  - Define the lexical rules of the language, such as the syntax and semantics of the tokens, the reserved words, the operators, and the delimiters.
  - Use regular expressions to specify the patterns of the tokens, such as the format of identifiers, constants, and literals.
  - Construct a finite automaton or a state diagram that can recognize the tokens based on the regular expressions.
  - Write a C program that can simulate the finite automaton or the state diagram, using variables, arrays, and functions.
  - Use input and output functions to read the source code from a file and write the tokens to another file or the standard output.
  - Use conditional and loop statements to handle the transitions between the states and the actions to be performed when a token is recognized or an error occurs.
  - Use string and character functions to manipulate the input and output strings and characters, such as concatenating, comparing, copying, and converting.
  - Test and debug the lexical analyzer using sample inputs and outputs, and check for any errors or exceptions.



# Spaces, tabs and new lines

- Spaces, tabs and new lines are special characters that are used to format text and code in various ways.
- Spaces are used to separate words and symbols, and to align text and code. A space is represented by the ASCII code 32 or the Unicode code U+0020.
- Tabs are used to create indents and to align text and code. A tab is represented by the ASCII code 9 or the Unicode code U+0009. The width of a tab can vary depending on the editor or the context, but it is usually equivalent to four or eight spaces.
- New lines are used to create line breaks and to separate paragraphs and code blocks. A new line is represented by the ASCII code 10 or the Unicode code U+000A. In some systems, a new line is preceded by a carriage return, which is represented by the ASCII code 13 or the Unicode code U+000D.
- Spaces, tabs and new lines are often invisible or rendered as whitespace in most editors and viewers, but they can be made visible by enabling certain options or using special symbols. For example, in markdown, a space can be shown as `&nbsp;`, a tab as `&emsp;`, and a new line as `<br>`.
- Spaces, tabs and new lines have different functions and effects depending on the language and the format. For example, in HTML, multiple spaces and new lines are collapsed into a single space, unless they are inside a `<pre>` tag or a `<code>` tag. In Python, indentation with spaces or tabs is used to define the scope of code blocks, and a new line is used to end a statement, unless it is inside parentheses or brackets. In markdown, two spaces at the end of a line create a line break, and an empty line creates a paragraph break.



# 2. Implementation of Lexical Analyzer using Lex Tool

- Lex is a tool that generates lexical analyzers, also known as scanners or tokenizers, from a set of rules that specify the tokens to be recognized in the input stream.
- Lexical analyzers are programs that read an input stream of characters and produce an output stream of tokens, which are the basic units of meaning in a programming language or a text file.
- Lexical analyzers are often used as the first phase of a compiler or an interpreter, to divide the source code into tokens that can be processed by the subsequent phases, such as the parser or the semantic analyzer.
- Lex is based on the concept of regular expressions, which are a concise and powerful way of describing patterns of characters. A regular expression can be used to define a token, such as a keyword, an identifier, a number, a string literal, or a comment.
- Lex uses a special notation to write the rules for the lexical analyzer. A rule consists of two parts: a pattern and an action. The pattern is a regular expression that matches a sequence of characters in the input stream. The action is a fragment of C code that is executed when the pattern is matched. The action usually returns a token code or a value to the calling program, or performs some other operation, such as printing an error message or updating a counter.
- Lex rules have the following general form:

    `pattern   action`

- The pattern and the action are separated by whitespace (spaces or tabs). The action is enclosed in curly braces `{ }`. The action can span multiple lines, but the pattern must be on a single line. A semicolon `;` can be used to terminate the action, but it is optional.
- Lex rules are written in a file with the extension `.l` or `.lex`. The file can also contain some optional sections, such as definitions, declarations, start conditions, and user subroutines. These sections are delimited by special symbols: `%{` and `%}` for the definitions section, `%%` for the rules section, and `%{` and `%}` for the user subroutines section. The declarations section can contain any C code that is copied verbatim to the generated C file. The definitions section can contain macros or definitions of regular expressions that can be used in the rules. The start conditions section can define different states or modes for the lexical analyzer, which can be switched by using the `BEGIN` macro in the actions. The user subroutines section can contain any C functions that are used by the actions or the calling program.
- The following is an example of a Lex file that implements a simple lexical analyzer for a subset of the C language:

    ```
    %{ /* definitions section */
    #include <stdio.h>
    #include <stdlib.h>
    #define MAXID 32 /* maximum length of an identifier */
    enum tokentype { /* token codes */
        T_EOF, T_INT, T_FLOAT, T_CHAR, T_IF, T_ELSE, T_WHILE, T_FOR, T_RETURN, T_ID, T_NUM, T_STR, T_LPAR, T_RPAR, T_LBRA, T_RBRA, T_LBRC, T_RBRC, T_COMMA, T_SEMI, T_PLUS, T_MINUS, T_MUL, T_DIV, T_MOD, T_ASSIGN, T_EQ, T_NE, T_LT, T_LE, T_GT, T_GE, T_AND, T_OR, T_NOT
    };
    char lexeme[MAXID+1]; /* buffer to store the current lexeme */
    int lineno = 1; /* line number counter */
    %}

    /* regular expression definitions */
    letter [A-Za-z_]
    digit [0-9]
    id {letter}({letter}|{digit})*
    num {digit}+(\.{digit}+)?(E[+-]?{digit}+)?
    str \"(\\.|[^\\"])*\"
    ws [ \t\n]+

    %%

    /* rules section */
    {ws} { /* ignore whitespace and newline */ 
        if (*yytext == '\n') lineno++; /* increment line number */
    }
    "int" { return T_INT; }
    "float" { return T_FLOAT; }
    "char" { return T_CHAR; }
    "if" { return T_IF; }
    "else" { return T_ELSE; }
    "while" { return T_WHILE; }
    "for" { return T_FOR; }
    "return" { return T_RETURN; }
    {id} { /* identifier */
        strncpy(lexeme, yytext, MAXID); /* copy the lexeme to the buffer

```




# 3. Generate YACC specification for a few syntactic categories.

- YACC stands for Yet Another Compiler-Compiler, which is a tool that generates a parser for a given grammar.
- A parser is a program that analyzes the syntactic structure of a given input and checks if it conforms to the rules of the grammar.
- A grammar is a set of production rules that define the syntax of a language.
- A syntactic category is a group of symbols that can be substituted for each other in a production rule.
- For example, in the grammar of arithmetic expressions, E is a syntactic category that represents any expression, and can be substituted by E + E, E - E, E * E, E / E, or (E).
- To generate a YACC specification for a few syntactic categories, we need to follow these steps:

  - Define the tokens that represent the terminal symbols of the grammar, such as numbers, operators, parentheses, etc.
  - Define the precedence and associativity of the operators, if any.
  - Define the start symbol of the grammar, which is usually the syntactic category that represents the whole input.
  - Define the production rules for each syntactic category, using the tokens and other syntactic categories as symbols.
  - Write the actions that the parser should perform when it recognizes a production rule, such as evaluating the expression, printing the result, etc.

- For example, here is a YACC specification for the syntactic categories of arithmetic expressions, identifiers, and assignments:

```
%token NUM ID
%left '+' '-'
%left '*' '/'
%%
S: E '\n' { printf("%d\n", $1); }
 | ID '=' E '\n' { sym[$1] = $3; }
 ;
E: E '+' E { $$ = $1 + $3; }
 | E '-' E { $$ = $1 - $3; }
 | E '*' E { $$ = $1 * $3; }
 | E '/' E { $$ = $1 / $3; }
 | '(' E ')' { $$ = $2; }
 | NUM { $$ = $1; }
 | ID { $$ = sym[$1]; }
 ;
%%
```

- In this specification, NUM and ID are the tokens that represent numbers and identifiers, respectively.
- The operators have left associativity and precedence as defined by the %left directives.
- The start symbol is S, which represents either an expression followed by a newline, or an assignment followed by a newline.
- The production rules for E, ID, and '=' are defined using the tokens and other syntactic categories as symbols.
- The actions are written in C code inside curly braces, and use the $$ and $n variables to refer to the value of the left-hand side and the n-th right-hand side symbol, respectively.
- The sym array is used to store the values of the identifiers.



Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to recognize a valid arithmetic expression that uses operator +, -, *, and /. Here is the content in markdown format:

# Program to recognize a valid arithmetic expression that uses operator +, -, *, and /

An arithmetic expression is a combination of operands and operators that can be evaluated to a single value. For example, `2 + 3 * 4` is an arithmetic expression that evaluates to `14`.

To recognize a valid arithmetic expression, we need to follow some rules and conventions:

- The expression must have at least one operand and zero or more operators.
- The operands can be integers, decimals, or variables. For example, `2`, `3.14`, and `x` are valid operands.
- The operators can be +, -, *, or /. For example, `+`, `-`, `*`, and `/` are valid operators.
- The expression must follow the order of operations, which is parentheses, exponentiation, multiplication and division, and addition and subtraction. For example, `(2 + 3) * 4` is valid, but `2 + 3 * 4)` is not valid.
- The expression must have balanced parentheses, which means that every opening parenthesis must have a matching closing parenthesis. For example, `(2 + 3) * (4 - 5)` is valid, but `(2 + 3 * (4 - 5)` is not valid.
- The expression must not have any syntax errors, such as missing operands, operators, or parentheses. For example, `2 + * 4` is not valid, because there is a missing operand between `+` and `*`.

One way to write a program to recognize a valid arithmetic expression is to use a stack data structure. A stack is a collection of items that follows the last-in, first-out (LIFO) principle, which means that the last item added to the stack is the first item removed from the stack. For example, if we add `a`, `b`, and `c` to a stack, then the stack will look like this:

```
c
b
a
```

And if we remove an item from the stack, we will get `c`, and the stack will look like this:

```
b
a
```

We can use a stack to store the operands and operators of the expression, and check if they are valid and follow the order of operations. Here is the pseudocode of the algorithm:

```
# Initialize an empty stack
stack = []

# Loop through each character of the expression
for char in expression:

  # If the character is an opening parenthesis, push it to the stack
  if char == "(":
    stack.push(char)

  # If the character is a closing parenthesis, pop the stack until an opening parenthesis is found
  elif char == ")":
    # If the stack is empty, the expression is not valid
    if stack.is_empty():
      return False
    # Pop the stack and store the popped item
    popped = stack.pop()
    # Loop until an opening parenthesis is found
    while popped != "(":
      # If the stack is empty, the expression is not valid
      if stack.is_empty():
        return False
      # Pop the stack and store the popped item
      popped = stack.pop()
  
  # If the character is an operator, push it to the stack
  elif char in "+-*/":
    stack.push(char)

  # If the character is an operand, push it to the stack
  elif char.is_operand():
    stack.push(char)

  # If the character is anything else, the expression is not valid
  else:
    return False

# After looping through the expression, check if the stack is empty or has only one operand
# If yes, the expression is valid
# If no, the expression is not valid
if stack.is_empty() or (stack.size() == 1 and stack.peek().is_operand()):
  return True
else:
  return False
```

This program will return `True` if the expression is valid, and `False` otherwise. For example, if the expression is `2 + 3 * 4`, the program will return `True`. If the expression is `2 + * 4`, the program will return `False`.



Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to recognize a valid variable which starts with a letter followed by any number of letters or digits. Here is the content in markdown format:

# Program to recognize a valid variable which starts with a letter followed by any number of letters or digits

- A variable is a name given to a memory location that can store a value of a certain type.
- A valid variable name must follow some rules, such as:
  - It must start with a letter (either uppercase or lowercase) or an underscore (_).
  - It can contain any number of letters, digits, or underscores after the first character.
  - It cannot contain any other symbols, such as spaces, punctuation marks, or operators.
  - It cannot be a reserved word, such as `if`, `else`, `for`, `while`, etc.
- To write a program to recognize a valid variable, we can use a regular expression (regex) to match the pattern of a valid variable name.
- A regular expression is a sequence of characters that defines a search pattern for text.
- A regex can use some special characters, called metacharacters, to specify the rules of the pattern, such as:
  - `^` matches the beginning of a string.
  - `$` matches the end of a string.
  - `[ ]` matches any one of the characters inside the brackets.
  - `+` matches one or more occurrences of the preceding character or group.
  - `*` matches zero or more occurrences of the preceding character or group.
  - `|` matches either the left or the right expression.
  - `( )` groups a subexpression as a single unit.
- To match a valid variable name, we can use the following regex:

  - `^[A-Za-z_][A-Za-z0-9_]*$`
  - This regex means:
    - The variable name must start with a letter or an underscore, followed by any number of letters, digits, or underscores, and end with the same.
    - The `^` and `$` metacharacters ensure that the whole string is matched, not just a part of it.
    - The `[A-Za-z_]` inside the brackets matches any letter or underscore.
    - The `[A-Za-z0-9_]` inside the brackets matches any letter, digit, or underscore.
    - The `+` and `*` metacharacters indicate that the preceding character or group can repeat one or more times or zero or more times, respectively.
- To write a program to recognize a valid variable using this regex, we can use a programming language that supports regex, such as Python, Java, C#, etc.
- Here is an example of a Python program that uses the `re` module to import the regex functions:

```python
# Import the re module
import re

# Define the regex pattern for a valid variable name
pattern = "^[A-Za-z_][A-Za-z0-9_]*$"

# Ask the user to enter a variable name
variable = input("Enter a variable name: ")

# Use the re.match function to check if the variable name matches the pattern
match = re.match(pattern, variable)

# If there is a match, print "Valid variable name"
if match:
  print("Valid variable name")
# Else, print "Invalid variable name"
else:
  print("Invalid variable name")
```

- Here is an example of the output of the program:

```
Enter a variable name: x
Valid variable name
```

```
Enter a variable name: _y
Valid variable name
```

```
Enter a variable name: 1z
Invalid variable name
```

```
Enter a variable name: a+b
Invalid variable name
```

```
Enter a variable name: for
Invalid variable name
```




# c) Implementation of Calculator using LEX and YACC

- LEX and YACC are tools that help in creating lexical analyzers and parsers for a given grammar.
- A lexical analyzer is a program that converts a stream of characters into a stream of tokens, such as numbers, operators, identifiers, etc.
- A parser is a program that analyzes the syntactic structure of a stream of tokens and checks if it conforms to a given grammar. A grammar is a set of rules that define the syntax of a language.
- A calculator is an example of a program that can be implemented using LEX and YACC. A calculator can perform arithmetic operations on numbers and evaluate expressions.
- To implement a calculator using LEX and YACC, we need to do the following steps:

  - Define the tokens and the regular expressions that match them in a LEX file. For example, we can define tokens for numbers, operators, parentheses, etc.
  - Define the grammar and the actions that are executed when a rule is matched in a YACC file. For example, we can define rules for expressions, terms, factors, etc. and use the actions to perform the calculations and store the results in a variable.
  - Compile the LEX and YACC files using the commands `lex` and `yacc` to generate the C source code for the lexical analyzer and the parser.
  - Compile the C source code using a C compiler and link it with the library `libfl.a` to create the executable file for the calculator.
  - Run the executable file and enter the expressions to be evaluated by the calculator.

- Here is an example of a LEX file for a simple calculator that can handle integers, addition, subtraction, multiplication, and division:

  ```
  %{
  #include "y.tab.h"
  %}

  %%
  [0-9]+  { yylval = atoi(yytext); return NUMBER; }
  [ \t\n] { /* ignore whitespace */ }
  [-+*/()] { return *yytext; }
  . { printf("Invalid character: %s\n", yytext); exit(1); }
  %%
  ```

- Here is an example of a YACC file for a simple calculator that can handle integers, addition, subtraction, multiplication, and division:

  ```
  %{
  #include <stdio.h>
  %}

  %token NUMBER

  %left '+' '-'
  %left '*' '/'

  %%

  expr: expr '+' expr { $$ = $1 + $3; }
      | expr '-' expr { $$ = $1 - $3; }
      | expr '*' expr { $$ = $1 * $3; }
      | expr '/' expr { $$ = $1 / $3; }
      | '(' expr ')' { $$ = $2; }
      | NUMBER { $$ = $1; }
      ;

  %%

  int main() {
    printf("Enter an expression: ");
    yyparse();
    return 0;
  }

  int yyerror(char *s) {
    printf("Error: %s\n", s);
    return 0;
  }
  ```

- To compile and run the calculator, we can use the following commands:

  ```
  lex calc.l
  yacc -d calc.y
  cc y.tab.c -lfl -o calc
  ./calc
  ```



Hello, I am Sydney, your AI assistant. I can help you with your query.

# d) Convert the BNF rules into YACC form and write code to generate abstract syntax tree

- BNF (Backus-Naur form) is a notation for describing the syntax of a language using production rules.
- YACC (Yet Another Compiler-Compiler) is a tool that generates a parser from a grammar written in BNF form.
- An abstract syntax tree (AST) is a data structure that represents the syntactic structure of a program or an expression.
- To convert BNF rules into YACC form, we need to follow some steps:
  - Identify the terminals and non-terminals of the grammar and declare them using %token and %type directives.
  - Write the production rules in the format: non-terminal : symbol-list ;
  - Use curly braces { } to enclose the semantic actions that manipulate the AST nodes.
  - Use $$ to refer to the value of the left-hand side non-terminal and $n to refer to the value of the nth symbol on the right-hand side.
  - Use node() function to create an AST node with a given operator and operands.
- For example, consider the following BNF rules for a simple arithmetic expression grammar:

```
<expr> ::= <term> | <term> + <expr> | <term> - <expr>
<term> ::= <factor> | <factor> * <term> | <factor> / <term>
<factor> ::= <number> | ( <expr> )
<number> ::= <digit> | <digit> <number>
<digit> ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
```

- The corresponding YACC form with code to generate AST is:

```
%token NUMBER
%type <val> expr term factor number

%%

expr : term { $$ = $1; }
     | term '+' expr { $$ = node('+', $1, $3); }
     | term '-' expr { $$ = node('-', $1, $3); }
     ;

term : factor { $$ = $1; }
     | factor '*' term { $$ = node('*', $1, $3); }
     | factor '/' term { $$ = node('/', $1, $3); }
     ;

factor : number { $$ = $1; }
       | '(' expr ')' { $$ = $2; }
       ;

number : NUMBER { $$ = node('N', $1, NULL); }
       ;

%%
```



Hello, I am Sydney, your AI assistant. I can help you with your programming tasks. Here is the content you requested:

# 4. Write program to find ε – closure of all states of any given NFA with ε transition.

- An NFA with ε transition is a nondeterministic finite automaton that can move from one state to another without consuming any input symbol, by using a special transition labeled ε.
- The ε-closure of a state q is the set of all states that can be reached from q by following only ε transitions, including q itself.
- The ε-closure of a set of states Q is the union of the ε-closures of all states in Q.
- To find the ε-closure of all states of an NFA with ε transition, we can use a recursive algorithm that performs a depth-first search on the transition graph of the NFA, starting from each state and marking the visited states.
- The pseudocode of the algorithm is as follows:

```
# Input: An NFA with ε transition N = (Q, Σ, δ, q0, F)
# Output: A dictionary that maps each state in Q to its ε-closure

# Initialize an empty dictionary C
C = {}

# Define a recursive function that finds the ε-closure of a state q
def find_epsilon_closure(q):
  # If q is already in C, return its value
  if q in C:
    return C[q]
  # Otherwise, initialize an empty set S
  else:
    S = {}
    # Add q to S
    S.add(q)
    # For each state p that can be reached from q by an ε transition
    for p in δ(q, ε):
      # Recursively find the ε-closure of p and add it to S
      S = S.union(find_epsilon_closure(p))
    # Store S as the value of q in C
    C[q] = S
    # Return S
    return S

# For each state q in Q
for q in Q:
  # Call the recursive function to find the ε-closure of q
  find_epsilon_closure(q)

# Return C as the final result
return C
```



# 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transition is a nondeterministic finite automaton that can make transitions without consuming any input symbol, denoted by ε. An NFA without ε transition is a nondeterministic finite automaton that can only make transitions by consuming input symbols.

To convert an NFA with ε transition to an NFA without ε transition, we can use the following algorithm:

- For each state q in the NFA with ε transition, compute ε-closure(q), which is the set of states that can be reached from q by following only ε transitions.
- For each state q in the NFA with ε transition, and for each input symbol a, compute the transition function δ'(q, a) as follows:
  - δ'(q, a) = ∪{δ(p, a) | p ∈ ε-closure(q)}, where δ(p, a) is the set of states that can be reached from p by consuming a in the NFA with ε transition.
- The NFA without ε transition has the same set of states and final states as the NFA with ε transition, but the transition function is δ' instead of δ.
- The initial state of the NFA without ε transition is ε-closure(q0), where q0 is the initial state of the NFA with ε transition.

Here is a pseudocode for the algorithm:

```
function convert(NFA with ε transition):
  NFA without ε transition = new NFA()
  NFA without ε transition.states = NFA with ε transition.states
  NFA without ε transition.final_states = NFA with ε transition.final_states
  NFA without ε transition.initial_state = ε-closure(NFA with ε transition.initial_state)
  for each state q in NFA without ε transition.states:
    for each input symbol a in NFA without ε transition.alphabet:
      NFA without ε transition.transition_function[q, a] = ∅
      for each state p in ε-closure(q):
        NFA without ε transition.transition_function[q, a] = NFA without ε transition.transition_function[q, a] ∪ NFA with ε transition.transition_function[p, a]
  return NFA without ε transition
```



Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to convert NFA to DFA. Here is the content in markdown format:

# Program to convert NFA to DFA

## Introduction

- NFA stands for nondeterministic finite automaton, which is a mathematical model of computation that accepts or rejects a string based on the possible transitions from the initial state to the final states.
- DFA stands for deterministic finite automaton, which is a special case of NFA where each state has exactly one transition for each input symbol and there are no epsilon transitions (transitions without any input symbol).
- Converting NFA to DFA is a process of eliminating nondeterminism and epsilon transitions from NFA and creating an equivalent DFA that accepts the same language as the NFA.

## Algorithm

- The algorithm for converting NFA to DFA is based on the concept of **subset construction**, which means that each state of the DFA corresponds to a subset of states of the NFA.
- The algorithm works as follows:

  1. Create a new initial state for the DFA, which is the epsilon closure of the initial state of the NFA. The epsilon closure of a state is the set of all states that can be reached from that state by following epsilon transitions only.
  2. For each state of the DFA, and for each input symbol, find the set of states that can be reached from that state by following the input symbol and then taking the epsilon closure. This set is the next state of the DFA for that input symbol.
  3. If the next state is not already in the DFA, add it as a new state and repeat step 2 for it.
  4. Mark any state of the DFA as final if it contains a final state of the NFA.

## Example

- Consider the following NFA that accepts the language of all strings over {a, b} that end with ab:

NFA

- The steps for converting this NFA to DFA are:

  1. The initial state of the DFA is the epsilon closure of the initial state of the NFA, which is {q0, q1, q3}.
  2. From the state {q0, q1, q3}, on input a, the next state is the epsilon closure of {q2}, which is {q2, q3}. This state is not in the DFA, so we add it as a new state.
  3. From the state {q0, q1, q3}, on input b, the next state is the epsilon closure of {q1}, which is {q1, q3}. This state is already in the DFA, so we do not add it again.
  4. From the state {q2, q3}, on input a, the next state is the epsilon closure of {q2}, which is {q2, q3}. This state is already in the DFA, so we do not add it again.
  5. From the state {q2, q3}, on input b, the next state is the epsilon closure of {q1, q4}, which is {q1, q3, q4}. This state is not in the DFA, so we add it as a new state.
  6. From the state {q1, q3, q4}, on input a, the next state is the epsilon closure of {q2}, which is {q2, q3}. This state is already in the DFA, so we do not add it again.
  7. From the state {q1, q3, q4}, on input b, the next state is the epsilon closure of {q1, q4}, which is {q1, q3, q4}. This state is already in the DFA, so we do not add it again.
  8. The final states of the DFA are those that contain a final state of the NFA, which are {q1, q3, q4} and {q2, q3}.

- The resulting DFA is:

DFA

## Code

- Here is a possible Python code for implementing the algorithm:

```python
# Define the NFA as a dictionary of dictionaries
# The keys are the states and the values are dictionaries of transitions
# The keys of the inner dictionaries are the input symbols and the values are sets of next states
# Epsilon transitions are denoted by the empty string ''

nfa = {
    '

```




Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to minimize any given DFA. Here is the content in markdown format:

# Program to minimize any given DFA

A DFA (deterministic finite automaton) is a finite state machine that accepts or rejects a given string based on its transition function and final states. A DFA can be minimized by removing unreachable states and equivalent states.

## Removing unreachable states

Unreachable states are those states that cannot be reached from the initial state by any input string. To remove unreachable states, we can use the following algorithm:

- Start with a set S that contains only the initial state.
- Repeat until S does not change:
  - For each state q in S and each input symbol a, add the state δ(q, a) to S, where δ is the transition function of the DFA.
- Remove all states that are not in S from the DFA.

## Removing equivalent states

Equivalent states are those states that have the same behavior for any input string, i.e., they either accept or reject the same strings. To remove equivalent states, we can use the following algorithm:

- Start with a partition P of the states into two sets: F and Q - F, where F is the set of final states and Q is the set of all states.
- Repeat until P does not change:
  - For each pair of sets A and B in P, and each input symbol a, check if there is a pair of states p in A and q in B such that δ(p, a) and δ(q, a) are in different sets of P. If so, split A and B into two sets each, one containing the states that have transitions to the same set of P, and the other containing the states that have transitions to different sets of P.
- Replace each set in P with a single state, and update the transition function and the initial and final states accordingly.

## Example

Consider the following DFA:

DFA

To minimize this DFA, we first remove the unreachable state 4. The resulting DFA is:

DFA without state 4

Then, we remove the equivalent states 1 and 3. The partition P is initially {{0}, {1, 3}, {2}}, and after one iteration, it becomes {{0}, {1}, {2, 3}}. The resulting DFA is:

Minimized DFA



# 8. Develop an operator precedence parser for a given language.

- An operator precedence parser is a bottom-up parser that can parse a subset of context-free grammars, namely those that are operator precedence grammars.
- An operator precedence grammar is a grammar that has the following properties:
  - Every production is of the form `A -> w`, where `A` is a non-terminal and `w` is a string of terminals and/or non-terminals.
  - No production has an empty right-hand side, i.e., `w` is not empty.
  - There are no two distinct productions with the same non-terminal on the left-hand side and the same terminal on the right-hand side, i.e., if `A -> w` and `A -> x` are two productions, then `w` and `x` do not start with the same terminal.
  - For every pair of terminals `a` and `b`, there is a precedence relation between them, denoted by `a < b`, `a = b`, or `a > b`, which is consistent and transitive. The precedence relation determines the order of evaluation of the operators represented by the terminals.
- An operator precedence parser works as follows:
  - It uses a stack to store symbols (terminals and non-terminals) and an input buffer to store the remaining input string.
  - It scans the input from left to right and performs one of the following actions at each step:
    - Shift: If the top of the stack is `$` (the end-of-input marker) or has lower precedence than the next input symbol, push the next input symbol onto the stack and advance the input pointer.
    - Reduce: If the top of the stack has higher precedence than the next input symbol, pop symbols from the stack until a handle is found. A handle is a substring of the stack that matches the right-hand side of a production. Replace the handle by the corresponding left-hand side non-terminal and push it onto the stack.
    - Accept: If the stack contains only the start symbol and the input buffer contains only `$`, the parsing is successful and the parser halts.
    - Error: If none of the above actions can be performed, the parser reports an error and halts.
- An example of an operator precedence parser for a simple arithmetic language is given below:

  - The grammar of the language is:

    ```
    E -> E + E | E * E | (E) | id
    ```

  - The precedence relation of the terminals is:

    ```
    $ < id, (, +, *
    id > $, +, *, )
    ( < id, (, +, *
    ) > id, (, +, *, $
    + < id, (, +
    + > +, *, ), $
    * < id, (, *
    * > +, *, ), $
    ```

  - The parsing table for the grammar is:

    | Stack | Input | Action |
    | ----- | ----- | ------ |
    | $     | id + id * id $ | Shift |
    | $ id  | + id * id $ | Reduce by E -> id |
    | $ E   | + id * id $ | Shift |
    | $ E + | id * id $ | Shift |
    | $ E + id | * id $ | Reduce by E -> id |
    | $ E + E | * id $ | Reduce by E -> E + E |
    | $ E   | * id $ | Shift |
    | $ E * | id $ | Shift |
    | $ E * id | $ | Reduce by E -> id |
    | $ E * E | $ | Reduce by E -> E * E |
    | $ E   | $ | Accept |



# Simulate First and Follow of any given grammar

- First and follow are two sets that are used to determine the parsing table of a grammar.
- First set of a symbol is the set of terminals that can appear at the beginning of a string derived from that symbol.
- Follow set of a symbol is the set of terminals that can appear immediately after that symbol in a string derived from the start symbol.
- To find the first set of a symbol, we can use the following rules:
  - If the symbol is a terminal, then the first set is just that terminal.
  - If the symbol is a non-terminal, then for each production of the form `A -> α`, we add the first set of `α` to the first set of `A`, except for the empty string `ε`.
  - If the symbol is a non-terminal and there is a production of the form `A -> ε`, then we add `ε` to the first set of `A`.
  - If the symbol is a string of symbols, then we add the first set of the first symbol to the first set of the string, except for `ε`. If the first symbol can derive `ε`, then we also add the first set of the second symbol, and so on, until we reach a symbol that cannot derive `ε` or the end of the string.
- To find the follow set of a symbol, we can use the following rules:
  - If the symbol is the start symbol, then we add `$` (the end-of-input marker) to the follow set of the symbol.
  - If the symbol is a non-terminal and there is a production of the form `A -> αBβ`, then we add the first set of `β` to the follow set of `B`, except for `ε`.
  - If the symbol is a non-terminal and there is a production of the form `A -> αB` or `A -> αBβ` where `β` can derive `ε`, then we add the follow set of `A` to the follow set of `B`.
- To simulate the first and follow sets of a given grammar, we can use the following algorithm:
  - Initialize the first and follow sets of each symbol to be empty.
  - Repeat the following steps until no more changes occur:
    - For each production of the form `A -> α`, apply the rules for finding the first set of `A`.
    - For each production of the form `A -> αBβ`, apply the rules for finding the follow set of `B`.
  - Return the first and follow sets of each symbol.
- For example, given the following grammar:

```
S -> AB
A -> a | ε
B -> b | ε
```

- We can simulate the first and follow sets as follows:

```
First(S) = First(A) = {a, ε}
First(B) = {b, ε}
Follow(S) = {$}
Follow(A) = First(B) - {ε} = {b}
Follow(B) = Follow(S) = {$}
```

- Therefore, the first and follow sets of the grammar are:

```
First(S) = {a, ε}
First(A) = {a, ε}
First(B) = {b, ε}
Follow(S) = {$}
Follow(A) = {b}
Follow(B) = {$}
```



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is the content I have generated for you:

# 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of top-down parser that uses a set of recursive procedures to process the input. Each procedure implements one of the production rules of the grammar, and calls itself or other procedures as needed.

To construct a recursive descent parser for an expression, we need to follow these steps:

- Define the grammar of the expression language, and make sure it is unambiguous and suitable for recursive descent parsing. For example, we can use the following grammar:

```
E -> T + E | T
T -> F * T | F
F -> (E) | id
```

- Write a procedure for each non-terminal symbol in the grammar, and use the lookahead symbol to decide which production rule to apply. For example, we can write the following procedures in pseudocode:

```
procedure E()
  T() // parse a term
  if lookahead = '+' then
    match('+') // consume the '+'
    E() // parse another expression
  end if
end procedure

procedure T()
  F() // parse a factor
  if lookahead = '*' then
    match('*') // consume the '*'
    T() // parse another term
  end if
end procedure

procedure F()
  if lookahead = '(' then
    match('(') // consume the '('
    E() // parse an expression
    match(')') // consume the ')'
  else if lookahead = id then
    match(id) // consume the identifier
  else
    error() // report a syntax error
  end if
end procedure
```

- Write a procedure to match the input symbols with the expected symbols, and advance the lookahead symbol. For example, we can write the following procedure in pseudocode:

```
procedure match(symbol)
  if lookahead = symbol then
    lookahead = next input symbol // get the next symbol from the input
  else
    error() // report a syntax error
  end if
end procedure
```

- Write a procedure to initialize the parser and start the parsing process. For example, we can write the following procedure in pseudocode:

```
procedure parse()
  lookahead = next input symbol // get the first symbol from the input
  E() // parse an expression
  if lookahead = end of input then
    success() // report a successful parsing
  else
    error() // report a syntax error
  end if
end procedure
```

- Test the parser with some sample inputs and verify the results. For example, we can test the parser with the input `id + id * id`, and the parser should accept it and produce the following parse tree:

```
    E
   / \
  T   E
 /   / \
F   T   E
|  / \  |
id F  T F
   |  | |
   id F id
      |
      id
```



# 11. Construct a Shift Reduce Parser for a given language.

A shift reduce parser is a type of bottom-up parser that uses a stack and an input buffer to parse a given string. The parser performs two main operations: shift and reduce.

- Shift: The parser moves the next input symbol from the input buffer to the top of the stack.
- Reduce: The parser replaces the topmost symbols on the stack with a non-terminal symbol, according to a production rule in the grammar.

The parser repeats these operations until either the input buffer is empty and the stack contains only the start symbol, or an error occurs. The parser can use a parsing table to decide which operation to perform at each step, based on the current state of the stack and the input buffer.

The following steps describe how to construct a shift reduce parser for a given language:

1. Write the grammar for the language in the form of production rules. The grammar should be unambiguous and free of left recursion and common prefixes.
2. Convert the grammar into an augmented grammar by adding a new start symbol and a new production rule of the form S' -> S, where S is the original start symbol.
3. Construct the canonical collection of LR(0) items for the augmented grammar. An LR(0) item is a production rule with a dot (.) indicating the current position of the parser. The canonical collection is a set of sets of LR(0) items, where each set is called a state and represents a possible configuration of the stack and the input buffer. The canonical collection can be constructed by applying the following rules:

  - Start with the initial state, which contains only the item S' -> .S
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then add all the items of the form B -> .c to the same state, where c is any string of symbols that can be derived from B. This is called the closure operation.
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then create a new state that contains only the item A -> aB.b and add a transition from the current state to the new state labeled with B. This is called the goto operation.
  - Repeat the closure and goto operations until no new states or transitions can be added.

4. Construct the parsing table for the canonical collection of LR(0) items. The parsing table has two parts: an action table and a goto table. The action table has one row for each state and one column for each terminal symbol and the end-of-input marker ($). The goto table has one row for each state and one column for each non-terminal symbol. The entries in the parsing table are determined by the following rules:

  - For each state, if it contains an item of the form A -> a.b, where a and b are strings of symbols and b is not empty, then the entry in the action table for that state and the first symbol of b is "shift s", where s is the state that can be reached by following the transition labeled with b from the current state. This means that the parser should perform a shift operation and move to state s.
  - For each state, if it contains an item of the form A -> a., where a is a string of symbols, then the entry in the action table for that state and the lookahead symbol (the next input symbol or $) is "reduce r", where r is the number of the production rule A -> a in the grammar. This means that the parser should perform a reduce operation and apply the production rule A -> a.
  - For each state, if it contains the item S' -> S., then the entry in the action table for that state and $ is "accept". This means that the parser should accept the input string as valid.
  - For each state, if it contains an item of the form A -> a.Bb, where a and b are strings of symbols and B is a non-terminal, then the entry in the goto table for that state and B is the state that can be reached by following the transition labeled with B from the current state. This means that the parser should move to that state after performing a reduce operation with a production rule that has B on the right-hand side.
  - For any other entry in the parsing table, leave it blank or mark it as "error". This means that the parser should report an error if it encounters that situation.

5. Use the parsing table to parse a given input string. The parser starts with an empty stack and the input string in the input buffer.



# Loop unrolling

- Loop unrolling is a technique to optimize the performance of a program by reducing the number of iterations of a loop.
- Loop unrolling can reduce the overhead of loop control instructions, such as branch, compare, and increment, and increase the instruction-level parallelism of the code.
- Loop unrolling can also improve the cache locality of the data accessed by the loop, and reduce the number of pipeline stalls or cache misses.
- Loop unrolling can be done manually by the programmer, or automatically by the compiler or the processor.
- Loop unrolling can be applied to any loop that has a fixed or predictable number of iterations, and does not contain any break, continue, or return statements inside the loop body.
- Loop unrolling can be done by replicating the loop body multiple times, and adjusting the loop counter and the loop bounds accordingly.
- For example, consider the following loop that adds two arrays of size N:

```c
for (int i = 0; i < N; i++) {
  c[i] = a[i] + b[i];
}
```

- This loop can be unrolled by a factor of 4, meaning that the loop body is replicated 4 times, and the loop counter is incremented by 4 in each iteration:

```c
for (int i = 0; i < N; i += 4) {
  c[i] = a[i] + b[i];
  c[i+1] = a[i+1] + b[i+1];
  c[i+2] = a[i+2] + b[i+2];
  c[i+3] = a[i+3] + b[i+3];
}
```

- This loop unrolling reduces the number of iterations of the loop from N to N/4, and the number of loop control instructions from N to N/4.
- This loop unrolling also increases the instruction-level parallelism, as the four additions can be executed in parallel by the processor, if it has enough functional units and registers.
- This loop unrolling also improves the cache locality, as the four elements of each array are accessed consecutively, and are likely to be in the same cache line.
- However, loop unrolling also has some drawbacks, such as:
  - Increasing the code size and the instruction cache pressure, which may lead to more cache misses or branch mispredictions.
  - Introducing alignment or padding issues, which may cause performance degradation or memory waste.
  - Requiring extra handling for the case when the loop bound is not divisible by the unrolling factor, which may introduce more branch instructions or conditional statements.
  - Making the code less readable and maintainable, especially if the loop body is complex or contains function calls or nested loops.



# 13. Write a program to perform constant propagation.

Constant propagation is a compiler optimization technique that replaces the use of constant variables with their values at compile time. This can improve the performance and readability of the code, as well as eliminate unnecessary memory accesses.

A program to perform constant propagation can be written in pseudocode as follows:

```
// Input: a list of statements in the form of (variable, operator, operand1, operand2)
// Output: a list of statements with constant propagation applied

// Initialize an empty dictionary to store the values of constant variables
constants = {}

// Initialize an empty list to store the output statements
output = []

// Loop through each statement in the input list
for each statement in input:

  // Extract the variable, operator, operand1 and operand2 from the statement
  (variable, operator, operand1, operand2) = statement

  // If the operator is "=", then the statement is an assignment
  if operator == "=":

    // If the operand1 is a constant value, then store it in the constants dictionary
    if operand1 is a constant value:
      constants[variable] = operand1

    // Else, if the operand1 is a constant variable, then replace it with its value from the constants dictionary
    else if operand1 is a constant variable:
      operand1 = constants[operand1]

    // Add the statement to the output list
    output.append((variable, operator, operand1, operand2))

  // Else, if the operator is not "=", then the statement is an expression
  else:

    // If the operand1 is a constant value or a constant variable, then replace it with its value from the constants dictionary
    if operand1 is a constant value or a constant variable:
      operand1 = constants[operand1]

    // If the operand2 is a constant value or a constant variable, then replace it with its value from the constants dictionary
    if operand2 is a constant value or a constant variable:
      operand2 = constants[operand2]

    // If both operands are constant values, then evaluate the expression and assign the result to the variable
    if operand1 and operand2 are constant values:
      variable = evaluate(operator, operand1, operand2)

    // Add the statement to the output list
    output.append((variable, operator, operand1, operand2))

// Return the output list
return output
```

For example, given the following input list of statements:

```
a = 10
b = a + 5
c = b * 2
d = c - a
e = d / 5
```

The output list of statements after applying constant propagation would be:

```
a = 10
b = 15
c = 30
d = 20
e = 4
```



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic 14. Implement Intermediate code generation for simple expressions.

# 14. Implement Intermediate code generation for simple expressions

Intermediate code generation is the process of translating a source program into an intermediate representation that is independent of the target machine and the source language. Intermediate code can be in the form of abstract syntax trees, three-address code, quadruples, triples, or indirect triples.

The purpose of intermediate code generation is to facilitate the analysis and optimization of the program, and to simplify the final code generation phase.

One of the common forms of intermediate code is three-address code, which consists of a sequence of instructions, each of which has at most three operands. A three-address instruction can have the following general form:

`x = y op z`

where `x`, `y`, and `z` are names, constants, or compiler-generated temporaries, and `op` is an arithmetic, logical, or relational operator.

To generate three-address code for simple expressions, we can use the following algorithm:

- Scan the expression from left to right and assign priorities to each operator according to the operator precedence rules.
- Identify the subexpression with the highest priority and generate a temporary variable for its value. Generate a three-address instruction of the form `t = y op z`, where `t` is the temporary variable, `y` and `z` are the operands of the subexpression, and `op` is the operator.
- Replace the subexpression with the temporary variable in the original expression and repeat the previous steps until the expression is reduced to a single variable or constant.
- The final variable or constant is the result of the expression.

For example, consider the expression:

`a + b * c - d / e`

The priorities of the operators are as follows:

`a + b * c - d / e`
`   3   3   2   2`

The subexpression with the highest priority is `b * c`, so we generate a temporary variable `t1` and a three-address instruction:

`t1 = b * c`

We replace the subexpression with `t1` and get:

`a + t1 - d / e`

The next subexpression with the highest priority is `d / e`, so we generate another temporary variable `t2` and a three-address instruction:

`t2 = d / e`

We replace the subexpression with `t2` and get:

`a + t1 - t2`

The next subexpression with the highest priority is `a + t1`, so we generate another temporary variable `t3` and a three-address instruction:

`t3 = a + t1`

We replace the subexpression with `t3` and get:

`t3 - t2`

The final subexpression is `t3 - t2`, so we generate another temporary variable `t4` and a three-address instruction:

`t4 = t3 - t2`

The final variable `t4` is the result of the expression.

The complete sequence of three-address instructions for the expression is:

`t1 = b * c`
`t2 = d / e`
`t3 = a + t1`
`t4 = t3 - t2`



Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write the content in markdown format on the topic of implementing the back end of the compiler which takes the three address code and produces the 8086 assembly language. Here is the content:

# Implementing the back end of the compiler which takes the three address code and produces the 8086 assembly language

- The back end of the compiler is the part that generates the target code from the intermediate code, such as the three address code (TAC).
- The 8086 assembly language is a low-level programming language for the Intel 8086 microprocessor, which has a 16-bit architecture and supports 8-bit and 16-bit data types.
- To implement the back end of the compiler, we need to perform the following steps:

  - Define the target machine model, which specifies the registers, memory, instructions, and addressing modes of the 8086 processor.
  - Define the instruction selection algorithm, which maps each TAC instruction to one or more 8086 assembly instructions, based on the target machine model and the TAC operands.
  - Define the register allocation algorithm, which assigns the TAC temporary variables to the 8086 registers or memory locations, based on the availability and usage of the registers.
  - Define the instruction scheduling algorithm, which reorders the 8086 assembly instructions to optimize the performance and reduce the stalls, based on the dependencies and latencies of the instructions.
  - Generate the 8086 assembly code by applying the instruction selection, register allocation, and instruction scheduling algorithms to the TAC code.

- Here is an example of how to implement the back end of the compiler for a simple TAC code:

  - TAC code:

    ```
    a = b + c
    d = a - e
    ```

  - Target machine model:

    - Registers: AX, BX, CX, DX, SI, DI, BP, SP
    - Memory: 64 KB of addressable space, divided into segments and offsets
    - Instructions: MOV, ADD, SUB, etc.
    - Addressing modes: register, immediate, direct, indirect, indexed, based, etc.

  - Instruction selection algorithm:

    - For each TAC instruction, choose the 8086 assembly instruction that performs the same operation and has the same or compatible operands.
    - For example, for the TAC instruction `a = b + c`, we can choose the 8086 assembly instruction `ADD a, b, c`, which adds the contents of b and c and stores the result in a.
    - If there is no single 8086 assembly instruction that matches the TAC instruction, we can use a sequence of 8086 assembly instructions that achieves the same effect.
    - For example, for the TAC instruction `d = a - e`, we can use the following sequence of 8086 assembly instructions:

      ```
      MOV d, a
      SUB d, e
      ```

      which moves the contents of a to d and then subtracts the contents of e from d.

  - Register allocation algorithm:

    - For each TAC temporary variable, assign a 8086 register or a memory location, based on the availability and usage of the registers.
    - For example, we can assign the TAC temporary variables a, b, c, d, and e to the 8086 registers AX, BX, CX, DX, and SI, respectively.
    - If there are not enough registers to hold all the TAC temporary variables, we can use a spill strategy, which stores some of the variables in memory and loads them back to registers when needed.
    - For example, if we have only four registers, we can spill the variable e to a memory location, such as [BP-4], and use the following sequence of 8086 assembly instructions for the TAC instruction `d = a - e`:

      ```
      MOV DX, AX
      MOV SI, [BP-4]
      SUB DX, SI
      ```

      which moves the contents of AX to DX, loads the contents of [BP-4] to SI, and subtracts the contents of SI from DX.

  - Instruction scheduling algorithm:

    - For each sequence of 8086 assembly instructions, reorder them to optimize the performance and reduce the stalls, based on the dependencies and latencies of the instructions.
    - For example, we can use a list scheduling algorithm, which maintains a list of ready instructions, which have no unresolved dependencies, and a list of active instructions, which are being executed by the processor.
    - The algorithm iterates over the list of ready instructions and selects the



# Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor supports a variety of instructions that can be used for different purposes. Some of the common types of instructions are:

- Data transfer instructions: These instructions are used to move data between registers, memory, and I/O ports. Some examples are MOV, PUSH, POP, IN, and OUT.
- Arithmetic instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication, and division. Some examples are ADD, SUB, MUL, DIV, and INC.
- Logical instructions: These instructions are used to perform bitwise logical operations like AND, OR, XOR, and NOT. Some examples are AND, OR, XOR, and NEG.
- Shift and rotate instructions: These instructions are used to shift or rotate the bits of a register or a memory operand. Some examples are SHL, SHR, SAL, SAR, ROL, and ROR.
- Branch instructions: These instructions are used to alter the flow of execution based on some condition. Some examples are JMP, JZ, JNZ, JC, and JNC.
- Loop instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. Some examples are LOOP, LOOPE, LOOPNE, and LOOPNZ.
- String instructions: These instructions are used to manipulate strings of bytes or words in memory. Some examples are MOVSB, MOVSW, CMPSB, CMPSW, SCASB, and SCASW.
- Flag manipulation instructions: These instructions are used to set, clear, or test the status flags of the 8086 microprocessor. Some examples are STC, CLC, CMC, STD, CLD, and LAHF.
- Miscellaneous instructions: These instructions are used for various other purposes like interrupt handling, stack operations, and processor control. Some examples are INT, IRET, HLT, NOP, and LOCK.

Each instruction has a specific format and syntax that must be followed when writing assembly code. The general format of an instruction is:

`mnemonic operand1, operand2`

where mnemonic is the name of the instruction, operand1 is the destination operand, and operand2 is the source operand. The operands can be registers, memory locations, immediate values, or I/O ports. The comma separates the operands and the operands are separated by spaces from the mnemonic.

For example, the instruction:

`MOV AX, 1234h`

moves the hexadecimal value 1234h into the AX register. The instruction:

`ADD BX, [SI]`

adds the value stored at the memory location pointed by the SI register to the BX register and stores the result in BX. The instruction:

`JMP LABEL`

jumps to the instruction labeled as LABEL. The instruction:

`IN AL, 80h`

reads a byte from the I/O port 80h and stores it in the AL register.

To assemble and run an 8086 assembly program, one needs an assembler, a linker, and an emulator. An assembler is a program that converts the assembly code into machine code. A linker is a program that combines the machine code with other libraries and modules. An emulator is a program that simulates the 8086 microprocessor and executes the machine code.

One example of an 8086 assembler is MASM (Microsoft Macro Assembler), which is a widely used assembler for the x86 architecture. MASM has a simple syntax and supports macros, directives, and structures. To assemble a MASM program, one can use the command:

`ML filename.asm`

where filename.asm is the name of the assembly file. This will produce a filename.obj file, which is the object file containing the machine code.

To link the object file with other libraries and modules, one can use the command:

`LINK filename.obj`

where filename.obj is the name of the object file. This will produce a filename.exe file, which is the executable file that can be run on an emulator.

One example of an 8086 emulator is DOSBox, which is a free and open-source emulator that can run DOS programs on various platforms. DOSBox can emulate the 8086 microprocessor and the CGA, EGA, VGA, and Tandy graphics modes. To run an executable file on DOSBox, one can use the command:

`filename.exe`

where filename.exe is the name of the executable file. This will start the execution of the program and display the output on the emulator screen.



# Add, Sub, Jump etc.

These are some of the basic instructions in assembly language, which is a low-level programming language that directly controls the hardware of a computer.

- Add: This instruction adds two operands and stores the result in the destination operand. For example, `add eax, ebx` adds the values of the registers eax and ebx and stores the sum in eax.
- Sub: This instruction subtracts the second operand from the first operand and stores the result in the destination operand. For example, `sub eax, ebx` subtracts the value of ebx from eax and stores the difference in eax.
- Jump: This instruction transfers the control flow to another location in the program, specified by a label or an address. For example, `jmp loop` jumps to the instruction labeled as loop. There are different types of jump instructions, such as conditional jumps, which depend on the status of some flags in the processor. For example, `jz loop` jumps to loop only if the zero flag is set, which means the previous arithmetic or logical operation resulted in zero.



# Note: The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- This note implies that the instructor has the authority and discretion to change the experiments according to the course objectives, the availability of resources, the level of difficulty, and the feedback from the students.
- The instructor may add new experiments to introduce new concepts, techniques, or applications that are relevant to the course.
- The instructor may delete experiments that are outdated, redundant, or irrelevant to the course.
- The instructor may modify or tune experiments to adjust the scope, the duration, the difficulty, or the expected outcomes of the experiments.
- The instructor should communicate the changes to the experiments to the students in advance and provide clear instructions and expectations for each experiment.
- The instructor should also explain the rationale behind the changes and how they will benefit the students' learning and assessment.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write some content in markdown format on the topic of why open source tools should be preferred to conduct the lab (C, C++, Lex or Flex and Yacc or Bison). Here is what I have written:

# Why open source tools should be preferred to conduct the lab (C, C++, Lex or Flex and Yacc or Bison)

- Open source tools are software that are freely available for anyone to use, modify, and distribute. They are developed and maintained by a community of developers and users who collaborate and share their code and feedback.
- Open source tools have many advantages over proprietary or closed source tools, especially for conducting the lab (C, C++, Lex or Flex and Yacc or Bison). Some of these advantages are:

  - **Cost-effectiveness**: Open source tools do not require any license fees or subscriptions to use. They can be downloaded and installed on any computer without any restrictions. This can save a lot of money for students and instructors who need to use these tools for the lab.
  - **Quality**: Open source tools are often more reliable, secure, and bug-free than proprietary tools. This is because they are constantly tested, reviewed, and improved by a large and diverse community of developers and users. They also follow open standards and protocols that ensure compatibility and interoperability with other software and hardware.
  - **Customizability**: Open source tools can be easily modified and adapted to suit the specific needs and preferences of the users. They can be extended with new features, plugins, libraries, or modules that are also open source and compatible. They can also be integrated with other open source tools to create a comprehensive and flexible toolchain for the lab.
  - **Learning**: Open source tools can provide a great opportunity for learning and skill development for students and instructors. They can access and study the source code of these tools to understand how they work, how they are designed, and how they can be improved. They can also contribute to the development and maintenance of these tools by reporting bugs, suggesting enhancements, or submitting patches.
  - **Support**: Open source tools have a strong and active community of developers and users who provide support and assistance to each other. They can use various channels such as forums, mailing lists, wikis, blogs, or social media to ask questions, share tips, or solve problems. They can also benefit from the extensive documentation, tutorials, and examples that are available online for these tools.

- Therefore, open source tools should be preferred to conduct the lab (C, C++, Lex or Flex and Yacc or Bison) as they offer many benefits in terms of cost, quality, customizability, learning, and support. They can help students and instructors to achieve their learning objectives and outcomes in an efficient and effective way.



# YACC Tools (Unix/Linux Utilities)

- YACC stands for Yet Another Compiler-Compiler. It is a computer program for the Unix operating system developed by Stephen C. Johnson.
- YACC is a parser generator, which means it can produce a program that can analyze the syntax of a given input according to a set of grammar rules.
- YACC can generate parsers for various kinds of applications, such as compilers, interpreters, calculators, command-line interfaces, etc.
- YACC takes a grammar specification file as input, which contains the rules for the syntax of the input language, and produces a C source code file as output, which contains the parser function.
- YACC uses the LALR(1) algorithm to generate the parser, which is a variant of the LR(1) algorithm that reduces the size of the parsing tables.
- YACC is supplied as a standard utility on BSD and AT&T Unix. GNU-based Linux distributions include Bison, a forward-compatible YACC replacement.
- YACC works in conjunction with another Unix utility called LEX, which is a lexical analyzer generator. LEX can produce a program that can scan the input and identify the tokens (words, symbols, numbers, etc) that are used by the parser.
- YACC and LEX are useful tools for writing compilers and interpreters, but they also have a wider range of applications. They can be used to process any structured text, such as configuration files, data formats, query languages, etc.
- YACC and LEX are examples of meta-programming, which is the technique of writing programs that can generate other programs.



# Curriculum & Evaluation Scheme CS & CSE (V & VI semester) 19

- The curriculum and evaluation scheme for computer science and engineering (CS & CSE) for the fifth and sixth semesters of the 2019 batch is based on the 2018 scheme of R.V. College of Engineering or the 2020 scheme of Dr. A.P.J. Abdul Kalam Technical University , depending on the affiliation of the college.
- The curriculum consists of theory courses, laboratory courses, project work, seminar, and internship. The theory courses cover topics such as computer algorithms, operating systems, database management systems, computer networks, software engineering, artificial intelligence, natural language processing, cryptography and network security, etc.
- The evaluation scheme consists of internal sessional exams (ISE), mid semester exams (MSE), and end semester exams (ESE). The weightage of each component varies depending on the course. The minimum passing marks for each course is 40%.
- The following table shows the curriculum and evaluation scheme for CS & CSE (V & VI semester) 19 based on the 2018 scheme of R.V. College of Engineering:

| Course Code | Course Title | Teaching Scheme (L-T-P) | Credits | Evaluation Scheme (ISE I-MSE-ISE II-ESE) |
| --- | --- | --- | --- | --- |
| 18CS51 | Management and Entrepreneurship for IT Industry | 3-0-0 | 3 | 10-30-10-50 |
| 18CS52 | Computer Networks | 3-0-0 | 3 | 10-30-10-50 |
| 18CS53 | Database Management Systems | 3-0-0 | 3 | 10-30-10-50 |
| 18CS54 | Automata Theory and Computability | 3-0-0 | 3 | 10-30-10-50 |
| 18CS55 | Application Development using Python | 3-0-0 | 3 | 10-30-10-50 |
| 18CS56 | Operating Systems | 3-0-0 | 3 | 10-30-10-50 |
| 18CSL57 | Database Management Systems Laboratory | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CSL58 | Application Development using Python Laboratory | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CSL59 | Operating Systems Laboratory | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CIV60 | Environmental Studies | 3-0-0 | 3 | 10-30-10-50 |
| 18KAK51 | Kannada Kali | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CS61 | Software Engineering | 3-0-0 | 3 | 10-30-10-50 |
| 18CS62 | Compiler Design | 3-0-0 | 3 | 10-30-10-50 |
| 18CS63 | Computer Graphics and Visualization | 3-0-0 | 3 | 10-30-10-50 |
| 18CS64 | Artificial Intelligence and Machine Learning | 3-0-0 | 3 | 10-30-10-50 |
| 18CS65x | Professional Elective I | 3-0-0 | 3 | 10-30-10-50 |
| 18CS66x | Professional Elective II | 3-0-0 | 3 | 10-30-10-50 |
| 18CSL67 | Compiler Design Laboratory | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CSL68 | Computer Graphics Laboratory with mini project | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CSL69 | Artificial Intelligence and Machine Learning Laboratory | 0-0-1.5 | 1.5 | 25-25-25-25 |
| 18CPC67 | Project Work Phase I + Internship | 0-

