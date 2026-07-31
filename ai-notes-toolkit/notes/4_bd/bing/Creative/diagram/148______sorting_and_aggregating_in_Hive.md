#### Sorting and Aggregating in Hive

- Sorting data in Hive can be achieved by using a standard `ORDER BY` clause, but it has a drawback. `ORDER BY` produces a result that is totally sorted, as expected, but to do so it sets the number of reducers to one, making it very inefficient for large datasets.
- A better alternative for sorting data in Hive is to use the `SORT BY` clause, which sorts the data within each reducer. This means that the number of reducers can be set to a higher value, improving the performance. However, the result is not globally sorted, as different reducers may have different ranges of values.
- Another option for sorting data in Hive is to use the `DISTRIBUTE BY` clause, which distributes the data among the reducers based on a hash function of the specified columns. This ensures that rows with the same values in the distributed columns are sent to the same reducer. This can be useful for performing joins or aggregations on those columns.
- Aggregating data in Hive can be done by using the built-in aggregate functions, such as `MAX`, `MIN`, `AVG`, `SUM`, `COUNT`, etc. These functions are usually used with the `GROUP BY` clause, which groups the data by one or more columns and applies the aggregate function to each group. If there is no `GROUP BY` clause specified, it aggregates over the whole table by default.
- Hive also supports advanced aggregation by using `GROUPING SETS`, `ROLLUP`, `CUBE`, analytic functions, and windowing. These features allow for more complex and flexible grouping and aggregation of data, such as computing subtotals, totals, and averages at different levels of granularity.
- An example of sorting and aggregating data in Hive is:

```sql
-- Create a table with some sample data
CREATE TABLE sales (product STRING, category STRING, quantity INT, price DOUBLE)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',';
LOAD DATA LOCAL INPATH 'sales.csv' INTO TABLE sales;

-- Sort the data by product name and price in ascending order
SELECT * FROM sales SORT BY product, price;

-- Aggregate the data by category and compute the total quantity and revenue
SELECT category, SUM(quantity) AS total_quantity, SUM(quantity * price) AS total_revenue
FROM sales GROUP BY category;

-- Aggregate the data by category and product and compute the average price
SELECT category, product, AVG(price) AS average_price
FROM sales GROUP BY category, product;

-- Aggregate the data by category and product and compute the average price and the total quantity
-- using grouping sets
SELECT category, product, AVG(price) AS average_price, SUM(quantity) AS total_quantity
FROM sales GROUP BY category, product GROUPING SETS ((category, product), (category), ());
```