# Dictionary representing web configuration settings

webConfig = {
    'website': 'example.com',
    'dbType': 'PostgreSQL',
    'dbUser': 'admin',
    'dbPassword': 'securepassword123'
}

# Web Configuration Dictionary
print(f"Type: {type(webConfig)}")  # <class 'dict'>
print(f"Length of webConfig: {len(webConfig)}")  # Length of webConfig: 4

print(" ")
print(f"Website: {webConfig['website']}")  # Website: example.com
print(f"Database Type: {webConfig['dbType']}")  # Database Type: PostgreSQL
print(f"Database User: {webConfig['dbUser']}")  # Database User: admin
print(f"Database Password: {webConfig['dbPassword']}")  # Database Password: securepassword123

print(" ")
print(webConfig.keys())    # dict_keys(['website', 'dbType', 'dbUser', 'dbPassword'])
print(webConfig.values())  # dict_values(['example.com', 'PostgreSQL', 'admin', 'securepassword123'])
print(webConfig.items())   # dict_items([('website', 'example.com'), ('dbType', 'PostgreSQL'), ('dbUser', 'admin'), ('dbPassword', 'securepassword123')])

print(" ")
for key, value in webConfig.items():
    print(f"{key}: {value}")
# Output:
# website: example.com
# dbType: PostgreSQL
# dbUser: admin
# dbPassword: securepassword123

print(" ")
for key in webConfig.keys():
    print(f"Config key: {key}")
# Output:
# Config key: website
# Config key: dbType
# Config key: dbUser
# Config key: dbPassword

print(" ")
for value in webConfig.values():
    print(f"Config value: {value}")
# Output:
# Config value: example.com
# Config value: PostgreSQL
# Config value: admin
# Config value: securepassword123
