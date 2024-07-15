import yaml

# Open and load the YAML file
with open('sample.yml', 'r') as file:
    data = yaml.safe_load(file)

# Print the data using the format() method
print("Name: {}".format(data['Name']))
print("Age: {}".format(data['Age']))
print("Height: {}".format(data['Height']))
print("Weight: {}".format(data['Weight']))
print("Message: {}".format(data['message']))
print("List:")
for item in data['food']:
    print("  - {}".format(item))
