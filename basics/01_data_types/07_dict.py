# Dict

contacts = {
    "Alice": "alice@example.com",
    "Bob": "bob@example.com",
    "Charlie": "charlie@example.com"
}

contacts["David"] = "david@example.com"

print(f"Type: {type(contacts)}") # <class 'dict'>
print(f"Length of contacts: {len(contacts)}")  # Length of contacts: 4

print(f"Alice's email: {contacts['Alice']}")  # Alice's email: alice@example.com
print(f"David's email: {contacts['David']}")  # David's email: david@example.com

print(contacts.keys())    # dict_keys(['Alice', 'Bob', 'Charlie', 'David'])
print(contacts.values())  # dict_values(['alice@example.com', 'bob@example.com, 'bob@example.com, 'david@example.com])
print(contacts.items())   # dict_items([('Alice', 'alice@example.com'), ('Bob', 'bob@example.com'), ('Charlie', 'charlie@example.com'), ('David', 'david@example.com')])

for name, email in contacts.items():
    print(f"{name}: {email}")
# Output:
# Alice: alice@example.com
# Bob: bob@example.com
# Charlie: charlie@example.com
# David: david@example.com

for names in contacts.keys():
    print(f"Contact name: {names}")
# Output:
# Contact name: Alice
# Contact name: Bob
# Contact name: Charlie
# Contact name: David

for email in contacts.values():
    print(f"Contact email: {email}")
# Output:
# Contact email: alice@example.com
# Contact email: bob@example.com
# Contact email: charlie@example.com
# Contact email: david@example.com