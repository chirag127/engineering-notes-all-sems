 Here is the formal content on the topic "String handling in Core Java" in markdown format:

#### String handling in Core Java

1. Creating Strings:
- String literals: "Hello World"
- String object: new String("Hello World")

2. String Length:
- .length() method: int length = "Hello World".length(); //Outputs 11

3. Extracting substrings:
- .substring(beginIndex): str.substring(2); //Outputs "llo World"
- .substring(beginIndex, endIndex): str.substring(2, 5); //Outputs "llo"

4. Comparing Strings:
- .equals(): str.equals("Hello World"); //Outputs true
- .equalsIgnoreCase(): str.equalsIgnoreCase("hello world"); //Outputs true
- >, >=, <, <=: Used for comparing strings lexicographically

5. Searching Strings:
- .indexOf(ch): str.indexOf('l'); //Outputs 2 (Index of first 'l')
- .lastIndexOf(ch): str.lastIndexOf('l'); //Outputs 3 (Index of last 'l')
- .contains(str): str.contains("World"); //Outputs true

6. Modifying Strings:
- .replace(oldChar, newChar): str.replace('l', 'x'); //Outputs "Hxello World"
- .toUpperCase(): str.toUpperCase(); //Outputs "HELLO WORLD"
- .toLowerCase(): str.toLowerCase(); //Outputs "hello world"

7. Splitting and Joining Strings:
- .split(regex): str.split(" "); //Outputs ["Hello", "World"]
- .join(array): String.join("-", {"Hello", "World"}); //Outputs "Hello-World"