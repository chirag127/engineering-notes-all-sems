According to the search results, Error for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing is a term that refers to the impact an undiscovered error has on future development activities or product behavior. It is also known as defect propagation or defect amplification.

One way to illustrate this concept is to use a diagram that shows the software engineering work flow and the errors introduced and detected at each stage. For example, the following diagram is drawn using ASCII characters:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
| Requirements   |     | Design         |     | Coding         |     | Testing        |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
| Errors         |     | Errors         |     | Errors         |     | Errors         |
| introduced: 10 |     | introduced: 20 |     | introduced: 30 |     | introduced: 10 |
| detected:   5  |     | detected:  10  |     | detected:  15  |     | detected:  20  |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
| Errors         |     | Errors         |     | Errors         |     | Errors         |
| remaining:  5  |---->| remaining: 15  |---->| remaining: 30  |---->| remaining: 30  |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
```

The diagram shows that errors introduced at earlier stages are not detected until later stages, and they cause more errors to be introduced at each stage. This increases the cost and effort of fixing the errors and reduces the quality of the software product. Therefore, it is important to perform software reviews and testing at each stage to find and resolve errors as early as possible.