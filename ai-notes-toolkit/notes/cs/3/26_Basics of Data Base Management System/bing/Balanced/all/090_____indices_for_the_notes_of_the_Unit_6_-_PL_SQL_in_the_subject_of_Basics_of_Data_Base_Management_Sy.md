# Unit 6 - PL/SQL

## Introduction

- PL/SQL stands for Procedural Language/Structured Query Language.
- It is an extension of SQL that allows users to write procedural code in a database environment.
- It supports variables, constants, data types, operators, expressions, control structures, loops, functions, procedures, triggers, packages, cursors, exceptions, and arrays.
- It can be used to create and execute stored procedures, functions, and triggers, which are reusable blocks of code that can perform complex tasks and improve performance.
- It can also be used to embed SQL statements in a procedural code, which can handle errors and manipulate data more efficiently.

## Advantages of PL/SQL

- PL/SQL allows users to combine the power of SQL with the flexibility of procedural programming.
- PL/SQL can reduce network traffic and improve performance by executing multiple SQL statements in a single block of code on the server side, rather than sending them one by one from the client side.
- PL/SQL can enhance the security and integrity of data by enforcing business rules and logic in the database layer, rather than relying on the application layer.
- PL/SQL can simplify the maintenance and debugging of complex applications by modularizing the code into reusable and self-contained units.
- PL/SQL can increase the portability and compatibility of applications by following the ANSI/ISO SQL standards and running on any Oracle platform.

## PL/SQL Architecture

- PL/SQL is a block-structured language, which means that the code is organized into logical units called blocks.
- A block consists of three sections: declaration, executable, and exception.
- The declaration section defines the variables, constants, cursors, and user-defined data types that are used in the block.
- The executable section contains the SQL statements and PL/SQL statements that perform the main logic of the block.
- The exception section handles the errors and exceptions that may occur during the execution of the block.
- A block can be nested inside another block, creating a hierarchical structure of blocks.
- A block can be named or anonymous, depending on whether it has an identifier or not.
- A named block can be a stored procedure, function, or trigger, which can be invoked by other blocks or applications.
- An anonymous block is a one-time block that is not stored in the database and is executed only once.