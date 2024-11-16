person = {
    "name": "John",
    "gender": "Male",
    "age": 30,
    "address": "123 Street",
    "phone": "555-1234"
}

key = input("What information would you like to know about the person? ")
if key in person:
    print(person[key])
else:
    print("Key not found!")
