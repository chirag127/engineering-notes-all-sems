 Here is the content in markdown format for the given topic:

### Mutation Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

Mutation testing is a method of software testing that involves making small changes to the source code of a program to evaluate the quality of test cases.

- Mutation testing adds faults (bugs) into a program by changing the source code in random ways. The tests then run on the mutated program. If the tests detect the change, the test has passed. If the test does not detect a mutated changed version, it has failed.
- The percentage of mutations detected by tests is termed "mutation score". A high mutation score means tests are detecting changes effectively and indicates a high quality of tests.
- Advantages: It gives a measurable value/score to test suite quality. It checks for code coverage as well as test effectiveness. It can identify missing test cases.
- Disadvantages: It can be computationally expensive as multiple mutated versions of the program may have to be tested. It does not check for functional correctness, only structural correctness.
- Example: Changing an > to a >= in if condition. Swapping true and false in boolean expression. Replacing + with -.
- Applications: Mutation testing is used to improve the quality of software testing and test suites. It helps evaluate and enhance the effectiveness of written tests.

Tips to remember:
- Think of mutations as bugs intentionally inserted
- High mutation score = High quality tests
- Checks for coverage as well as effectiveness
- Computationally expensive
- Checks structural correctness, not functional correctness

Does this help? Let me know if you would like me to modify or add anything.