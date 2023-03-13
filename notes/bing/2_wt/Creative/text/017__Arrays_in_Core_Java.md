#### Arrays in Core Java

- An array is a collection of elements of the same data type that are stored in contiguous memory locations.
- An array can be declared using the syntax: `dataType[] arrayName;` or `dataType arrayName[];`
- An array can be initialized using the syntax: `arrayName = new dataType[size];` or `arrayName = {element1, element2, ..., elementN};`
- The size of an array is fixed and cannot be changed once it is created. The size can be obtained using the `length` attribute of the array: `arrayName.length`
- The elements of an array can be accessed using the index operator: `arrayName[index]`. The index starts from 0 and goes up to size-1.
- An array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- An array can be returned from a method using the syntax: `return arrayName;`
- An array can be multidimensional, meaning it can have more than one dimension. For example, a two-dimensional array can be declared using the syntax: `dataType[][] arrayName;`
- A two-dimensional array can be initialized using the syntax: `arrayName = new dataType[rows][columns];` or `arrayName = {{element1, element2, ..., elementN}, {element1, element2, ..., elementN}, ..., {element1, element2, ..., elementN}};`
- The elements of a two-dimensional array can be accessed using the syntax: `arrayName[row][column]`. The row and column indices start from 0 and go up to rows-1 and columns-1 respectively.
- A two-dimensional array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- A two-dimensional array can be returned from a method using the syntax: `return arrayName;`
- An array can be nested inside another array, creating a jagged array. For example, a jagged array can be declared using the syntax: `dataType[][] arrayName;`
- A jagged array can be initialized using the syntax: `arrayName = new dataType[size][];` or `arrayName = {{element1, element2, ..., elementN}, {element1, element2}, ..., {element1, element2, ..., elementN}};`
- The elements of a jagged array can be accessed using the syntax: `arrayName[index1][index2]`. The index1 starts from 0 and goes up to size-1. The index2 starts from 0 and goes up to the length of the subarray at index1.
- A jagged array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- A jagged array can be returned from a method using the syntax: `return arrayName;`