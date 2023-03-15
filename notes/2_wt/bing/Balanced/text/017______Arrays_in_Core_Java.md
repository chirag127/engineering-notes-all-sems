#### Arrays in Core Java

- An array is a collection of elements of the same data type that are stored in contiguous memory locations.
- An array can be declared using the syntax: `dataType[] arrayName;` or `dataType arrayName[];`
- An array can be initialized using the syntax: `arrayName = new dataType[size];` or `arrayName = {element1, element2, ...};`
- The size of an array is fixed and cannot be changed once it is created. The size can be obtained using the `length` property of the array: `arrayName.length`
- The elements of an array can be accessed using the index operator: `arrayName[index]`. The index starts from 0 and goes up to size-1.
- An array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- An array can be returned from a method using the syntax: `return arrayName;`
- An array can be multidimensional, meaning it can have more than one dimension. For example, a two-dimensional array can be declared using the syntax: `dataType[][] arrayName;`
- A two-dimensional array can be initialized using the syntax: `arrayName = new dataType[rows][columns];` or `arrayName = {{element1, element2, ...}, {element3, element4, ...}, ...};`
- The elements of a two-dimensional array can be accessed using the index operator: `arrayName[row][column]`. The row and column indices start from 0 and go up to rows-1 and columns-1 respectively.
- A two-dimensional array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- A two-dimensional array can be returned from a method using the syntax: `return arrayName;`
- An array can also be jagged, meaning it can have different lengths for each row. For example, a jagged array can be declared using the syntax: `dataType[][] arrayName;`
- A jagged array can be initialized using the syntax: `arrayName = new dataType[rows][];` and then assigning each row separately: `arrayName[0] = new dataType[size1]; arrayName[1] = new dataType[size2]; ...`
- The elements of a jagged array can be accessed using the index operator: `arrayName[row][column]`. The row index starts from 0 and goes up to rows-1. The column index depends on the length of each row and can vary from 0 to size-1.
- A jagged array can be passed as an argument to a method using the syntax: `methodName(arrayName);`
- A jagged array can be returned from a method using the syntax: `return arrayName;`