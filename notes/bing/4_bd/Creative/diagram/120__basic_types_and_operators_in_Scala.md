Scala has nine basic types: Byte, Short, Int, Long, Char, String, Float, Double, and Boolean. These types are all objects, unlike Java's primitive types. Scala also supports operators, which are methods that can be applied to values of any type. Operators can be infix, prefix, or postfix, and they have different precedences and associativities depending on their first character.

#### Basic types and operators in Scala

```
+-----------------+-----------------+-----------------+-----------------+
|     Byte        |     Short       |      Int        |      Long       |
| 8-bit signed    | 16-bit signed   | 32-bit signed   | 64-bit signed   |
| integer         | integer         | integer         | integer         |
| -128 to 127     | -32768 to 32767 | -2^31 to 2^31-1 | -2^63 to 2^63-1 |
|                 |                 |                 |                 |
| + - * / %       | + - * / %       | + - * / %       | + - * / %       |
| & | ^ ~ << >> >>>| & | ^ ~ << >> >>>| & | ^ ~ << >> >>>| & | ^ ~ << >> >>>|
| toShort toInt   | toByte toInt    | toByte toShort  | toByte toShort  |
| toLong toChar   | toLong toChar   | toLong toChar   | toInt toChar    |
| toFloat toDouble| toFloat toDouble| toFloat toDouble| toFloat toDouble|
+-----------------+-----------------+-----------------+-----------------+
|     Char        |     String      |     Float       |     Double      |
| 16-bit unsigned | sequence of     | 32-bit IEEE     | 64-bit IEEE     |
| Unicode         | characters      | 754 single      | 754 double      |
| 0 to 65535      |                 | precision       | precision       |
|                 |                 | floating point  | floating point  |
|                 |                 | numbers         | numbers         |
|                 |                 |                 |                 |
| +               | +               | + - * / %       | + - * / %       |
| toByte toShort  | toInt toDouble  | toByte toShort  | toByte toShort  |
| toInt toLong    | toBoolean       | toInt toLong    | toInt toLong    |
| toFloat toDouble|                 | toChar toDouble | toChar toFloat  |
+-----------------+-----------------+-----------------+-----------------+
|     Boolean     |                 |                 |                 |
| true or false   |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
| ! && || ^       |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
```