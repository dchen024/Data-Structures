# Create an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements: O(1)
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modifying elements: O(1)
my_array[1] = 10
print(my_array)  # Output: [1, 10, 3, 4, 5]

# Adding elements: O(1)
my_array.append(6)
print(my_array)  # Output: [1, 10, 3, 4, 5, 6]

# Removing elements: O(n)
my_array.pop(2)
print(my_array)  # Output: [1, 10, 4, 5, 6]

# Array length: O(1)
print(len(my_array))  # Output: 5

# Iterating over the array: O(n)
for element in my_array:
    print(element)

# Output:
# 1
# 10
# 4
# 5
# 6
