#### Compliance of Big Data

Compliance in the context of big data refers to the adherence to laws, regulations, and standards that govern the collection, storage, and use of large amounts of data. Here is an example of code that checks for compliance with the General Data Protection Regulation (GDPR) when handling user data:

```python
def check_gdpr_compliance(user_data):
    # Check if user has given consent for data processing
    if not user_data['consent']:
        return False
    # Check if data is being processed for a specific, explicit, and legitimate purpose
    if not user_data['purpose']:
        return False
    # Check if data is being processed in a transparent manner
    if not user_data['transparency']:
        return False
    # Check if data is being processed in a way that ensures its security
    if not user_data['security']:
        return False
    return True
```
This code checks if the user has given consent for data processing, if the data is being processed for a specific, explicit, and legitimate purpose, if the data is being processed in a transparent manner, and if the data is being processed in a way that ensures its security. If any of these conditions are not met, the function returns `False`, indicating non-compliance with the GDPR. Otherwise, the function returns `True`, indicating compliance with the GDPR.