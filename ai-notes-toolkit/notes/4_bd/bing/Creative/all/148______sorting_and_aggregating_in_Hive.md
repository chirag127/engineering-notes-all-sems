#### Sorting and Aggregating in Hive

- Sorting and aggregating are common operations in data analysis that involve rearranging or summarizing data based on some criteria.
- Hive supports two types of sorting: **order by** and **sort by**.
- **Order by** sorts the entire result set in ascending or descending order according to one or more columns. It uses only one reducer, which can be slow and inefficient for large data sets.
- **Sort by** sorts the data within each reducer partition in ascending or descending order according to one or more columns. It uses multiple reducers, which can be faster and more scalable for large data sets. However, the order of the partitions is not guaranteed.
- To sort the data globally across all partitions, Hive provides the **distribute by** clause, which can be used in conjunction with **sort by**. The **distribute by** clause specifies how to partition the data based on one or more columns. The **sort by** clause then sorts the data within each partition.
- For example, the following query distributes the data by the year column and sorts the data by the month column within each year partition:

```sql
select year, month, sales from sales_table
distribute by year
sort by month;
```

- Aggregating is the process of applying a function to a group of rows to produce a single value. Hive supports various aggregate functions, such as **sum**, **count**, **avg**, **min**, **max**, etc.
- To apply an aggregate function to the entire result set, simply use the function in the select clause. For example, the following query calculates the total sales from the sales_table:

```sql
select sum(sales) as total_sales from sales_table;
```

- To apply an aggregate function to a subset of rows based on some criteria, use the **group by** clause. The **group by** clause specifies one or more columns to group the rows by. The aggregate function is then applied to each group. For example, the following query calculates the average sales per year from the sales_table:

```sql
select year, avg(sales) as avg_sales from sales_table
group by year;
```

- To filter the groups based on some condition, use the **having** clause. The **having** clause is similar to the **where** clause, but it applies to the groups after the **group by** clause. For example, the following query calculates the average sales per year from the sales_table, but only for the years with more than 10 records:

```sql
select year, avg(sales) as avg_sales from sales_table
group by year
having count(*) > 10;
```

- To sort the groups based on some column, use the **order by** clause. The **order by** clause can be used after the **group by** clause to sort the groups in ascending or descending order. For example, the following query calculates the average sales per year from the sales_table and sorts the results by the average sales in descending order:

```sql
select year, avg(sales) as avg_sales from sales_table
group by year
order by avg_sales desc;
```

- To limit the number of rows returned by the query, use the **limit** clause. The **limit** clause can be used at the end of the query to specify the maximum number of rows to return. For example, the following query returns the top 5 years with the highest average sales from the sales_table:

```sql
select year, avg(sales) as avg_sales from sales_table
group by year
order by avg_sales desc
limit 5;
```

- Sorting and aggregating are powerful tools for data analysis that can help to explore, summarize, and compare data in Hive.