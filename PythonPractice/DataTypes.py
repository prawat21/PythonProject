import pytest

# Dictionaries are used for storing data in Key, Value pairs
# Cannot store duplicate keys, if used then the value is overridden
# The values in dictionary items can be of any data type:
# Examples: - String, list,int, and boolean data types
dictionary_test = {
    "brand": "Ford",
    "model": ["Mustang", "EcoSport", "Ford", "FreeStyle"],
    "year": 1964,
    "year": 2020,
    "Variant": "Petrol",
    "Electric": False
}
print(dictionary_test)
print(len(dictionary_test)) # provide the length of dictionary
