 Here is the content in Markdown format for the topic ## Unit 6 - Object Oriented Testing:

## Unit 6 - Object Oriented Testing

Object Oriented Testing involves testing individual objects/classes and their interactions. Some key points to keep in mind:

- Test public methods of classes. These are the interfaces that other objects will use to interact with the class.
- Test getter and setter methods to ensure proper encapsulation.
- Test constructors to ensure objects are initialized properly.
- Test collaboration between objects by creating test objects that simulate collaborators and assert that messages are sent correctly.
- Follow principles of good unit testing like isolation, automation, repeatability, etc.
- Use mocking frameworks to create mock objects that simulate collaborators. This keeps unit tests focused on the object being tested and not dependent on other objects.
- Write tests before production code (TDD) to drive design and ensure high test coverage.

Some advantages of OOT are:

- Tests individual components in isolation, so failures are easy to debug.
- Serves as documentation for how a class is intended to be used.
- Catches bugs early in the development cycle.
- Supports refactoring - tests can be run to ensure existing functionality is not broken by changes.

Some disadvantages are:

- Can be time-consuming to write and maintain many unit tests.
- Does not test integration between components - separate integration tests are needed for this.
- Relies on testing public interfaces, so does not directly test all internal logic/data.
- Can be difficult to test asynchronous or timed behavior.

Examples of things to test:

- Constructors: Test no-arg, arg, exception cases
- Getters/Setters: Test getting/setting with different values, including boundary cases
- Methods: Test typical use cases, exception cases, empty input, null input, etc.
- Object collaboration: Initialize test doubles for collaborating objects and assert correct messaging

I hope this helps you learn about Object Oriented Testing! Let me know if you would like me to elaborate on any of the points or add more details.