Extreme Programming (XP) is an agile software development framework that aims to produce higher quality software, and higher quality of life for the development team. XP is the most specific of the agile frameworks regarding appropriate engineering practices for software development. 

The five values of XP are communication, simplicity, feedback, courage, and respect. 

The five rules of XP are planning, managing, designing, coding, and testing. 

The 12 XP practices are:

- The Planning Game: A meeting where the customer and the developers agree on the scope and priority of the features to be implemented in the next iteration. 
- Small Releases: The software is released frequently, with a minimal set of features, to get feedback from the customer and reduce the risk of failure. 
- Metaphor: A common vision and vocabulary that guides the design and development of the system. 
- Simple Design: The system is designed to meet the current requirements, without adding unnecessary complexity or functionality. 
- Test-Driven Development: The developers write automated unit tests before writing the code, and refactor the code to make it pass the tests. 
- Refactoring: The developers continuously improve the design and structure of the code, without changing its behavior, to make it more readable, maintainable, and extensible. 
- Pair Programming: Two developers work together on the same code, one writing and the other reviewing, to increase quality and productivity. 
- Collective Code Ownership: Any developer can modify any part of the code, as long as they follow the coding standards and run the tests. 
- Continuous Integration: The code is integrated and tested several times a day, to avoid integration conflicts and bugs. 
- Coding Standards: The developers follow a consistent set of rules and conventions for writing and formatting the code, to make it easier to read and understand. 
- Customer On Site: A representative of the customer is available to the developers, to provide feedback, clarify requirements, and set priorities. 
- Sustainable Pace: The developers work at a reasonable and consistent speed, without overtime or burnout, to maintain their motivation and quality. 

The following diagram illustrates the basic architecture of XP in spm:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|   Customer      |     |   Developers    |     |   Software      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Requirements   |     |  Planning Game  |     |  Small Releases |
|                 |---->|                 |---->|                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Feedback       |<----|  Customer On    |<----|  Feedback       |
|                 |     |  Site           |     |                 |
+-----------------+     +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Metaphor       |     |  Simple Design  |
                        |                 |---->|                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Test-Driven    |     |  Refactoring    |
                        |  Development    |---->|                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Pair           |     |  Collective     |
                        |  Programming    |---->|  Code Ownership |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Continuous     |     |  Coding         |
                        |  Integration    |---->|  Standards      |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  Sustainable    |     |  Sustainable    |
                        |  Pace           |---->|  Pace           |
                        +-----------------+     +-----------------+
```