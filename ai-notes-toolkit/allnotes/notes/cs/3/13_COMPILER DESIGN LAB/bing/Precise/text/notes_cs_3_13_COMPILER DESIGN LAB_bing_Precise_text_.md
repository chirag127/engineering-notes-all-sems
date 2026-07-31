

## Course Outcome (CO) Bloom’s Knowledge Level (KL)

- Course Outcome (CO) refers to the expected knowledge, skills, and attitudes that students should possess upon completion of a specific course.
- Bloom’s Knowledge Level (KL) is a framework for categorizing educational goals and objectives based on the level of cognitive complexity.
- The framework consists of six levels: Remembering, Understanding, Applying, Analyzing, Evaluating, and Creating.
- COs are often mapped to Bloom’s KL to ensure that the course objectives are aligned with the desired level of cognitive complexity.
- This mapping helps instructors design assessments and instructional activities that are appropriate for the desired level of learning.
- By aligning COs with Bloom’s KL, instructors can ensure that students are challenged to think critically and apply their knowledge in meaningful ways.



### At the end of the course, the student will be able to:

1. Demonstrate a comprehensive understanding of the course material.
2. Apply the concepts and theories learned in the course to real-world situations.
3. Analyze and evaluate information critically and effectively.
4. Communicate ideas and arguments clearly and effectively in both written and oral forms.
5. Work collaboratively with others to achieve common goals.
6. Demonstrate ethical and professional behavior in all course-related activities.
7. Use technology effectively to enhance learning and communication.
8. Engage in self-directed learning and continuous improvement.
9. Demonstrate an appreciation for diversity and multiculturalism.
10. Develop and implement strategies for achieving personal and academic goals.



#### CO 1 Identify patterns, tokens & regular expressions for lexical analysis. K2, K4

Lexical analysis is the process of converting a sequence of characters into a sequence of tokens. It is the first phase of the compilation process. Here are some key points to remember:

1. **Patterns**: A pattern is a description of the form that the lexemes of a token may take. In other words, it is a rule for describing what a token looks like. For example, an identifier in many programming languages must start with a letter or an underscore, followed by zero or more letters, digits, or underscores.

2. **Tokens**: A token is a sequence of characters that represents a single logical entity. Common examples of tokens include identifiers, keywords, operators, and punctuation symbols. Tokens are the basic building blocks of a program's source code.

3. **Regular expressions**: A regular expression is a pattern that describes a set of strings. It is a powerful tool for specifying patterns and can be used to define the lexemes of a token. For example, the regular expression `[a-zA-Z_][a-zA-Z0-9_]*` can be used to define the pattern for an identifier in many programming languages.

In summary, lexical analysis involves identifying patterns, tokens, and regular expressions to convert a sequence of characters into a sequence of tokens. This is an important step in the compilation process, as it lays the foundation for the subsequent phases.



#### CO 2 Design Lexical analyser for given language using C and LEX /YACC tools K3, K5

- A lexical analyzer is a program that takes a stream of characters as input and produces a stream of tokens as output.
- C is a general-purpose programming language that can be used to write a lexical analyzer.
- LEX is a tool that generates lexical analyzers. It takes a specification of the tokens to be recognized and generates C code that implements the lexical analyzer.
- YACC is a tool that generates parsers. It takes a specification of the grammar of a language and generates C code that implements a parser for that language.
- To design a lexical analyzer for a given language using C and LEX/YACC tools, the following steps can be followed:
  1. Define the tokens to be recognized by the lexical analyzer.
  2. Write a LEX specification that describes the tokens and the actions to be taken when a token is recognized.
  3. Use LEX to generate C code that implements the lexical analyzer.
  4. Write a YACC specification that describes the grammar of the language.
  5. Use YACC to generate C code that implements a parser for the language.
  6. Write additional C code to integrate the lexical analyzer and the parser and to implement any additional functionality required by the language.
  7. Compile and test the resulting program.
- K3 and K5 refer to the cognitive levels of the Bloom's Taxonomy. K3 refers to the "Application" level, where the student is expected to apply the knowledge in a practical situation. K5 refers to the "Evaluation" level, where the student is expected to make judgments based on criteria and standards.



#### CO 3 Design and analyze top down and bottom up parsers. K4, K5

- **Top-down parsing** refers to the process of constructing a parse tree for an input string, starting from the start symbol and proceeding in a top-down manner, by expanding the non-terminals into their corresponding production rules.

- **Bottom-up parsing** refers to the process of constructing a parse tree for an input string, starting from the leaves and proceeding in a bottom-up manner, by reducing the input string to the start symbol.

- **Designing top-down parsers** involves the use of recursive descent parsing or LL parsing algorithms. These algorithms use a set of parsing rules to predict the next production rule to apply, based on the current input symbol and the current non-terminal being expanded.

- **Designing bottom-up parsers** involves the use of shift-reduce parsing or LR parsing algorithms. These algorithms use a parsing table to determine the next action to take, based on the current state of the parser and the current input symbol.

- **Analyzing top-down parsers** involves checking the grammar for left recursion and left factoring, and ensuring that the grammar is LL(1) (i.e., can be parsed by an LL(1) parser).

- **Analyzing bottom-up parsers** involves checking the grammar for conflicts (i.e., shift-reduce or reduce-reduce conflicts) and ensuring that the grammar is LR(0), SLR(1), LALR(1), or LR(1) (i.e., can be parsed by the corresponding type of LR parser).

