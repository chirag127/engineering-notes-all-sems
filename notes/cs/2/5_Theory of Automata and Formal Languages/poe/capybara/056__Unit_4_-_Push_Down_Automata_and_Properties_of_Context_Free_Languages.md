## Unit 4 - Push Down Automata and Properties of Context Free Languages

Push Down Automata (PDA) is a computational model that is an extension of Finite Automata. In PDA, we have an additional memory stack that allows us to store and retrieve data. Context-Free Grammars (CFG) is another formal language that generates context-free languages. Properties of Context-Free Languages can be defined using CFGs and PDAs.

Here are some important points to consider while studying Push Down Automata and Properties of Context Free Languages:

1. Push Down Automata (PDA) is a machine that can accept or reject strings in a language that a Context-Free Grammar generates. PDA consists of states, input tape, stack, and transition function.

2. The stack in PDA is used to store symbols, and it works on Last-In-First-Out (LIFO) principle. The stack can only be accessed from the top.

3. The transition function in PDA defines how the machine moves from one state to another. It takes into account the current state, input symbol, and top of the stack.

4. PDAs can recognize Context-Free Languages but not Context-Sensitive Languages or Recursive Languages.

5. Context-Free Grammars (CFG) is a formal language that generates context-free languages. CFG consists of terminals, non-terminals, start symbol, and production rules. 

6. The start symbol in CFG is a non-terminal that defines the initial string. Production rules define how the non-terminals can be replaced with terminals and non-terminals.

7. CFG is used to define the syntax of programming languages, natural languages, and many other formal languages.

8. Properties of Context-Free Languages can be defined using CFGs and PDAs. Some common properties of context-free languages are Closure Properties, Pumping Lemma, and Normal Forms.

9. The Closure Properties of Context-Free Languages include Union, Intersection, and Concatenation. These properties state that if two context-free languages are combined using these operations, the resulting language is also context-free.

10. The Pumping Lemma is a tool used to prove that a language is not context-free. It states that if a language is context-free, then there exists a constant 'p' such that any string in the language can be divided into three parts, and the middle part can be repeated any number of times.

11. Normal Forms are used to simplify production rules in CFG. There are two Normal Forms: Chomsky Normal Form and Greibach Normal Form.

Remember to practice problems related to Push Down Automata and Context Free Grammars to have a better understanding of the concepts.