### Testing techniques and their applicability for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing

Testing techniques are methods used to design and execute tests to evaluate software applications. Testing techniques can be classified into two main categories: functional and non-functional testing.

Functional testing techniques verify that the software meets the specified requirements and performs the expected functions. Functional testing techniques include:

- Unit testing: Testing individual methods and functions of the classes, components, or modules used by the software. Unit testing is usually automated and can run very quickly by a continuous integration server.
- Integration testing: Testing how different modules or services used by the software work together. Integration testing can be done at different levels, such as component, subsystem, or system level.
- Functional testing: Testing the functions of the software by emulating business scenarios, based on functional requirements. Functional testing can be done using black-box testing, which does not require knowledge of the internal structure or code of the software, or white-box testing, which does require such knowledge.
- Acceptance testing: Testing whether the software meets the acceptance criteria of the customer or end-user. Acceptance testing can be done by the customer, the end-user, or a third-party.

Non-functional testing techniques verify that the software meets the quality attributes and performance standards. Non-functional testing techniques include:

- Performance testing: Testing how the software performs under different workloads and conditions. Performance testing can include load testing, which evaluates performance under real-life load conditions, stress testing, which evaluates performance under extreme conditions, and endurance testing, which evaluates performance over a long period of time.
- Usability testing: Testing how well a customer or end-user can use the software to complete a task. Usability testing can include user interface testing, which evaluates the appearance and functionality of the user interface, and user experience testing, which evaluates the satisfaction and engagement of the user.
- Security testing: Testing how well the software protects the data and resources from unauthorized access or attacks. Security testing can include vulnerability testing, which identifies the weaknesses and loopholes of the software, penetration testing, which simulates an attack on the software, and ethical hacking, which exploits the vulnerabilities of the software to improve its security.
- Reliability testing: Testing how well the software functions under normal and abnormal conditions. Reliability testing can include fault tolerance testing, which evaluates how the software handles errors and failures, recovery testing, which evaluates how the software recovers from errors and failures, and availability testing, which evaluates how often the software is operational and accessible.

The applicability of testing techniques depends on the type, size, complexity, and scope of the software project, as well as the available time, resources, and budget. Some general guidelines for choosing testing techniques are:

- Start with unit testing and integration testing, as they are the most basic and essential types of testing, and can help detect and fix defects early in the development process.
- Use functional testing and acceptance testing to ensure that the software meets the functional requirements and the customer's expectations.
- Use non-functional testing to ensure that the software meets the quality and performance standards, and to identify and improve the areas that need optimization.
- Use a combination of manual and automated testing, as manual testing can help uncover hard-to-predict scenarios and situations that can lead to software errors, while automated testing can help save time and resources, and increase the coverage and reliability of testing.
- Use exploratory testing, which is a type of manual testing that involves testing the software without a predefined plan or script, to discover new features, functionalities, or defects that may not be covered by other testing techniques.

Some mnemonics and learning tricks for testing techniques and their applicability are:

- **FURPS**: A mnemonic for the main categories of non-functional testing: Functionality, Usability, Reliability, Performance, and Security.
- **CRUD**: A mnemonic for the main types of operations that can be tested in functional testing: Create, Read, Update, and Delete.
- **PICT**: A tool for pairwise testing, which is a technique that tests all possible combinations of two parameters in a software system. PICT stands for Pairwise Independent Combinatorial Testing.
- **STRIDE**: A mnemonic for the main types of threats that can be tested in security testing: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, and Elevation