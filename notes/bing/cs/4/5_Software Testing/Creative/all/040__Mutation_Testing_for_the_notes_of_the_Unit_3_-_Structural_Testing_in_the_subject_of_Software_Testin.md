### Mutation Testing for the notes of the Unit 3 - Structural Testing in the subject of Software Testing

- Mutation testing is a form of white box testing in which testers change specific components of an application's source code to ensure a software test suite will be able to detect the changes .
- Mutation testing is used to design new software tests and evaluate the quality of existing software tests .
- Mutation testing involves modifying a program in small ways, such as changing a variable, operator, or statement, to create many versions called mutants .
- Each mutant is expected to behave differently from the original program and produce an error or a failure .
- A test case is applied to the original program and also to the mutant program. A test case is said to kill a mutant if it causes the mutant to produce a different output from the original program.
- The goal of mutation testing is to create a test suite that can kill all the mutants, or at least a high percentage of them .
- The quality of a test suite can be measured by the mutation score, which is the ratio of the number of killed mutants to the total number of mutants .
- Mutation testing can help the tester develop effective tests or locate weaknesses in the test data used for the program.
- Mutation testing can also help the tester find faults or bugs in the original program that are not detected by the test suite .
- Mutation testing can be applied at different levels of testing, such as unit testing, integration testing, or system testing .
- Mutation testing can be performed manually or with the help of automated tools .
- Mutation testing has some advantages, such as:
  - It can improve the quality and coverage of the test suite .
  - It can reveal subtle or hidden errors in the program .
  - It can provide feedback to the tester about the effectiveness of the test cases .
- Mutation testing also has some disadvantages, such as:
  - It can be computationally expensive and time-consuming, as it requires generating and executing many mutants .
  - It can be difficult to determine the validity and equivalence of the mutants .
  - It can be challenging to apply mutation testing to complex or large programs .

#### Example of mutation testing

Suppose we have the following original program that checks if a person is eligible for a mother-daughter program based on their ages:

```javascript
function isEligible(mother_age, daughter_age) {
  if (mother_age >= 18 && daughter_age <= 12) {
    return true;
  } else {
    return false;
  }
}
```

We can create some mutants by changing the operators or values in the program, such as:

```javascript
// Mutant 1: Change >= to >
function isEligible(mother_age, daughter_age) {
  if (mother_age > 18 && daughter_age <= 12) {
    return true;
  } else {
    return false;
  }
}

// Mutant 2: Change <= to <
function isEligible(mother_age, daughter_age) {
  if (mother_age >= 18 && daughter_age < 12) {
    return true;
  } else {
    return false;
  }
}

// Mutant 3: Change 18 to 19
function isEligible(mother_age, daughter_age) {
  if (mother_age >= 19 && daughter_age <= 12) {
    return true;
  } else {
    return false;
  }
}

// Mutant 4: Change 12 to 13
function isEligible(mother_age, daughter_age) {
  if (mother_age >= 18 && daughter_age <= 13) {
    return true;
  } else {
    return false;
  }
}
```

We can then write some test cases to test the original program and the mutants, such as:

```javascript
// Test case 1: mother_age = 20, daughter_age = 10
// Expected output: true
// Actual output for original program: true
// Actual output for mutant 1: true