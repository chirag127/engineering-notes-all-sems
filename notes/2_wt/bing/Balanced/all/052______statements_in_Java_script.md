#### Statements in JavaScript

- A statement is a piece of code that performs some action or produces some value.
- Statements can be simple or complex, depending on the number of sub-statements they contain.
- Statements are executed in order, from top to bottom, unless there is a control flow statement that changes the order of execution.
- Statements are usually terminated by a semicolon (;), but it is optional in most cases. However, it is recommended to use semicolons to avoid ambiguity and errors.
- Some examples of simple statements are:

```javascript
var x = 10; // variable declaration and assignment
console.log(x); // output statement
x++; // increment statement
return x; // return statement
```

- Some examples of complex statements are:

```javascript
if (x > 10) { // if statement with a block of sub-statements
  console.log("x is greater than 10");
  x--;
} else { // else statement with another block of sub-statements
  console.log("x is less than or equal to 10");
  x++;
}

for (var i = 0; i < 10; i++) { // for loop statement with a block of sub-statements
  console.log(i);
}

function add(a, b) { // function declaration statement with a block of sub-statements
  return a + b;
}
```

- Some common types of statements in JavaScript are:

  - Declaration statements: These statements declare variables, functions, classes, or modules. They use keywords such as `var`, `let`, `const`, `function`, `class`, or `import`.
  - Expression statements: These statements evaluate an expression and produce a value. They can be assignments, calls, operations, literals, or any other valid expression.
  - Control flow statements: These statements alter the order of execution of the statements. They can be conditional statements (such as `if`, `else`, `switch`, `case`), loop statements (such as `for`, `while`, `do-while`, `break`, `continue`), or jump statements (such as `return`, `throw`, `try`, `catch`, `finally`).
  - Empty statement: This statement does nothing. It is just a semicolon (;) by itself. It can be used to fill a place where a statement is expected but not needed.

- Some mnemonics and learning tricks for statements in JavaScript are:

  - Remember the acronym D.E.C.L.A.R.E. for the types of declaration statements: `var`, `let`, `const`, `function`, `class`, `import`, and `export`.
  - Remember the acronym C.L.O.J.U.R.E. for the types of control flow statements: `if`, `else`, `switch`, `case`, `for`, `while`, `do-while`, `break`, `continue`, `return`, `throw`, `try`, `catch`, `finally`, and `with`.
  - Remember the acronym E.S.C.A.P.E. for the types of expression statements: `=`, `()`, `+`, `-`, `*`, `/`, `%`, `**`, `++`, `--`, `!`, `~`, `&&`, `||`, `?`, `:`, `==`, `===`, `!=`, `!==`, `<`, `<=`, `>`, `>=`, `&`, `|`, `^`, `<<`, `>>`, `>>>`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `&=`, `|=`, `^=`, `<<=`, `>>=`, `>>>=`, `=>`, `[]`, `{}`, `.``, `,`, `;`, and `` ` ``.
  - Remember the acronym S.E.M.I. for when to use semicolons: `S`tatement, `E`xpression, `M`ultiple lines, `I`nitializer.