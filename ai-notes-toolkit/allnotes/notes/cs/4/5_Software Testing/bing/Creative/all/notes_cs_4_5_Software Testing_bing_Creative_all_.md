

## Unit 1 - Review of Software Engineering

- Software engineering is the application of engineering principles and practices to the development, operation, and maintenance of software systems.
- Software engineering covers a wide range of activities, such as:
  - Requirements analysis: eliciting, specifying, and validating the needs and expectations of the stakeholders for the software system.
  - Design: defining the architecture, components, interfaces, and data structures of the software system.
  - Implementation: coding, testing, debugging, and documenting the software system.
  - Verification and validation: ensuring that the software system meets the requirements and quality standards.
  - Deployment: delivering, installing, and configuring the software system for the intended users and environments.
  - Maintenance: correcting, improving, and adapting the software system to changing needs and conditions.
  - Evolution: managing the changes and updates to the software system over its life cycle.
- Software engineering also involves the application of various methods, tools, and standards to support the software development process, such as:
  - Software process models: frameworks that describe the phases, activities, tasks, and deliverables of a software project, such as waterfall, agile, iterative, or spiral models.
  - Software engineering disciplines: specialized areas of knowledge and practice that focus on specific aspects of software engineering, such as software quality, software testing, software security, software configuration management, or software project management.
  - Software engineering standards: guidelines and best practices that define the quality criteria, processes, and documentation for software engineering, such as ISO/IEC 12207, IEEE 830, or CMMI.
  - Software engineering tools: software applications that automate or facilitate various tasks and activities of software engineering, such as requirements management tools, design tools, programming tools, testing tools, or deployment tools.



# Overview of Software Evolution

- Software evolution is the continual development of a piece of software after its initial release to address changing stakeholder and/or market requirements .
- Software evolution is important because organizations invest large amounts of money in their software and are completely dependent on this software. Software evolution helps software adapt to new business needs, improve quality, fix defects, and cope with environmental changes.
- Software evolution refers to the dynamic behavior of software systems, as they are maintained and enhanced over their lifetimes. Software evolution is particularly important as systems in organizations become longer-lived.
- Software development and evolution can be thought of as an integrated, iterative process that can be represented using a spiral model. The spiral model combines the features of the waterfall model and the prototyping model, and adds risk analysis and evaluation phases.
- The process of software evolution is driven by requests for changes and includes change impact analysis, release planning, system implementation and releasing a system to customers. Requests for changes may come from different sources, such as users, developers, managers, or regulators.
- Software evolution is governed by some empirical laws, such as Lehman's laws, which describe the properties and behavior of evolving software systems. Some of these laws are:

  - Continuing change: A program that is used in a real-world environment must change, or else it becomes progressively less useful in that environment.
  - Increasing complexity: As a program evolves, its structure tends to become more complex, unless work is done to maintain or reduce it.
  - Self-regulation: The global activity of a program evolution process is statistically self-regulating, with the distribution of product and process measures close to normal.
  - Conservation of organizational stability: The average effective global activity rate in an evolving software system is invariant over the product's lifetime.
  - Conservation of familiarity: The incremental change in each release of a software system is approximately constant.
  - Continuing growth: The functionality offered by a software system must continually increase to maintain user satisfaction.
  - Declining quality: The quality of a software system will appear to be declining unless it is rigorously maintained and adapted to operational environment changes.
  - Feedback system: Software evolution is a multi-level, multi-loop, multi-agent feedback system, and must be treated as such to achieve significant improvement over any reasonable base.



# SDLC for the notes of the Unit 1 - Review of Software Engineering

- SDLC stands for Software Development Life Cycle    .
- It is a process used in software engineering to design, develop, test, and deploy software applications    .
- It is a structured approach to software development that helps organizations to improve the quality of their software products, reduce costs, and minimize risks  .
- It consists of several phases, each with its own activities, deliverables, and outcomes    .
- The common phases of SDLC are    :
  - Requirement analysis: This phase involves gathering and analyzing the needs and expectations of the stakeholders and users of the software application    .
  - Planning: This phase involves defining the scope, objectives, schedule, budget, resources, and risks of the software project    .
  - Software design: This phase involves creating the architectural and detailed design of the software application, such as the data structures, algorithms, interfaces, and modules    .
  - Software development: This phase involves writing and testing the source code of the software application, following the design specifications and coding standards    .
  - Software testing: This phase involves verifying and validating the functionality, performance, usability, security, and quality of the software application, using various testing techniques and tools    .
  - Software deployment: This phase involves releasing and installing the software application to the target environment, such as the production server, cloud platform, or end-user device    .
  - Software maintenance: This phase involves providing ongoing support and updates to the software application, such as fixing bugs, adding features, and enhancing performance    .
- There are different models of SDLC, such as waterfall, agile, iterative, spiral, and hybrid, that vary in the sequence, iteration, and feedback of the phases    .
- The choice of the SDLC model depends on the size, complexity, scope, and requirements of the software project, as well as the preferences and capabilities of the software team    .
- The benefits of using SDLC are  :
  - It provides a clear and consistent framework for software development  .
  - It improves the communication and collaboration among the stakeholders and software team  .
  - It enhances the efficiency and effectiveness of the software development process  .
  - It reduces the errors and defects in the software application  .
  - It ensures the satisfaction and quality of the software application  .



# Testing Process

The testing process is a set of activities that aim to verify and validate the quality of a software product. The testing process can be divided into four main phases: planning, analysis, design, and execution.

## Planning

Planning is the first phase of the testing process, where the objectives, scope, strategy, and resources of the testing are defined. Planning also involves identifying the stakeholders, risks, assumptions, and constraints of the testing. Some of the main activities and deliverables of the planning phase are:

- Test plan: A document that describes the overall approach and scope of the testing, including the test objectives, test items, test environment, test schedule, test roles and responsibilities, test tools, test techniques, test metrics, test deliverables, and test risks.
- Test estimation: A process of estimating the effort, time, and cost required for the testing activities, based on the size, complexity, and quality of the test items, and the availability and capability of the test resources.
- Test case management: A process of organizing, managing, and tracking the test cases, test data, test results, and test defects throughout the testing process, using a test management tool or a test management system.

## Analysis

Analysis is the second phase of the testing process, where the test items are analyzed and the test requirements are derived. Analysis also involves reviewing and verifying the test items for completeness, consistency, and correctness. Some of the main activities and deliverables of the analysis phase are:

- Test requirements: A set of statements that specify what needs to be tested, how it should be tested, and what the expected results are. Test requirements can be derived from various sources, such as user requirements, functional specifications, design documents, use cases, user stories, or acceptance criteria.
- Test coverage: A measure of how much of the test items are covered by the test requirements, expressed as a percentage or a ratio. Test coverage can be calculated at different levels, such as requirement coverage, function coverage, code coverage, or branch coverage.
- Test traceability: A process of establishing and maintaining the relationships between the test items, test requirements, test cases, test results, and test defects, using a traceability matrix or a traceability tool. Test traceability helps to ensure that the testing is complete, consistent, and relevant, and to identify the impact of changes in the test items or test requirements.

## Design

Design is the third phase of the testing process, where the test cases and test data are designed and prepared, based on the test requirements and the test strategy. Design also involves selecting and applying the appropriate test techniques, test tools, and test methods for the testing. Some of the main activities and deliverables of the design phase are:

- Test cases: A set of inputs, actions, and expected outputs that are used to test a specific test requirement or test scenario. Test cases can be designed using various techniques, such as equivalence partitioning, boundary value analysis, decision table testing, state transition testing, use case testing, or exploratory testing.
- Test data: A set of values or information that are used as inputs or outputs for the test cases. Test data can be generated, collected, or modified using various tools, such as data generators, data extractors, data converters, or data editors.
- Test scripts: A set of instructions or commands that are used to execute the test cases, either manually or automatically, using a test tool or a test framework. Test scripts can be written in various languages, such as Java, Python, C#, or SQL.

## Execution

Execution is the fourth and final phase of the testing process, where the test cases are executed and the test results are recorded and evaluated. Execution also involves reporting and resolving the test defects, and reporting and communicating the test status and progress. Some of the main activities and deliverables of the execution phase are:

- Test execution: A process of running the test cases and test scripts, either manually or automatically, using a test tool or a test framework, and observing and recording the test results, such as pass, fail, or inconclusive.
- Test defect: A deviation or discrepancy between the actual and expected results of a test case, indicating a fault or an error in the test item. Test defects can be reported, tracked, and managed using a defect management tool or a defect management system.
- Test report: A document that summarizes and communicates the results, findings, and outcomes of the testing, including the test objectives, test scope, test coverage, test metrics, test defects, test issues, test risks, and test recommendations.



# Terminologies in Testing

- Testing is the process of verifying and validating that a software product or system meets the specified requirements and expectations of the stakeholders.
- Testing can be performed at different levels and types, depending on the objectives, scope, and context of the testing activity.
- Testing can also be classified into different techniques, based on the methods and criteria used to design and execute test cases.
- Testing can be formal or informal, depending on the degree of planning, documentation, and control involved in the testing process.
- Testing can be part of the software development life cycle (SDLC) or the software testing life cycle (STLC), depending on the phase and role of testing in the software project.
- Some of the common terminologies used in testing are:

  - **SDLC (Software Development Life Cycle)**: An international standard for software life-cycle processes that defines all the tasks required for developing and maintaining software. It consists of several phases, such as planning, analysis, design, implementation, testing, deployment, and maintenance.
  - **Test Level**: A specific instantiation of a test process that corresponds to a particular phase or stage of the SDLC. For example, unit testing, integration testing, system testing, and acceptance testing are different test levels.
  - **Test Type**: A group of test activities that aim to evaluate a specific quality attribute or characteristic of the software product or system. For example, functional testing, non-functional testing, security testing, and usability testing are different test types.
  - **Test Design Technique**: A method or procedure used to derive and select test cases based on the test objectives, test basis, and test criteria. For example, specification-based testing, structure-based testing, and experience-based testing are different test design techniques.
  - **STLC (Software Testing Life Cycle)**: A systematic approach for planning, designing, executing, evaluating, and reporting the testing activities and results. It consists of several phases, such as test planning, test analysis, test design, test implementation, test execution, test evaluation, and test closure.
  - **Informal Testing**: Testing that is performed without following a formal or structured process, such as test planning, test documentation, test execution, and test reporting. It is usually done by the developers or testers themselves, without any external review or supervision. For example, ad hoc testing, exploratory testing, and error guessing are types of informal testing.
  - **Test Planning**: The activity of defining the scope, objectives, approach, and resources for the testing process. It involves identifying the test items, test levels, test types, test techniques, test environment, test schedule, test roles, test risks, and test deliverables.
  - **Test Documentation**: The activity of creating and maintaining the artifacts that describe the testing process and results. It includes the test plan, test cases, test scripts, test data, test logs, test reports, test incidents, and test summaries.
  - **Test Execution**: The activity of running the test cases or test scripts on the test items or test objects, using the test data and test tools, in the test environment, and recording the test results and test incidents.
  - **Test Evaluation**: The activity of assessing the test results and test incidents, and comparing them with the test objectives and test criteria, to determine the quality and status of the software product or system, and to identify any defects or issues that need to be resolved.
  - **Test Closure**: The activity of finalizing and archiving the test documentation, test deliverables, test environment, and test tools, and releasing the test resources. It also involves evaluating the test process and identifying the lessons learned and improvement actions for future testing projects.



# Error

- An error is a human action that produces an incorrect or undesired result.
- Errors can occur at any stage of the software development life cycle, such as requirements, design, coding, testing, or maintenance.
- Errors can be classified into three types: syntax errors, semantic errors, and logical errors.
- Syntax errors are violations of the rules of the programming language, such as missing a semicolon or a parenthesis. Syntax errors are usually detected by the compiler or the interpreter and prevent the program from running.
- Semantic errors are violations of the meaning or the logic of the program, such as using the wrong variable name or the wrong operator. Semantic errors are not detected by the compiler or the interpreter, but they cause the program to produce incorrect or unexpected results.
- Logical errors are violations of the intended functionality or the specification of the program, such as missing a condition or a loop. Logical errors are also not detected by the compiler or the interpreter, but they cause the program to fail to meet the user's or the client's expectations or requirements.



# Fault

- A fault is an error or defect in a software program that causes it to produce incorrect or unexpected results .
- A fault is also known as a bug, defect, flaw, or mistake  .
- A fault can occur at any stage of the software development process, from the initial design to the final deployment .
- Common types of faults include coding errors, design flaws, and requirements errors .
- A fault is the basic reason for software malfunction and is synonymous with the commonly used term bug .
- A fault is a state that causes the software to fail and therefore it does not achieve its necessary function.
- A fault can be detected by testing, debugging, or reviewing the software  .
- A fault can be corrected by fixing the error or defect in the software  .
- A fault can be prevented by following good software engineering practices, such as design reviews, code reviews, testing, and quality assurance  .



# Failure

- Failure is the inability of a software system or component to perform its required functions within specified performance requirements.
- Failure occurs when the software fails to perform in the real environment.
- Failure is the result of the presence of faults or errors in the software.
- Failure can have various consequences, such as loss of data, damage to hardware, harm to users, or violation of laws or regulations.
- Failure can be classified into different types, such as:
  - Functional failure: when the software does not meet the functional requirements or specifications.
  - Non-functional failure: when the software does not meet the non-functional requirements or quality attributes, such as performance, usability, security, reliability, etc.
  - Catastrophic failure: when the software causes severe damage or harm to the system, users, or environment.
  - Recoverable failure: when the software can resume its normal operation after a failure.
  - Unrecoverable failure: when the software cannot resume its normal operation after a failure.
- Failure can be prevented or reduced by applying various software engineering techniques, such as:
  - Requirements engineering: to elicit, analyze, specify, and validate the software requirements.
  - Design engineering: to create a high-level and low-level design of the software system or component.
  - Coding engineering: to implement the software design using a programming language and following coding standards and guidelines.
  - Testing engineering: to verify and validate the software functionality, quality, and performance using various testing methods and tools.
  - Maintenance engineering: to correct, improve, or adapt the software to changing needs or environments.



# Verification for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Verification is the process of checking whether the software meets the specified requirements and design specifications.
- Verification can be done by various methods such as reviews, inspections, walkthroughs, audits, and testing.
- Verification aims to ensure that the software is built correctly and conforms to the standards and guidelines.
- Verification can be performed at different stages of the software development life cycle, such as planning, analysis, design, coding, testing, and maintenance.
- Verification can be classified into two types: static verification and dynamic verification.
- Static verification is the process of checking the software artifacts without executing them, such as documents, models, code, etc.
- Static verification can be done by manual or automated techniques, such as peer reviews, static analysis tools, code quality metrics, etc.
- Static verification can help to detect errors, inconsistencies, ambiguities, and deviations from the requirements and design specifications.
- Dynamic verification is the process of checking the software artifacts by executing them, such as test cases, test scripts, etc.
- Dynamic verification can be done by manual or automated techniques, such as unit testing, integration testing, system testing, acceptance testing, etc.
- Dynamic verification can help to validate the functionality, performance, reliability, and usability of the software.
- Verification is an important activity in software engineering, as it can help to improve the quality, efficiency, and effectiveness of the software.



# Validation for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Software engineering is the application of engineering principles and practices to the development and maintenance of software systems that meet the needs and expectations of stakeholders.
- Software engineering involves activities such as requirements analysis, design, implementation, testing, deployment, maintenance, and evolution of software systems.
- Software engineering is guided by standards, methodologies, models, processes, tools, and best practices that aim to improve the quality, productivity, and reliability of software development and maintenance.
- Software engineering is a multidisciplinary field that requires knowledge and skills from various domains such as computer science, mathematics, engineering, management, psychology, and communication.
- Software engineering is also influenced by the context and characteristics of the software project, such as the application domain, the size and complexity of the system, the budget and schedule constraints, the customer and user requirements, the organizational culture and structure, and the legal and ethical issues.
- Software engineering is an evolving and dynamic field that adapts to the changing needs and demands of the software industry and society.

- Validation is the process of checking whether the software system meets the specified requirements and satisfies the intended purpose and expectations of the stakeholders.
- Validation is usually performed after the software system is implemented and before it is deployed to the operational environment.
- Validation is also known as verification, acceptance testing, or quality assurance testing.
- Validation involves activities such as planning, designing, executing, and evaluating test cases and test scenarios that cover the functional and non-functional requirements of the software system.
- Validation also involves reporting and analyzing the test results, identifying and resolving the defects, and ensuring that the software system meets the quality standards and criteria.
- Validation is a collaborative and iterative process that involves the participation and feedback of various stakeholders such as developers, testers, customers, users, managers, and regulators.



# Difference Between Verification and Validation

- Verification and validation are two important activities in software engineering that aim to ensure the quality of software products and processes.
- Verification is the process of checking whether the software conforms to the specified requirements and design specifications. It answers the question "Are we building the product right?"
- Validation is the process of checking whether the software meets the expectations and needs of the end-users and stakeholders. It answers the question "Are we building the right product?"
- Verification is usually done before validation, and it involves static testing techniques such as reviews, inspections, walkthroughs, and audits.
- Validation is usually done after verification, and it involves dynamic testing techniques such as unit testing, integration testing, system testing, and acceptance testing.
- Verification is mainly concerned with the internal quality of the software, such as functionality, reliability, performance, maintainability, etc.
- Validation is mainly concerned with the external quality of the software, such as usability, security, compatibility, portability, etc.
- Verification helps to detect errors and defects in the early stages of software development, which reduces the cost and effort of fixing them later.
- Validation helps to ensure that the software satisfies the customer requirements and delivers the expected value and benefits.



# Test Cases for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Test case 1: Verify that the notes cover the definition and objectives of software engineering.
  - Expected result: The notes should explain what software engineering is, why it is important, and what are the main goals of software engineering.
  - Actual result: The notes provide a clear and concise definition of software engineering, and list the objectives of software engineering as producing software that is reliable, efficient, maintainable, and meets the user's needs.
  - Pass/Fail: Pass

