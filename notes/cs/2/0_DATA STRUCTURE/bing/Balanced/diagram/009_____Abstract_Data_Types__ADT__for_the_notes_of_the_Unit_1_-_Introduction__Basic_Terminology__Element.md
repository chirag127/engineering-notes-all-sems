Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here is the content I have generated for the topic of Abstract Data Types (ADT) for the notes of the Unit 1 - Introduction: Basic Terminology, Elementary Data Organization, Built in Data Types in C. Algorithm, Efficiency of an Algorithm, Time and Space Complexity, Asymptotic notations: Big Oh, Big Theta and Big Omega, Time-Space trade-off. Abstract Data Types (ADT) in the subject of DATA STRUCTURE.

### Abstract Data Types (ADT)

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported and the behavior of those operations.
- An ADT does not specify how the data structure is implemented, only the interface that it provides to the user or other data structures.
- An ADT can be implemented using different data structures, such as arrays, linked lists, trees, etc. The choice of implementation depends on the efficiency and complexity of the operations required by the ADT.
- An ADT can be defined using a specification language, such as pseudocode, that describes the syntax and semantics of the operations. For example, the ADT of a stack can be defined as follows:

```
ADT Stack
  Data: a collection of elements of the same type
  Operations:
    push(x): add element x to the top of the stack
    pop(): remove and return the element at the top of the stack
    peek(): return the element at the top of the stack without removing it
    isEmpty(): return true if the stack is empty, false otherwise
    size(): return the number of elements in the stack
  Axioms:
    isEmpty() = true if and only if size() = 0
    pop() and peek() are undefined if isEmpty() = true
    push(x); pop() = x
    push(x); peek() = x
    push(x); size() = size() + 1
    pop(); size() = size() - 1
```

- An ADT can be used to abstract the details of the data structure and focus on the functionality and logic of the operations. For example, the ADT of a queue can be used to model a waiting line, a printer queue, a buffer, etc.
- An ADT can also be used to design and implement complex data structures, such as graphs, trees, heaps, etc. by combining simpler ADTs, such as lists, sets, maps, etc. For example, the ADT of a graph can be defined as follows:

```
ADT Graph
  Data: a collection of vertices and edges, where each edge connects two vertices
  Operations:
    addVertex(v): add vertex v to the graph
    removeVertex(v): remove vertex v and all its incident edges from the graph
    addEdge(u, v): add an edge between vertices u and v to the graph
    removeEdge(u, v): remove the edge between vertices u and v from the graph
    adjacent(u, v): return true if there is an edge between vertices u and v, false otherwise
    neighbors(v): return a collection of vertices that are adjacent to vertex v
    degree(v): return the number of edges incident to vertex v
    vertices(): return a collection of all the vertices in the graph
    edges(): return a collection of all the edges in the graph
  Axioms:
    addVertex(v); removeVertex(v) = the original graph
    addEdge(u, v); removeEdge(u, v) = the original graph
    adjacent(u, v) = true if and only if (u, v) is in edges()
    neighbors(v) = the set of vertices u such that adjacent(u, v) = true
    degree(v) = the number of elements in neighbors(v)
    vertices() = the set of all the vertices in the graph
    edges() = the set of all the edges in the graph
```

- An ADT can be tested and verified using various methods, such as unit testing, formal methods, etc. The test cases and proofs should cover the correctness and completeness of the operations and the axioms. For example, to test the ADT of a stack, one can use the following test cases:

```
Test case 1: create an empty stack and check if isEmpty() = true and size() = 0
Test case 2: push 1, 2, 3 to the stack and check if peek() = 3, size() = 3 and isEmpty() = false
Test case 3: pop the stack three