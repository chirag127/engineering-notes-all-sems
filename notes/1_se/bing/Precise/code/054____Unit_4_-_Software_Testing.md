## Unit 4 - Software Testing

Software testing is the process of evaluating a software application to ensure that it meets the specified requirements and produces the desired results. This is done by executing the software under controlled conditions and verifying that it behaves as expected. There are several types of software testing, including unit testing, integration testing, system testing, and acceptance testing.

Here is an example of a simple unit test in Python:

```python
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
```

This test checks that the `add` function correctly adds two numbers together. The `assert` statements verify that the function returns the expected result for each test case. If any of the assertions fail, the test will fail and an error message will be displayed.
