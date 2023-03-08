 Here is the content in markdown format for the topic ### statements that alter the flow of control for the notes of the Unit 3 - Syntax-directed Translation in the subject of Compiler Design:

### If-then-else statements

- If-then-else statements alter the flow of control depending on a condition.
- The syntax is:

```
if (condition) then
    statements
else
    statements
end if
```

- If the condition evaluates to true, then the then block statements are executed.
- If the condition evaluates to false, then the else block statements are executed.
- Only one of the then or else blocks are executed, not both.
- Examples:

```
if (x > y) then
    print("x is greater than y")
else
    print("x is not greater than y")
end if
```

### Case statements

- Case statements alter the flow of control based on a variable value.
- The syntax is:

```
case variable of
    value1:
        statements
    value2:
        statements
    ...
end case
```

- The variable is evaluated and matched against the different case values.
- When a match is found, the corresponding statements are executed.
- If no match is found, no statements are executed.
- Examples:

```
case x of
    1:
        print("x is 1")
    2:
        print("x is 2")
end case
```

[Detailed explanations, examples, ascii diagrams, etc can be added here for the topics]