# Operators in JS

- Operators are symbols that perform some operations on one or more operands (values or variables).
- Operators can be classified into different types based on the number of operands, the type of operands, and the functionality of the operator.
- Some of the common types of operators in JS are:

  - Arithmetic operators: These operators perform basic mathematical operations such as addition, subtraction, multiplication, division, remainder, exponentiation, increment, and decrement. For example:

    - `5 + 3` evaluates to `8`
    - `7 - 2` evaluates to `5`
    - `4 * 3` evaluates to `12`
    - `9 / 3` evaluates to `3`
    - `10 % 3` evaluates to `1`
    - `2 ** 3` evaluates to `8`
    - `x++` increments the value of `x` by `1`
    - `y--` decrements the value of `y` by `1`

  - Assignment operators: These operators assign a value to a variable. The basic assignment operator is `=`. There are also compound assignment operators that combine an arithmetic operator with the assignment operator. For example:

    - `x = 5` assigns the value `5` to the variable `x`
    - `y += 3` is equivalent to `y = y + 3`
    - `z -= 2` is equivalent to `z = z - 2`
    - `a *= 4` is equivalent to `a = a * 4`
    - `b /= 2` is equivalent to `b = b / 2`
    - `c %= 3` is equivalent to `c = c % 3`
    - `d **= 2` is equivalent to `d = d ** 2`

  - Comparison operators: These operators compare two operands and return a boolean value (`true` or `false`) based on the result of the comparison. There are two types of comparison operators: equality and relational. For example:

    - Equality operators: These operators check if the operands are equal or not. There are two types of equality operators: strict and loose. Strict equality operators (`===` and `!==`) compare the operands without converting their types, while loose equality operators (`==` and `!=`) convert the operands to the same type before comparing them. For example:

      - `5 === 5` evaluates to `true`
      - `5 === '5'` evaluates to `false`
      - `5 == 5` evaluates to `true`
      - `5 == '5'` evaluates to `true`
      - `5 !== 5` evaluates to `false`
      - `5 !== '5'` evaluates to `true`
      - `5 != 5` evaluates to `false`
      - `5 != '5'` evaluates to `false`

    - Relational operators: These operators check if the operands are greater than, less than, greater than or equal to, or less than or equal to each other. For example:

      - `5 > 3` evaluates to `true`
      - `5 < 3` evaluates to `false`
      - `5 >= 5` evaluates to `true`
      - `5 <= 5` evaluates to `true`
      - `5 >= 6` evaluates to `false`
      - `5 <= 4` evaluates to `false`

  - Logical operators: These operators perform logical operations on one or more operands and return a boolean value based on the result of the operation. There are three logical operators in JS: AND (`&&`), OR (`||`), and NOT (`!`). For example:

    - AND operator: This operator returns `true` if both operands are `true`, and `false` otherwise. For example:

      - `true && true` evaluates to `true`
      - `true && false` evaluates to `false`
      - `false && true` evaluates to `false`
      - `false && false` evaluates to `false`

    - OR operator: This operator returns `true` if either operand is `true`, and `false` otherwise. For example:

      - `true || true` evaluates to `true`
      - `true || false` evaluates to `true`
      - `false || true` evaluates to `true`
      - `false || false` evaluates to `false`

    - NOT operator: This operator returns the opposite of the operand. For example:

      - `!true` evaluates to `false`
      - `!false` evaluates to `true`

  - String operators: These operators perform operations on