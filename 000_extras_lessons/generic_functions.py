import json
from functools import singledispatch
from datetime import datetime

# Seralize data in Python and convert it from Python data type to JSON

class User:
    def __init__(self, name, age, joined_date):
        self.name = name
        self.age = age
        self.joined_date = joined_date

# Decorator function
@singledispatch
def to_serializable(obj):
    """Fallback serializer for unsupported types."""
    raise TypeError(f"Type {type(obj).__name__} not serializable")

# convert datetime to universial time format
@to_serializable.register
def _(obj: datetime):
    return obj.isoformat()

# convert set to list
@to_serializable.register
def _(obj: set):
    return list(obj)

# convert User to dict
@to_serializable.register
def _(obj: User):
    return {
        "name": obj.name,
        "age": obj.age,
        "joined_date": obj.joined_date.isoformat(),
    }

# Example of data input
data = {
    "user": User("Alice", 30, datetime(2022, 1, 20)),
    "tags": {"python", "json", "singledispatch"},
    "created_at": datetime.now()
}

# Convert to JSON
json_str = json.dumps(data, default=to_serializable, indent=2)
print(json_str)
