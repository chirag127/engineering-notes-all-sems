 Here is the content written in formal tone with markdown format without any emojis or external links:

### Namespace for the notes of the Unit 4 - C++ Basics in the subject of Object Oriented System Design:

1. Namespace is a feature added in C++ to solve the problem of namespace collisions and naming conflicts.
2. A namespace is a declarative region that provides a scope to the identifiers (names of types, functions, variables, etc) inside it. This allows to logically group entities that are somehow related.
3. Declaring identifiers inside a namespace allows to distinguish between identically-named entities in different namespaces.
4. The format to define a namespace is:
   namespace namespace_name {
   // declarations
   }
5. We can split the declarations over multiple files and the entities remain in the same namespace.
6. Namespace declarations can be nested, which means we can have namespaces inside other namespaces. This allows to create a hierarchic namespace structure.
7. To refer to an entity inside a namespace, we use the scope resolution operator (::). For example:
   namespace foo {
       int bar;
   }
   foo::bar = 1; // Reference an entity in the foo namespace

The content focuses on explaining the key points about namespace in C++ in a formal manner with points and without any emojis or informal expressions. The markdown format is used and no external links are included. Please let me know if you would like me to modify or add any other points to the content.