 Here is the content in markdown format without any emojis or external links and in formal tone:

### Stored Function

1. A stored function is a named PL/SQL block which can take input parameters and return a value.
2. It is similar to a procedure except that it returns a value.
3. The return type can be a scalar data type like NUMBER, VARCHAR2, DATE, etc. or a record type or a table type.
4. The advantages of stored functions are:
    - Reusability - The function can be invoked many times.
    - Flexibility - Different applications can use the same function.
    - Maintainability - The function code is stored in one place and any change is immediately available to all applications.
    - Improved Performance - The call to a function is a single SQL statement which is more efficient than writing the same logic in multiple places.
5. The syntax for creating a stored function is:
CREATE [OR REPLACE] FUNCTION function_name
(parameter_name [IN|OUT|IN OUT] parameter_type, ...)
RETURN return_type
IS
    declaration_section
BEGIN
    executable_section
    RETURN return_value;
EXCEPTION
    exception_handling_section
END;

6. Examples:
    - A function to calculate the square of a number:
        CREATE FUNCTION square(x IN NUMBER)
        RETURN NUMBER
        IS
        BEGIN
            RETURN x * x;
        END;
    - A function to concatenate two strings:
        CREATE FUNCTION concat_string(str1 IN VARCHAR2, str2 IN VARCHAR2)
        RETURN VARCHAR2
        IS
        BEGIN
            RETURN str1 || str2;
        END;