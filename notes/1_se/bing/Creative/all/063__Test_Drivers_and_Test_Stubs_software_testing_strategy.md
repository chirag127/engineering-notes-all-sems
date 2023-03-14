#### Test Drivers and Test Stubs software testing strategy

- Test Drivers and Test Stubs are two types of test harness, which is a collection of software and test data that is configured together in order to test a unit of a program by stimulating various conditions while constantly monitoring its outputs and behavior.
- Test Drivers and Test Stubs are used to replace the modules that are not available or developed yet, but are still needed in the testing of other modules against expected functionality and features.
- Test Drivers and Test Stubs simulate the features and functionalities of the missing modules, and have the ability to serve the features that a module can provide. This reduces unnecessary delay in testing and makes the testing process faster.
- Test Stubs are mainly used in Top-Down integration testing while the Drivers are used in Bottom-up integration testing, thus increasing the efficiency of the testing process.
- Test Stubs are developed by software developers to use them in place of modules, if the respective modules are not developed, missing in developing stage, or are unavailable currently while Top-down testing of modules.
- Test Stubs are also known as "called programs" as they receive instructions from the higher-level modules and return the corresponding values that are used by the modules.
- Test Stubs are divided into four basic categories based on what they do:
  - Shows the traced messages, 
  - Shows the displayed message if any, 
  - Returns the corresponding values that are utilized by modules, 
  - Returns the value of the chosen parameters (arguments) that were used by the testing modules.
- Test Drivers serve the same purpose as Test Stubs, but Test Drivers are used in Bottom-up integration testing and are also more complex than Test Stubs.
- Test Drivers are also used when some modules are missing and unavailable at the time of testing of a specific module because of some unavoidable reasons, to act in absence of the required module.
- Test Drivers are also known as "calling programs" as they call the lower-level modules and perform their testing.
- Test Drivers can also be used when high-level modules are missing and can also be used when lower-level modules are missing.

Example of Test Stubs:

Suppose we have an application in which there are three modules, say Login, Add student and Cancel Admission. Now suppose we are doing unit testing of the module Login and the modules Add Student and Cancel Admission are yet not prepared. Then we will create dummy modules for Add student and Cancel admission in order to carry out testing of Login modules. These dummy modules of Add student and Cancel admission are known as Test Stubs. They receive instructions from the login module and display the success or failure of login functionality.

Example of Test Drivers:

Suppose we have an application in which three modules are there, say Login, Add student and Cancel Admission. Now we want to do the testing of the Add student module. Add student module cannot run standalone; first, we have to enter into login page and then add student module will be executed. So Add Student module will be called by the Login module. Let us assume that the Login module has not been developed by the developers. In this case, we have to create a dummy module of Login which will call the Add student module and then the functionalities of the add student module will be tested.

Mnemonics and learning tricks for Test Drivers and Test Stubs software testing strategy:

- A possible mnemonic to remember the difference between Test Stubs and Test Drivers is: **S**tubs are used in **S**top-down testing and **D**rivers are used in **D**own-up testing.
- A possible learning trick to remember the difference between Test Stubs and Test Drivers is: Test Stubs are like the **sub**stitutes for the lower-level modules, while Test Drivers are like the **drive**rs for the higher-level modules.