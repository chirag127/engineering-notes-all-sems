### Red-Black Trees

- Red-black trees are a type of **binary search tree** that are **self-balancing** and **efficient** for storing and retrieving ordered data .
- Each node in a red-black tree has a **color** attribute that is either **red** or **black**  .
- The root of the tree is always **black**  .
- The **leaf nodes** (or **NIL nodes**) are also **black** and do not contain any data  .
- A **red node** cannot have a **red parent** or a **red child**. This is called the **no-red-edge property**  .
- Every path from a node to a leaf node contains the same number of **black nodes**. This is called the **black-height property**  .
- The **height** of a red-black tree is at most **2*log(n+1)**, where **n** is the number of nodes in the tree  .
- The basic operations on a red-black tree, such as **insertion**, **deletion**, and **search**, take **O(log n)** time in the worst case  .
- The insertion and deletion operations may violate the color and balance properties of the tree, so they require **rotations** and **recoloring** to restore the red-black tree properties  .
- Red-black trees are widely used in various applications, such as **databases**, **concurrent data structures**, **interval trees**, and **augmented trees** .