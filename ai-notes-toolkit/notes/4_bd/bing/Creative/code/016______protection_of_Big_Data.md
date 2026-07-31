Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for protection of Big Data. Here is one possible solution in Python:

#### Protection of Big Data

```python
# Import libraries
import pandas as pd
import numpy as np
import hashlib
import random

# Define a function to hash a column of data
def hash_column(data, column, salt=None):
  # If salt is not provided, generate a random salt
  if salt is None:
    salt = random.randint(0, 1000000)
  # Apply hashlib.sha256 to each value in the column, adding the salt
  hashed = data[column].apply(lambda x: hashlib.sha256((str(x) + str(salt)).encode()).hexdigest())
  # Return the hashed column and the salt
  return hashed, salt

# Load a sample dataset
data = pd.read_csv("sample_data.csv")

# Hash the sensitive columns, such as name, email, phone, etc.
data["name"], name_salt = hash_column(data, "name")
data["email"], email_salt = hash_column(data, "email")
data["phone"], phone_salt = hash_column(data, "phone")

# Save the hashed data and the salts
data.to_csv("hashed_data.csv", index=False)
salts = {"name": name_salt, "email": email_salt, "phone": phone_salt}
np.save("salts.npy", salts)
```