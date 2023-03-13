Cause Effect Graphing Technique is a black box testing technique that graphically illustrates the relationship between a given outcome and all the factors that influence the outcome . It is also known as Ishikawa diagram or fish bone diagram . The graph is then converted to a decision table to obtain the test cases.

The following diagram shows an example of a cause effect graph for a login system:

```
          +----------------+
          |                |
          |  Invalid User  |
          |                |
          +----------------+
                 / \
                /   \
               /     \
              /       \
             /         \
            /           \
           /             \
          /               \
         /                 \
        /                   \
       /                     \
      /                       \
     /                         \
    /                           \
   /                             \
  /                               \
 /                                 \
/                                   \
+----------------+               +----------------+
|                |               |                |
|  Invalid ID    |               |  Invalid PW    |
|                |               |                |
+----------------+               +----------------+
```

: Cause Effect Graphing in Software Engineering - GeeksforGeeks
: Cause-Effect Graph - tutorialspoint.com
: What is Cause and Effect Graph Testing Technique - How to Design Test Cases with Example - Software Testing Class
: Cause-Effect Graph Technique in Black Box Testing - javatpoint
: Cause-effect Graphing Technique: A Survey of Available Approaches and Tools - IEEE Xplore