- **K4** refers to the ability to analyze and evaluate information to make judgments and decisions.

- **K5** refers to the ability to create new knowledge by synthesizing information from multiple sources.



#### CO 4 Generate the intermediate code K4, K5

Intermediate code generation is a phase of the compiler that comes after the analysis phase and before the code optimization and target code generation phases. The purpose of intermediate code is to create a representation of the source code that is easier to translate into the target language.

- K4 and K5 are two intermediate code representations that can be generated by a compiler.
- K4 is a type of three-address code, where each instruction has at most three operands.
- K5 is a type of static single assignment form, where each variable is assigned exactly once and every variable is defined before it is used.
- Both K4 and K5 are designed to make code optimization and target code generation easier and more efficient.
- The choice between K4 and K5 depends on the specific requirements of the compiler and the target language.




#### CO 5 Generate machine code from the intermediate code forms K3, K4

- Machine code is a low-level programming language that is directly executable by a computer's central processing unit (CPU).
- Intermediate code forms, such as K3 and K4, are representations of a program that are generated by a compiler during the process of translating source code into machine code.
- The process of generating machine code from intermediate code forms involves several steps, including optimization, code generation, and assembly.
- Optimization involves analyzing the intermediate code to identify opportunities for improving its efficiency and performance.
- Code generation involves translating the optimized intermediate code into a sequence of machine instructions that can be executed by the CPU.
- Assembly involves converting the machine instructions into a binary format that can be loaded into memory and executed by the CPU.
- The use of intermediate code forms, such as K3 and K4, can facilitate the process of generating machine code by providing a higher-level representation of the program that is easier to analyze and optimize.
- The specific details of how machine code is generated from intermediate code forms K3 and K4 will depend on the particular compiler and target architecture being used.



## DETAILED SYLLABUS

A detailed syllabus is an outline or summary of the topics that will be covered in a course. It typically includes the following information:

1. Course title and description
2. Instructor information
3. Course objectives and learning outcomes
4. Course schedule, including dates and topics for each class session
5. Required and recommended reading materials
6. Assignments and assessments, including due dates and grading criteria
7. Course policies, including attendance, participation, and academic integrity
8. Contact information for the instructor and any teaching assistants

A detailed syllabus is an important tool for both students and instructors. For students, it provides a roadmap for the course and helps them to plan their time and prepare for assessments. For instructors, it serves as a guide for planning and delivering the course content.

It is important for students to read the syllabus carefully at the beginning of the course and to refer to it regularly throughout the semester. This will help them to stay on track and to meet the expectations of the instructor. If a student has any questions or concerns about the syllabus, they should discuss them with the instructor as soon as possible.



### Design and Implementation of a Lexical Analyzer for a Given Language Using C

A lexical analyzer, also known as a lexer or scanner, is a program that takes a stream of characters as input and produces a stream of tokens as output. These tokens represent the smallest meaningful units of the input, such as keywords, identifiers, and literals.

Here are the steps to design and implement a lexical analyzer for a given language using C:

1. **Define the tokens**: The first step is to define the tokens that the lexical analyzer will recognize. These tokens will depend on the language being analyzed. For example, if the language is C, the tokens might include keywords such as `if`, `else`, and `while`, as well as identifiers, literals, and operators.

2. **Write regular expressions for the tokens**: Once the tokens have been defined, the next step is to write regular expressions that describe the patterns of characters that make up each token. For example, a regular expression for an identifier in C might be `[a-zA-Z_][a-zA-Z0-9_]*`, which matches a sequence of characters that starts with a letter or underscore and is followed by zero or more letters, digits, or underscores.

3. **Implement the lexical analyzer**: The lexical analyzer can be implemented using a finite automaton, which is a machine that reads the input one character at a time and transitions between states based on the current character and the current state. The states of the finite automaton correspond to the regular expressions for the tokens, and the transitions between states are determined by the characters in the input.

4. **Ignore redundant characters**: The lexical analyzer should be designed to ignore redundant characters, such as whitespace and comments, that do not affect the meaning of the program. This can be done by adding special states to the finite automaton that recognize and ignore these characters.

In summary, to design and implement a lexical analyzer for a given language using C, one needs to define the tokens, write regular expressions for the tokens, implement the lexical analyzer using a finite automaton, and design the lexical analyzer to ignore redundant characters. This process can be applied to any language to create a lexical analyzer that can be used as the first stage of a compiler or interpreter.



### Spaces, Tabs and New Lines

- **Spaces** are characters used to separate words and symbols in text. They are represented by the ASCII code 32 and are typically created by pressing the space bar on a keyboard.

- **Tabs** are characters used to align text in columns. They are represented by the ASCII code 9 and are typically created by pressing the tab key on a keyboard. The width of a tab character is usually equivalent to 8 spaces, but this can vary depending on the software being used.

- **New lines** are characters used to indicate the end of a line of text and the beginning of a new one. They are represented by the ASCII code 10 (line feed) or 13 (carriage return) depending on the operating system. New lines are typically created by pressing the enter or return key on a keyboard.

These characters are commonly used in text editors and word processors to format and organize text. They can also be used in programming languages to improve the readability of code. However, their use and interpretation can vary depending on the context and the software being used. It is important to understand the differences between these characters and how they are used in different situations.



### 2. Implementation of Lexical Analyzer using Lex Tool

