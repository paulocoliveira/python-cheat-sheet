# Dictionary Functions

# Retrieving all keys from a dictionary

test_case = {"name": "Login", "execution_time_sec": 15, "status": "passed"}
keys = test_case.keys()
print(keys)  # Output: dict_keys(['name', 'execution_time_sec', 'status'])

# Checking if a key exists in a dictionary

test_case = {"name": "Login", "execution_time_sec": 15, "status": "passed"}
exists = "name" in test_case
print(exists)  # Output: True

# Accessing the values of a dictionary

test_case = {"name": "Login", "execution_time_sec": 15, "status": "passed"}
values = test_case.values()
print(values)  # Output: dict_values(['Login', 15, 'passed'])

# Removing a key-value pair from a dictionary

test_case = {"name": "Login", "execution_time_sec": 15, "status": "passed"}
removed_value = test_case.pop("execution_time_sec")
print(removed_value)  # Output: 15

# Merging two dictionaries

test_case_info = {"name": "Login", "execution_time_sec": 15, "status": "passed"}
test_case_data = {"type": "positive", "environment": "production"}
merged_dict = {**test_case_info, **test_case_data}
print(merged_dict)  # Output: {'name': 'Login', 'execution_time_sec': 15, 'status': 'passed', 'type': 'positive', 'environment': 'production'}