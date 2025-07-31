class DatabaseConnection:
    # The single instance will be stored in this private variable
    _instance = None

    # Private constructor to prevent direct instantiation
    def __new__(cls):
        # Only create a new instance if it doesn't already exist
        if not cls._instance:
            cls._instance = super().__new__(cls)  # Equivalent to super(DatabaseConnection, cls).__new__(cls)

            # Initialize the connection or any other setup tasks
            cls._instance.connection = "Database connection established"
        return cls._instance

    def read_data(self):
        print("Reading data from the database...")

    def write_data(self):
        print("Writing data to the database...")

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True, both refer to the same instance


# In the above code, we're creating multiple instances of the DatabaseConnection class.

# Each instance has its own independent connection to the database.
# This could lead to inconsistency in the following ways:

# 1. **Multiple Instances**: Multiple database connections are opened, which can waste resources.

# 2. **Inconsistent Access**: One instance might be reading from the database while another writes, leading to conflicting states.

# 3. **No Global Access Point**: There is no central point to access or manage the connection, leading to potential errors where one part of the program could use one connection, while another part uses a different one, causing data inconsistency.



"""
In the Singleton pattern, we ensure that only one instance of a class is created.
To achieve this, we override the __new__ method, which is responsible for creating a new instance.

1. **Calling the Parent's `__new__` with `super()`**:
   - We use `super()` to call the parent class's `__new__` method (from the `object` class).
   - This ensures that the instance is created properly, following the inheritance protocol.
   - The `super()` call returns a new instance of the class, but we only want to create one instance.

2. **Storing the Instance in `cls._instance`**:
   - We store the created instance in `cls._instance`, a class-level variable.
   - This allows us to track the instance, and **only return the same instance** when requested again.
   - If `cls._instance` is already set (i.e., an instance already exists), we skip creating a new one and return the existing instance.

3. **Singleton Behavior**:
   - Without `cls._instance`, each call to the class would create a new instance, violating the Singleton pattern.
   - By storing the instance in `cls._instance`, we ensure **one shared instance** across the entire program.
"""
