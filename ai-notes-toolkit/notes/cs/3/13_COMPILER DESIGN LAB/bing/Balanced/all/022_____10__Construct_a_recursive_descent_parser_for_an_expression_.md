# 10. Construct a recursive descent parser for an expression.

A recursive descent parser is a type of top-down parser that uses a set of recursive procedures to process the input. Each procedure corresponds to a non-terminal symbol in the grammar of the language. The parser starts with the start symbol and recursively applies the rules of the grammar until it either accepts or rejects the input.

To construct a recursive descent parser for an expression, we need to follow these steps:

- Define the grammar of the expression language. For example, we can use the following grammar to parse arithmetic expressions with addition, subtraction, multiplication, division, and parentheses:

```
E -> T + E | T - E | T
T -> F * T | F / T | F
F -> (E) | num
```

- Write a procedure for each non-terminal symbol in the grammar. The procedure should take the input string as a parameter and return a boolean value indicating whether the input matches the corresponding non-terminal symbol. The procedure should also advance the input pointer to the next character after the matched part. For example, we can write the following procedures in pseudocode:

```
// Procedure for E -> T + E | T - E | T
function E(input) {
  // Save the current input pointer
  let backup = input.pointer
  // Try to match T + E
  if T(input) and input.current == '+' {
    // Advance the input pointer
    input.pointer++
    // Try to match E
    if E(input) {
      // Return true if both T and E are matched
      return true
    }
  }
  // Restore the input pointer
  input.pointer = backup
  // Try to match T - E
  if T(input) and input.current == '-' {
    // Advance the input pointer
    input.pointer++
    // Try to match E
    if E(input) {
      // Return true if both T and E are matched
      return true
    }
  }
  // Restore the input pointer
  input.pointer = backup
  // Try to match T
  if T(input) {
    // Return true if T is matched
    return true
  }
  // Return false if none of the alternatives are matched
  return false
}

// Procedure for T -> F * T | F / T | F
function T(input) {
  // Save the current input pointer
  let backup = input.pointer
  // Try to match F * T
  if F(input) and input.current == '*' {
    // Advance the input pointer
    input.pointer++
    // Try to match T
    if T(input) {
      // Return true if both F and T are matched
      return true
    }
  }
  // Restore the input pointer
  input.pointer = backup
  // Try to match F / T
  if F(input) and input.current == '/' {
    // Advance the input pointer
    input.pointer++
    // Try to match T
    if T(input) {
      // Return true if both F and T are matched
      return true
    }
  }
  // Restore the input pointer
  input.pointer = backup
  // Try to match F
  if F(input) {
    // Return true if F is matched
    return true
  }
  // Return false if none of the alternatives are matched
  return false
}

// Procedure for F -> (E) | num
function F(input) {
  // Save the current input pointer
  let backup = input.pointer
  // Try to match (E)
  if input.current == '(' {
    // Advance the input pointer
    input.pointer++
    // Try to match E
    if E(input) and input.current == ')' {
      // Advance the input pointer
      input.pointer++
      // Return true if both ( and E and ) are matched
      return true
    }
  }
  // Restore the input pointer
  input.pointer = backup
  // Try to match num
  if isNum(input.current) {
    // Advance the input pointer
    input.pointer++
    // Return true if num is matched
    return true
  }
  // Return false if none of the alternatives are matched
  return false
}

// Helper function to check if a character is a digit
function isNum(char) {
  return char >= '0' and char <= '9'
}
```

- Call the procedure for the start symbol with the input string and check the result. If the result is true and the input pointer reaches the end of the string, the input is accepted. Otherwise, the input is rejected. For example, we can write the following function to parse an expression:

```
// Function

```