Lex is a tool used to generate lexical analyzers, which are programs that recognize lexical patterns in text. Here are the steps to implement a lexical analyzer using Lex:

1. Define the regular expressions for the tokens to be recognized.
2. Write the Lex specification file, which consists of three sections separated by `%%`:
    - The first section contains declarations and includes.
    - The second section contains the regular expressions and the associated actions.
    - The third section contains additional code and functions.
3. Run the Lex tool on the specification file to generate the C source code for the lexical analyzer.
4. Compile the generated C source code to create the lexical analyzer program.
5. Use the lexical analyzer program to process input text and recognize tokens.

Lex is commonly used in conjunction with the Yacc parser generator tool to create compilers and interpreters for programming languages. The lexical analyzer generated by Lex reads the input text and converts it into a sequence of tokens, which are then passed to the parser generated by Yacc for syntactic analysis.



### 3. Generate YACC specification for a few syntactic categories.

YACC (Yet Another Compiler Compiler) is a tool that generates a parser for a given grammar. Here are the steps to generate a YACC specification for a few syntactic categories:

1. Define the tokens: The first step in creating a YACC specification is to define the tokens that will be used in the grammar. This is done using the `%token` directive. For example, to define tokens for identifiers, numbers, and basic arithmetic operators, the following lines could be used:
```
%token IDENTIFIER NUMBER PLUS MINUS TIMES DIVIDE
```

2. Define the grammar: The next step is to define the grammar using production rules. Each production rule has a left-hand side (LHS) and a right-hand side (RHS). The LHS is a non-terminal symbol, while the RHS is a sequence of terminal and non-terminal symbols. For example, to define a simple grammar for arithmetic expressions, the following production rules could be used:
```
expr: expr PLUS term
    | expr MINUS term
    | term
    ;

term: term TIMES factor
    | term DIVIDE factor
    | factor
    ;

factor: NUMBER
    | IDENTIFIER
    | LPAREN expr RPAREN
    ;
```

3. Define the actions: YACC allows the user to define actions that are executed when a production rule is reduced. Actions are specified using C code enclosed in curly braces `{}`. For example, to evaluate the value of an arithmetic expression, the following actions could be used:
```
expr: expr PLUS term { $$ = $1 + $3; }
    | expr MINUS term { $$ = $1 - $3; }
    | term { $$ = $1; }
    ;

term: term TIMES factor { $$ = $1 * $3; }
    | term DIVIDE factor { $$ = $1 / $3; }
    | factor { $$ = $1; }
    ;

factor: NUMBER { $$ = $1; }
    | IDENTIFIER { $$ = lookup($1); }
    | LPAREN expr RPAREN { $$ = $2; }
    ;
```

4. Run YACC: Once the tokens, grammar, and actions have been defined, the YACC specification can be processed by the YACC tool to generate a parser. This is typically done by invoking YACC from the command line with the name of the specification file as an argument. For example, to generate a parser from a specification file named `mygrammar.y`, the following command could be used:
```
yacc mygrammar.y
```

This will generate a file named `y.tab.c` that contains the C code for the parser. This file can then be compiled and linked with the rest of the program to create an executable that can parse input according to the specified grammar.



### a) Program to recognize a valid arithmetic expression that uses operator +, – , * and /.

A valid arithmetic expression is a string of characters that represents a mathematical calculation. It can contain numbers, operators (+, -, *, /), and parentheses. To recognize a valid arithmetic expression, a program can follow these steps:

1. **Check for balanced parentheses**: The program should check if the expression has an equal number of opening and closing parentheses. If the number of opening and closing parentheses is not equal, the expression is not valid.

2. **Check for valid characters**: The program should check if the expression contains only valid characters (numbers, operators, and parentheses). If the expression contains any other character, it is not valid.

3. **Check for valid operator placement**: The program should check if the operators are placed correctly in the expression. Operators should not be placed at the beginning or end of the expression, and they should not be placed next to each other.

4. **Check for division by zero**: The program should check if the expression contains a division by zero. If the expression contains a division by zero, it is not valid.

By following these steps, a program can recognize if an arithmetic expression that uses the operators +, -, *, and / is valid or not.



### b) Program to recognize a valid variable which starts with a letter followed by any number of letters or digits.

A valid variable name in most programming languages must start with a letter or an underscore, followed by any number of letters, digits, or underscores. Here is an example of a program that checks if a given string is a valid variable name:

```python
import re

def is_valid_variable_name(name):
    # Regular expression to match a valid variable name
    pattern = '^[a-zA-Z_][a-zA-Z0-9_]*$'
    if re.match(pattern, name):
        return True
    else:
        return False
```

This program uses a regular expression to match the given string against the pattern for a valid variable name. The `^` at the beginning of the pattern indicates that the match must start at the beginning of the string, while the `$` at the end indicates that the match must end at the end of the string. The `[a-zA-Z_]` part of the pattern matches a single letter or underscore, while the `[a-zA-Z0-9_]*` part matches zero or more letters, digits, or underscores.

Here are some examples of how this program can be used:

```python
print(is_valid_variable_name('myVariable')) # True
print(is_valid_variable_name('_private_var')) # True
print(is_valid_variable_name('2nd_var')) # False
print(is_valid_variable_name('var-with-hyphen')) # False
```

In the first two examples, the given strings are valid variable names, so the function returns `True`. In the last two examples, the given strings are not valid variable names, so the function returns `False`.



