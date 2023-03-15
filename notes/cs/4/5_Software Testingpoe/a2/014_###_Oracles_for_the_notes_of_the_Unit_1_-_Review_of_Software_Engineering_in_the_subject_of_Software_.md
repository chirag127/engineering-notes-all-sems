 Here is the content in markdown format for the given topic:

### Oracles for the notes of the Unit 1 - Review of Software Engineering in the subject of Software Testing

- An oracle is a mechanism or process used to determine whether the actual output of a software system is correct with respect to the expected output.
- Oracles are important in software testing as they are used to determine whether the test case has passed or failed. Without an oracle, a tester cannot determine whether the system was working correctly or not for a given test input.
- Some common types of oracles include:
    - Expected Output: The actual output is compared with expected output calculated manually or specified in requirements.
    - Previously computed results: The actual output is compared with results computed previously, possibly by an independent system.
    - Expert opinions: Experts evaluate whether the actual output is reasonable given the input.
    - Formally proven properties: Some properties of the output can be proven formally from the specification and the proven properties can be used for oracle comparison.
    - Visual inspection: The human tester inspects the output and determines correctness.
    - Contracts or assertions: The code itself contains assertions or contracts that can be used to verify correctness.
- The pros and cons of different oracles should be considered while selecting an appropriate oracle for a system under test. An ideal oracle should be automatic, fast, inexpensive, and provide reliable correctness assessments. However, selecting such an ideal oracle is challenging in practice due to various trade-offs.
- Some useful mnemonics and tips to remember the oracles are:
    - EO: Expected Output
    - PCR: Previously Computed Results
    - EO: Expert Opinions
    - FP: Formally Proven properties
    - VI: Visual Inspection
    - CA: Contracts or Assertions