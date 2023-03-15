# Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing**  , meaning that they can maintain a **logarithmic height** even after insertion and deletion operations .
- Red-black trees have the following **properties** :
  - Every node is either **red** or **black**.
  - The root of the tree is always **black**.
  - Every leaf node (NIL) is **black**.
  - If a node is **red**, then both its children are **black**.
  - Every simple path from a node to a descendant leaf node has the same number of **black** nodes. This number is called the **black height** of the node.
- Red-black trees can be used to store and retrieve **ordered** data efficiently, such as text fragments or numbers.
- Red-black trees have a **guaranteed time complexity** of O(log n) for basic operations like insertion, deletion, and search .
- Red-black trees use a mechanism called **rotation** to restore the balance of the tree after insertion or deletion . Rotation is a local operation that changes the structure of the tree without affecting the order of the elements.
- Red-black trees can be used in a wide range of applications due to their efficient performance and versatility. Some examples are:
  - Implementing **associative arrays** or **maps**, such as the C++ STL map and set, and the Java TreeMap and TreeSet classes.
  - Implementing **priority queues**, such as the C++ STL priority_queue and the Java PriorityQueue class.
  - Implementing **interval trees**, which are used for storing and querying intervals or ranges of values.
  - Implementing **concurrent skip lists**, which are used for concurrent access and modification of ordered data structures.