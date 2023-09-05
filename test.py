import example_pb2

# Create a Person object
person = example_pb2.Person()
person.name = "Alice"
person.age = 30
person.email = "alice@example.com"

# Serialize the Person object to a binary string
serialized_person = person.SerializeToString()
print("Serialized Person: ", serialized_person)

# Deserialize the binary string back to a Person object
deserialized_person = example_pb2.Person()
deserialized_person.ParseFromString(serialized_person)

# Access deserialized object properties
print("Deserialized Person: ", deserialized_person)
print("Name: ", deserialized_person.name)
print("Age: ", deserialized_person.age)
print("Email: ", deserialized_person.email)