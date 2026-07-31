# Cursors

Cursors are database objects that allow you to manipulate data in a row-by-row manner. They are useful when you need to perform complex logic or calculations on individual records, or when you need to update or delete data based on certain conditions. Cursors are also helpful when you need to fetch data from multiple tables and join them in a single result set.

## Types of Cursors

There are different types of cursors depending on the database system and the characteristics of the result set. Some common types are:

- Static cursor: A static cursor creates a copy of the result set and works on the copy. It is not affected by any changes made to the original data source. It allows moving forward and backward through the rows.
- Dynamic cursor: A dynamic cursor reflects any changes made to the original data source while the cursor is open. It allows moving forward and backward through the rows. It may skip or repeat rows if the data is modified by other transactions.
- Forward-only cursor: A forward-only cursor only allows moving forward through the rows. It does not support backward scrolling. It may or may not reflect changes made to the original data source.
- Keyset-driven cursor: A keyset-driven cursor creates a set of unique identifiers (keys) for the rows in the result set and works on the keys. It allows moving forward and backward through the rows. It reflects changes made to the non-key columns of the original data source, but not changes that affect the key columns or the membership of the rows.

## Cursor Operations

To use a cursor, you need to perform the following steps:

- Declare a cursor: A cursor is declared by defining a SQL statement that returns a result set and assigning a name to the cursor. You can also specify the type and other options for the cursor.
- Open a cursor: A cursor is opened by executing the SQL statement and allocating the resources for the cursor. This makes the result set available for processing.
- Fetch data from a cursor: A cursor is fetched by retrieving one row or a block of rows from the current position in the result set and storing them in variables or columns. You can also specify the direction of the fetch, such as next, previous, first, last, etc.
- Close a cursor: A cursor is closed by releasing the resources allocated for the cursor and removing the result set from memory. This makes the cursor unavailable for further processing.
- Deallocate a cursor: A cursor is deallocated by removing the cursor definition and name from the database. This makes the cursor name available for reuse.

## Cursor Syntax

The syntax for declaring, opening, fetching, closing, and deallocating a cursor may vary depending on the database system. Here are some examples of cursor syntax in different databases:

- SQL Server:

```sql
-- Declare a cursor
DECLARE cursor_name CURSOR [ LOCAL | GLOBAL ] [ FORWARD_ONLY | SCROLL ] [ STATIC | KEYSET | DYNAMIC | FAST_FORWARD ] [ READ_ONLY | SCROLL_LOCKS | OPTIMISTIC ] [ TYPE_WARNING ] FOR select_statement [ FOR UPDATE [ OF column_name [ ,...n ] ] ]

-- Open a cursor
OPEN cursor_name

-- Fetch data from a cursor
FETCH [ NEXT | PRIOR | FIRST | LAST | ABSOLUTE { n | @nvar } | RELATIVE { n | @nvar } ] FROM cursor_name [ INTO @variable_name [ ,...n ] ]

-- Close a cursor
CLOSE cursor_name

-- Deallocate a cursor
DEALLOCATE cursor_name
```

- Oracle:

```sql
-- Declare a cursor
CURSOR cursor_name [ ( parameter_name [ IN | OUT | IN OUT ] datatype [ ,...n ] ) ] IS select_statement;

-- Open a cursor
OPEN cursor_name [ ( argument [ ,...n ] ) ];

-- Fetch data from a cursor
FETCH cursor_name INTO variable_name [ ,...n ];

-- Close a cursor
CLOSE cursor_name;
```

- MySQL:

```sql
-- Declare a cursor
DECLARE cursor_name CURSOR FOR select_statement;

-- Open a cursor
OPEN cursor_name;

-- Fetch data from a cursor
FETCH cursor_name INTO variable_name [ ,...n ];

-- Close a cursor
CLOSE cursor_name;
```

- PostgreSQL:

```sql
-- Declare a cursor
DECLARE cursor_name [ [ NO ] SCROLL ] CURSOR [ WITH [ NO ] HOLD ] [ FOR select_statement ];

-- Open a cursor
-- No explicit OPEN statement is required

-- Fetch data from a cursor
FETCH [ direction [ FROM | IN ] ] cursor_name [ INTO target ];

-- Close a cursor
CLOSE cursor_name;
```

## Cursor Examples

Here are some examples