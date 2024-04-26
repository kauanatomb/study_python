# Append (Add an element to the end of the list)
recipes = ["pizza", "pasta", "salad", "noodles"]
recipes.append('burger')
print(f"One more recipe in my list {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles', 'burger']

# Clear (Remove all the elements from the list)
recipes.clear()
print(f"Cleaned my recipe list {recipes}")  # []

# Copy (Return a copy of the list)
recipes = ["pizza", "pasta", "salad", "noodles"]
new_recipes_list = recipes.copy()
print(f"New recipe list {new_recipes_list}")  # ['pizza', 'pasta', 'salad', 'noodles']
print(f"Old recipe list {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles']

# Count (Return the number of elements with the specified value)
recipes.count("pizza")  # 0

# Extend (Add the elements of a list (or any iterable), to the end of the current list)
recipes.extend(["burger", "cake"])
print(f"Extended recipe list {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles', 'burger', 'cake']

# Index (Return the index of the first element with the specified value)
recipes.index("pizza")  # 0

# Insert (Add an element at the specified position)
recipes.insert(1, "burger")
print(f"Inserted burger at position 1 {recipes}")  # ['pizza', 'burger', 'pasta', 'salad', 'noodles', 'burger', 'cake']

# Pop (Remove the element at the specified position or the last element if the position is not specified)
recipes.pop(1)
print(f"Popped burger at position 1 {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles', 'burger', 'cake']

# Remove (Remove the first item with the specified value)
recipes.remove("burger")
print(f"Removed burger from the list {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles', 'cake']

# Reverse (Reverse the order of the list)
recipes.reverse()
print(f"Reversed recipe list {recipes}")  # ['cake', 'noodles', 'salad', 'pasta', 'pizza']

# Len (Return the number of elements in the list)
print(f"Number of recipes in my list {len(recipes)}")  # 5

# Sort (Sort the list)
recipes.sort(reverse=True)
print(f"Sorted recipe list {recipes}")  # ['salad', 'pasta', 'pizza', 'noodles', 'cake']

# Sorted (Return a new sorted list from the elements of the list)
sorted_recipes = sorted(recipes)
print(f"Sorted recipe list {sorted_recipes}")  # ['cake', 'noodles', 'pasta', 'pizza', 'salad']