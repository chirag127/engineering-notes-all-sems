#### Pseudo Codes in Software Design

Pseudo code is a term which is often used in programming and algorithm based fields. It is a methodology that allows the programmer to represent the implementation of an algorithm. Simply, we can say that it’s the cooked up representation of an algorithm.

Pseudo code is an important part of designing an algorithm, it helps the programmer in planning the solution to the problem as well as the reader in understanding the approach to the problem. Pseudo code is an intermediate state between algorithm and program that plays supports the transition of the algorithm into the program.

Pseudo code does not use any programming language in its representation instead it uses the simple English language text as it is intended for human understanding rather than machine reading. Pseudo code acts as the bridge between your brain and computer’s code executor. It allows you to plan instructions which follow a logical pattern, without including all of the technical details.

Since pseudo code is an informal method of program design, you don’t have to obey any set-out rules. You make the rules yourself. Pseudo code is a great way of getting started with software programming as a beginner. Pseudo code is a technique used to describe the distinct steps of an algorithm in a manner that’s easy to understand for anyone with basic programming knowledge.

Here is an example of pseudo code for finding the maximum element in an array:

```
// declare an array of numbers
array = [10, 20, 30, 40, 50]

// assume the first element is the maximum
max = array[0]

// loop through the array from the second element
for i = 1 to array.length - 1
  // compare the current element with the maximum
  if array[i] > max
    // update the maximum
    max = array[i]
  end if
end for

// print the maximum
print max
```