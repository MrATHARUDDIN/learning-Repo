# ================================================
# 🧠 Python Dictionary Notes
# ================================================

# Dictionaries = a collection of {key: value} pairs
# ✅ Ordered (as of Python 3.7+)
# ✅ Changeable (mutable)
# ✅ No duplicate keys allowed

# 🔑 Keys must be unique and immutable (e.g., strings, numbers, tuples)
# 🔓 Values can be any data type and may be duplicated

# ================================================
# 🛠️ Creating a dictionary
# ================================================
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(capitals.get("India"))  # Safer way to access a value

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital doesn't exist")


capitals.update({"Germany": "Berlin"})     # Adds new entry
capitals.update({"USA": "Detroit"})        # Updates existing entry


print(capitals)



# ================================================
# ❌ Removing items (examples)
# ================================================
# capitals.pop("China")        # Removes key "China"
# del capitals["c keyRussia"]       # Deletes specifi
# capitals.clear()             # Clears the dictionary
# del capitals                 # Deletes the entire dictionary


# ================================================
# 🔁 Looping through dictionary (example)
# ================================================
for country, capital in capitals.items():
     print(country, ":", capital)



# ================================================
# 🧰 Useful dictionary methods
# ================================================
# .get(key)         → Returns value or None if key not found
# .keys()           → Returns all keys
# .values()         → Returns all values
# .items()          → Returns list of (key, value) pairs
# .update({...})    → Adds/updates key-value pairs
# .pop(key)         → Removes key and returns its value
# .clear()          → Empties the dictionary

# ================================================
# End of Dictionary Notes
# ================================================
