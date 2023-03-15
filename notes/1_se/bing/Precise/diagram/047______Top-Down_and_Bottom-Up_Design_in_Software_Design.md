#### Top-Down and Bottom-Up Design in Software Design

Top-down and bottom-up are two approaches to the design of software. Here is an ASCII diagram that illustrates the difference between the two approaches:

```
Top-Down:                        Bottom-Up:

+----------------+               +----------------+
| High-level     |               | Low-level      |
| design         |               | components     |
+--------+-------+               +-------+--------+
         |                               |
         v                               v
+----------------+               +----------------+
| Mid-level      |               | Mid-level      |
| design         |               | components     |
+--------+-------+               +-------+--------+
         |                               |
         v                               v
+----------------+               +----------------+
| Low-level      |               | High-level     |
| components     |               | design         |
+----------------+               +----------------+
```

In top-down design, the high-level design is created first, and then broken down into more detailed, lower-level components. In bottom-up design, the low-level components are created first, and then combined to form higher-level components and eventually the overall design.
