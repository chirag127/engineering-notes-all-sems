### Storage Allocation in Block Structured Language

Storage allocation is an important aspect of programming languages as it is responsible for managing the memory and storage space required to execute a program. In block structured languages, storage allocation is done at the block level, which means that each block of code has its own set of variables and memory space.

#### Types of Storage Allocation

There are two types of storage allocation in block structured languages - static and dynamic.

##### Static Storage Allocation

Static storage allocation is done at compile time and the memory space is allocated to the variables before the program is executed. This type of storage allocation is used for variables that have a fixed memory size and do not change during the execution of the program. 

Advantages of Static Storage Allocation:
- It is faster than dynamic storage allocation as the memory space is already allocated before the program is executed.
- It is more efficient as the memory space is fixed and does not change during the execution of the program.

Disadvantages of Static Storage Allocation:
- It cannot be used for variables that have a dynamic size.
- It wastes memory space if the variable is not used or is only used for a short period of time.

##### Dynamic Storage Allocation

Dynamic storage allocation is done at runtime and the memory space is allocated to the variables during the execution of the program. This type of storage allocation is used for variables that have a dynamic size and can change during the execution of the program.

Advantages of Dynamic Storage Allocation:
- It can be used for variables that have a dynamic size.
- It is more memory efficient as the memory space is allocated only when required.

Disadvantages of Dynamic Storage Allocation:
- It is slower than static storage allocation as the memory space is allocated during the execution of the program.
- It is less efficient as the memory space can change during the execution of the program.

#### Examples of Storage Allocation

Let's take an example to understand storage allocation in block structured languages:

```
1  program example;
2  var
3     a, b: integer;
4  begin
5     a := 10;
6     b := 20;
7     if a > b then
8        begin
9           writeln('a is greater than b');
10       end
11     else
12       begin
13          writeln('b is greater than a');
14       end;
15  end.
```

In the above example, the variables `a` and `b` are declared in line 3 and their memory space is allocated during the execution of the program. The values of `a` and `b` are assigned in lines 5 and 6 respectively. The if-else statement in lines 7-14 checks the values of `a` and `b` and outputs the result accordingly. 

#### Conclusion

In conclusion, storage allocation is an important aspect of block structured languages as it is responsible for managing the memory and storage space required to execute a program. Static and dynamic storage allocation are the two types of storage allocation used in block structured languages. While static storage allocation is faster and more efficient, dynamic storage allocation is more flexible and memory efficient.