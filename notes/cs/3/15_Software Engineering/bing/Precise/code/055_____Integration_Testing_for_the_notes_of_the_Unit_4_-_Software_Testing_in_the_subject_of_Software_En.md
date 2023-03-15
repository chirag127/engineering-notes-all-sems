### Integration Testing

Integration testing is a level of software testing where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units. Test drivers and test stubs are used to assist in Integration Testing.

- Integration testing is performed after unit testing and before system testing.
- Integration testing takes as its input modules that have been unit tested, groups them in larger aggregates, applies tests defined in an integration test plan to those aggregates, and delivers as its output the integrated system ready for system testing.
- The main objective of integration testing is to test the interface between the modules.
- Integration testing is a systematic technique for constructing the program structure while conducting tests to uncover errors associated with interfacing.
- The objective is to take unit tested components and build a program structure that has been dictated by design.
- There are different approaches to perform integration testing, such as big bang, top-down, bottom-up, sandwich/hybrid, and risk-based integration testing.
- Big Bang Integration Testing: In this approach, all the modules are integrated simultaneously, after which everything is tested as a whole.
- Top-Down Integration Testing: In this approach, testing takes place from top to bottom, following the control flow or architectural structure. The highest-level modules are tested first, and lower-level modules are tested step by step after that.
- Bottom-Up Integration Testing: In this approach, the lowest level components are tested first, then used to facilitate the testing of higher-level components. The process is repeated until the component at the top of the hierarchy is tested.
- Sandwich/Hybrid Integration Testing: This approach is a combination of top-down and bottom-up approaches.
- Risk-Based Integration Testing: In this approach, the risk assessment is used to decide the order in which the components should be integrated and tested.