### c) Implementation of Calculator using LEX and YACC

LEX and YACC are tools used for generating lexical analyzers and parsers, respectively. They can be used to implement a calculator by following these steps:

1. Define the grammar for the calculator in YACC. This includes specifying the rules for mathematical expressions, such as the order of operations and the use of parentheses.
2. Write the lexical analyzer in LEX. This involves defining the tokens that the calculator will recognize, such as numbers and operators.
3. Use YACC to generate a parser based on the grammar defined in step 1. This parser will take the input from the user and convert it into a syntax tree.
4. Write the code to evaluate the syntax tree and perform the calculations. This can be done using a recursive function that traverses the tree and performs the appropriate operations.
5. Compile and run the calculator program.

By using LEX and YACC, the implementation of a calculator can be simplified and made more efficient. These tools automate the process of generating the lexical analyzer and parser, allowing the developer to focus on the logic of the calculator itself.







### 4. Write program to find ε – closure of all states of any given NFA with ε transition.

The ε-closure of a state `q` in an NFA with ε transition is the set of all states that can be reached from `q` by following only ε-transitions. This can be calculated using a depth-first search algorithm.

Here is an example of a program in Python that calculates the ε-closure of all states of a given NFA with ε transition:

```python
def epsilon_closure(nfa, state):
    stack = [state]
    closure = set()
    while stack:
        current_state = stack.pop()
        closure.add(current_state)
        if current_state in nfa.transitions and None in nfa.transitions[current_state]:
            for next_state in nfa.transitions[current_state][None]:
                if next_state not in closure:
                    stack.append(next_state)
    return closure

def epsilon_closure_all_states(nfa):
    closures = {}
    for state in nfa.states:
        closures[state] = epsilon_closure(nfa, state)
    return closures
```

This program takes as input an NFA object with a `states` attribute representing the set of states and a `transitions` attribute representing the transition function. The `epsilon_closure` function calculates the ε-closure of a single state, while the `epsilon_closure_all_states` function calculates the ε-closure of all states by calling the `epsilon_closure` function for each state.

The `epsilon_closure` function uses a stack to keep track of the states that need to be visited. It starts with the given state and adds it to the closure set. Then, it checks if the current state has ε-transitions and, if so, adds the next states to the stack if they are not already in the closure set. This process is repeated until the stack is empty, at which point the closure set contains the ε-closure of the given state.

The `epsilon_closure_all_states` function simply calls the `epsilon_closure` function for each state in the NFA and stores the result in a dictionary, where the keys are the states and the values are the corresponding ε-closures.

This program can be used to find the ε-closure of all states of any given NFA with ε transition. It is important to note that the ε-closure of a state can include the state itself.



### 5. Write program to convert NFA with ε transition to NFA without ε transition.

An NFA with ε transition is a type of non-deterministic finite automaton (NFA) that allows transitions between states without consuming any input symbols. This is achieved through the use of ε transitions, which are transitions that can be taken without consuming any input symbols.

To convert an NFA with ε transitions to an NFA without ε transitions, the following steps can be taken:

1. Identify all ε transitions in the NFA.
2. For each ε transition, identify the states that are reachable from the source state of the ε transition without consuming any input symbols.
3. For each state that is reachable from the source state of the ε transition, add transitions from the source state to the reachable state for each input symbol that has a transition from the reachable state.
4. Remove all ε transitions from the NFA.

Here is an example of a program that can be used to convert an NFA with ε transitions to an NFA without ε transitions:

```python
def remove_epsilon_transitions(nfa):
    # Step 1: Identify all ε transitions
    epsilon_transitions = []
    for state in nfa.states:
        for transition in state.transitions:
            if transition.symbol == 'ε':
                epsilon_transitions.append(transition)

    # Step 2: For each ε transition, identify the states that are reachable from the source state
    for epsilon_transition in epsilon_transitions:
        source_state = epsilon_transition.source
        reachable_states = find_reachable_states(source_state, nfa)

        # Step 3: For each reachable state, add transitions from the source state for each input symbol
        for reachable_state in reachable_states:
            for transition in reachable_state.transitions:
                if transition.symbol != 'ε':
                    source_state.add_transition(transition.symbol, transition.destination)

    # Step 4: Remove all ε transitions
    for state in nfa.states:
        state.transitions = [transition for transition in state.transitions if transition.symbol != 'ε']

def find_reachable_states(state, nfa, visited=None):
    if visited is None:
        visited = set()
    visited.add(state)
    reachable_states = set()
    for transition in state.transitions:
        if transition.symbol == 'ε' and transition.destination not in visited:
            reachable_states.add(transition.destination)
            reachable_states |= find_reachable_states(transition.destination, nfa, visited)
    return reachable_states
```

This program takes as input an NFA with ε transitions and returns an equivalent NFA without ε transitions. The `remove_epsilon_transitions` function follows the steps outlined above to convert the NFA. The `find_reachable_states` function is a helper function that is used to find all states that are reachable from a given state without consuming any input symbols.



### 6. Write program to convert NFA to DFA

