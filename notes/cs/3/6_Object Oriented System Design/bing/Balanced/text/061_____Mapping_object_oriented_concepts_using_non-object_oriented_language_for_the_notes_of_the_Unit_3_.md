### Mapping object oriented concepts using non-object oriented language

- Object oriented concepts are based on the idea of creating and manipulating objects that have attributes and behaviors.
- Non-object oriented languages are based on the idea of manipulating data and performing operations on them using functions and procedures.
- To map object oriented concepts using non-object oriented language, the programmer must translate the classes, objects, methods, inheritance, polymorphism and encapsulation into the target language's data structures, functions, pointers and memory management.
- The steps required to implement a design are:

  - Translate classes into data structures: A class can be represented by a structure or a record that contains the data members of the class as fields. The structure or record can also have a pointer to a function table that contains the pointers to the methods of the class.
  - Translate objects into variables: An object can be represented by a variable of the structure or record type that corresponds to the class of the object. The variable can be allocated either statically or dynamically using memory allocation functions.
  - Translate methods into functions: A method can be represented by a function that takes the object as the first argument (or as an implicit argument in some languages). The function can access and modify the data members of the object using the pointer to the structure or record. The function can also call other methods of the object using the function table pointer.
  - Translate inheritance into composition: Inheritance can be represented by composing the structure or record of the base class as a field in the structure or record of the derived class. The function table pointer of the derived class can point to a function table that contains the pointers to the methods of both the base and the derived class.
  - Translate polymorphism into function pointers: Polymorphism can be represented by using function pointers to call the appropriate method of the object depending on its type. The function table pointer of the object can be used to access the function pointer of the method that matches the signature of the call. The function pointer can then be invoked with the object as the argument.
  - Translate encapsulation into access control: Encapsulation can be represented by using access control mechanisms of the target language to restrict the visibility and modification of the data members and methods of the class. The structure or record of the class can be declared as private or protected, and the functions that implement the methods can be declared as public or friend. The functions that access the data members and methods of the class can be defined in the same file or module as the class definition.

- An example of mapping object oriented concepts using non-object oriented language is given below:

  - C++ class definition:

    ```cpp
    class Node {
      private:
        Node* next;
        int data;
      public:
        Node();
        int getData();
        void setData(int d);
        Node* getNext();
        void setNext(Node* n);
    };
    ```

  - C structure and function table definition:

    ```c
    typedef struct _Node Node;

    typedef struct _NodeFunctionTable {
      int (*getData)(Node* node);
      void (*setData)(Node* node, int d);
      Node* (*getNext)(Node* node);
      void (*setNext)(Node* node, Node* n);
    } NodeFunctionTable;

    struct _Node {
      NodeFunctionTable* functionTable;
      Node* next;
      int data;
    };
    ```

  - C functions that implement the methods:

    ```c
    // Constructor
    Node* createNode() {
      Node* node = (Node*)malloc(sizeof(Node));
      node->functionTable = (NodeFunctionTable*)malloc(sizeof(NodeFunctionTable));
      node->functionTable->getData = getNodeData;
      node->functionTable->setData = setNodeData;
      node->functionTable->getNext = getNodeNext;
      node->functionTable->setNext = setNodeNext;
      node->next = NULL;
      node->data = 0;
      return node;
    }

    // Getter for data
    int getNodeData(Node* node) {
      if(node != NULL) {
        return node->data;
      }
      else {
        return -1;
      }
    }

    // Setter for data
    void setNodeData(Node* node, int d) {
      if(node != NULL) {
        node->data = d;
      }
    }

    // Getter for next
    Node* getNodeNext(Node* node) {
      if(node != NULL) {
        return node->next;
      }
      else {
        return NULL;
      }
    }

    // Setter for next