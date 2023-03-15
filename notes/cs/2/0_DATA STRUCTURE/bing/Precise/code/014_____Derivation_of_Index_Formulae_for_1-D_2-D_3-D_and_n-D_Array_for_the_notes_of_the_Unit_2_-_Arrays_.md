### Derivation of Index Formulae for 1-D,2-D,3-D and n-D Array

The index formulae for arrays are used to calculate the memory address of an element in an array. The formulae vary depending on the dimension of the array and the order in which the elements are stored.

#### 1-D Array

For a 1-D array, the memory address of an element can be calculated using the formula:

`Address = Base + (Index * Element_Size)`

Where `Base` is the memory address of the first element in the array, `Index` is the index of the element, and `Element_Size` is the size of each element in the array.

#### 2-D Array

For a 2-D array, the memory address of an element can be calculated using the formula:

`Address = Base + ((Row * Number_of_Columns + Column) * Element_Size)`

Where `Base` is the memory address of the first element in the array, `Row` is the row index of the element, `Column` is the column index of the element, `Number_of_Columns` is the number of columns in the array, and `Element_Size` is the size of each element in the array.

#### 3-D Array

For a 3-D array, the memory address of an element can be calculated using the formula:

`Address = Base + (((Depth * Number_of_Rows + Row) * Number_of_Columns + Column) * Element_Size)`

Where `Base` is the memory address of the first element in the array, `Depth` is the depth index of the element, `Row` is the row index of the element, `Column` is the column index of the element, `Number_of_Rows` is the number of rows in the array, `Number_of_Columns` is the number of columns in the array, and `Element_Size` is the size of each element in the array.

#### n-D Array

For an n-D array, the memory address of an element can be calculated using the formula:

`Address = Base + (((((...((Index_n * Size_n-1 + Index_n-1) * Size_n-2 + Index_n-2) * ... * Size_1) + Index_1) * Size_0) + Index_0) * Element_Size)`

Where `Base` is the memory address of the first element in the array, `Index_n` is the index of the element in the nth dimension, `Size_n` is the size of the nth dimension, and `Element_Size` is the size of each element in the array.

These formulae can be used to calculate the memory address of an element in an array of any dimension and order. They are essential for efficient access to elements in an array.