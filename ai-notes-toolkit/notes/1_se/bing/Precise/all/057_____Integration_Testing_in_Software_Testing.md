### Integration Testing in Software Testing

Integration testing is a level of software testing where individual units are combined and tested as a group. The purpose of this level of testing is to expose faults in the interaction between integrated units. Test drivers and test stubs are used to assist in Integration Testing.

- Integration testing is done after unit testing and before system testing.
- Integration testing takes as its input modules that have been unit tested, groups them in larger aggregates, applies tests defined in an integration test plan to those aggregates, and delivers as its output the integrated system ready for system testing.

#### Advantages of Integration Testing
- It helps to find issues that occur when different modules interact with each other.
- It helps to verify the functional, performance, and reliability requirements placed on major design items.
- It helps to ensure that the integrated modules work correctly together.

#### Disadvantages of Integration Testing
- It can be time-consuming and expensive.
- It can be difficult to isolate defects.

#### Types of Integration Testing
- **Big Bang Integration Testing**: All the modules are integrated at once and then tested.
- **Top-Down Integration Testing**: Testing takes place from top to bottom, following the control flow or architectural structure. Components or systems are substituted by stubs.
- **Bottom-Up Integration Testing**: Testing takes place from the bottom of the control flow upwards. Components or systems are substituted by drivers.
- **Sandwich/Hybrid Integration Testing**: A combination of top-down and bottom-up approaches.

#### Mnemonics and Learning Tricks
- **B**ig **B**ang **I**ntegration **T**esting: **BBIT**.
- **T**op-**D**own **I**ntegration **T**esting: **TDIT**.
- **B**ottom-**U**p **I**ntegration **T**esting: **BUIT**.
- **S**andwich/**H**ybrid **I**ntegration **T**esting: **SHIT**.

#### Example
Suppose we have three modules A, B, and C. A calls B, and B calls C. In top-down integration testing, we would first test A with a stub for B. Then, we would integrate B and test A and B together with a stub for C. Finally, we would integrate C and test all three modules together.

In bottom-up integration testing, we would first test C with a driver. Then, we would integrate B and test B and C together with a driver for A. Finally, we would integrate A and test all three modules together.

In big bang integration testing, we would integrate all three modules at once and test them together.

In sandwich/hybrid integration testing, we would use a combination of top-down and bottom-up approaches. For example, we could test A with a stub for B, test C with a driver, integrate B, and then test all three modules together.