- Test case 2: Verify that the notes cover the software development life cycle (SDLC) and its phases.
  - Expected result: The notes should describe the SDLC as a process of planning, designing, implementing, testing, and maintaining software, and explain the activities and deliverables of each phase.
  - Actual result: The notes outline the SDLC and its phases as follows:
    - Requirement analysis: Gathering and analyzing the user's needs and expectations for the software.
    - Design: Creating a blueprint of the software architecture and components.
    - Implementation: Coding and integrating the software modules and components.
    - Testing: Verifying and validating the software functionality and quality.
    - Deployment: Delivering and installing the software to the user's environment.
    - Maintenance: Providing support and updates for the software after deployment.
  - Pass/Fail: Pass

- Test case 3: Verify that the notes cover the software process models and their types.
  - Expected result: The notes should explain what software process models are, why they are needed, and what are the main types of software process models.
  - Actual result: The notes define software process models as frameworks that define the tasks, activities, and roles involved in software development, and state that they are needed to provide structure, guidance, and control for the software project. The notes also describe the main types of software process models as follows:
    - Waterfall model: A linear and sequential model that follows the phases of the SDLC in a fixed order, with each phase depending on the completion of the previous one.
    - Incremental model: A model that divides the software project into smaller increments, each of which follows the SDLC phases and delivers a working software product.
    - Iterative model: A model that repeats the SDLC phases for each iteration, with each iteration producing a refined and improved version of the software product.
    - Spiral model: A model that combines the features of the incremental and iterative models, with each iteration consisting of four stages: planning, risk analysis, development, and evaluation.
    - Agile model: A model that emphasizes flexibility, adaptability, and collaboration, with short and frequent iterations, continuous feedback, and self-organizing teams.
  - Pass/Fail: Pass

- Test case 4: Verify that the notes cover the software quality and its attributes.
  - Expected result: The notes should define what software quality is, why it is important, and what are the main attributes of software quality.
  - Actual result: The notes state that software quality is the degree to which the software meets the user's requirements, expectations, and standards, and that it is important to ensure the software's reliability, usability, efficiency, and maintainability. The notes also list the main attributes of software quality as follows:
    - Functionality: The ability of the software to perform its intended functions correctly and completely.
    - Reliability: The ability of the software to operate without failures or errors under normal and abnormal conditions.
    - Usability: The ease and satisfaction with which the user can learn, use, and interact with the software.
    - Efficiency: The ability of the software to use the minimum amount of resources (such as time, memory, and CPU) to achieve its functions.
    - Maintainability: The ease and cost with which the software can be modified, updated, and repaired.
    - Portability: The ability of the software to run on different platforms, environments, and devices without significant changes.
  - Pass/Fail: Pass

- Test case 5: Verify that the notes cover the software testing and its objectives.
  - Expected result: The notes should explain what software testing is, why it is necessary, and what are the main objectives of software testing.
  - Actual result: The notes define software testing as the process of executing the software with the intention of finding and removing defects, and state that it is necessary to ensure the software's quality, functionality, and performance. The notes also mention the main objectives of software testing as follows:
    - Verification: To check whether the software conforms to the specified requirements and design.
    - Validation: To check whether the software meets the



# Testing Suite for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Software engineering is a branch of computer science that deals with the design, implementation, and maintenance of complex computer programs .
- Software engineers apply engineering principles and knowledge of programming languages to build software solutions for end users.
- Software engineering involves various activities, such as:
  - Requirements analysis: identifying and defining the needs and expectations of the stakeholders and the users of the software system.
  - Software design: creating a high-level blueprint of the software architecture, components, interfaces, and data structures.
  - Software development: writing, testing, debugging, and documenting the source code of the software system.
  - Software testing: verifying and validating the functionality, quality, performance, and reliability of the software system.
  - Software deployment: installing, configuring, and launching the software system in the target environment.
  - Software maintenance: updating, modifying, and fixing the software system to cope with changing requirements, errors, and new technologies.
- Software engineering follows various models, methods, and processes to guide and manage the software development life cycle, such as:
  - Waterfall model: a sequential and linear approach that divides the software development into distinct phases, such as requirements, design, implementation, testing, and maintenance.
  - Agile model: an iterative and incremental approach that emphasizes collaboration, feedback, and adaptation, and delivers working software in short cycles, called sprints.
  - Spiral model: a risk-driven and evolutionary approach that combines the features of the waterfall and agile models, and involves four phases: planning, risk analysis, engineering, and evaluation.
  - V-model: a verification and validation approach that maps each phase of the software development to a corresponding phase of testing, such as unit testing, integration testing, system testing, and acceptance testing.
- Software engineering faces various challenges, such as:
  - Complexity: software systems are often large, distributed, heterogeneous, and dynamic, and require sophisticated design and implementation techniques.
  - Quality: software systems must meet the functional and non-functional requirements of the stakeholders and the users, and adhere to the standards and best practices of software engineering.
  - Cost: software systems must be developed within the budget and time constraints of the project, and optimize the use of resources and tools.
  - Change: software systems must be adaptable and maintainable to cope with changing requirements, errors, and new technologies.



# Test for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Software engineering is a branch of computer science that deals with the design, implementation, and maintenance of complex computer programs .
- Software engineers apply engineering principles and knowledge of programming languages to build software solutions for end users.
- Software engineering is an engineering-style system of software development that involves the following activities:
  - Requirements analysis: defining the problem and the desired outcomes of the software
  - Design: creating a high-level plan of the software architecture and components
  - Implementation: writing the source code and testing the functionality of the software
  - Verification and validation: checking the quality and correctness of the software against the requirements and specifications
  - Deployment: delivering the software to the customers or users
  - Maintenance: fixing bugs, adding features, and updating the software as needed
- Software engineering is a dynamic and evolving field that requires continuous learning and adaptation to new technologies, tools, and methodologies.
- Software engineering is also a collaborative and interdisciplinary field that involves communication and coordination with other stakeholders, such as customers, users, managers, and other software engineers.



# Oracles

- An oracle is a mechanism for determining whether a test has passed or failed.
- An oracle compares the output of the system under test, for a given input, to the expected output.
- An oracle can be a human, a document, a program, or a combination of these.
- An oracle can be derived from various sources, such as specifications, requirements, domain knowledge, or previous versions of the system.
- An oracle can be complete, partial, or inconsistent, depending on how well it can determine the correctness of the system output.
- An oracle can be deterministic, probabilistic, or heuristic, depending on how it handles uncertainty and variability in the system output.
- An oracle can be explicit, implicit, or derived, depending on how it is defined and implemented.
- An oracle can be static, dynamic, or adaptive, depending on how it changes over time and across test cases.
- An oracle can be internal, external, or hybrid, depending on how it interacts with the system under test.
- An oracle can be exact, inexact, or approximate, depending on how it measures the difference between the actual and expected output.
- An oracle can be absolute, relative, or subjective, depending on how it compares the system output to a reference standard.
- An oracle can be oracle-based, test-based, or model-based, depending on how it is designed and constructed.
- An oracle can be formal, informal, or semi-formal, depending on how it is specified and verified.
- An oracle can be reusable, disposable, or configurable, depending on how it can be applied to different systems and contexts.
- An oracle can be efficient, effective, or optimal, depending on how it balances the trade-offs between cost, quality, and coverage.
- An oracle can be realistic, ideal, or hypothetical, depending on how it reflects the actual behavior and expectations of the system.

