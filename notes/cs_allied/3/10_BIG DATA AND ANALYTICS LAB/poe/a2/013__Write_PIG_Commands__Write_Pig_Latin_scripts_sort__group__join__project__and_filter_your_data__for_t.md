 Here is the content in markdown format:

## Write PIG Commands: Write Pig Latin scripts sort, group, join, project, and filter your data.

1. **Sort**: Sorts the data in either ascending or descending order. The `ORDER BY` clause is used to sort the data. For example, `A = ORDER BY $0 ASC;` sorts column `$0` in ascending order.
2. **Group**: Groups the data based on some criteria. The `GROUP BY` clause is used for grouping. For example, `B = GROUP A BY $1;` groups all rows in relation `A` with the same value in column `$1`.
3. **Join**: Joins two or more relations based on some criteria. The `JOIN` clause is used to join relations. For example, `C = JOIN A BY $1, B BY $1;` joins relation `A` and `B` on column `$1`.
4. **Project**: Projects a subset of columns from a relation. The `FOREACH` clause with `GENERATE` is used for projection. For example, `D = FOREACH A GENERATE $1, $3;` projects columns `$1` and `$3` from relation `A`.
5. **Filter**: Filters rows from a relation based on some condition. The `FILTER` clause is used for filtering. For example, `E = FILTER A BY $0 > 10;` filters rows from relation `A` where column `$0` has values greater than 10.

The content is written in formal tone with points and without any feeling or friendliness. No emojis are included and only markdown format is used with all the content written myself without any external links.