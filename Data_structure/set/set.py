# Great for operations like union, intersection, difference, and symmetric difference

# Set (remove duplicates from a list)
recipes = ['pizza', 'pasta', 'salad', 'noodles', 'pizza', 'pasta', 'salad', 'noodles']
print(f"Recipes with duplicates {recipes}")  # ['pizza', 'pasta', 'salad', 'noodles', 'pizza', 'pasta', 'salad', 'noodles']
print(f"Recipes without duplicates {set(recipes)}")  # {'salad', 'noodles', 'pizza', 'pasta'}

# Union (Return a set containing the union of sets)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(f"Union of sets {set1.union(set2)}")  # {1, 2, 3, 4, 5, 6}

# Intersection (Return a set containing the intersection of sets)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"Intersection of sets {set1.intersection(set2)}")  # {2, 3}

# Difference (Return a set containing the difference between two or more sets)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"Difference between sets {set1.difference(set2)}")  # {1}
print(f"Difference between sets {set2.difference(set1)}")  # {4}

# Symmetric Difference (Return a set with the symmetric differences of two sets)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(f"Symmetric difference between sets {set1.symmetric_difference(set2)}")  # {1, 4}

# Is subset (Return True if all items in set1 are present in set2)
set1 = {1, 2}
set2 = {1, 2, 3}
print(f"Is subset {set1.issubset(set2)}")  # True

# Is superset (Return True if all items in set2 are present in set1)
set1 = {1, 2, 3}
set2 = {1, 2}
print(f"Is superset {set1.issuperset(set2)}")  # True

# Is disjoint (Return True if no items in set1 are present in set2)
set1 = {1, 2}
set2 = {3, 4}
print(f"Is disjoint {set1.isdisjoint(set2)}")  # True

# Add (Add a new element to the set)
set1 = {1, 2, 3}
set1.add(4)
print(f"Added an element to the set {set1}")  # {1, 2, 3, 4}

# Pop (Remove the firt element from the set)
set1 = {1, 2, 3}
set1.pop()
print(f"Poped the first element from the set {set1}")  # {2, 3}

# Remove (Remove the specified element from the set)
set1 = {1, 2, 3}
set1.remove(2)
print(f"Removed the specified element from the set {set1}")  # {1, 3}

# Discard (Remove the specified element from the set)
set1 = {1, 2, 3}
set1.discard(2)
print(f"Discarded the specified element from the set {set1}")  # {1, 3}

# Difference between remove and discard
# if you remove an element that does not exist, remove will raise an error
# while discard will not

# In check if the element is in the set
set1 = {1, 2, 3}
print(f"Check if the element is in the set {1 in set1}")  # True
print(f"Check if the element is in the set {4 in set1}")  # False