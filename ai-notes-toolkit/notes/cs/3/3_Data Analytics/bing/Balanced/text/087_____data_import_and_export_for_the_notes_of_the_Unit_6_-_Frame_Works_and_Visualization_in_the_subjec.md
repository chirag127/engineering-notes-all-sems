### Data Import and Export

- Data analysis generally uses data from other sources in various formats, so we need to import the data first so that it can be processed.
- The most commonly used tools or software for data analysis using Python is Jupyter Notebook.
- In Python, importing data into a Jupyter Notebook is quite easy, with only three steps:
  - Import pandas
  - Define variable to store url path or dataset file
  - Use the read_csv method to import the data
- For example, to import a csv file from a url, we can write:

```python
import pandas as pd
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
countries = pd.read_csv(url)
```

- To export data from Python to a file, we can use the to_csv method.
- For example, to export the countries data frame to a csv file, we can write:

```python
countries.to_csv("countries.csv")
```

- We can also import and export data in other formats, such as Excel, JSON, HTML, SQL, etc .
- For example, to import an Excel file, we can use the read_excel method:

```python
import pandas as pd
excel_file = "sample_data.xlsx"
data = pd.read_excel(excel_file)
```

- To export data to a JSON file, we can use the to_json method:

```python
data.to_json("sample_data.json")
```

- To import data from a SQL database, we can use the read_sql method:

```python
import pandas as pd
import sqlite3
conn = sqlite3.connect("sample.db")
sql_query = "SELECT * FROM table_name"
data = pd.read_sql(sql_query, conn)
```

- To export data to a HTML file, we can use the to_html method:

```python
data.to_html("sample_data.html")
```

- Data import and export are essential skills for data analysis, as they allow us to access and manipulate data from various sources and formats.