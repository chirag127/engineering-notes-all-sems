### Equivalence Class Testing for the notes of the Unit 2 - Functional Testing in the subject of Software Testing

Equivalence Class Testing is a black-box testing technique that divides the input data of a software unit into partitions of equivalent data from which test cases can be derived. The idea is to select one representative value from each partition or equivalence class, and use it as a test case. This technique tries to reduce the number of test cases that must be developed, while still covering all possible scenarios and errors.

The steps to perform Equivalence Class Testing are:

- Identify the input and output attributes of the software unit.
- Analyze the requirements specification and identify the valid and invalid ranges or conditions for each attribute.
- Partition the valid ranges or conditions into equivalence classes, such that all the values in one class are expected to behave similarly.
- Partition the invalid ranges or conditions into equivalence classes, such that all the values in one class are expected to cause an error or an exception.
- Select one representative value from each equivalence class as a test case.
- Execute the test cases and verify the expected results.

An example of Equivalence Class Testing is the next-date problem, which is to find the next date for a given date in the format of day-month-year. The input attributes are day, month and year, and the output attribute is the next date. The valid and invalid ranges or conditions for each attribute are:

- Day: valid range is 1 to 31, depending on the month and year. Invalid range is anything outside the valid range, such as 0, -1, 32, etc.
- Month: valid range is 1 to 12. Invalid range is anything outside the valid range, such as 0, -1, 13, etc.
- Year: valid range is 1800 to 2048. Invalid range is anything outside the valid range, such as 1799, 2049, etc.

The equivalence classes for each attribute are:

- Day: D1: day between 1 to 28; D2: 29; D3: 30; D4: 31
- Month: M1: month has 30 days; M2: month has 31 days; M3: month is February
- Year: Y1: year is a leap year; Y2: year is a normal year

The output classes are:

- Increment day
- Reset day and increment month
- Increment year
- Invalid date

The test cases can be selected as follows:

- Test Case 1: D1-M1-Y1 -> Increment day
- Test Case 2: D1-M1-Y2 -> Increment day
- Test Case 3: D1-M2-Y1 -> Increment day
- Test Case 4: D1-M2-Y2 -> Increment day
- Test Case 5: D1-M3-Y1 -> Increment day
- Test Case 6: D1-M3-Y2 -> Increment day
- Test Case 7: D2-M1-Y1 -> Increment day
- Test Case 8: D2-M1-Y2 -> Increment day
- Test Case 9: D2-M2-Y1 -> Increment day
- Test Case 10: D2-M2-Y2 -> Increment day
- Test Case 11: D2-M3-Y1 -> Reset day and increment month
- Test Case 12: D2-M3-Y2 -> Invalid date
- Test Case 13: D3-M1-Y1 -> Reset day and increment month
- Test Case 14: D3-M1-Y2 -> Reset day and increment month
- Test Case 15: D3-M2-Y1 -> Increment day
- Test Case 16: D3-M2-Y2 -> Increment day
- Test Case 17: D3-M3-Y1 -> Invalid date
- Test Case 18: D3-M3-Y2 -> Invalid date
- Test Case 19: D4-M1-Y1 -> Invalid date
- Test Case 20: D4-M1-Y2 -> Invalid date
- Test Case 21: D4-M2-Y1 -> Reset day and increment month
- Test Case 22: D4-M2-Y2 -> Reset day and increment month
- Test Case 23: D4-M3-Y1 -> Invalid date
- Test Case 24: D4-M3-Y2 -> Invalid date
- Test Case 25: D1-M12-Y1 -> Increment day
- Test Case 26: D1-M