class local:

    # Class Variable
    area = 'T nagar'

    # The init method or constructor
    def __init__(name, age):

        # Instance Variable
        name.age = age

    # Adds an instance variable
    def set(name, height):
        name.height = height

    # Retrieves instance variable
    def get(name):
        return name.height, name.age, name. area


# Driver Code
o = local(101)
o.set("Rahul, Ap")
print(o.get())
