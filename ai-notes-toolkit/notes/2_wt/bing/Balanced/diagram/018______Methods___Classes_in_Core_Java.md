A method is a behavior of an object that operates on the data or variables defined within a class. A class is a blueprint or template that contains both data and methods that operate on that data. In Java, every method must belong to a class and every class must be declared with the class keyword. To call a method, you need to use the object name of the class followed by a dot operator and the method name with parentheses. For example, objectName.methodName(). If the method is defined with the static modifier, you can call it directly without using an object name. For example, methodName().

#### Methods & Classes in Core Java

```
+-----------------+     +-----------------+
|                 |     |                 |
|     Class A     |     |     Class B     |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  - x : int      |     |  - y : int      |
|  - s : String   |     |  - z : double   |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  + getX() : int |     |  + getY() : int |
|  + setX(int)    |     |  + setY(int)    |
|  + getS() : String   |  + getZ() : double |
|  + setS(String) |     |  + setZ(double) |
|                 |     |                 |
+-----------------+     +-----------------+
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        |                     |
        V                     V
+-----------------+     +-----------------+
|                 |     |                 |
|   objectA       |     |   objectB       |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  x = 10         |     |  y = 20         |
|  s = "Hello"    |     |  z = 3.14       |
|                 |     |                 |
+-----------------+     +-----------------+
|                 |     |                 |
|  objectA.getX() |     |  objectB.getY() |
|  objectA.setX(15)   |  objectB.setZ(2.71) |
|  objectA.getS() |     |  objectB.getZ() |
|  objectA.setS("World") |                 |
|                 |     |                 |
+-----------------+     +-----------------+
```

The diagram above shows two classes, Class A and Class B, with their data and methods. The data are represented by variables with a minus sign (-) and the methods are represented by functions with a plus sign (+). The data types and return types of the variables and methods are also shown. The diagram also shows two objects, objectA and objectB, that are created from the classes using the new keyword. The objects have their own copies of the data and can access the methods of their classes. The diagram also shows some examples of how to call the methods using the dot operator.