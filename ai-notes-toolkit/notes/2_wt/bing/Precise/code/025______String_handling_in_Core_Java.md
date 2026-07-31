#### String handling in Core Java
```java
public class StringHandling {
    public static void main(String[] args) {
        String str = "Hello, World!";
        System.out.println("Original String: " + str);

        // Get the length of the string
        int length = str.length();
        System.out.println("Length of the string: " + length);

        // Concatenate two strings
        String str2 = " Have a nice day!";
        String concatenatedString = str.concat(str2);
        System.out.println("Concatenated String: " + concatenatedString);

        // Get a character at a specific index
        char ch = str.charAt(7);
        System.out.println("Character at index 7: " + ch);

        // Get the index of a character
        int index = str.indexOf('W');
        System.out.println("Index of character 'W': " + index);

        // Convert string to uppercase
        String upperCaseString = str.toUpperCase();
        System.out.println("Uppercase String: " + upperCaseString);

        // Convert string to lowercase
        String lowerCaseString = str.toLowerCase();
        System.out.println("Lowercase String: " + lowerCaseString);

        // Check if string starts with a specific prefix
        boolean startsWith = str.startsWith("Hello");
        System.out.println("String starts with 'Hello': " + startsWith);

        // Check if string ends with a specific suffix
        boolean endsWith = str.endsWith("World!");
        System.out.println("String ends with 'World!': " + endsWith);

        // Replace characters in a string
        String replacedString = str.replace('l', 'x');
        System.out.println("Replaced String: " + replacedString);

        // Split string into an array of substrings
        String[] splitString = str.split(", ");
        System.out.println("Split String: ");
        for (String s : splitString) {
            System.out.println(s);
        }

        // Trim leading and trailing whitespaces
        String str3 = "   Hello, World!   ";
        String trimmedString = str3.trim();
        System.out.println("Trimmed String: " + trimmedString);
    }
}
```