An NFA (Nondeterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there may be several possible next states. A DFA (Deterministic Finite Automaton) is a finite state machine where for each pair of state and input symbol, there is one and only one possible next state.

Here are the steps to convert an NFA to a DFA:

1. Create a start state for the DFA by taking the epsilon closure of the start state of the NFA.
2. Create a transition table for the DFA using the transition table of the NFA. For each state in the DFA and each input symbol, find the set of NFA states reachable from the current DFA state using the input symbol and take the epsilon closure of this set. This set of NFA states will be a single state in the DFA.
3. For each state in the DFA, if it is made up of one or more accepting states of the NFA, mark it as an accepting state in the DFA.
4. Repeat step 2 until all states and transitions have been added to the DFA.

This is the general algorithm for converting an NFA to a DFA. The specific implementation may vary depending on the programming language and data structures used. It is important to note that the resulting DFA may have more states than the original NFA. This is because the DFA must explicitly keep track of all possible states that the NFA could be in at any given time.



### 7. Write program to minimize any given DFA.

A DFA (Deterministic Finite Automaton) is a finite state machine that accepts or rejects a given string of symbols, by running through a state sequence uniquely determined by the string. Minimizing a DFA refers to finding an equivalent DFA with the minimum number of states.

Here is an algorithm to minimize any given DFA:

1. **Distinguish accepting and non-accepting states**: Divide the states of the DFA into two sets, one containing all accepting states and the other containing all non-accepting states.
2. **Partition the states**: For each pair of states, check if they can be distinguished by any input string. If they can be distinguished, place them in different sets. Repeat this process until no more partitions can be made.
3. **Construct the minimized DFA**: Create a new state in the minimized DFA for each set of states in the partition. The initial state of the minimized DFA is the set containing the initial state of the original DFA. The accepting states of the minimized DFA are the sets containing accepting states of the original DFA. The transition function is defined by the transitions of the representative states of each set.

Here is an example of a program in Python that implements the above algorithm to minimize a given DFA:

```python
def minimize_dfa(dfa):
    # Step 1: Distinguish accepting and non-accepting states
    accepting_states = set(dfa.accepting_states)
    non_accepting_states = set(dfa.states) - accepting_states
    partition = [accepting_states, non_accepting_states]

    # Step 2: Partition the states
    new_partition = []
    for part in partition:
        for state1 in part:
            for state2 in part:
                if state1 != state2:
                    for symbol in dfa.alphabet:
                        next_state1 = dfa.transition_function[state1][symbol]
                        next_state2 = dfa.transition_function[state2][symbol]
                        if next_state1 in accepting_states and next_state2 not in accepting_states:
                            new_partition.append(set([state1]))
                            new_partition.append(set([state2]))
                            break
    if new_partition:
        partition = new_partition

    # Step 3: Construct the minimized DFA
    minimized_dfa = DFA()
    minimized_dfa.alphabet = dfa.alphabet
    minimized_dfa.states = range(len(partition))
    minimized_dfa.initial_state = [i for i, part in enumerate(partition) if dfa.initial_state in part][0]
    minimized_dfa.accepting_states = [i for i, part in enumerate(partition) if part & accepting_states]
    minimized_dfa.transition_function = {}
    for i, part in enumerate(partition):
        state = next(iter(part))
        minimized_dfa.transition_function[i] = {}
        for symbol in dfa.alphabet:
            next_state = dfa.transition_function[state][symbol]
            for j, part in enumerate(partition):
                if next_state in part:
                    minimized_dfa.transition_function[i][symbol] = j
                    break
    return minimized_dfa
```

This program takes as input a DFA object with the following attributes: `states`, `alphabet`, `transition_function`, `initial_state`, and `accepting_states`. It returns a new DFA object that is equivalent to the input DFA but with the minimum number of states.



### 8. Develop an operator precedence parser for a given language.

An operator precedence parser is a type of parser for computer languages that is used to determine the order of operations when evaluating expressions. It is based on the concept of operator precedence, which specifies the order in which operators are evaluated in an expression.

Here are the steps to develop an operator precedence parser for a given language:

1. **Define the grammar**: The first step in developing an operator precedence parser is to define the grammar of the language. This includes specifying the set of terminal and non-terminal symbols, as well as the production rules that define how the symbols can be combined to form valid expressions.

2. **Determine the precedence and associativity of operators**: The next step is to determine the precedence and associativity of the operators in the language. This information is used to determine the order in which the operators are evaluated when parsing an expression.

3. **Construct the parsing table**: Once the precedence and associativity of the operators have been determined, the next step is to construct the parsing table. This table is used to guide the parsing process by specifying the actions that the parser should take when it encounters a particular combination of symbols.

4. **Implement the parsing algorithm**: The final step is to implement the parsing algorithm. This involves using the parsing table to guide the parsing process, and applying the production rules to construct the parse tree for a given expression.

By following these steps, it is possible to develop an operator precedence parser for a given language. This type of parser is commonly used in compilers and interpreters to evaluate expressions and perform other language processing tasks.



### 9. Write program to find Simulate First and Follow of any given grammar.

First and Follow are important concepts in the construction of predictive parsers for context-free grammars. The First set of a symbol is the set of terminal symbols that can appear as the first symbol in a string derived from that symbol. The Follow set of a symbol is the set of terminal symbols that can appear immediately after that symbol in a sentential form.

Here is an example of how to find the First and Follow sets of a given grammar:

1. Begin by finding the First set for each terminal symbol. The First set of a terminal symbol is simply the terminal symbol itself.
2. For each production rule in the grammar, find the First set of the right-hand side of the rule. If the first symbol on the right-hand side is a terminal symbol, then the First set of the right-hand side is the First set of that terminal symbol. If the first symbol on the right-hand side is a non-terminal symbol, then the First set of the right-hand side is the union of the First sets of all the productions that have that non-terminal symbol on the left-hand side.
3. To find the Follow set of a non-terminal symbol, begin by adding the end-of-input marker to the Follow set of the start symbol. Then, for each production rule in the grammar, if the non-terminal symbol appears on the right-hand side of the rule, add the First set of the symbol immediately following it to the Follow set of the non-terminal symbol. If there is no symbol following the non-terminal symbol, or if the First set of the following symbol contains the empty string, then add the Follow set of the left-hand side of the rule to the Follow set of the non-terminal symbol.
4. Repeat step 3 until no more terminal symbols can be added to any Follow set.

Here is an example of a program that finds the First and Follow sets of a given grammar:

```python
def first(symbol, grammar):
    first_set = set()
    if symbol.isupper():
        for rule in grammar[symbol]:
            if rule == 'epsilon':
                first_set.add('epsilon')
            else:
                first_set = first_set.union(first(rule[0], grammar))
    else:
        first_set.add(symbol)
    return first_set

def follow(symbol, grammar, follow_sets):
    follow_set = set()
    if symbol == list(grammar.keys())[0]:
        follow_set.add('$')
    for key, rules in grammar.items():
        for rule in rules:
            if symbol in rule:
                index = rule.index(symbol)
                if index == len(rule) - 1:
                    follow_set = follow_set.union(follow_sets[key])
                else:
                    first_set = first(rule[index + 1], grammar)
                    if 'epsilon' in first_set:
                        first_set.remove('epsilon')
                        follow_set = follow_set.union(follow_sets[key])
                    follow_set = follow_set.union(first_set)
    return follow_set

def first_follow(grammar):
    first_sets = {}
    follow_sets = {}
    for key in grammar.keys():
        first_sets[key] = first(key, grammar)
        follow_sets[key] = set()
    while True:
        prev_follow_sets = follow_sets.copy()
        for key in grammar.keys():
            follow_sets[key] = follow(key, grammar, follow_sets)
        if prev_follow_sets == follow_sets:
            break
    return first_sets, follow_sets

grammar = {
    'S': ['AB', 'BC'],
    'A': ['aA', 'epsilon'],
    'B': ['bB', 'epsilon'],
    'C': ['cC', 'epsilon']
}

first_sets, follow_sets = first_follow(grammar)

print('First sets:')
for key, value in first_sets.items():
    print(key, value)

print('Follow sets:')
for key, value in follow_sets.items():
    print(key, value)
```

This program defines three functions: `first`, `follow`, and `first_follow`. The `first` function takes a symbol and a grammar as input and returns the First set of the symbol. The `follow` function takes a symbol, a grammar, and a dictionary of Follow sets as input and returns the Follow set of the symbol. The `first_follow` function takes a grammar as input and returns the First and Follow sets of all the non-terminal symbols in the grammar.

The program then defines a grammar as a dictionary, where the keys are the non-terminal symbols and the values are lists of production rules. The program calls the `first_follow` function to find the First and Follow sets of the grammar, and then prints the results.

This is an example of how to write a program to find the First and Follow sets of a given grammar. It



### 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of top-down parser that uses a set of recursive procedures to process the input. Each procedure typically represents a non-terminal symbol in the grammar of the language being parsed. Here are the steps to construct a recursive descent parser for an expression:

1. **Define the grammar**: The first step in constructing a recursive descent parser is to define the grammar of the language being parsed. This involves identifying the terminal and non-terminal symbols, as well as the production rules that define how the non-terminal symbols can be derived from the terminal symbols.

2. **Write the parsing procedures**: Once the grammar has been defined, the next step is to write the parsing procedures. Each procedure should correspond to a non-terminal symbol in the grammar and should implement the production rules for that symbol.

3. **Handle the terminal symbols**: The parsing procedures should also handle the terminal symbols in the input. This typically involves checking if the current input symbol matches the expected terminal symbol and advancing the input if it does.

4. **Implement the recursive calls**: The parsing procedures should make recursive calls to other parsing procedures as needed to implement the production rules for the non-terminal symbols.

5. **Handle errors**: The parser should also be able to handle errors in the input. This can be done by adding error-handling code to the parsing procedures to detect and report any errors that occur during parsing.

By following these steps, you can construct a recursive descent parser for an expression. It is important to note that recursive descent parsers can be inefficient for certain types of grammars, so it is important to carefully analyze the grammar and the input before deciding to use this approach.



### 11. Construct a Shift Reduce Parser for a given language.

A shift-reduce parser is a type of bottom-up parser that uses a stack to hold the grammar symbols and an input buffer to hold the input string. The parser operates by performing one of two actions: shift or reduce.

1. **Shift**: This action involves moving the next input symbol from the input buffer to the top of the stack.

2. **Reduce**: This action involves recognizing a handle, which is a substring of the stack that matches the right side of a production rule, and replacing it with the non-terminal symbol on the left side of the production rule.

The parser repeats these actions until either the input string is successfully parsed or an error is encountered. The following steps can be followed to construct a shift-reduce parser for a given language:

1. Define the grammar for the language, including the production rules and the start symbol.

2. Create a parsing table that specifies the action to be taken (shift or reduce) for each combination of stack top symbol and next input symbol.

3. Implement the shift-reduce parsing algorithm using the parsing table and the defined grammar.

4. Test the parser on sample input strings to ensure that it correctly recognizes valid strings and rejects invalid strings.

It is important to note that not all grammars are suitable for shift-reduce parsing. A grammar must be unambiguous and free of conflicts (such as shift-reduce conflicts and reduce-reduce conflicts) to be successfully parsed using a shift-reduce parser. In some cases, it may be necessary to modify the grammar to make it suitable for shift-reduce parsing.



### 12. Write a program to perform loop unrolling

Loop unrolling is a technique used to optimize the execution time of a program by reducing the number of iterations of a loop. This is done by replicating the body of the loop multiple times and adjusting the loop control variable accordingly.

Here is an example of loop unrolling in C:

```c
#include <stdio.h>

int main() {
    int i;
    for (i = 0; i < 100; i += 5) {
        printf("%d\n", i);
        printf("%d\n", i + 1);
        printf("%d\n", i + 2);
        printf("%d\n", i + 3);
        printf("%d\n", i + 4);
    }
    return 0;
}
```

In this example, the loop iterates 20 times instead of 100 times, and the body of the loop is executed 5 times in each iteration. This can result in faster execution time, especially if the loop body contains computationally expensive operations.

However, loop unrolling can also increase the size of the code and make it less readable. It is important to carefully consider the trade-offs before using this technique.

- Loop unrolling can reduce the number of iterations of a loop.
- This is done by replicating the body of the loop multiple times.
- Loop unrolling can result in faster execution time.
- However, it can also increase the size of the code and make it less readable.
- It is important to carefully consider the trade-offs before using this technique.



### 13. Write a program to perform constant propagation

Constant propagation is a compiler optimization technique that aims to reduce the number of computations performed at runtime by replacing variables with their constant values whenever possible.

Here is an example of a program that performs constant propagation:

```python
def constant_propagation(code):
    # Initialize a dictionary to store the values of constants
    constants = {}
    # Split the code into lines
    lines = code.split('\n')
    # Iterate over the lines of code
    for line in lines:
        # Split the line into tokens
        tokens = line.split()
        # Check if the line is an assignment statement
        if len(tokens) == 3 and tokens[1] == '=':
            # Check if the right-hand side is a constant
            if tokens[2].isdigit():
                # Store the constant value in the dictionary
                constants[tokens[0]] = int(tokens[2])
            # Check if the right-hand side is a variable
            elif tokens[2] in constants:
                # Replace the variable with its constant value
                constants[tokens[0]] = constants[tokens[2]]
    # Iterate over the lines of code again
    for i, line in enumerate(lines):
        # Split the line into tokens
        tokens = line.split()
        # Iterate over the tokens
        for j, token in enumerate(tokens):
            # Check if the token is a variable
            if token in constants:
                # Replace the variable with its constant value
                tokens[j] = str(constants[token])
        # Join the tokens back into a line
        lines[i] = ' '.join(tokens)
    # Join the lines back into code
    return '\n'.join(lines)
```

This program takes as input a string representing the code to be optimized and returns a new string representing the optimized code. The program works by first identifying all the constants in the code and storing their values in a dictionary. Then, it iterates over the lines of code again, replacing any occurrences of variables with their constant values whenever possible.

Here is an example of how to use this program:

```python
code = """
x = 3
y = x
z = y + 5
"""

optimized_code = constant_propagation(code)
print(optimized_code)
```

This will output the following optimized code:

```
x = 3
y = 3
z = 3 + 5
```

As you can see, the variable `y` has been replaced with its constant value `3`, reducing the number of computations that need to be performed at runtime. This is a simple example, but constant propagation can be a powerful optimization technique for more complex programs.



### 14. Implement Intermediate code generation for simple expressions

Intermediate code generation is a phase in the compilation process where the source code is transformed into an intermediate representation that is easier for the compiler to manipulate and optimize. This intermediate representation is typically machine-independent and can be used to generate code for different target architectures.

Here are the steps to implement intermediate code generation for simple expressions:

1. **Lexical Analysis:** The first step is to perform lexical analysis on the source code to identify the tokens and their types. This can be done using a lexical analyzer or scanner.

2. **Syntax Analysis:** The next step is to perform syntax analysis on the tokens to generate a parse tree or abstract syntax tree (AST) that represents the structure of the source code. This can be done using a parser.

3. **Semantic Analysis:** After generating the AST, the next step is to perform semantic analysis to check for any semantic errors and to resolve any ambiguities in the source code. This can be done using a symbol table and type checking.

4. **Intermediate Code Generation:** Once the AST has been generated and the semantic analysis has been performed, the next step is to generate the intermediate code. This can be done by traversing the AST and generating the intermediate code for each node in the tree.

5. **Optimization:** After generating the intermediate code, the next step is to perform optimization to improve the efficiency of the code. This can be done using various optimization techniques such as constant folding, dead code elimination, and loop unrolling.

6. **Code Generation:** The final step is to generate the target code from the intermediate code. This can be done using a code generator that generates the machine code for the target architecture.

In summary, intermediate code generation for simple expressions involves performing lexical analysis, syntax analysis, semantic analysis, intermediate code generation, optimization, and code generation. These steps can be implemented using various tools and techniques such as lexical analyzers, parsers, symbol tables, type checking, and code generators.



### 15. Implement the back end of the compiler which takes the three address code and produces the 8086 assembly language

The back end of a compiler is responsible for generating the target code from the intermediate representation, in this case, the three address code. The target code for this specific implementation is the 8086 assembly language.

Here are the steps to implement the back end of the compiler:

1. **Translate the three address code into assembly instructions**: Each three address code instruction can be translated into one or more assembly instructions. The translation process involves mapping the operations and operands of the three address code to their equivalent assembly instructions and registers.

2. **Optimize the generated assembly code**: The generated assembly code can be optimized to improve its performance. This can be done by applying techniques such as instruction scheduling, register allocation, and peephole optimization.

3. **Generate the final assembly code**: The final step is to generate the complete assembly code by combining the translated and optimized instructions. This code can then be assembled and linked to produce the final executable.

In summary, the back end of the compiler takes the three address code and produces the 8086 assembly language by translating the instructions, optimizing the generated code, and generating the final assembly code. This process is essential for producing efficient and effective target code.



### Instructions that can be assembled and run using an 8086 assembler

The 8086 microprocessor is a 16-bit CPU that can execute a variety of assembly language instructions. Some of the basic instructions that can be assembled and run using an 8086 assembler are:

1. **MOV**: This instruction is used to move data from one location to another. The data can be moved between registers, between a register and memory, or between memory locations.

2. **ADD**: This instruction is used to add two operands and store the result in the destination operand. The operands can be registers, memory locations, or immediate values.

3. **SUB**: This instruction is used to subtract the second operand from the first operand and store the result in the destination operand. The operands can be registers, memory locations, or immediate values.

4. **MUL**: This instruction is used to multiply two operands and store the result in the destination operand. The operands can be registers, memory locations, or immediate values.

5. **DIV**: This instruction is used to divide the first operand by the second operand and store the result in the destination operand. The operands can be registers, memory locations, or immediate values.

6. **JMP**: This instruction is used to transfer control to a different part of the program. The destination can be specified using a label, a register, or a memory location.

These are just a few examples of the instructions that can be assembled and run using an 8086 assembler. There are many more instructions available, each with its own specific function and syntax. It is important to consult the 8086 instruction set reference for a complete list of instructions and their usage.



### Add, Sub, Jump etc.

- `Add` is an instruction used to add two numbers and store the result in a specified location.
- `Sub` is an instruction used to subtract one number from another and store the result in a specified location.
- `Jump` is an instruction used to transfer control to a different location in the program.
- These instructions are commonly used in assembly language programming.
- They are fundamental operations that can be used to perform more complex calculations and control the flow of a program.
- Understanding these instructions is essential for anyone learning assembly language programming.




### Note: The Instructor may add/delete/modify/tune experiments, wherever he/she feels in a justified manner

- This statement indicates that the instructor has the authority to make changes to the experiments in the course.
- The instructor may add new experiments, delete existing ones, modify them, or tune them to better fit the course objectives.
- The instructor is expected to make these changes in a justified manner, meaning that the changes should be reasonable and serve a specific purpose.
- This flexibility allows the instructor to adapt the course material to the needs of the students and to keep the course up-to-date with the latest developments in the field.



### Open Source Tools for Conducting Lab

- Open source tools are software programs that are freely available to the public and can be modified and distributed by anyone.
- For conducting a lab, it is suggested that open source tools should be preferred.
- Some of the open source tools that can be used for conducting a lab include C, C++, Lex, and Flex.
- These tools are widely used and have a large community of developers and users who contribute to their development and provide support.
- Using open source tools can have several benefits, including cost savings, flexibility, and the ability to customize the tools to meet specific needs.
- Additionally, using open source tools can promote collaboration and knowledge sharing among students and researchers.
- In summary, using open source tools for conducting a lab can provide many benefits and is a recommended practice.



### YACC tools (Unix/Linux utilities)

YACC (Yet Another Compiler Compiler) is a Unix/Linux utility that generates a parser for a given grammar. It is commonly used to develop compilers and interpreters for programming languages.

- YACC reads the grammar of a language from a specification file and generates a C program that can parse that language.
- The generated C program is called a parser, which takes a stream of tokens as input and produces a parse tree as output.
- YACC is often used in conjunction with a lexical analyzer generator such as LEX, which generates a C program that can tokenize the input stream.
- The combination of YACC and LEX allows developers to easily create compilers and interpreters for custom languages.
- YACC was originally developed by Stephen C. Johnson at AT&T Bell Laboratories in the 1970s.
- YACC has since been replaced by more modern parser generators such as Bison and ANTLR, but it remains an important tool in the development of compilers and interpreters.




### Curriculum & Evaluation Scheme CS & CSE (V & VI semester) 19

The curriculum and evaluation scheme for the Computer Science (CS) and Computer Science and Engineering (CSE) programs for the fifth and sixth semesters is designed to provide students with a comprehensive understanding of the core concepts and practical skills required in the field.

1. The curriculum includes a range of courses covering topics such as data structures and algorithms, computer networks, operating systems, database systems, and software engineering.
2. The evaluation scheme is designed to assess students' understanding of the course material and their ability to apply their knowledge in practical situations.
3. The evaluation may include a combination of written exams, practical exams, assignments, and project work.
4. The specific details of the curriculum and evaluation scheme may vary between institutions and may be subject to change.

It is important for students to familiarize themselves with the specific curriculum and evaluation scheme for their program and institution to ensure that they are adequately prepared for their exams and assessments.

