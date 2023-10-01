# Creating a hashmap
# Time complexity: O(n), where n is the number of key-value pairs being inserted
hashmap = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}

# Accessing values
# Time complexity: O(1)
print(hashmap["key1"])  # Output: value1

# Modifying values
# Time complexity: O(1)
hashmap["key2"] = "new value"
print(hashmap["key2"])  # Output: new value

# Adding new key-value pairs
# Time complexity: O(1)
hashmap["key4"] = "value4"
print(hashmap["key4"])  # Output: value4

# better way to add new key-value pair
# if the key already exists it doesn't replace the value
hashmap.setdefault("key4", "value4")
print(hashmap["key4"]) # Output: value4 

# Checking if a key exists
# Time complexity: O(1)
if "key3" in hashmap:
    print("Key 'key3' exists")

# Removing a key-value pair
# Time complexity: O(1)
del hashmap["key1"]
print(hashmap.get("key1"))  # Output: None

# Iterating over keys
# Time complexity: O(n), where n is the number of key-value pairs in the hashmap
for key in hashmap:
    print(key, hashmap[key])

# Iterating over key-value pairs
# Time complexity: O(n), where n is the number of key-value pairs in the hashmap
for key, value in hashmap.items():
    print(key, value)
