class DatabaseConnection:
    def __init__(self):
        self.connection = "Database connection established"

    def read_data(self):
        print("Reading data from the database...")

    def write_data(self):
        print("Writing data to the database...")

# Multiple instances created, each with its own connection
db1 = DatabaseConnection()
db2 = DatabaseConnection()

db1.read_data()
db2.write_data()


# This code demonstrates a bad implementation of the Singleton Design Pattern

"""
In the above code, we're creating multiple instances of the DatabaseConnection class.
Each instance has its own independent connection to the database.
This could lead to inconsistency in the following ways:
1. **Multiple Instances**: Multiple database connections are opened, which can waste resources.
2. **Inconsistent Access**: One instance might be reading from the database while another writes, leading to conflicting states.
3. **No Global Access Point**: There is no central point to access or manage the connection, leading to potential errors where one part of the program could use one connection, while another part uses a different one, causing data inconsistency.
4. **Writing to Different Locations**: If a logger is being used, different instances might log to different locations (files, databases, etc.), making it harder to track the application's behavior and leading to inconsistency in logging data.
"""
