I am Sydney, your AI assistant. I can help you with any topic. You asked me to draw a detailed ASCII diagram for 7. WAP to find the greatest of three numbers. Here is the diagram:

```
+-----------------+     +-----------------+     +-----------------+
| Input three     |     | Compare the     |     | Output the      |
| numbers: a, b, c| --> | numbers: a > b? | --> | greatest number |
+-----------------+     +-----------------+     +-----------------+
                          |               |
                          | Yes           | No
                          |               |
                          v               v
                     +-----------------+     +-----------------+
                     | Compare the     |     | Compare the     |
                     | numbers: a > c? | --> | numbers: b > c? |
                     +-----------------+     +-----------------+
                          |               |
                          | Yes           | No
                          |               |
                          v               v
                     +-----------------+     +-----------------+
                     | Output a as the |     | Output c as the |
                     | greatest number |     | greatest number |
                     +-----------------+     +-----------------+
```