: Test oracle - Wikipedia (https://en.wikipedia.org/wiki/Test_Oracle)



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Impracticality of Testing All Data for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing.

# Impracticality of Testing All Data

- Testing all data means to execute a software system with every possible input and output combination.
- Testing all data is impractical because:
  - It is impossible to test all data for software systems that have infinite or very large input domains, such as web applications, databases, or operating systems.
  - It is time-consuming and costly to test all data for software systems that have finite but complex input domains, such as graphical user interfaces, embedded systems, or games.
  - It is unnecessary to test all data for software systems that have simple or redundant input domains, such as calculators, text editors, or converters.
- Testing all data is also ineffective because:
  - It does not guarantee the absence of faults or errors in the software system, as some faults may be triggered by specific sequences or states of inputs and outputs, not by individual values.
  - It does not ensure the quality or usability of the software system, as some quality attributes, such as reliability, performance, or security, depend on the context and environment of the software system, not on the input and output values.
  - It does not satisfy the needs or expectations of the users or stakeholders of the software system, as some user requirements, such as functionality, usability, or compatibility, may not be fully captured or specified by the input and output values.



# Impracticality of Testing All Paths

- Testing all paths of a software system is impractical because of the following reasons:
  - The number of paths in a software system can be very large, even infinite, depending on the complexity and the structure of the system. For example, a system with loops, recursion, or concurrency can have an unbounded number of paths.
  - The time and resources required to test all paths can be prohibitive, especially for large and complex systems. Testing all paths would require exhaustive input generation, execution, and verification, which can be costly and time-consuming.
  - The benefit of testing all paths can be marginal, as not all paths are equally important or likely to contain faults. Testing all paths would not guarantee the absence of faults, as some faults may be triggered by specific inputs, environmental conditions, or interactions with other systems. Testing all paths would also not guarantee the satisfaction of the user requirements, as some paths may be irrelevant or undesirable for the intended functionality and quality of the system.
- Therefore, testing all paths of a software system is impractical and not recommended. Instead, testing should focus on selecting and prioritizing the most relevant and critical paths, based on criteria such as coverage, risk, complexity, frequency, and user feedback. Testing should also employ techniques such as equivalence partitioning, boundary value analysis, and error guessing to reduce the number of test cases and increase their effectiveness.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Software Testing. Here is the verification for the notes of Unit 1 - Review of Software Engineering:

# Verification for the notes of Unit 1 - Review of Software Engineering

- The notes should cover the following topics:
  - The definition and objectives of software engineering
  - The software development life cycle (SDLC) and its phases
  - The software process models and their advantages and disadvantages
  - The software quality attributes and metrics
  - The software verification and validation techniques and their differences
  - The software testing levels and types
  - The software testing principles and strategies
  - The software testing standards and guidelines
- The notes should provide clear and concise explanations of the concepts and terms, with examples and diagrams where appropriate.
- The notes should highlight the key points and summarize the main ideas at the end of each topic.
- The notes should include relevant references and citations for further reading and research.
- The notes should be well-organized, formatted, and proofread for errors and typos.
- The notes should be consistent and coherent in style, tone, and terminology.



# Verification Methods

Verification methods are the techniques that are used to check that the software products and processes conform to the specified requirements and standards. Verification ensures that the software is built correctly and meets the expectations of the stakeholders. Verification is also known as static testing, as it does not involve executing the software.

Some common verification methods in software engineering are:

- **Peer reviews**: This method involves reviewing the software documents or code with a group of peers, looking for errors, inconsistencies, and improvements. Peer reviews can be informal or formal, depending on the level of rigor and documentation required. Peer reviews can help to detect defects early in the software development life cycle and improve the quality of the software products and processes.  

- **Walk-throughs**: This method is a formal and systematic type of peer review, where the author of the software document or code presents it to a group of reviewers, who ask questions and provide feedback. The purpose of walk-throughs is to ensure that the software document or code is clear, complete, and consistent, and that it meets the specified requirements and standards. Walk-throughs can also help to identify potential risks and issues that may arise in the software development or testing.  

- **Inspections**: This method is a more formal and rigorous type of peer review, where the software document or code is examined by a group of reviewers, who follow a predefined checklist and report the defects and issues they find. The purpose of inspections is to detect and eliminate defects and errors in the software document or code, and to ensure that it complies with the specified requirements and standards. Inspections can also help to improve the productivity and efficiency of the software development and testing processes.  

- **Analysis**: This method involves using mathematical or logical techniques to verify the correctness, completeness, and consistency of the software document or code. Analysis can be performed manually or with the help of tools, such as static analyzers, model checkers, or formal methods. The purpose of analysis is to prove or disprove the properties and behaviors of the software document or code, and to ensure that it satisfies the specified requirements and standards. Analysis can also help to reduce the complexity and ambiguity of the software document or code, and to improve its reliability and performance.  

- **Demonstration**: This method involves showing or illustrating the functionality, features, or capabilities of the software product or process to the stakeholders, such as customers, users, or managers. Demonstration can be performed with the help of prototypes, mock-ups, or simulations. The purpose of demonstration is to verify that the software product or process meets the expectations and needs of the stakeholders, and to obtain their feedback and approval. Demonstration can also help to increase the confidence and satisfaction of the stakeholders, and to facilitate the communication and collaboration among the software development and testing teams.  

- **Inspection**: This method involves checking or testing the physical or tangible aspects of the software product or process, such as the hardware, the user interface, the documentation, or the packaging. Inspection can be performed manually or with the help of tools, such as measuring devices, scanners, or cameras. The purpose of inspection is to verify that the software product or process conforms to the specified quality and safety standards, and to detect and correct any defects or errors. Inspection can also help to ensure the usability and accessibility of the software product or process, and to prevent any potential failures or hazards.



# SRS Verification for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- SRS stands for Software Requirements Specification, which is a document that describes the functional and non-functional requirements of a software system.
- SRS verification is the process of checking whether the SRS document is complete, consistent, correct, feasible, testable, and traceable.
- SRS verification can be done by various methods, such as:
  - Inspection: A formal review of the SRS document by a team of experts, who identify and report any defects or issues.
  - Walkthrough: An informal review of the SRS document by the stakeholders, who provide feedback and suggestions for improvement.
  - Prototyping: A technique of creating a mock-up or a simulation of the software system, based on the SRS document, to validate the requirements and get early feedback from the users.
  - Analysis: A technique of applying mathematical or logical tools to the SRS document, to verify its consistency, completeness, and correctness.
- SRS verification is important for ensuring the quality of the software system, as it helps to:
  - Avoid ambiguity, confusion, and misunderstanding of the requirements among the stakeholders.
  - Detect and eliminate any errors, inconsistencies, or gaps in the requirements at an early stage of the software development life cycle.
  - Reduce the cost and effort of rework, change requests, and defect fixing in the later stages of the software development life cycle.
  - Enhance the testability and traceability of the requirements, which facilitates the software testing and maintenance activities.



# Source Code Reviews

Source code reviews are a software quality assurance process in which software's source code is analyzed manually by a team or by using an automated code review tool. The motive is purely, to find bugs, resolve errors, and for most times, improving code quality.

Some of the benefits of source code reviews are:

- They help detect and fix logical errors, security vulnerabilities, and code smells at an early stage .
- They improve the code quality by enforcing coding standards, best practices, and design principles .
- They facilitate knowledge sharing and learning among developers, as they can review each other's code and provide feedback and suggestions .
- They increase the confidence and trust in the software product, as the code is verified by multiple reviewers and meets the requirements and expectations .

Some of the challenges of source code reviews are:

- They can be time-consuming and tedious, especially for large and complex code bases .
- They can introduce conflicts and disagreements among developers, if the feedback is not constructive, respectful, and consistent .
- They can be affected by human factors, such as bias, fatigue, and distraction, which can reduce the effectiveness and accuracy of the reviews .
- They can be difficult to implement and maintain, if there is no clear and agreed-upon process, tool, and criteria for the reviews .

To overcome these challenges, some of the best practices and techniques for source code reviews are:

- Define and document the code review process, including the roles, responsibilities, and expectations of the reviewers and the reviewees .
- Use a code review tool that supports collaboration, automation, and integration with other tools, such as version control, issue tracking, and testing .
- Follow a code review checklist that covers the main aspects of the code, such as functionality, readability, maintainability, security, and performance .
- Provide and receive feedback in a timely, polite, and constructive manner, and focus on the code, not the person .
- Track and resolve the issues and suggestions raised during the code review, and ensure that the code meets the quality standards and requirements .



# User Documentation Verification for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- User documentation verification is the process of checking the quality and accuracy of the user manuals, guides, tutorials, and other documents that are intended for the end-users of a software system.
- User documentation verification is important because it ensures that the user documentation is consistent, complete, correct, clear, and concise, and that it meets the user's needs and expectations.
- User documentation verification can be done by using various methods, such as:
  - Peer review: A peer review is a formal or informal evaluation of the user documentation by one or more experts in the same or related field. Peer review can help identify errors, omissions, ambiguities, and inconsistencies in the user documentation, and provide feedback and suggestions for improvement.
  - Inspection: An inspection is a systematic and structured examination of the user documentation by a team of reviewers, following a predefined checklist or set of criteria. Inspection can help detect defects, deviations, and non-conformities in the user documentation, and provide recommendations for correction and enhancement.
  - Testing: Testing is a process of verifying the user documentation by executing it on a sample of users, tasks, and scenarios. Testing can help evaluate the usability, effectiveness, efficiency, and satisfaction of the user documentation, and identify issues and problems that may affect the user's performance and experience.
  - Evaluation: An evaluation is a process of assessing the user documentation by measuring it against a set of standards, guidelines, or metrics. Evaluation can help determine the quality, value, and impact of the user documentation, and provide evidence and justification for decision making and improvement.

- User documentation verification should be done throughout the software development life cycle, from the planning and analysis phase to the maintenance and evolution phase. User documentation verification should be aligned with the software verification activities, and should involve the stakeholders, such as the developers, testers, users, and managers. User documentation verification should be documented and reported, and should follow the principles of continuous improvement and feedback.



# Software Project Audit

- A software project audit is a formal review of a software project to check its quality, progress or adherence to plans, standards and regulations.
- A software project audit is conducted by either internal teams or by one or more independent auditors .
- A software project audit aims to maximize the success of a project by detecting its potential risks and weaknesses.
- A software project audit also evaluates the performance of every single team member in the IT department.
- A software project audit may be conducted for many reasons, such as:
  - To verify the compliance of the software product, process, or set of processes with specifications, standards, contractual agreements, or other criteria.
  - To assess the quality and effectiveness of the software development process and its deliverables.
  - To identify the strengths and weaknesses of the software project and its management.
  - To provide recommendations for improvement and corrective actions.
  - To ensure the alignment of the software project with the business objectives and stakeholder expectations.
- A software project audit typically involves the following steps:
  - Planning the audit: defining the scope, objectives, criteria, and methodology of the audit.
  - Collecting the data: gathering the relevant information and evidence from the software project documents, artifacts, and stakeholders.
  - Analyzing the data: evaluating the data against the audit criteria and identifying the gaps, issues, and best practices.
  - Reporting the results: preparing and presenting the audit report that summarizes the findings, conclusions, and recommendations of the audit.
  - Following up the audit: monitoring and verifying the implementation of the audit recommendations and the resolution of the audit issues.



# Tailoring Software Quality Assurance Program by Reviews

- Software quality assurance (SQA) is the process of ensuring that a software program meets the quality goals and standards set by the stakeholders, such as functionality, reliability, usability, security, performance, etc.
- SQA involves various activities and techniques, such as planning, testing, inspection, review, audit, measurement, analysis, improvement, etc.
- Reviews are one of the most important and effective techniques for SQA, as they allow the identification and correction of defects and issues in the software artifacts (such as requirements, design, code, test cases, etc.) before they become costly and risky to fix.
- Reviews can be classified into different types, such as informal reviews, walkthroughs, technical reviews, inspections, etc., depending on the purpose, scope, format, participants, and outcome of the review process.
- Tailoring is the process of adapting and modifying a standard or generic process, method, or technique to suit the specific needs and characteristics of a particular project, organization, or domain.
- Tailoring SQA program by reviews means selecting and applying the most appropriate and effective review techniques for each software artifact, phase, and activity, based on the factors such as size, complexity, criticality, risk, maturity, etc. of the software project and organization.
- Tailoring SQA program by reviews can help to achieve the following benefits:
  - Improve the quality and reliability of the software products and processes by detecting and removing defects and issues early and efficiently.
  - Reduce the cost and time of software development and maintenance by avoiding rework, errors, failures, and delays.
  - Enhance the communication and collaboration among the software stakeholders by involving them in the review process and sharing feedback and suggestions.
  - Increase the customer satisfaction and confidence by delivering software products that meet or exceed their expectations and requirements.
  - Comply with the relevant standards and regulations by following the best practices and guidelines for SQA and reviews.



# Walkthrough for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

## Introduction

- Software engineering is the discipline of applying engineering principles and practices to the development, operation, and maintenance of software systems.
- Software testing is the process of verifying and validating that a software system meets the specified requirements and behaves as expected.
- Software testing is an essential part of software engineering, as it helps to ensure the quality, reliability, and security of software products.
- Software testing can be performed at different levels of abstraction, such as unit testing, integration testing, system testing, and acceptance testing.
- Software testing can also be classified into different types, such as functional testing, non-functional testing, structural testing, and behavioral testing.

## Software Development Life Cycle (SDLC)

- Software development life cycle (SDLC) is a framework that defines the phases and activities involved in the development of a software system.
- The main phases of SDLC are: planning, analysis, design, implementation, testing, deployment, and maintenance.
- Planning: This phase involves defining the scope, objectives, and feasibility of the software project, as well as identifying the stakeholders, risks, and constraints.
- Analysis: This phase involves gathering and analyzing the requirements of the software system, as well as modeling the system behavior and structure using various techniques, such as use cases, data flow diagrams, entity-relationship diagrams, etc.
- Design: This phase involves designing the architecture, components, interfaces, and data structures of the software system, as well as selecting the appropriate technologies, tools, and standards to be used.
- Implementation: This phase involves coding, debugging, and documenting the software system, as well as integrating the components and modules.
- Testing: This phase involves verifying and validating the software system against the requirements and specifications, as well as identifying and resolving the defects and errors.
- Deployment: This phase involves installing, configuring, and delivering the software system to the end users or customers, as well as providing training and support.
- Maintenance: This phase involves providing corrective, adaptive, perfective, and preventive maintenance to the software system, as well as monitoring and evaluating its performance and quality.

## Software Development Models

- Software development models are methodologies that describe how the software development process is organized and managed.
- There are various software development models, such as waterfall, incremental, iterative, agile, spiral, etc.
- Each model has its own advantages and disadvantages, and the choice of the model depends on the nature, size, complexity, and requirements of the software project.
- Waterfall model: This model follows a linear and sequential approach, where each phase of SDLC is completed before moving to the next phase. This model is simple, easy to follow, and suitable for well-defined and stable projects. However, this model is rigid, inflexible, and does not accommodate changes or feedback easily. It also requires a lot of documentation and testing at the end of the development cycle, which may delay the delivery and increase the cost and risk of the project.
- Incremental model: This model divides the software project into smaller and manageable increments, where each increment is developed and delivered separately. This model allows early delivery and feedback, as well as better risk management and quality assurance. However, this model requires careful planning and coordination, as well as a clear definition of the increments and their dependencies. It also may result in inconsistent and incompatible increments, as well as increased complexity and maintenance effort.
- Iterative model: This model follows a cyclic and repetitive approach, where the software system is developed and refined through multiple iterations. Each iteration consists of a mini SDLC, where the system is analyzed, designed, implemented, tested, and evaluated. This model allows flexibility and adaptability, as well as continuous improvement and learning. However, this model requires frequent communication and collaboration, as well as a clear vision and scope of the system. It also may result in over-engineering and rework, as well as increased cost and time of the project.
- Agile model: This model follows a dynamic and collaborative approach, where the software system is developed and delivered incrementally and iteratively, based on the changing needs and expectations of the customers and stakeholders. This model emphasizes on customer satisfaction, teamwork, feedback, and responsiveness, as well as simplicity, quality, and efficiency. However, this model requires a high level of commitment and discipline, as well as a skilled and experienced team. It also may result in lack of documentation and structure, as well as difficulty in scaling and integrating the system.
- Spiral model: This model combines the features of the waterfall and iterative models, where the software system is developed and refined through multiple loops or spirals. Each spiral consists of four phases: planning, risk analysis, engineering, and evaluation. This model allows a



# Inspection for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- Inspection is a formal and systematic technique for finding defects in software artifacts such as requirements, design, code, and test cases.
- Inspection involves a team of reviewers who follow a well-defined process to examine the artifact, identify defects, and suggest improvements.
- Inspection is also known as static testing, as it does not require executing the software or test cases.
- Inspection has several benefits, such as:
  - It can detect defects early in the software development life cycle, reducing the cost and effort of fixing them later.
  - It can improve the quality and reliability of the software product, as well as the productivity and morale of the developers.
  - It can provide feedback and learning opportunities for the developers, as well as the reviewers.
  - It can facilitate communication and coordination among the stakeholders, such as customers, developers, testers, and managers.
- Inspection has several challenges, such as:
  - It requires a significant amount of time and resources, especially for large and complex artifacts.
  - It depends on the skill and experience of the reviewers, as well as their motivation and attitude.
  - It may not detect all types of defects, such as performance, usability, or security issues.
  - It may introduce new defects or misunderstandings, if the reviewers are not careful or consistent.
- Inspection consists of several phases, such as:
  - Planning: The inspection leader selects the artifact to be inspected, the reviewers, the roles, the schedule, the checklist, and the entry and exit criteria.
  - Overview: The inspection leader provides an overview of the artifact and its context, and clarifies any doubts or questions from the reviewers.
  - Preparation: The reviewers individually study the artifact and identify potential defects, using the checklist and their own expertise.
  - Inspection meeting: The reviewers meet and discuss their findings, using a moderator to facilitate the discussion and a recorder to document the defects and suggestions.
  - Rework: The author of the artifact corrects the defects and implements the suggestions, using the inspection report as a guide.
  - Follow-up: The inspection leader verifies that the rework has been done correctly and that no new defects have been introduced, using the exit criteria as a measure.



# Configuration Audits

- Configuration audits are an essential process in ensuring the quality and reliability of a software product .
- Configuration audits provide an independent evaluation of the system's functionality, performance, and consistency with the relevant requirement specifications.
- Configuration audits also verify that the software configuration items (CIs) have been developed and completed in accordance with the documents and requirements that define them .
- Configuration audits are part of the configuration management process, which is a systems engineering process that tracks and monitors changes to a software system's configuration metadata.
- Configuration audits are performed for all releases of a software product; however, audits of interim, internal releases may be less formal and rigorous, as defined by the project.
- There are two types of configuration audits: the Functional Configuration Audit (FCA) and the Physical Configuration Audit (PCA).
  - The FCA verifies that the software product meets the functional and performance requirements specified in the software requirements specification (SRS).
  - The PCA verifies that the software product conforms to the physical and technical characteristics specified in the software design description (SDD).
- Configuration audits are conducted by an independent team of auditors, who review the software product, the configuration documentation, and the configuration management records.
- Configuration audits are usually performed at the end of each software development phase, such as design, coding, testing, and integration.
- Configuration audits help to identify and resolve any discrepancies, errors, or defects in the software product and the configuration documentation.
- Configuration audits also help to ensure that the software product is ready for delivery, deployment, and operation.



## Unit 2 - Functional Testing

- Functional testing is a type of software testing that verifies that the software performs as expected according to the requirements or specifications.
- Functional testing involves testing the functionality of the software at various levels, such as unit, integration, system, and acceptance testing.
- Functional testing can be performed manually or with the help of automated tools.
- Functional testing can be classified into different types, such as black-box testing, white-box testing, and gray-box testing, depending on the level of knowledge of the internal structure and logic of the software.
- Black-box testing is a type of functional testing that focuses on the input and output of the software, without considering the internal implementation details. Black-box testing techniques include equivalence partitioning, boundary value analysis, decision table testing, state transition testing, use case testing, etc.
- White-box testing is a type of functional testing that examines the internal structure and logic of the software, such as the code, branches, loops, conditions, etc. White-box testing techniques include statement coverage, branch coverage, path coverage, condition coverage, etc.
- Gray-box testing is a type of functional testing that combines both black-box and white-box testing approaches, using partial knowledge of the internal structure and logic of the software. Gray-box testing techniques include error guessing, exploratory testing, etc.
- Functional testing aims to ensure that the software meets the functional requirements and expectations of the users and stakeholders, and that it is free of defects and errors that may affect its functionality.



# Boundary Value Analysis for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

- Boundary value analysis (BVA) is a software testing technique in which tests are designed to include representatives of boundary values in a range.
- Boundary values are the values at the edges or limits of an equivalence class, such as the minimum, maximum, or just inside or outside the boundaries.
- The idea behind BVA is that the behavior of the software is more likely to be incorrect at the boundaries than within the equivalence classes.
- BVA can help to find errors and bugs that may occur due to incorrect handling of boundary conditions, such as off-by-one errors, overflow errors, or boundary violations.
- BVA can be applied to both input and output values of the software, as well as internal values such as loop counters, array indices, or flags.
- BVA can be used in combination with equivalence partitioning (EP) to test the boundaries between the equivalence classes.
- BVA can be performed using the following steps:
  - Identify the equivalence classes and their boundaries for the input and output values of the software.
  - Select test cases that cover the minimum and maximum values of each equivalence class, as well as values just above and below the boundaries.
  - Execute the test cases and verify the expected results.
  - Repeat the process for internal values if applicable.
- BVA can be illustrated using the following example:
  - Suppose the software accepts an integer input between 1 and 1000, and outputs the square of the input.
  - The equivalence classes and their boundaries are:
    - Valid class: 1 to 1000, with boundaries 1 and 1000.
    - Invalid class: less than 1 or greater than 1000, with boundaries 0 and 1001.
  - The test cases using BVA are:
    - Test case 1: input = 1, output = 1 (minimum valid value).
    - Test case 2: input = 1000, output = 1000000 (maximum valid value).
    - Test case 3: input = 0, output = error message (minimum invalid value).
    - Test case 4: input = 1001, output = error message (maximum invalid value).
    - Test case 5: input = 2, output = 4 (just above the minimum valid value).
    - Test case 6: input = 999, output = 998001 (just below the maximum valid value).
    - Test case 7: input = -1, output = error message (just below the minimum invalid value).
    - Test case 8: input = 1002, output = error message (just above the maximum invalid value).
- BVA can help to improve the quality and coverage of software testing by focusing on the most critical and error-prone areas of the software.



# Equivalence Class Testing

Equivalence class testing is a black box testing technique that divides the input domain of a system into classes of data that are expected to behave similarly. The main idea is to select one representative value from each class as a test case, instead of testing all possible values. This reduces the number of test cases and increases the test coverage.

## Advantages of Equivalence Class Testing

- It helps to identify the optimal number of test cases that cover all the possible scenarios.
- It avoids redundant and unnecessary test cases that do not add value to the testing process.
- It saves time and resources by focusing on the most relevant and critical test cases.

## Steps to Perform Equivalence Class Testing

- Analyze the system requirements and specifications to identify the input parameters and output results.
- Partition the input domain into valid and invalid equivalence classes based on the expected behavior and functionality of the system.
- Select one representative value from each equivalence class as a test case.
- Execute the test cases and verify the output results with the expected results.
- Report any defects or discrepancies found during the testing process.

## Example of Equivalence Class Testing

Consider a system that accepts a user name and a password as input and validates them against a database. The system requirements are as follows:

- The user name should be a valid email address.
- The password should be between 8 and 16 characters long and should contain at least one uppercase letter, one lowercase letter, one digit, and one special character.
- The system should display a message indicating whether the login is successful or not.

The input domain can be partitioned into the following equivalence classes:

- Valid user name and valid password (valid class)
- Valid user name and invalid password (invalid class)
- Invalid user name and valid password (invalid class)
- Invalid user name and invalid password (invalid class)

The test cases can be selected as follows:

- Test case 1: user name = sydney@bing.com, password = Sydney@123 (valid class)
- Test case 2: user name = sydney@bing.com, password = sydney (invalid class)
- Test case 3: user name = sydney, password = Sydney@123 (invalid class)
- Test case 4: user name = sydney, password = sydney (invalid class)

The expected results are as follows:

- Test case 1: The system should display a message "Login successful".
- Test case 2: The system should display a message "Invalid password".
- Test case 3: The system should display a message "Invalid user name".
- Test case 4: The system should display a message "Invalid user name and password".



# Decision Table Based Testing

- Decision table based testing is a software testing technique used to test system behavior for different input combinations  .
- It is a systematic approach where the different input combinations and their corresponding system behavior (output) are captured in a tabular form.
- It is also called a cause-effect table, as it shows the causes (conditions) and effects (actions) of the system.
- It is useful for testing complex business logic that involves multiple conditions and resulting actions  .

## Advantages of Decision Table Based Testing

- It helps to cover all possible scenarios and avoid missing any test cases  .
- It simplifies the test design and execution process by using a concise and clear format  .
- It facilitates communication and collaboration among developers, testers, and business analysts, as they can easily understand and verify the logic and requirements  .
- It reduces the maintenance effort by allowing easy updates and modifications to the table  .

## Scope of Decision Table Based Testing

- Decision table based testing is applicable for testing any system that has a finite number of inputs and outputs, and a well-defined set of rules or conditions that govern the system behavior   .
- Some examples of such systems are:

  - Banking systems that have different interest rates and fees based on customer type, account type, balance, etc.
  - E-commerce systems that have different discounts and offers based on product category, quantity, payment method, etc.
  - Insurance systems that have different premiums and benefits based on policy type, age, health, etc.
  - Login systems that have different access levels and permissions based on user role, password, etc.

## How to Create a Decision Table for Testing?

- The steps to create a decision table for testing are   :

  - Identify the input conditions and output actions of the system under test.
  - List all the possible values or states for each input condition and output action.
  - Determine the number of columns (test cases) required for the table by calculating the product of the number of values for each input condition.
  - Assign a unique identifier to each column (test case) and label each row with the input condition or output action name.
  - Fill the table with the appropriate values or states for each input condition and output action for each test case.
  - Simplify the table by eliminating any duplicate or redundant test cases, or by using wildcards (*) to represent any value or state.
  - Review and verify the table for accuracy and completeness.

## Example of a Decision Table for Testing

- Consider a login system that has the following input conditions and output actions:

  - Input conditions:
    - Username: valid or invalid
    - Password: valid or invalid
  - Output actions:
    - Login: success or failure
    - Error message: displayed or not displayed

- A decision table for testing this system can be created as follows:

| Test Case | Username | Password | Login | Error Message |
| --------- | -------- | -------- | ----- | ------------- |
| TC1       | Valid    | Valid    | Success | Not Displayed |
| TC2       | Valid    | Invalid  | Failure | Displayed     |
| TC3       | Invalid  | Valid    | Failure | Displayed     |
| TC4       | Invalid  | Invalid  | Failure | Displayed     |

- This table can be simplified by using a wildcard (*) to represent any value for the password input condition, as the system behavior is the same for any invalid password:

| Test Case | Username | Password | Login | Error Message |
| --------- | -------- | -------- | ----- | ------------- |
| TC1       | Valid    | Valid    | Success | Not Displayed |
| TC2       | Valid    | *        | Failure | Displayed     |
| TC3       | Invalid  | *        | Failure | Displayed     |



# Cause Effect Graphing Technique

- Cause Effect Graphing Technique is a black box testing technique that illustrates the relationship between a outcome and the factors influencing the outcome graphically  .
- It is also known as Ishikawa diagram or fish bone diagram.
- It is generally used for hardware testing but now adapted to software testing, usually tests external behavior of a system.
- It starts with a set of requirements and determines the minimum possible test cases for maximum test coverage which reduces test execution time and cost.
- It involves the following steps  :
  - Identify the causes (input conditions) and effects (output conditions) for the system under test.
  - Draw a cause-effect graph that shows the logical relationships between the causes and effects using symbols such as AND, OR, NOT, etc.
  - Assign a unique identifier to each cause and effect.
  - Convert the cause-effect graph into a decision table that lists all possible combinations of causes and effects.
  - Simplify the decision table by eliminating redundant or invalid combinations.
  - Generate test cases from the decision table by selecting one test case for each column of the table.
- An example of cause-effect graphing technique for the triangle problem is shown below:

Cause-effect graph for triangle problem

- The corresponding decision table and test cases are shown below:

Decision table for triangle problem

Test cases for triangle problem

- The advantages of cause-effect graphing technique are :
  - It helps to identify the root causes of a problem and the possible solutions.
  - It helps to reduce the number of test cases by eliminating redundant or invalid combinations.
  - It helps to ensure the completeness and consistency of the requirements.
  - It helps to improve the communication and collaboration among the stakeholders.
- The disadvantages of cause-effect graphing technique are :
  - It may be difficult to draw the cause-effect graph for complex systems with many causes and effects.
  - It may be time-consuming and tedious to convert the cause-effect graph into a decision table and test cases.
  - It may not be able to handle the dynamic behavior of the system or the dependencies among the causes and effects.



## Unit 3 - Structural Testing

- Structural testing is a type of software testing that focuses on the internal structure, design, and implementation of the software system or component.
- Structural testing is also known as white-box testing, glass-box testing, or logic-driven testing, as it requires knowledge of the source code, control flow, data flow, and logic of the software under test.
- The main objectives of structural testing are to verify the quality of the code, to measure the code coverage, to identify and eliminate dead or redundant code, and to detect and correct errors or defects in the code.
- Structural testing can be applied at different levels of testing, such as unit testing, integration testing, system testing, and regression testing.
- Structural testing can be performed using various techniques, such as statement coverage, branch coverage, condition coverage, path coverage, data flow testing, and mutation testing.
- Statement coverage is a technique that measures the percentage of executable statements in the code that are executed by the test cases.
- Branch coverage is a technique that measures the percentage of branches or decision points in the code that are executed by the test cases.
- Condition coverage is a technique that measures the percentage of logical conditions in the code that are evaluated to both true and false by the test cases.
- Path coverage is a technique that measures the percentage of paths or sequences of statements and branches in the code that are executed by the test cases.
- Data flow testing is a technique that analyzes the flow of data values through the variables, parameters, and return values of the code, and designs test cases to cover the defined or used data values.
- Mutation testing is a technique that generates and executes variants or mutants of the code by introducing small changes or faults, and compares the outputs of the original and mutated code to evaluate the effectiveness of the test cases.



# Control Flow Testing

Control flow testing is a type of software testing that uses the program's control flow as a model. Control flow testing is a structural testing strategy that comes under white box testing. Control flow testing is used to develop test cases of a program, where the tester selects a large portion of the program to test and to set the testing path.

## Objectives of Control Flow Testing

- To identify the execution paths through a module of program code and then create and execute test cases to cover those paths.
- To detect errors in the logic and structure of the program, such as missing or incorrect branches, loops, conditions, etc.
- To measure the coverage of the test cases based on the number of paths, branches, statements, or conditions executed.

## Steps of Control Flow Testing

- Draw a control flow graph (CFG) of the program, which is a graphical representation of the program's structure and logic. A CFG consists of nodes and edges, where nodes represent basic blocks of code and edges represent the flow of control between them.
- Identify the independent paths in the CFG, which are paths that do not share any node or edge with other paths. Independent paths can be found using techniques such as cyclomatic complexity, basis path testing, or path sensitizing.
- Design test cases for each independent path, using input values and expected outputs that exercise the path. Test cases can be derived using techniques such as boundary value analysis, equivalence partitioning, or error guessing.
- Execute the test cases and compare the actual outputs with the expected outputs. Report any discrepancies or failures as defects.
- Calculate the coverage of the test cases based on the number of paths, branches, statements, or conditions executed. Coverage can be measured using metrics such as path coverage, branch coverage, statement coverage, or condition coverage.

## Advantages of Control Flow Testing

- It detects almost half of the defects that are determined during the unit testing. It also determines almost one-third of the defects of the whole program.
- It can be performed manually or automated as the control flow graph that is used can be made by hand or by tools.
- It helps to improve the quality and reliability of the software by ensuring that all the possible paths and scenarios are tested.
- It helps to identify the dead code or unreachable code that can be removed or optimized.

## Disadvantages of Control Flow Testing

- It can be time-consuming and complex to draw the control flow graph and identify the independent paths for large and complex programs.
- It can be difficult to design test cases that cover all the paths, especially if there are many conditional statements or loops in the program.
- It can be costly and impractical to achieve 100% coverage, as some paths may be rarely or never executed in real scenarios.
- It does not test the functionality or the data flow of the program, only the structure and logic. It may miss some errors that are related to the input or output data or the specifications of the program.



# Path Testing

Path testing is a white-box testing method that involves using the source code of a program in order to find every possible executable path. It helps to determine all faults lying within a piece of code .

## Path Testing Techniques

- **Control Flow Graph**: The program is converted into a control flow graph by representing the code into nodes and edges. Nodes represent statements or blocks of code, and edges represent the flow of control between them. The control flow graph can be used to identify the different paths that can be executed in the program .
- **Cyclomatic Complexity**: Cyclomatic complexity is a metric that measures the number of linearly independent paths in a program. It can be calculated using the formula: `V(G) = E - N + 2`, where `E` is the number of edges, `N` is the number of nodes, and `V(G)` is the cyclomatic complexity of the graph `G`. Cyclomatic complexity can be used to determine the minimum number of test cases required to cover all the paths in the program .
- **Basis Path Testing**: Basis path testing is a technique that uses the cyclomatic complexity to find a basis set of paths that can cover all the paths in the program. A basis set is a set of paths that are linearly independent, meaning that no path can be constructed by combining other paths in the set. Basis path testing involves the following steps :
  - Draw a control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Find a basis set of paths by using a set of rules, such as:
    - Start from the entry node and follow any edge until reaching the exit node or a node that has already been visited.
    - If a node has already been visited, backtrack to the previous node and follow a different edge.
    - Repeat until all the edges have been traversed at least once.
  - Generate test cases to exercise each path in the basis set.



# Independent Paths

- Independent paths are paths through a program's control flow graph that cannot be reproduced by combining other paths .
- Independent paths are important for path testing, a structural testing method that aims to cover all possible executable paths in a program .
- Path testing can help to find faults in the logic and design of a program, and reduce redundant tests .
- To find the independent paths, we can use the cyclomatic complexity, which is a measure of the number of linearly independent paths in a program .
- Cyclomatic complexity can be calculated by using the formula: V(G) = E - N + 2, where E is the number of edges, N is the number of nodes, and V(G) is the cyclomatic complexity of the graph G .
- Alternatively, we can use the formula: V(G) = P + 1, where P is the number of predicate nodes, which are nodes that contain a condition .
- Once we have the cyclomatic complexity, we can generate test cases for each independent path by using the following steps :
  - Draw the control flow graph of the program.
  - Calculate the cyclomatic complexity of the graph.
  - Identify the basis set of independent paths, which is a set of paths that covers all the edges and nodes of the graph.
  - Derive test cases that can execute each path in the basis set.
  - Run the test cases and check the results.



# Generation of Graph from Program

- A graph is a mathematical structure that represents the relationships between a set of objects, called nodes or vertices, and a set of pairs of objects, called edges or arcs.
- A graph can be used to model the control flow of a program, which is the sequence of execution of statements and branches based on conditions and loops.
- A control flow graph (CFG) is a type of graph that shows the possible paths of execution of a program, where each node represents a basic block (a sequence of statements that are always executed together) and each edge represents a transfer of control between basic blocks.
- A CFG can be derived from the source code of a program by identifying the entry and exit points, the basic blocks, and the control flow edges between them.
- A CFG can be used for various purposes in software testing, such as measuring the complexity of a program, generating test cases, and evaluating the coverage of test cases.
- One way to measure the complexity of a program is to use the cyclomatic complexity, which is a metric that counts the number of linearly independent paths in a CFG. The cyclomatic complexity can be calculated by using the formula:

  - `V(G) = E - N + 2`, where `V(G)` is the cyclomatic complexity, `E` is the number of edges, and `N` is the number of nodes in the CFG.
  - `V(G) = P + 1`, where `P` is the number of predicate nodes (nodes that have more than one outgoing edge) in the CFG.
- One way to generate test cases for a program is to use the path testing method, which aims to cover all the possible paths of execution in a CFG. The path testing method involves the following steps:

  - Construct the CFG of the program from the source code.
  - Calculate the cyclomatic complexity of the CFG.
  - Identify a set of linearly independent paths in the CFG that covers all the edges. The number of paths should be equal to the cyclomatic complexity.
  - Generate test cases for each path by using techniques such as random testing or symbolic testing.
- One way to evaluate the coverage of test cases for a program is to use the branch coverage criterion, which measures the percentage of edges in the CFG that are executed by the test cases. The branch coverage criterion can be defined as:

  - `BC = (Ee / E) * 100`, where `BC` is the branch coverage, `Ee` is the number of edges executed by the test cases, and `E` is the total number of edges in the CFG.
  - The branch coverage criterion can be improved by using different definitions of branch covering, such as decision coverage, condition coverage, or multiple condition coverage, which consider the outcomes of the predicate nodes in the CFG.
- A decision graph is a type of graph that represents the logical expressions of the predicate nodes in a CFG, where each node represents a condition or a decision, and each edge represents a logical operator or a branch. A decision graph can be used to compare and clarify different definitions of branch covering in software testing.



# Identification of Independent Paths for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Path testing is a method of testing the logic of a program by designing test cases that cover all possible paths of execution.
- Independent paths are paths that have at least one edge (or statement) that is not shared by any other path.
- Independent paths are important because they help to ensure that every statement and branch of the program is executed at least once, and that no redundant tests are performed.
- To identify independent paths, the following steps are usually followed:
  - Draw a control flow graph (CFG) of the program, which is a graphical representation of the program's structure, showing the nodes (or blocks) and edges (or transitions) between them.
  - Calculate the cyclomatic complexity (CC) of the CFG, which is a measure of the number of linearly independent paths in the graph. CC can be computed using one of these formulas:
    - CC = E - N + 2, where E is the number of edges and N is the number of nodes in the graph.
    - CC = R + 1, where R is the number of regions (or enclosed areas) in the graph.
    - CC = D + 1, where D is the number of decision points (or nodes with more than one outgoing edge) in the graph.
  - Select a basis set of paths, which is a set of independent paths that covers all the edges in the graph. The number of paths in the basis set should be equal to the CC of the graph. One way to select a basis set is to start from the entry node and follow each possible branch until reaching the exit node, and then repeat the process for each decision point until all the edges are covered.
  - Derive test cases for each path in the basis set, using appropriate input values and expected outputs. The test cases should exercise the logic of the program and reveal any errors or defects in the code.



# Cyclomatic Complexity

Cyclomatic complexity is a software metric that measures the number of independent paths in a program's source code. It is useful for evaluating the complexity and quality of a program, as well as for planning and executing structural testing.

## Types of Cyclomatic Complexity

There are two types of cyclomatic complexity: essential and actual.

- Essential cyclomatic complexity is the minimum number of paths that are necessary to test the logic of a program. It is calculated by removing all the edges and nodes that do not affect the logic of the program, such as error handling and exception handling.
- Actual cyclomatic complexity is the total number of paths that exist in a program. It is calculated by counting the number of edges and nodes in the control flow graph of the program.

## Tools Used for Cyclomatic Complexity

There are various tools that can be used to calculate and visualize the cyclomatic complexity of a program, such as:

- Visual Studio: It provides a code metrics feature that can calculate the cyclomatic complexity of a program and display it in a table or a graph. It can also highlight the code regions that have high complexity and suggest ways to refactor them.
- SonarQube: It is an open-source platform that can perform static code analysis and measure the cyclomatic complexity of a program. It can also provide other quality metrics, such as code coverage, code smells, bugs, and vulnerabilities.
- Lizard: It is a command-line tool that can measure the cyclomatic complexity of various programming languages, such as C, C++, Java, Python, and Ruby. It can also generate reports in XML, CSV, or HTML formats.

## Advantages of Cyclomatic Complexity

Some of the advantages of using cyclomatic complexity are:

- It can help to identify the areas of the program that are more prone to errors and defects, and thus require more testing and debugging.
- It can help to improve the code quality and readability by suggesting ways to simplify the logic and reduce the number of decision points.
- It can help to estimate the testing effort and resources needed to cover all the possible paths in the program.
- It can help to evaluate the risk and maintainability of the program by indicating the level of complexity and coupling.



# Data Flow Testing

Data flow testing is a type of structural testing that focuses on the data variables and their values in a program. It is a white-box testing technique that examines the data flow with respect to the variables used in the code. It examines the initialization of variables and checks their values at each instance. It also checks the paths of the program according to the locations of definitions and uses of variables in the code  .

Some of the benefits of data flow testing are:

- It can detect errors related to the use of uninitialized variables, dead code, and redundant computations.
- It can improve the test coverage and the quality of the code.
- It can help in debugging and maintenance of the code.

Some of the challenges of data flow testing are:

- It can be complex and time-consuming to identify all the data flow paths and variables in a large program.
- It can be difficult to generate test cases that cover all the data flow paths and variables.
- It can be dependent on the programming language and the compiler used for the code.

Some of the strategies of data flow testing are:

- All-Defs: This strategy requires that every definition of a variable is covered by at least one test case.
- All-Uses: This strategy requires that every use of a variable is covered by at least one test case.
- All-DU-Paths: This strategy requires that every definition-use pair of a variable is covered by at least one test case along a feasible path.
- All-C-Uses: This strategy requires that every computational use of a variable is covered by at least one test case.
- All-P-Uses: This strategy requires that every predicate use of a variable is covered by at least one test case.

Some of the tools that can be used for data flow testing are:

- Data Flow Analyzer: This tool can generate a control flow graph and a data flow graph for a given program and identify the data flow paths and variables.
- Data Flow Coverage: This tool can measure the data flow coverage of a given test suite and report the missing data flow paths and variables.
- Data Flow Test Generator: This tool can generate test cases that cover the data flow paths and variables of a given program.



# Mutation Testing

Mutation testing is a form of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes. Changes introduced to the software are intended to cause errors in the program. Mutation testing is used to design new software tests and evaluate the quality of existing software tests. Mutation testing is typically used to conduct unit tests.

The steps to execute mutation testing are :

- Faults are introduced into the source code of the program by creating many versions called mutants. Each mutant has a single change in the code, such as replacing an operator, changing a variable name, or deleting a statement.
- Test cases are applied to the original program and also to the mutant program. A test case is said to kill a mutant if it causes the mutant to produce a different output from the original program. A test case is said to pass a mutant if it causes the mutant to produce the same output as the original program.
- The mutation score is calculated as the ratio of the number of killed mutants to the total number of mutants. The mutation score indicates how effective the test suite is at detecting faults in the program. A high mutation score means that the test suite is able to find most of the mutants, while a low mutation score means that the test suite is missing many mutants.

The benefits of mutation testing are:

- It helps to improve the quality and coverage of the test suite by revealing the weaknesses and gaps in the test cases.
- It helps to measure the fault detection capability of the test suite by providing a quantitative metric (mutation score).
- It helps to identify the redundant or equivalent mutants that do not affect the program behavior and can be removed from the testing process.

The challenges of mutation testing are:

- It is computationally expensive and time-consuming to generate and execute a large number of mutants for a complex program.
- It is difficult to determine the correctness of the mutants and the test cases, especially when the program specification is ambiguous or incomplete.
- It is hard to automate the mutation testing process and integrate it with the software development lifecycle.



## Unit 4 - Regression Testing

- Regression testing is the process of retesting a software system after changes have been made to ensure that the changes have not introduced new defects or affected the existing functionality.
- Regression testing can be performed at different levels of testing, such as unit, integration, system, or acceptance testing.
- Regression testing can be done manually or automatically, depending on the availability of test cases, test tools, and resources.
- Regression testing can be classified into three types: retest all, selective, and test suite minimization.
  - Retest all is the simplest approach, where all the existing test cases are executed again after any change in the software. This ensures complete coverage, but it is also time-consuming and expensive.
  - Selective is the most common approach, where only a subset of the existing test cases are executed based on some criteria, such as the impact of the change, the risk of the functionality, or the history of the defects. This reduces the testing effort, but it also requires a good selection strategy and traceability between test cases and requirements.
  - Test suite minimization is the most advanced approach, where the existing test cases are analyzed and reduced to a minimum set that still covers all the functionalities and requirements. This optimizes the testing effort, but it also requires sophisticated techniques and tools to perform the analysis and minimization.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You asked me to write the content in markdown format on the topic of regression testing for the notes of the unit 4 - regression testing in the subject of software testing. Here is what I have written:

# Regression Testing

- Regression testing is the process of retesting a software system after making changes to it, such as adding new features, fixing bugs, or modifying existing functionality.
- The purpose of regression testing is to ensure that the changes have not introduced any new defects or broken any existing functionality in the system.
- Regression testing can be done at different levels of testing, such as unit testing, integration testing, system testing, or acceptance testing, depending on the scope and impact of the changes.
- Regression testing can be performed manually or automatically, using tools and frameworks that can execute test cases and compare the expected and actual results.
- Regression testing can be classified into different types, such as:

  - Retest all: This type of regression testing involves re-executing all the test cases in the test suite, regardless of whether they are affected by the changes or not. This type of regression testing is comprehensive, but also time-consuming and expensive.
  - Selective: This type of regression testing involves selecting and re-executing only the test cases that are relevant to the changes made in the system. This type of regression testing is efficient, but also requires a good test case selection strategy and criteria.
  - Prioritized: This type of regression testing involves prioritizing the test cases based on some factors, such as risk, impact, frequency, or complexity, and re-executing them in a certain order. This type of regression testing is effective, but also requires a good test case prioritization strategy and criteria.
  - Hybrid: This type of regression testing involves combining different types of regression testing, such as retest all, selective, and prioritized, to achieve a balance between coverage and cost. This type of regression testing is flexible, but also requires a good test case management and execution strategy.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the content in markdown format on the topic of regression test cases selection for the notes of the unit 4 - regression testing in the subject of software testing. Here is the content I have generated:

# Regression Test Cases Selection

Regression testing is the process of retesting the modified parts of a software system and ensuring that no new defects have been introduced due to the changes. Regression testing can be done at different levels of testing, such as unit testing, integration testing, system testing, and acceptance testing.

Regression test cases are the test cases that are executed during regression testing. Regression test cases can be selected from the existing test suite or newly designed for the modified parts of the software. The selection of regression test cases depends on various factors, such as:

- The scope and extent of the changes made to the software
- The criticality and complexity of the modified parts of the software
- The availability and cost of the test resources, such as time, personnel, and tools
- The coverage and effectiveness of the existing test suite
- The risk and impact of potential defects in the modified parts of the software

There are different techniques and strategies for selecting regression test cases, such as:

- Retest all: This technique involves re-executing all the test cases in the existing test suite, regardless of the changes made to the software. This technique ensures maximum coverage and effectiveness, but it is also very costly and time-consuming.
- Retest modified: This technique involves re-executing only the test cases that are directly affected by the changes made to the software. This technique reduces the cost and time of regression testing, but it may miss some defects that are indirectly affected by the changes.
- Retest modified and related: This technique involves re-executing the test cases that are directly or indirectly affected by the changes made to the software. This technique considers the dependencies and interactions among the software components and ensures better coverage and effectiveness than the retest modified technique, but it is also more costly and time-consuming than the retest modified technique.
- Prioritize test cases: This technique involves ranking the test cases in the existing test suite according to some criteria, such as the frequency of execution, the severity of defects, the complexity of the software, the risk of failure, etc. and selecting the test cases with higher priority for regression testing. This technique optimizes the cost and time of regression testing, but it may compromise the coverage and effectiveness of the test suite.
- Minimize test cases: This technique involves reducing the size of the existing test suite by eliminating the redundant or obsolete test cases and selecting the test cases that provide the maximum coverage and effectiveness for regression testing. This technique also optimizes the cost and time of regression testing, but it requires a thorough analysis and evaluation of the test suite.

The selection of regression test cases is an important and challenging task in software testing. It requires a balance between the cost and time of regression testing and the coverage and effectiveness of the test suite. The selection of regression test cases should be based on the objectives and requirements of the software project and the characteristics and constraints of the software system.



# Reducing the number of test cases for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is the process of retesting the modified or updated software to ensure that it still meets the specified requirements and does not introduce any new defects.
- Regression testing is considered to be the most expensive phase in software testing, as it requires running a large number of test cases repeatedly.
- Test case reduction is the technique of eliminating or minimizing the redundant or unnecessary test cases from the regression test suite, while preserving the fault detection capability and coverage criteria  .
- Test case reduction can save time, cost, and resources in regression testing, and improve the efficiency and effectiveness of the testing process  .
- Test case reduction can be performed manually or with the help of automated tools.
- Some of the common techniques for test case reduction are  :
  - Requirement-based: This technique selects the test cases that satisfy the testing requirements with the minimum number of test cases. It can be done by mapping the test cases to the requirements and eliminating the test cases that do not cover any requirement or cover the same requirement as another test case.
  - Coverage-based: This technique selects the test cases that ensure the maximum coverage of the code, functionality, or features with the minimum number of test cases. It can be done by measuring the coverage of each test case and eliminating the test cases that do not contribute to the coverage or have overlapping coverage with another test case.
  - Genetic algorithm: This technique uses a population-based search method that mimics the natural evolution process to find the optimal test case subset. It can be done by encoding the test cases as chromosomes, assigning fitness values based on the coverage and fault detection criteria, and applying genetic operators such as selection, crossover, and mutation to generate new test case subsets until a termination condition is met.
  - Case-based reasoning: This technique uses a memory-based approach that searches for the most similar problems and solutions to the current problem. It can be done by classifying the test cases into three categories: case, auxiliary, and pivotal. Case test cases are the ones that are most relevant to the current problem and are retained in the test suite. Auxiliary test cases are the ones that are less relevant to the current problem and are removed from the test suite. Pivotal test cases are the ones that are critical for the fault detection and are retained in the test suite.
- The effectiveness of the test case reduction technique can be evaluated by comparing the original and reduced test suites in terms of the following metrics  :
  - Reduction rate: The percentage of test cases that are eliminated from the original test suite.
  - Fault detection rate: The percentage of faults that are detected by the reduced test suite.
  - Coverage rate: The percentage of code, functionality, or features that are covered by the reduced test suite.
  - Execution time: The time required to run the reduced test suite.
  - Cost: The resources required to perform the test case reduction and execute the reduced test suite.



# Code coverage prioritization technique

- Code coverage prioritization technique is a method of ordering test cases based on their ability to cover the code under test.
- The goal of this technique is to maximize the testing coverage with the least cost and effort.
- Code coverage prioritization technique can be applied at different levels of granularity, such as statement, branch, function, or module.
- Code coverage prioritization technique can be classified into two categories: total coverage and additional coverage.
  - Total coverage prioritization orders test cases based on the total number of code elements covered by each test case. For example, a test case that covers 10 statements will be given higher priority than a test case that covers 5 statements.
  - Additional coverage prioritization orders test cases based on the additional number of code elements covered by each test case that are not covered by the previous test cases. For example, a test case that covers 3 new statements will be given higher priority than a test case that covers 2 new statements.
- Code coverage prioritization technique can be useful for regression testing, which is the process of retesting the modified software to ensure that no new defects are introduced and the existing functionality is preserved.
- Code coverage prioritization technique can help to select the most relevant and effective test cases for regression testing, and to reduce the testing time and resources.
- Code coverage prioritization technique can also help to identify the code elements that are not covered by any test case, and to improve the test suite quality and completeness.



# Reducing the number of test cases for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is the process of retesting a software system after changes have been made to ensure that the changes have not introduced new faults or adversely affected the existing functionality.
- Regression testing can be costly and time-consuming, especially for large and complex systems that undergo frequent changes.
- Therefore, it is desirable to reduce the number of test cases that need to be executed for regression testing, while still maintaining a high level of test coverage and fault detection effectiveness.
- Some of the techniques for reducing the number of test cases for regression testing are:

  - Test case prioritization: This technique involves ranking the test cases according to some criteria, such as their likelihood of revealing faults, their importance for the system requirements, their execution time, or their historical performance. The test cases are then executed in the order of their priority, until a certain budget or stopping condition is reached. This technique can increase the rate of fault detection and the early feedback to the developers, while reducing the overall testing effort.
  - Test case selection: This technique involves selecting a subset of test cases from the original test suite that are relevant for the changes made to the system. The selection can be based on various criteria, such as the code coverage, the requirements coverage, the dependency analysis, or the impact analysis. The selected test cases are then executed for regression testing, while the rest are omitted. This technique can reduce the testing effort and the redundancy of test cases, while preserving the test coverage and the fault detection effectiveness.
  - Test case minimization: This technique involves removing or combining test cases from the original test suite that are redundant or unnecessary for the changes made to the system. The minimization can be based on various criteria, such as the code coverage, the requirements coverage, the dependency analysis, or the impact analysis. The minimized test suite is then executed for regression testing, while the removed or combined test cases are discarded. This technique can reduce the testing effort and the redundancy of test cases, while preserving the test coverage and the fault detection effectiveness.



# Prioritization guidelines for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Regression testing is the process of retesting the modified parts of a software system and the parts that might be affected by the modifications to ensure that no new defects have been introduced.
- Regression testing is important because software changes can introduce new errors or break existing functionality, which can affect the quality and reliability of the software.
- Regression testing can be performed at different levels of testing, such as unit testing, integration testing, system testing, and acceptance testing.
- Regression testing can be done manually or automatically, depending on the availability of test cases, test tools, and resources.
- Regression testing can be classified into three types: retest all, selective, and test suite minimization.
  - Retest all is the simplest approach, which involves re-executing all the existing test cases for the entire software system. This approach ensures high coverage, but it is also time-consuming and costly.
  - Selective is the most common approach, which involves selecting a subset of test cases that are relevant to the modified parts of the software system and the parts that might be affected by the modifications. This approach reduces the testing effort, but it also requires a criterion to select the test cases.
  - Test suite minimization is the most advanced approach, which involves reducing the size of the test suite while maintaining the same coverage as the original test suite. This approach optimizes the testing effort, but it also requires sophisticated techniques and tools to perform the minimization.
- Regression testing can be guided by various criteria, such as code coverage, fault coverage, risk analysis, impact analysis, and test case prioritization.
  - Code coverage is the measure of how much of the source code is executed by the test cases. Code coverage can be used to select the test cases that cover the modified or affected parts of the code, or to minimize the test suite by removing the redundant test cases that cover the same parts of the code.
  - Fault coverage is the measure of how many faults are detected by the test cases. Fault coverage can be used to select the test cases that have a high probability of detecting new or existing faults, or to minimize the test suite by removing the ineffective test cases that do not detect any faults.
  - Risk analysis is the process of identifying and assessing the potential risks associated with the software changes. Risk analysis can be used to select the test cases that cover the high-risk parts of the software system, or to prioritize the test cases based on the severity and likelihood of the risks.
  - Impact analysis is the process of analyzing the dependencies and relationships among the software components. Impact analysis can be used to select the test cases that cover the direct or indirect impact of the software changes, or to prioritize the test cases based on the degree and scope of the impact.
  - Test case prioritization is the process of ordering the test cases according to some criteria, such as fault detection effectiveness, execution time, cost, or importance. Test case prioritization can be used to execute the test cases in an optimal order, or to minimize the test suite by removing the low-priority test cases.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of priority category for the notes of the Unit 4 - Regression Testing in the subject of Software Testing.

# Priority category for the notes of the Unit 4 - Regression Testing

- Regression testing is the process of retesting a software system after changes have been made to ensure that the changes have not introduced new defects or affected the existing functionality.
- Regression testing can be classified into three priority categories based on the risk and impact of the changes: high, medium, and low.
- High priority regression testing is performed when the changes are critical or have a high impact on the system, such as fixing major bugs, adding new features, or modifying the core functionality. High priority regression testing aims to verify that the changes have not broken the system or caused severe errors. High priority regression testing should be done as soon as possible after the changes are made and before releasing the system to the users or customers.
- Medium priority regression testing is performed when the changes are moderate or have a medium impact on the system, such as enhancing existing features, improving performance, or refactoring the code. Medium priority regression testing aims to verify that the changes have not affected the quality or usability of the system or caused minor errors. Medium priority regression testing should be done after high priority regression testing and before the final testing phase.
- Low priority regression testing is performed when the changes are minor or have a low impact on the system, such as fixing typos, updating documentation, or changing the user interface. Low priority regression testing aims to verify that the changes have not introduced any new defects or affected the functionality of the system. Low priority regression testing should be done after medium priority regression testing and before the final testing phase.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You have asked me to write the scheme for the notes of the Unit 4 - Regression Testing in the subject of Software Testing. Here is my attempt:

# Unit 4 - Regression Testing

## Introduction
- Regression testing is the process of retesting a software system after changes have been made to ensure that the changes do not introduce new defects or break existing functionality.
- Regression testing is important because software systems are often complex and interdependent, and changes can have unintended consequences that affect the quality and reliability of the system.
- Regression testing can be performed at different levels of granularity, such as unit testing, integration testing, system testing, and acceptance testing, depending on the scope and impact of the changes.
- Regression testing can be done manually or automatically, depending on the availability and suitability of test cases, test tools, and test resources.
- Regression testing can be done in different ways, such as retesting all test cases, retesting selected test cases, or retesting based on test coverage analysis, depending on the test strategy and test objectives.

## Types of Regression Testing
- There are different types of regression testing, such as:
  - Corrective regression testing: This is done when there are no changes in the specifications or requirements, but only bug fixes or code modifications. The objective is to verify that the fixes do not introduce new defects or affect other parts of the system.
  - Progressive regression testing: This is done when there are changes in the specifications or requirements, such as adding new features or functionalities. The objective is to verify that the new features or functionalities work as expected and do not affect the existing features or functionalities.
  - Retrospective regression testing: This is done when there are changes in the environment or platform, such as upgrading the hardware, software, or operating system. The objective is to verify that the system works as expected in the new environment or platform and does not encounter any compatibility or performance issues.

## Techniques of Regression Testing
- There are different techniques of regression testing, such as:
  - Retest all: This is the simplest and most comprehensive technique, where all the test cases are re-executed after each change. This ensures maximum test coverage and defect detection, but it is also time-consuming and resource-intensive.
  - Retest selected: This is a more efficient and selective technique, where only a subset of test cases are re-executed after each change. This reduces the test effort and cost, but it also requires a clear and rational criterion for selecting the test cases, such as the impact analysis, the risk analysis, or the priority analysis.
  - Retest based on coverage: This is a more dynamic and adaptive technique, where the test cases are re-executed based on the test coverage analysis. This ensures that the test cases cover the modified code or functionality, and also identifies the redundant or obsolete test cases that can be removed or updated. This technique requires a test coverage tool that can measure and report the test coverage.

## Challenges of Regression Testing
- There are some challenges of regression testing, such as:
  - Test case maintenance: This is the challenge of keeping the test cases up-to-date and consistent with the changes in the system. This requires a regular review and revision of the test cases, as well as a proper documentation and traceability of the test cases.
  - Test case selection: This is the challenge of choosing the appropriate and optimal test cases for regression testing. This requires a systematic and objective approach that can balance the test coverage and test effort, as well as a reliable and accurate test data and test oracle.
  - Test automation: This is the challenge of automating the regression testing process to reduce the manual effort and increase the test efficiency and effectiveness. This requires a suitable and stable test automation tool that can support the test environment and test scenarios, as well as a skilled and experienced test automation team.



# Risk Analysis for the notes of the Unit 4 - Regression Testing in the subject of Software Testing

- Risk analysis is the process of identifying and prioritizing the potential risks in software applications or systems that are under test .
- Risks are the possible outcomes or events that can cause loss or damage to the software or the organization .
- Risk analysis aims to quantify the severity and probability of the risks, and to categorize them according to their impact and likelihood .
- Risk analysis helps to allocate testing resources and efforts effectively, and to focus on the most critical and vulnerable areas of the software .
- Risk analysis can be performed at different stages of the software development life cycle, such as planning, design, implementation, testing, and deployment .
- Risk analysis can be done using various techniques, such as brainstorming, checklists, interviews, surveys, historical data, expert opinions, etc .
- Risk analysis can be supported by various tools, such as LogicManager, EHSInsight, EcoOnline, etc.
- Risk analysis can be classified into different types, such as business risks, testing risks, premature release risks, software risks, etc.
- Business risks are the risks that may affect the profitability, reputation, or market share of the organization.
- Testing risks are the risks that may arise from the testing process, such as lack of skills, tools, time, or requirements.
- Premature release risks are the risks that may occur when the software is released before it is fully tested or ready.
- Software risks are the risks that may affect the quality, functionality, performance, security, or reliability of the software.
- Regression testing is a type of software testing that verifies that the software still works as expected after any changes, such as bug fixes, enhancements, or updates .
- Regression testing is important to ensure that the changes do not introduce new defects or break existing features .
- Regression testing can be done manually or automatically, depending on the scope, complexity, and frequency of the changes .
- Regression testing can be done using various strategies, such as retest all, regression test selection, test case prioritization, etc .
- Retest all is a strategy that involves testing all the test cases in the test suite, regardless of the changes .
- Regression test selection is a strategy that involves testing only a subset of the test cases that are relevant to the changes .
- Test case prioritization is a strategy that involves testing the test cases in a certain order based on their importance, risk, or coverage .
- Risk analysis can be applied to regression testing to identify and prioritize the test cases that have the highest risk of failure or impact .
- Risk analysis can help to reduce the cost, time, and effort of regression testing, and to improve the effectiveness and efficiency of the testing process .
- Risk analysis can be done using various criteria, such as the frequency, severity, or complexity of the changes, the functionality, performance, or security of the features, the history, feedback, or defects of the software, etc .
- Risk analysis can be done using various methods, such as risk-based testing, risk matrix, risk impact analysis, etc .
- Risk-based testing is a method that involves testing the software based on the risk level of the test cases, such as high, medium, or low .
- Risk matrix is a method that involves plotting the test cases on a matrix based on their probability and impact of failure .
- Risk impact analysis is a method that involves calculating the risk exposure of the test cases based on their probability and impact of failure .
- Risk analysis can be done using various metrics, such as risk coverage, risk density, risk index, risk priority number, etc .
- Risk coverage is a metric that measures the percentage of the total risk that is covered by the test cases



## Unit 5 - Software Testing Activities

- Software testing is the process of verifying and validating that a software product meets the requirements and expectations of the stakeholders.
- Software testing activities include planning, designing, executing, and evaluating test cases, as well as reporting and managing defects, and ensuring quality assurance.
- Software testing activities can be classified into different levels, such as unit testing, integration testing, system testing, and acceptance testing, depending on the scope and objective of the testing.
- Software testing activities can also be classified into different types, such as functional testing, non-functional testing, structural testing, and change-related testing, depending on the aspect and attribute of the software product that is being tested.
- Software testing activities can be performed using different approaches, such as manual testing, automated testing, or a combination of both, depending on the feasibility, efficiency, and effectiveness of the testing.
- Software testing activities can be performed using different strategies, such as black-box testing, white-box testing, or gray-box testing, depending on the level of knowledge and access to the software product's internal structure and logic.
- Software testing activities can be performed using different techniques, such as equivalence partitioning, boundary value analysis, decision table testing, state transition testing, use case testing, etc., depending on the type and complexity of the software product and its requirements.
- Software testing activities can be performed using different tools, such as test management tools, test design tools, test execution tools, test data generation tools, test evaluation tools, defect tracking tools, etc., depending on the needs and preferences of the testers and the test environment.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on the levels of testing in software testing.

# Levels of Testing in Software Testing

Software testing is the process of verifying and validating that a software product meets the requirements and expectations of the stakeholders. Software testing can be performed at different levels of abstraction, depending on the scope, purpose, and context of the testing. The main levels of testing in software testing are:

- **Unit testing**: This is the lowest level of testing, where individual components or units of the software are tested in isolation. Unit testing checks if the software components are fulfilling their functionalities or not. Unit testing is usually done by the developers using tools and frameworks such as JUnit, NUnit, TestNG, etc. Unit testing helps to find defects early in the development cycle and improve the quality of the code.

- **Integration testing**: This is the level of testing where multiple components or units are combined and tested as a group. Integration testing checks the data flow and interaction between the modules and ensures that they work together as expected. Integration testing can be done in different ways, such as top-down, bottom-up, sandwich, or big-bang approach. Integration testing is usually done by the testers using tools and frameworks such as Selenium, Postman, SoapUI, etc. Integration testing helps to find defects in the interfaces and integration points of the software.

- **System testing**: This is the level of testing where the entire software system is tested as a whole. System testing evaluates both functional and non-functional requirements of the software, such as usability, performance, security, reliability, etc. System testing is usually done by the testers using tools and frameworks such as JMeter, LoadRunner, Appium, etc. System testing helps to find defects in the overall functionality and behavior of the software.

- **Acceptance testing**: This is the highest level of testing, where the software is tested by the end-users or customers to check if it meets their needs and expectations. Acceptance testing checks the requirements of a specification or contract are met as per its delivery. Acceptance testing can be done in different ways, such as alpha, beta, or user acceptance testing. Acceptance testing helps to ensure the satisfaction and acceptance of the software by the stakeholders.

These are the main levels of testing in software testing. Each level of testing has its own objectives, techniques, and tools. The levels of testing are not mutually exclusive, but rather complementary and interdependent. The levels of testing can be performed in a sequential or iterative manner, depending on the software development methodology and the testing strategy. The levels of testing help to ensure the quality and reliability of the software product.



# Debugging

- Debugging is the process of identifying and removing errors from computer hardware or software  .
- Debugging is also often used if another method of troubleshooting is applied without a debugger.
- Debugging contains "bug" because this word has been used for decades to describe all sorts of programming errors in software development.
- Debugging is a multistep process that involves the following steps:
  - Identifying a problem: This can be done by observing the symptoms of the error, such as incorrect output, abnormal behavior, or system crash.
  - Isolating the source of the problem: This can be done by using various techniques, such as tracing, breakpoints, logging, or testing.
  - Correcting the problem or determining a way to work around it: This can be done by modifying the code, changing the configuration, or applying a patch.
  - Testing the correction or workaround and making sure it works: This can be done by running the program again, checking the output, or performing regression testing.
- Debugging is an essential part of software testing activities, as it helps to ensure the quality, reliability, and functionality of the software. Debugging can be done at different levels of software development, such as unit testing, integration testing, system testing, or acceptance testing. Debugging can also be done by different roles, such as developers, testers, or users. Debugging can be done manually or with the help of tools, such as debuggers, profilers, or code analyzers. Debugging can be challenging, time-consuming, and complex, depending on the nature and size of the software, the type and number of errors, and the availability and quality of documentation and tools. Debugging can also be rewarding, satisfying, and fun, as it involves problem-solving, creativity, and learning.



# Testing techniques and their applicability

Testing techniques are the methods applied to evaluate a system or a component with a purpose to find if it satisfies the given requirements. Testing of a system helps to identify gaps, errors, or any kind of missing requirements differing from the actual requirements.

There are different types of testing techniques, each with its own advantages and disadvantages, and applicability to different scenarios. Some of the common testing techniques are:

- **Unit testing**: Validating that each software unit performs as expected. A unit is the smallest testable component of an application, such as a method or a function. Unit testing is very low level and close to the source of an application. It is generally quite cheap to automate and can run very quickly by a continuous integration server. Unit testing is applicable to any software development methodology and helps to ensure the quality and functionality of the individual units.

- **Integration testing**: Ensuring that software components or functions operate together. Integration testing is performed after unit testing and before system testing. It involves testing the interactions and interfaces between the units or modules of an application. Integration testing can be done in different ways, such as top-down, bottom-up, or sandwich approach. Integration testing is applicable to any software development methodology that involves modular design and helps to detect errors and inconsistencies in the integration of the components.

- **System testing**: Verifying whether the whole system works as intended. System testing is performed after integration testing and before acceptance testing. It involves testing the system as a whole, including its functionality, performance, reliability, security, usability, and compatibility with other systems. System testing can be done in different ways, such as functional, non-functional, or regression testing. System testing is applicable to any software development methodology that involves a complete and integrated system and helps to ensure that the system meets the specified requirements and expectations.

- **Acceptance testing**: Verifying whether the system meets the needs and expectations of the end-users and stakeholders. Acceptance testing is performed after system testing and before the system is deployed or delivered. It involves testing the system in a real or simulated environment, with real or simulated data, and with the involvement of the intended users or customers. Acceptance testing can be done in different ways, such as alpha, beta, or user acceptance testing. Acceptance testing is applicable to any software development methodology that involves a customer-oriented approach and helps to ensure that the system is acceptable and satisfactory to the users and stakeholders.

- **Performance testing**: Evaluating how well the system performs under various conditions, such as load, stress, endurance, or spike. Performance testing is a type of non-functional testing that can be done at any level of testing, such as unit, integration, system, or acceptance. Performance testing can be done in different ways, such as load testing, stress testing, endurance testing, or spike testing. Performance testing is applicable to any software development methodology that involves a performance-oriented approach and helps to ensure that the system meets the performance criteria and standards.

- **Security testing**: Ensuring that the system and application are protected from all types of loopholes, vulnerabilities, threats, and attacks. Security testing is a type of non-functional testing that can be done at any level of testing, such as unit, integration, system, or acceptance. Security testing can be done in different ways, such as penetration testing, vulnerability scanning, ethical hacking, or risk assessment. Security testing is applicable to any software development methodology that involves a security-oriented approach and helps to ensure that the system meets the security requirements and policies.

- **Usability testing**: Assessing how easy and user-friendly the system and application are for the end-users. Usability testing is a type of non-functional testing that can be done at any level of testing, such as unit, integration, system, or acceptance. Usability testing can be done in different ways, such as heuristic evaluation, user testing, or user feedback. Usability testing is applicable to any software development methodology that involves a user-oriented approach and helps to ensure that the system meets the usability criteria and standards.

These are some of the testing techniques and their applicability for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing. I hope this helps you to learn and prepare for your exams. If you have any questions or feedback, please let me know.



# Exploratory Testing

- Exploratory testing is an approach to software testing that is often described as simultaneous learning, test design, and execution.
- It focuses on discovery and relies on the guidance of the individual tester to uncover defects that are not easily covered in the scope of other tests.
- It is often thought of as a black box testing technique, but it can be applied to any test technique, at any stage in the development process.
- It emphasizes the tester's autonomy, skill and creativity, much as other Agile practices emphasize these qualities in developers.
- Some of the benefits of exploratory testing are:
  - It can find bugs that are missed by scripted testing or automated testing.
  - It can adapt to changing requirements and feedback quickly.
  - It can leverage the tester's intuition and experience.
  - It can provide fast and valuable feedback to the developers and stakeholders.
- Some of the challenges of exploratory testing are:
  - It can be difficult to document and reproduce the test cases and results.
  - It can be hard to measure the test coverage and quality.
  - It can be dependent on the tester's skill and availability.
  - It can be seen as unstructured and unprofessional by some managers or auditors.
- Some of the best practices for exploratory testing are:
  - Define a clear scope and objective for the testing session.
  - Use a variety of test techniques and heuristics to explore the system.
  - Use tools and techniques to record and report the test activities and findings.
  - Collaborate with other testers and stakeholders to share insights and feedback.
  - Review and refine the test strategy based on the test outcomes and learning.



# Automated Test Data Generation

- Automated test data generation is an activity that generates test data automatically for the software under test.
- The quality and effectiveness of testing is heavily dependent on the generated test data.
- The main benefits of automated test data generation are:
  - Vast generation speed, as well as the accuracy of generated data.
  - Ability to create test data that would ensure a sufficient level of quality of the final product by checking most of the various code paths, i.e., to provide maximum code coverage to satisfy some criteria (for example, statement or branch coverage).
  - Ability to mask or anonymize sensitive data to protect privacy and comply with regulations.
- The main challenges of automated test data generation are:
  - Ensuring the validity of the data, i.e., the generated data needs to be realistic and consistent with the business rules and constraints.
  - Ensuring the diversity of the data, i.e., the generated data needs to cover different scenarios and edge cases.
  - Ensuring the traceability of the data, i.e., the generated data needs to be linked to the test cases and the requirements.
- Some of the best test data generation tools are :
  - Avo iTDM – Intelligent Test Data Management: A test data management platform that empowers you to generate, mask, subset, and provision test data across the entire software testing lifecycle.
  - MOSTLY AI: An AI-powered synthetic data generator that creates realistic and privacy-preserving synthetic data from existing data sources.
  - DATPROF: A test data management solution that simplifies getting the right test data at the right moment, with features like data masking, data generation, data subsetting, and data provisioning.
  - EMS Data Generator: A tool that allows you to generate test data for various database systems, such as MySQL, PostgreSQL, Oracle, SQL Server, etc.
  - Redgate SQL Data Generator: A tool that generates realistic test data for SQL Server databases, with features like data anonymization, data customization, and data generation from existing data sources.
  - Informatica Test Data Management: A test data management solution that enables you to discover, classify, subset, mask, and provision test data for any testing environment.
  - Double: A tool that generates realistic test data for web and mobile applications, with features like data generation from real-world sources, data customization, and data export.



# Test Data for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing

- Software testing activities are the processes and tasks that are performed to check the quality and functionality of a software product or system.
- Software testing activities can be classified into four main levels: unit testing, integration testing, system testing, and acceptance testing .
- Unit testing is the process of validating that each software unit performs as expected. A unit is the smallest testable component of software, such as a function, a class, or a module .
- Integration testing is the process of ensuring that software components or functions operate together. Integration testing can be done in different ways, such as top-down, bottom-up, or sandwich .
- System testing is the process of verifying whether the whole system works as intended. System testing can involve different types of tests, such as functional, non-functional, performance, security, usability, etc .
- Acceptance testing is the process of confirming whether the software meets the requirements and expectations of the customer or user. Acceptance testing can be done by the customer, the user, or a third party .
- The software testing life cycle is the sequence of steps or phases that are followed during software testing activities. The software testing life cycle typically includes the following phases: test planning, test design, test execution, test reporting, and test closure .
- Test planning is the phase where the objectives, scope, strategy, resources, schedule, and risks of software testing activities are defined and documented. Test planning involves creating a test plan document that guides the testing process .
- Test design is the phase where the test cases, test data, test environment, and test tools are prepared and reviewed. Test design involves applying different techniques, such as black-box, white-box, or gray-box, to generate test cases that cover the test scenarios and test objectives .
- Test execution is the phase where the test cases are run on the software under test using the test data, test environment, and test tools. Test execution involves recording the test results, logging the defects, and tracking the test progress .
- Test reporting is the phase where the test results, test coverage, test metrics, and test status are summarized and communicated to the stakeholders. Test reporting involves creating a test report document that highlights the achievements, issues, and recommendations of software testing activities .
- Test closure is the phase where the software testing activities are formally completed and evaluated. Test closure involves verifying that all the test cases are executed, all the defects are resolved, and all the test deliverables are archived. Test closure also involves conducting a test review or a retrospective to identify the lessons learned and the best practices for future software testing activities .



# Approaches to test data generation for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing

Test data generation is the process of creating a set of data that can be used to test the functionality and performance of a software system. Test data can be either real data from previous operations or artificial data designed for specific purposes. Test data generation techniques are methods to produce test data efficiently and effectively.

Some of the common approaches to test data generation are:

- **Manual test data generation**: In this approach, the tester manually creates the test data based on the test cases and the requirements. This approach is easy to implement and does not require any additional tools. However, it can be time-consuming, error-prone, and limited in coverage. Manual test data generation is suitable for small and simple applications or for exploratory testing .
- **Automated test data generation**: In this approach, the tester uses tools or scripts to generate test data automatically. This approach can save time, reduce errors, and increase coverage. However, it can also be complex, costly, and dependent on the quality of the tools or scripts. Automated test data generation is suitable for large and complex applications or for regression testing .
- **Back-end data injection approach**: In this approach, the tester directly inserts the test data into the database or the data source of the application. This approach can bypass the user interface and the business logic layers and test the data integrity and consistency. However, it can also be risky, invasive, and require technical skills and access rights. Back-end data injection approach is suitable for testing the data layer or the back-end functionality of the application.
- **Third-party tool approach**: In this approach, the tester uses a third-party tool or service to generate test data. This approach can provide realistic, diverse, and large-scale test data. However, it can also be expensive, insecure, and dependent on the availability and reliability of the tool or service. Third-party tool approach is suitable for testing the performance, scalability, and security of the application .

: https://www.geeksforgeeks.org/approaches-for-test-data-generation-in-software-testing/
: https://www.testbytes.net/blog/5-test-data-generation-techniques-to-know/
: https://www.testbytes.net/blog/test-data-generation-techniques/
: https://www.testim.io/blog/test-data-is-critical-how-to-best-generate-manage-and-use-it/



# Test Data Generation Using Genetic Algorithm

- Test data generation is the process of creating a set of inputs for a software system that can be used to test its functionality, performance, reliability, security, etc.
- Test data generation can be done manually or automatically. Manual test data generation is time-consuming, error-prone, and may not cover all the possible scenarios. Automatic test data generation is more efficient, accurate, and can achieve higher coverage of the software behavior.
- Genetic algorithm (GA) is a bio-inspired optimization technique that mimics the natural evolution process. GA can be used to generate test data automatically by searching for the optimal or near-optimal inputs that satisfy some criteria, such as executing a specific statement, branch, path, or definition-use pair in the program under test .
- GA works by creating an initial population of random test data, and then applying genetic operators such as selection, crossover, and mutation to produce new test data. The quality of each test data is evaluated by a fitness function, which measures how well it meets the testing objective. The fitness function can be based on the program's structure, such as the number of statements or branches executed, or the program's behavior, such as the output values or the error messages .
- GA iterates until a termination condition is met, such as reaching a maximum number of generations, finding a test data with a perfect fitness, or reaching a predefined time limit. The best test data found by GA is then returned as the final solution .
- GA has some advantages over other automatic test data generation techniques, such as:
  - GA can handle complex and nonlinear problems that may not have analytical solutions or may be hard to solve by other methods.
  - GA can explore a large and diverse search space and avoid getting trapped in local optima.
  - GA can be easily adapted to different testing objectives and criteria by changing the fitness function and the genetic operators.
- GA also has some challenges and limitations, such as:
  - GA may require a lot of computational resources and time to find a good solution, especially for large and complex programs.
  - GA may not guarantee the completeness or correctness of the test data, as it is based on a heuristic search and may miss some important cases.
  - GA may need some domain knowledge and human intervention to design an effective fitness function and genetic operators for a specific problem.
- GA has been successfully applied to generate test data for simple programs and problems, such as numerical calculations, logical expressions, and string manipulations. However, GA is rarely used to generate test data for complex problems and programs, such as images, videos, sounds, and 3D models. Some possible research directions for improving GA for test data generation are:
  - Developing new fitness functions and genetic operators that can handle complex data types and structures.
  - Integrating GA with other techniques, such as program slicing, symbolic execution, and machine learning, to enhance the efficiency and effectiveness of the search process .
  - Evaluating and comparing the performance and quality of GA with other test data generation techniques on different benchmarks and domains.



# Test Data Generation Tools

Test data generation tools are software programs or libraries that help programmers and testers create and generate realistic and representative test data sets for various kinds of applications and use cases. Test data generation tools can be used for different purposes, such as:

- Unit testing: To verify the functionality of specific units or components of a software program as well as the interactions between various components of the application.
- Performance testing: To measure the speed, scalability, reliability, and resource consumption of the application under different workloads and scenarios.
- Security testing: To check the vulnerability and robustness of the application against malicious attacks and unauthorized access.
- Compliance testing: To ensure that the application meets the legal and regulatory requirements and standards of the domain or industry.
- Data masking: To protect the sensitive and confidential information in the production data by replacing it with realistic but fictitious data.

Some of the benefits of using test data generation tools are:

- They can save time and effort by automating the process of creating and populating test databases and files.
- They can increase the coverage and quality of testing by providing diverse and complex data sets that cover various edge cases and scenarios.
- They can reduce the dependency and risk of using production data by creating synthetic data that mimics the characteristics and behavior of the real data.
- They can enhance the reusability and maintainability of test data by allowing the testers to modify, update, and regenerate the data as per the changing requirements and specifications.

Some of the features and criteria to consider when choosing a test data generation tool are:

- The type and format of the data sources and targets that the tool supports, such as relational databases, NoSQL databases, flat files, XML files, JSON files, etc.
- The variety and complexity of the data generators that the tool provides, such as random, sequential, pattern-based, rule-based, domain-specific, etc.
- The ability and flexibility of the tool to customize and configure the data generation parameters, such as data size, data distribution, data range, data constraints, data dependencies, data relationships, etc.
- The quality and accuracy of the data generated by the tool, such as data validity, data consistency, data uniqueness, data realism, data representativeness, etc.
- The performance and scalability of the tool, such as data generation speed, data generation volume, data generation concurrency, data generation parallelism, etc.
- The usability and functionality of the tool, such as user interface, user documentation, user support, user feedback, user community, etc.

Some of the examples of test data generation tools are:

- DTM Data Generator: A reliable tool for delivering high-quality and realistic test data by generating data rows and schema objects for various databases and file formats. It supports more than 30 built-in data generators and allows the users to create custom data generators using scripts and expressions. It also offers data masking and data scrambling features to protect the sensitive data. 
- Visual Studio (Premium) Data Generator: A feature of the Visual Studio IDE that enables the users to generate test data for SQL Server databases. It allows the users to specify the data generation plan by defining the data generators, data distribution, and data constraints for each column of the table. It also supports data masking and data anonymization features to replace the real data with fictitious data. 
- Redgate SQL Data Generator: A tool that helps the users to populate SQL Server databases with realistic test data. It provides over 60 built-in data generators and allows the users to import data from existing sources or create custom data generators using Python scripts. It also supports data masking and data anonymization features to protect the sensitive data. 
- ApexSQL Generate: A tool that enables the users to generate test data for SQL Server databases. It supports over 200 built-in data generators and allows the users to import data from external sources or create custom data generators using regular expressions. It also supports data masking and data anonymization features to protect the sensitive data. 
- Upscene Advanced Data Generator: A tool that helps the users to create and generate test data for various databases and file formats. It supports over 40 built-in data generators and allows the users to create custom data generators using scripts and expressions. It also supports data masking and data anonymization features to protect the sensitive data. 
- EMS Data Generator: A tool that allows the users to generate test data for various databases and file formats. It supports over 20 built-in data generators and allows the users to create custom data generators using scripts and expressions. It also supports data masking and data anonymization



# Software Testing Tools

Software testing tools are the tools that are used for the testing of software. Software testing tools can help developers and testers to ensure the quality, functionality, performance, and security of the software they create. Software testing tools can also help to automate some testing tasks, reduce manual efforts, and provide faster feedback.

There are many types of software testing tools available, depending on the testing activities and objectives. Some of the common software testing tools are:

- **Test management tools**: These tools help to manage the testing process, such as planning, organizing, executing, and reporting test cases. They also help to track the test progress, defects, and requirements coverage. Some examples of test management tools are TestRail, Xray, and IBM Rational Test Workbench.
- **Functional testing tools**: These tools help to verify that the software meets the functional requirements and specifications. They can perform different types of functional testing, such as unit testing, integration testing, system testing, and regression testing. They can also support different testing approaches, such as black-box testing, white-box testing, and gray-box testing. Some examples of functional testing tools are Selenium  , IBM Rational Test Workbench, and Katalon Studio.
- **Performance testing tools**: These tools help to measure and improve the speed, scalability, reliability, and resource consumption of the software. They can perform different types of performance testing, such as load testing, stress testing, endurance testing, and spike testing. They can also simulate different user scenarios, network conditions, and workload patterns. Some examples of performance testing tools are Gatling , IBM Rational Performance Tester, and JMeter.
- **Security testing tools**: These tools help to identify and eliminate the vulnerabilities and risks in the software. They can perform different types of security testing, such as penetration testing, vulnerability scanning, code analysis, and compliance testing. They can also detect and prevent various types of attacks, such as SQL injection, cross-site scripting, denial-of-service, and phishing. Some examples of security testing tools are Nmap, ZAP, and IBM AppScan.
- **API testing tools**: These tools help to test the functionality, performance, and security of the application programming interfaces (APIs) that the software uses or provides. They can perform different types of API testing, such as RESTful testing, SOAP testing, GraphQL testing, and microservices testing. They can also validate the API responses, requests, and parameters. Some examples of API testing tools are Postman , IBM Rational Test Workbench, and SoapUI.
- **UI testing tools**: These tools help to test the usability, accessibility, and compatibility of the user interface (UI) of the software. They can perform different types of UI testing, such as graphical user interface (GUI) testing, web UI testing, mobile UI testing, and cross-browser testing. They can also capture and compare the UI screenshots, elements, and interactions. Some examples of UI testing tools are Selenium  , IBM Rational Test Workbench, and TestComplete.
- **Code analysis tools**: These tools help to analyze and improve the quality, readability, and maintainability of the source code of the software. They can perform different types of code analysis, such as static analysis, dynamic analysis, code coverage, code complexity, and code review. They can also detect and fix various types of code issues, such as bugs, errors, warnings, and smells. Some examples of code analysis tools are SonarQube, IBM Engineering Workflow Management, and CodeClimate.
- **Test automation tools**: These tools help to automate some or all of the testing tasks, such as test case creation, execution, and reporting. They can also integrate with other testing tools, such as test management tools, functional testing tools, and performance testing tools. They can also support different testing frameworks, languages, and platforms. Some examples of test automation tools are Selenium  , IBM Rational Test Workbench, and Katalon Studio.

These are some of the software testing tools that can be used for the notes of the Unit 5 - Software Testing Activities in the subject of Software Testing. However, there are many more software testing



# Software Test Plan

A software test plan is a document that outlines the what, when, how, who, and more of the project. It is prepared at the project level and in general, it defines work products to be tested, how they will be tested, and test type distribution among the testers. A software test plan is based on a software test strategy, which helps in understanding the broad objectives of the test and how a particular project or release is unique.

Some of the main components of a software test plan are:

- **Test scope**: This section describes the features, functions, and requirements that are in scope and out of scope for testing. It also defines the test levels, such as unit, integration, system, and acceptance testing, and the test types, such as functional, non-functional, regression, and exploratory testing.
- **Test objectives**: This section defines the specific goals and criteria for testing, such as test coverage, defect detection, quality assurance, and user satisfaction. It also specifies the entry and exit criteria for each test level, such as the minimum number of test cases executed, the maximum number of defects allowed, and the readiness of the test environment.
- **Test environment**: This section describes the hardware, software, network, and tools that are required for testing. It also defines the roles and responsibilities of the test team, such as test manager, test lead, test engineer, and test analyst. It also identifies the stakeholders and their expectations from testing, such as the project manager, the developers, the customers, and the end-users.
- **Test schedule and resources**: This section defines the test activities, tasks, and deliverables, along with their dependencies, durations, and milestones. It also estimates the effort, cost, and risk involved in testing, and allocates the resources, such as test personnel, test data, and test cases, accordingly. It also defines the test reporting and communication mechanisms, such as test status, test metrics, test logs, and test incidents.
- **Test approach and methodology**: This section describes the test design techniques, test execution methods, and test management processes that will be followed during testing. It also defines the test standards, guidelines, and best practices that will be adhered to during testing. It also describes the test automation strategy, if any, and the tools and frameworks that will be used for test automation.
- **Test deliverables**: This section lists the test artifacts that will be produced and maintained during testing, such as test plan, test cases, test scripts, test data, test results, test reports, test logs, and test defects. It also defines the format, content, and quality of the test deliverables, and the storage and retention policies for the test deliverables.

A software test plan is a dynamic and evolving document that should be updated and revised throughout the project lifecycle, as per the changes in the requirements, scope, schedule, and resources. A software test plan should be reviewed and approved by the relevant stakeholders before testing begins, and should be audited and evaluated after testing ends, to measure the effectiveness and efficiency of testing. A software test plan is a key document for ensuring the quality and success of the software project.



## Unit 6 - Object Oriented Testing

- Object oriented testing is a testing technique that focuses on the behavior and structure of objects and classes in an object oriented system.
- Object oriented testing can be divided into two categories: class testing and system testing.
- Class testing is the testing of individual classes and their methods, attributes, and interactions with other classes.
- System testing is the testing of the whole system as a collection of classes and objects that collaborate to achieve the system's functionality and quality attributes.
- Object oriented testing can be performed at different levels of abstraction, such as unit testing, integration testing, and system testing.
- Object oriented testing can also be performed using different approaches, such as white-box testing, black-box testing, and gray-box testing.
- White-box testing is a testing approach that uses the internal structure and implementation details of the system or class under test to design and execute test cases.
- Black-box testing is a testing approach that uses the external behavior and specification of the system or class under test to design and execute test cases, without considering the internal structure or implementation details.
- Gray-box testing is a testing approach that combines both white-box and black-box testing techniques, using both the internal structure and the external behavior of the system or class under test to design and execute test cases.
- Object oriented testing faces some challenges and issues that are specific to the object oriented paradigm, such as inheritance, polymorphism, dynamic binding, encapsulation, and reuse.
- Inheritance is the mechanism that allows a class to inherit the attributes and methods of another class, called the superclass or parent class. Inheritance can introduce complexity and ambiguity in testing, as a subclass or child class can override or extend the behavior of the superclass or parent class, and can also inherit the faults or defects of the superclass or parent class.
- Polymorphism is the mechanism that allows an object to behave differently depending on its type or context. Polymorphism can introduce complexity and uncertainty in testing, as an object can have multiple types or classes, and can respond differently to the same message or method invocation, depending on the type or class of the object at run-time.
- Dynamic binding is the mechanism that allows the selection of the appropriate method implementation for an object at run-time, based on the type or class of the object. Dynamic binding can introduce complexity and unpredictability in testing, as the behavior of an object can change at run-time, depending on the type or class of the object, and the method implementation can also change due to inheritance or polymorphism.
- Encapsulation is the mechanism that hides the internal structure and implementation details of an object or class from the outside world, and only exposes the public interface or specification of the object or class. Encapsulation can introduce difficulty and limitation in testing, as the internal state and behavior of an object or class can be inaccessible or invisible to the tester, and the tester can only rely on the public interface or specification of the object or class to design and execute test cases.
- Reuse is the mechanism that allows the reuse of existing classes and objects in the development of new systems or classes, without modifying or adapting the existing classes and objects. Reuse can introduce complexity and risk in testing, as the reused classes and objects can have unknown or hidden faults or defects, and can also have dependencies or interactions with other classes and objects that are not part of the new system or class.



# Definition for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

- Object Oriented Testing (OOT) is a software testing process that is conducted to test the software using object-oriented paradigms like, encapsulation, inheritance, polymorphism, etc.
- OOT is different from conventional testing strategies as the concepts of object-oriented programming are way different from that of conventional ones.
- The whole OOT revolves around the fundamental entity known as “class”, which is a blueprint for creating objects.
- OOT involves testing the classes, objects, methods, and interactions among them in the software system.
- OOT encompasses three levels, namely, unit testing, subsystem testing, and system testing.
- Unit testing focuses on testing the code of individual classes and methods.
- Subsystem testing focuses on testing the interactions and collaborations among a group of classes that form a subsystem.
- System testing focuses on testing the functionality and performance of the whole software system as a single entity.
- OOT requires a different set of testing techniques and tools than conventional testing, as the software structure, behavior, and quality attributes are different in object-oriented systems.
- Some of the common OOT techniques are class testing, state-based testing, scenario-based testing, fault-based testing, etc.
- Some of the common OOT tools are JUnit, NUnit, TestNG, etc.



# Issues for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing

Object oriented testing is a process of testing software that is developed using object oriented principles and techniques. Object oriented testing involves testing the classes, objects, methods, inheritance, polymorphism, encapsulation, and other features of object oriented programming.

Some of the issues that arise in object oriented testing are:

- **Testing base classes and derived classes**: Object oriented testing must ensure that the base classes and the derived classes are tested separately and together, as they may have different behaviors and interactions. Testing base classes involves testing the common functionality and attributes that are inherited by the derived classes. Testing derived classes involves testing the specific functionality and attributes that are added or overridden by the derived classes. Testing the interaction between base classes and derived classes involves testing the dynamic binding, method overriding, and polymorphism features of object oriented programming .

- **Testing abstract classes and interfaces**: Object oriented testing must also deal with the testing of abstract classes and interfaces, which are not instantiated but provide a template or a contract for the concrete classes that implement or extend them. Testing abstract classes and interfaces involves testing the methods and attributes that are declared but not defined by them, and ensuring that the concrete classes that implement or extend them follow the contract and provide the expected functionality .

- **Testing message passing and communication**: Object oriented testing must also consider the testing of message passing and communication between objects, which is the main mechanism of object oriented programming. Message passing involves sending and receiving messages between objects, which may trigger methods or change the state of the objects. Testing message passing and communication involves testing the correctness, completeness, and consistency of the messages, the parameters, the return values, and the effects of the messages on the objects .

- **Testing concurrency and synchronization**: Object oriented testing must also address the testing of concurrency and synchronization, which are features that allow multiple objects or threads to execute simultaneously and share resources. Concurrency and synchronization may introduce complexity and challenges in object oriented testing, such as deadlock, race condition, starvation, and inconsistency. Testing concurrency and synchronization involves testing the coordination, communication, and synchronization of the objects or threads, and ensuring that the shared resources are accessed and modified correctly and safely .

- **Testing inheritance and polymorphism**: Object oriented testing must also handle the testing of inheritance and polymorphism, which are features that allow objects to have different types and behaviors based on their class hierarchy. Inheritance and polymorphism may increase the reusability and flexibility of object oriented software, but they may also introduce complexity and ambiguity in object oriented testing, such as multiple inheritance, overriding, overloading, and dynamic binding. Testing inheritance and polymorphism involves testing the correctness, completeness, and consistency of the class hierarchy, the methods, the attributes, and the behaviors of the objects .

- **Testing encapsulation and information hiding**: Object oriented testing must also respect the testing of encapsulation and information hiding, which are features that allow objects to hide their internal details and expose only their public interface. Encapsulation and information hiding may improve the modularity and maintainability of object oriented software, but they may also limit the visibility and accessibility of the objects in object oriented testing, such as private methods, attributes, and state. Testing encapsulation and information hiding involves testing the public interface and the contract of the objects, and ensuring that the objects are consistent and reliable .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Class Testing for the notes of the Unit 6 - Object Oriented Testing in the subject of Software Testing.

# Class Testing

- Class testing is a testing technique that focuses on the verification of the behavior and structure of a class or a group of related classes in an object-oriented system.
- Class testing can be performed at two levels: intra-class testing and inter-class testing.
- Intra-class testing is the testing of the methods and attributes of a single class in isolation, without considering the interactions with other classes.
- Inter-class testing is the testing of the collaborations and dependencies among a set of classes that form a subsystem or a component.
- Class testing can be applied to both white-box and black-box testing approaches, depending on the level of access and visibility to the internal structure and implementation of the classes.
- Class testing can be conducted using various techniques, such as:
  - Equivalence partitioning: dividing the input domain of a class or a method into a set of equivalent classes that are expected to produce the same output or behavior.
  - Boundary value analysis: testing the values at or near the boundaries of the input domain of a class or a method, as they are more likely to reveal errors than the values in the middle.
  - State transition testing: testing the changes in the state of a class or an object as a result of the execution of the methods or the occurrence of the events.
  - Decision table testing: testing the combinations of conditions and actions that a class or a method can encounter, using a tabular representation of the logic.
  - Cause-effect graphing: testing the logical expressions that a class or a method uses to determine the output or the behavior, using a graphical representation of the causes and effects.
  - Data flow testing: testing the paths and interactions of the data within a class or a method, using a graphical representation of the data flow.
  - Mutation testing: testing the adequacy and effectiveness of the test cases by introducing small changes or faults in the code of a class or a method, and checking if the test cases can detect them.
- Class testing can be supported by various tools, such as:
  - Test case generators: tools that can automatically generate test cases for a class or a method based on the specification, the code, or the model of the class or the method.
  - Test drivers and stubs: tools that can simulate the behavior and the interface of the classes or the methods that are not yet implemented or available, to enable the testing of the classes or the methods that depend on them.
  - Test harnesses: tools that can provide a framework and an environment for executing and managing the test cases for a class or a method, and for collecting and analyzing the test results.
  - Test coverage analyzers: tools that can measure and report the extent to which the test cases have exercised the code or the functionality of a class or a method, and identify the untested or under-tested parts.
  - Test oracles: tools that can compare the actual output or behavior of a class or a method with the expected output or behavior, and report any discrepancies or deviations.



# Object Oriented Integration and System Testing

- Object oriented integration and system testing are two levels of testing in object oriented software development, which aim to ensure the quality and functionality of the software as a whole.
- Object oriented integration testing is the process of testing the interactions and interfaces between the classes or components of the software, which are grouped into subsystems or clusters .
- Object oriented system testing is the process of testing the software as a complete system, which includes the functional, non-functional, and hardware aspects of the software .
- Some of the challenges and techniques of object oriented integration and system testing are:

  - Testing inheritance and polymorphism: Inheritance and polymorphism are two key features of object oriented software, which allow the reuse and extension of existing classes. However, they also introduce complexity and variability in the software behavior, which makes testing more difficult. Some of the techniques to test inheritance and polymorphism are :
    - Testing the base class and the derived classes separately, and then testing the interactions between them.
    - Testing the overridden and overloaded methods in the derived classes, and ensuring that they conform to the specifications of the base class.
    - Testing the dynamic binding and late binding of methods, and ensuring that the correct method is invoked at runtime.
    - Testing the abstract classes and interfaces, and ensuring that the concrete classes that implement them provide the required functionality.
  - Testing encapsulation and information hiding: Encapsulation and information hiding are two principles of object oriented software, which allow the separation of concerns and the protection of data and implementation details. However, they also limit the visibility and accessibility of the classes or components, which makes testing more challenging. Some of the techniques to test encapsulation and information hiding are :
    - Testing the public methods and attributes of the classes or components, and ensuring that they provide the expected functionality and behavior.
    - Testing the private and protected methods and attributes of the classes or components, and ensuring that they do not violate the invariants and constraints of the software.
    - Testing the constructors and destructors of the classes or components, and ensuring that they initialize and finalize the objects properly.
    - Testing the exceptions and error handling mechanisms of the classes or components, and ensuring that they handle the abnormal situations gracefully.
  - Testing the integration of subsystems or clusters: The integration of subsystems or clusters is the process of combining the classes or components that have been tested individually or in groups, and ensuring that they work together as a coherent whole. There are different strategies and methods to perform the integration of subsystems or clusters, such as  :
    - Top-down integration: This strategy involves integrating the subsystems or clusters from the top level of the software hierarchy to the bottom level, starting with the main or driver subsystem or cluster, and then adding the subordinate or dependent subsystems or clusters one by one. This strategy allows the early testing of the major functionality and the control flow of the software, but it may require the use of stubs or dummy components to simulate the missing or incomplete subsystems or clusters.
    - Bottom-up integration: This strategy involves integrating the subsystems or clusters from the bottom level of the software hierarchy to the top level, starting with the basic or independent subsystems or clusters, and then combining them into higher-level subsystems or clusters. This strategy allows the early testing of the low-level functionality and the data flow of the software, but it may require the use of drivers or test harnesses to invoke and coordinate the subsystems or clusters.
    - Sandwich integration: This strategy involves integrating the subsystems or clusters from both the top and the bottom levels of the software hierarchy, and then meeting in the middle level. This strategy allows the simultaneous testing of the high-level and low-level functionality and the control and data flow of the software, but it may require the use of both stubs and drivers to facilitate the integration.
    - Incremental integration: This strategy involves integrating the subsystems or clusters in small increments, and testing each increment before adding the next one. This strategy allows the gradual and continuous testing of the software, and the detection and correction of errors at an early stage, but it may require the use of regression testing to ensure that the previous increments are not affected by the new ones.
    - Big-bang integration: This strategy involves integrating all the subsystems or clusters at once, and testing the software as a whole. This strategy allows the testing of the software in its final and complete form,



## Unit 7 - Testing Web Applications

- Web applications are software systems that run on web browsers and servers, and provide various functionalities and services to users over the internet.
- Testing web applications involves verifying the quality, functionality, usability, security, performance, and compatibility of web applications under different conditions and scenarios.
- Testing web applications requires a different approach and strategy than testing traditional desktop or mobile applications, due to the complexity and diversity of web technologies, architectures, and environments.
- Some of the challenges and issues that web application testing faces are:
  - Cross-browser and cross-platform compatibility: Web applications should work consistently and correctly on different browsers (such as Chrome, Firefox, Safari, etc.) and platforms (such as Windows, Linux, Mac, etc.).
  - Dynamic and interactive web elements: Web applications often use dynamic and interactive web elements (such as JavaScript, Ajax, HTML5, CSS3, etc.) that can change the content and layout of web pages without reloading them, and require more complex and sophisticated testing techniques and tools.
  - User interface and user experience: Web applications should provide a user-friendly and intuitive user interface and user experience, that meets the expectations and needs of the target users, and follows the web design principles and standards.
  - Security and privacy: Web applications should protect the confidentiality, integrity, and availability of the data and transactions of the users and the system, and prevent unauthorized access, modification, or disclosure of sensitive information, by implementing appropriate security measures and mechanisms.
  - Performance and scalability: Web applications should handle the load and traffic of multiple concurrent users and requests, and respond quickly and reliably, without compromising the functionality or quality of the service, by optimizing the web resources and components, and using suitable performance testing tools and methods.
  - Accessibility and localization: Web applications should be accessible and usable by all users, regardless of their physical, mental, or cultural differences, and comply with the web accessibility guidelines and standards, and support multiple languages and regions, by implementing proper accessibility and localization testing techniques and practices.



# Web Testing

Web testing is software testing that focuses on web applications. Web applications are software programs that run on web browsers and communicate with web servers. Web testing aims to ensure that web applications are functional, reliable, secure, compatible, and performant before they are deployed to the public .

Some of the benefits of web testing are:

- It prevents bugs and errors that can affect the user experience and the business reputation.
- It reduces development costs and time by identifying and fixing issues early in the development cycle.
- It improves performance and scalability by optimizing the web application's speed, load, and stress handling.
- It enhances security and privacy by detecting and preventing vulnerabilities and attacks.
- It ensures compatibility and usability by verifying that the web application works well across different browsers, devices, and platforms   .

Some of the types of web testing are:

- Functionality testing: It checks the functionality of the web application, such as links, forms, buttons, navigation, etc.
- Usability testing: It checks the usability of the web application, such as user interface, design, layout, content, etc.
- Compatibility testing: It checks the compatibility of the web application with different browsers, devices, operating systems, etc.
- Security testing: It checks the security of the web application, such as authentication, authorization, encryption, etc.
- Performance testing: It checks the performance of the web application, such as response time, throughput, load, stress, etc.
- Regression testing: It checks the web application for any regression issues after any changes or updates are made   .

Some of the tools and techniques used for web testing are:

- Manual testing: It involves testing the web application manually by human testers using test cases and scenarios.
- Automated testing: It involves testing the web application automatically by using software tools and scripts that simulate user actions and verify expected outcomes.
- Browser testing: It involves testing the web application on different browsers, such as Chrome, Firefox, Safari, etc.
- Device testing: It involves testing the web application on different devices, such as desktops, laptops, tablets, smartphones, etc.
- Cross-browser testing: It involves testing the web application on multiple browsers simultaneously to check for any inconsistencies or errors.
- Cross-device testing: It involves testing the web application on multiple devices simultaneously to check for any inconsistencies or errors.
- Load testing: It involves testing the web application under normal and peak load conditions to measure its performance and scalability.
- Stress testing: It involves testing the web application beyond its normal capacity to identify its breaking point and recovery time.
- Accessibility testing: It involves testing the web application for its accessibility and compliance with web standards and guidelines, such as WCAG, ADA, etc   .

Some of the challenges and best practices of web testing are:

- Challenges: Web testing can be challenging due to the complexity and diversity of web applications, the dynamic and evolving nature of web technologies, the variety and unpredictability of user behavior, the need for continuous testing and integration, the difficulty of ensuring quality and consistency across different environments, etc  .
- Best practices: Some of the best practices of web testing are: defining clear and realistic testing objectives and scope, designing and executing test cases and scenarios based on user requirements and expectations, using appropriate testing tools and techniques for different types of testing, performing testing at different stages of the development cycle, conducting testing on different browsers, devices, and platforms, prioritizing and reporting testing results and issues, following web standards and guidelines, etc  .



# User Interface Testing

User interface testing, or UI testing, is a type of testing that verifies the graphical elements of a web application, such as windows, buttons, text fields, menus, etc. UI testing ensures that the web application meets the specified requirements and provides a smooth and consistent user experience.

Some of the objectives of UI testing are:

- To check the functionality and usability of the web application
- To verify the alignment, size, color, font, and style of the UI elements
- To validate the navigation, links, and workflows of the web application
- To detect and report any errors, bugs, or defects in the UI
- To ensure the compatibility of the web application with different browsers, devices, and screen resolutions

Some of the benefits of UI testing are:

- It improves the quality and reliability of the web application
- It enhances the user satisfaction and retention
- It reduces the maintenance and support costs
- It increases the confidence and trust in the web application

Some of the challenges of UI testing are:

- It requires a lot of manual effort and time
- It is prone to human errors and inconsistencies
- It is difficult to automate and maintain
- It is affected by frequent changes in the UI design and requirements

Some of the best practices of UI testing are:

- To define clear and testable UI requirements and specifications
- To use a UI testing framework or tool that supports cross-browser and cross-device testing
- To design and execute UI test cases based on user scenarios and expected outcomes
- To prioritize and categorize UI test cases based on their importance and risk
- To perform UI testing at different stages of the development cycle, such as unit testing, integration testing, system testing, and regression testing
- To report and track UI test results and defects using a bug tracking system
- To review and update UI test cases regularly to cope with the changes in the UI design and requirements



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of usability testing for the notes of the unit 7 - testing web applications in the subject of software testing.

# Usability Testing

- Usability testing is a type of testing that evaluates how easy, efficient, and satisfying a web application is to use for the intended users.
- Usability testing can be performed at any stage of the development process, but it is usually done after the design and prototype stages, and before the launch and maintenance stages.
- Usability testing can be conducted in different ways, such as:
  - Lab testing: The users are invited to a controlled environment, such as a lab or a usability studio, where they are observed and recorded while using the web application.
  - Remote testing: The users are located in their natural settings, such as their homes or offices, and they use the web application through a remote connection, such as a video call or a screen-sharing tool.
  - Field testing: The users are visited by the testers in their natural settings, and they are observed and interviewed while using the web application in their real context.
- Usability testing can have different goals, such as:
  - Evaluating the usability of the web application against a set of criteria, such as usability heuristics, standards, or guidelines.
  - Comparing the usability of the web application with that of its competitors or alternatives.
  - Identifying the usability problems and issues of the web application and suggesting possible solutions or improvements.
  - Measuring the user satisfaction and loyalty of the web application and its features.
- Usability testing can involve different methods and techniques, such as:
  - Task analysis: The users are asked to perform a set of tasks or scenarios that represent the typical or critical use cases of the web application.
  - Think aloud: The users are asked to verbalize their thoughts, feelings, and actions while using the web application.
  - Questionnaires and surveys: The users are asked to fill out a form or a questionnaire that measures their opinions, preferences, and feedback on the web application.
  - Interviews and focus groups: The users are asked to participate in a discussion or a conversation with the testers or other users about their experiences and impressions of the web application.
  - Eye tracking: The users' eye movements and gaze patterns are tracked and recorded while using the web application.
  - Biometrics: The users' physiological responses, such as heart rate, blood pressure, skin conductance, or facial expressions, are measured and recorded while using the web application.



# Security Testing for Web Applications

Security testing is a process of identifying, preventing, and mitigating security vulnerabilities in web applications. It involves assessing the security of web applications by examining their code, architecture, and deployment environment. Security testing aims to protect the confidentiality, integrity, and availability of web applications and their data from malicious attacks.

Some of the common security risks and threats for web applications are:

- Injection attacks, such as SQL injection, command injection, and cross-site scripting (XSS)
- Broken authentication and session management, such as weak passwords, session hijacking, and credential theft
- Sensitive data exposure, such as unencrypted data, insecure storage, and improper access control
- Cross-site request forgery (CSRF), which allows an attacker to perform unauthorized actions on behalf of a legitimate user
- Security misconfiguration, such as default settings, outdated software, and improper error handling
- Insecure deserialization, which allows an attacker to execute arbitrary code or tamper with data by manipulating serialized objects
- Using components with known vulnerabilities, such as third-party libraries, frameworks, and plugins
- Insufficient logging and monitoring, which prevents timely detection and response to security incidents

The steps to perform security testing for web applications are:

1. Understanding business requirements: The first step is to understand the business expectations and security goals of the web application. This includes identifying the scope, objectives, and criteria of security testing, as well as the relevant regulations, standards, and best practices to follow.
2. Gathering data for security testing: The second step is to collect information about the web application and its environment, such as the architecture, design, functionality, features, components, dependencies, and interfaces. This also involves identifying the potential attack vectors, threat actors, and attack scenarios for the web application.
3. Creating a test plan and a traceability matrix: The third step is to create a test plan that defines the strategy, scope, approach, methods, tools, and resources for security testing. A traceability matrix is also created to map the security requirements to the test cases and ensure the coverage and completeness of security testing.
4. Deciding the tool for security testing: The fourth step is to select the appropriate tool or tools for security testing, based on the type, complexity, and functionality of the web application. Some of the common tools for security testing are:

  - Static analysis tools, which scan the source code of the web application for security vulnerabilities and coding errors
  - Dynamic analysis tools, which test the web application in a running state for security vulnerabilities and runtime errors
  - Penetration testing tools, which simulate real-world attacks on the web application to exploit security vulnerabilities and test the defense mechanisms
  - Vulnerability scanners, which scan the web application and its environment for known security vulnerabilities and provide recommendations for remediation
  - Security testing frameworks, which provide a comprehensive and standardized methodology for security testing, such as the OWASP Web Security Testing Guide (WSTG)

5. Executing security test cases for web application: The fifth step is to execute the security test cases for the web application, using the selected tool or tools. The security test cases should cover the following aspects of security testing:

  - Authentication testing, which verifies the identity and access rights of the users and the web application
  - Authorization testing, which verifies the permissions and restrictions of the users and the web application
  - Session management testing, which verifies the security and validity of the sessions and the cookies
  - Data validation testing, which verifies the input and output data of the web application for security vulnerabilities and errors
  - Error handling testing, which verifies the error messages and logs of the web application for security vulnerabilities and information leakage
  - Cryptography testing, which verifies the encryption and decryption of the data and the communication of the web application
  - Business logic testing, which verifies the functionality and logic of the web application for security vulnerabilities and flaws
  - Denial of service testing, which verifies the availability and performance of the web application under high load and stress conditions

6. Creating a detailed report: The final step is to create a detailed report that summarizes the results and findings of security testing. The report should include the following information:

  - The scope, objectives, and criteria of security testing
  - The tools and methods used for security testing
  - The test cases and test results of security testing
  - The security vulnerabilities and risks identified and their severity and impact
  - The recommendations and suggestions for remediation and improvement
  - The limitations and challenges of security testing
  - The lessons learned and best practices of security testing

Security



# Performance Testing for Web Applications

Performance testing is a type of software testing that aims to evaluate how well a web application performs under various conditions, such as user load, network latency, server response time, etc. Performance testing is important for ensuring that the web application meets the expected quality standards and provides a satisfactory user experience.

Some of the benefits of performance testing for web applications are:

- It helps to identify and eliminate performance bottlenecks and optimize the web application for faster and smoother operation.
- It helps to ensure that the web application can handle the expected and peak user traffic without compromising on functionality or reliability.
- It helps to measure and compare the performance of different versions or components of the web application and identify areas for improvement.
- It helps to evaluate the scalability and stability of the web application and determine the optimal resource utilization and allocation.
- It helps to prevent potential performance issues and failures that could affect the reputation and revenue of the web application.

Some of the types of performance testing for web applications are:

- Load testing: It simulates the normal and expected user load on the web application and measures its performance metrics, such as response time, throughput, error rate, etc.
- Stress testing: It simulates the extreme and unexpected user load on the web application and measures its performance limits, such as maximum capacity, breaking point, recovery time, etc.
- Endurance testing: It simulates the sustained and continuous user load on the web application and measures its performance over a long period of time, such as memory leaks, resource consumption, etc.
- Spike testing: It simulates the sudden and unpredictable user load on the web application and measures its performance under rapid changes, such as peak demand, load balancing, etc.
- Volume testing: It simulates the large and varied data load on the web application and measures its performance under different data volumes, such as database queries, storage capacity, etc.
- Scalability testing: It simulates the increasing and decreasing user load on the web application and measures its performance under different scalability scenarios, such as horizontal scaling, vertical scaling, etc.

Some of the steps for performing performance testing for web applications are:

- Identify the testing environment: It involves defining the hardware, software, network, and tools that will be used for the performance testing and ensuring that they are similar to the production environment.
- Design the test cases and scenarios: It involves specifying the performance testing objectives, requirements, and criteria, such as the type of performance testing, the user load, the performance metrics, the expected results, etc.
- Execute the test cases and scenarios: It involves running the performance testing tools and scripts that simulate the user load and actions on the web application and collecting the performance data and logs.
- Analyze the test results and reports: It involves processing and interpreting the performance data and logs and generating the performance reports and graphs that show the performance metrics and trends.
- Identify and resolve the performance issues: It involves comparing the actual and expected performance results and identifying the performance gaps and bottlenecks and suggesting the performance improvement actions and recommendations.



# Database testing for the notes of the Unit 7 - Testing Web Applications in the subject of Software Testing

- Database testing is a type of software testing that checks the schema, tables, triggers, etc. of the database under test.
- Database testing also checks data integrity and consistency, which means that the data is accurate, complete, and reliable.
- Database testing is important for web applications because it protects the web app from vulnerabilities like data loss, saves aborted transaction data, and prevents unauthorized access to information.
- Database testing involves creating complex queries to load/stress test the database and check its responsiveness.
- Database testing also involves checking the data manipulation operations such as insert, update, delete, and retrieve.
- Database testing can be done using various tools such as MS-Access, MS SQL Server, SQL Server, Oracle, Oracle Financial, MySQL, PostgreSQL, DB2, Toad, Admirer, etc.
- Database testing can be performed at different levels such as unit testing, integration testing, system testing, and acceptance testing.
- Database testing can be done using different techniques such as black-box testing, white-box testing, gray-box testing, and exploratory testing.
- Database testing can be done using different methods such as structural testing, functional testing, non-functional testing, and regression testing.
- Database testing can be done using different strategies such as top-down, bottom-up, sandwich, and hybrid.
- Database testing can be done using different types of test cases such as positive test cases, negative test cases, boundary test cases, and equivalence test cases.
- Database testing can be done using different types of test data such as valid data, invalid data, null data, and random data.
- Database testing can be done using different types of test scenarios such as normal scenarios, abnormal scenarios, error scenarios, and exception scenarios.
- Database testing can be done using different types of test scripts such as manual test scripts, automated test scripts, and hybrid test scripts.
- Database testing can be done using different types of test reports such as summary reports, detailed reports, and graphical reports.
- Database testing can be done using different types of test metrics such as defect density, defect severity, defect priority, defect resolution time, defect removal efficiency, test coverage, test effectiveness, and test efficiency.
- Database testing can be done using different types of test tools such as test management tools, test design tools, test execution tools, test data generation tools, test data comparison tools, test data validation tools, and test data migration tools.
- Database testing can be done using different types of test environments such as development environment, testing environment, staging environment, and production environment.
- Database testing can be done using different types of test standards such as IEEE, ISO, CMMI, and ISTQB.
- Database testing can be done using different types of test best practices such as planning, designing, executing, reporting, and improving.



# Post Deployment Testing for the notes of the Unit 7 - Testing Web Applications in the subject of Software Testing

- Post deployment testing is a type of testing in which the software is tested after it is being deployed to production.
- The purpose of post deployment testing is to ensure that the software functions as intended in the real environment and meets the user expectations.
- Post deployment testing involves the following activities  :
  - Post-deployment verification: The QA or Test lead verifies the software application as per the requirements and the test plans and test cases of the software application. This includes checking the configuration, functionality, performance, security, and usability of the software.
  - User acceptance testing: The end users or the stakeholders test the software to validate that it meets their needs and expectations. This may involve conducting surveys, interviews, feedback sessions, or usability tests with the users.
  - Monitoring and logging: The software is monitored and logged for any errors, bugs, performance issues, or user feedback. This helps to identify and resolve any issues that may arise in production and improve the quality of the software.
  - Maintenance and support: The software is maintained and supported by the development team or the service provider to ensure its availability, reliability, and security. This may involve providing patches, updates, bug fixes, or enhancements to the software.
- Post deployment testing is an essential part of the software development life cycle and the continuous integration and continuous delivery (CI/CD) pipeline  .
- Post deployment testing helps to ensure the quality, reliability, and user satisfaction of the software  .

