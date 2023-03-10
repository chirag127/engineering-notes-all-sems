
### Declarations 
Declarations are used to define the names of the nonterminals, terminals and the start symbol of the grammar. They are usually written in the form of a set of production rules.

### Case Statements 
Case statements are used to define the actions associated with the production rules. They are usually written in the form of a sequence of instructions, which are executed when the production rule is applied. 

### Advantages 
- Declarations and case statements make it easier to understand and debug the grammar. 
- They provide a formal way to express the grammar. 
- They provide a way to add semantic information to the grammar. 

### Disadvantages 
- Declarations and case statements can be difficult to understand and debug. 
- They can be difficult to maintain if the grammar is changed. 
- They can be difficult to extend if new features are added to the grammar. 

### Examples 
Consider the following grammar: 

```
S -> A B
A -> a
B -> b
```

The declarations and case statements for this grammar could be written as follows: 

Declarations: 
```
N = {S, A, B} 
T = {a, b} 
S = S
```

Case Statements: 
```
S: 
  A(); 
  B();
A: 
  emit('a'); 
B: 
  emit('b');
```