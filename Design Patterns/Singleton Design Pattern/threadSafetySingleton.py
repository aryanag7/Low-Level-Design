import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Ensures thread safety when creating the instance
                if cls._instance is None:  # Double-check to avoid race conditions
                    cls._instance = super().__new__(cls)
                    cls._instance.cache = {}  # Initialize cache // instance-level attribute
                    cls._instance.logger = []  # Initialize logger (as a simple list here)
                    cls._instance.db_connection = "Database connected"  # Initialize db connection
        return cls._instance

    def get_cache(self):
        return self.cache

    def set_cache(self, key, value):
        self.cache[key] = value

    def log(self, message):
        self.logger.append(message)  # Simple log implementation

    def get_db_connection(self):
        return self.db_connection



def __new__(cls):
        if cls._instance is None:  # First check (without locking)
            with cls._lock:  # Acquire lock only if instance is not created yet
                if cls._instance is None:  # Second check (with locking)
                    cls._instance = super().__new__(cls)
                    # Initialize other attributes here
        return cls._instance



# Client code demonstrating the Singleton behavior

# Create the first instance (Singleton instance)
singleton1 = Singleton()

# Setting values using the set_cache method
singleton1.set_cache("user1", "Alice")
singleton1.set_cache("user2", "Bob")

# Logging some messages
singleton1.log("First log entry")
singleton1.log("Second log entry")

# Print the cache and logs to verify data is stored
print("Cache from singleton1:", singleton1.get_cache())  # Should show both user1 and user2
print("Logger from singleton1:", singleton1.logger)  # Should show both log entries

# Create another instance (should be the same instance as singleton1)
singleton2 = Singleton()

# Accessing the cache and logs from the second instance
print("Cache from singleton2:", singleton2.get_cache())  # Should show same data as singleton1
print("Logger from singleton2:", singleton2.logger)  # Should show same log entries as singleton1

# Verifying that both instances are the same
print(singleton1 is singleton2)  # Should print True because both are the same instance



"""
Above code ensures that the Singleton class is thread-safe, meaning that even if multiple threads try to create an instance at the same time, only one instance will be created. 
Double-check locking is used to ensure that the instance is created only once, even if multiple threads reach the `__new__` method simultaneously.

Normal Lock always acquires the lock, leading to higher overhead but ensuring thread safety.

Double Lock optimizes performance by checking first (without the lock) and acquiring the lock only when necessary, making it more efficient in multithreaded environments.

Second Check (inside the lock): After acquiring the lock, we check again whether the instance has been created. This second check is necessary because another thread might have created the instance between the time we checked and acquired the lock.

"""

"""
Real Use Cases for Singleton Pattern with Double-Checked Locking:
1. **Database Connection**: Ensures that only one database connection is created and shared across multiple threads, avoiding unnecessary resource consumption.
2. **Logger**: Guarantees a single instance of the logger for consistent logging across threads, ensuring thread-safety and preventing log duplication.
3. **Configuration Manager**: Loads and shares configuration settings across threads, ensuring it's only loaded once, improving efficiency and avoiding redundant loading.
Double-checked locking optimizes thread safety and performance by reducing unnecessary locking while ensuring proper synchronization during instance creation.
"""



"""
_lock: A lock is created to ensure that only one thread can enter the critical section of code (where the instance is created).

with cls._lock:: This acquires the lock, and ensures that other threads cannot access the block of code inside the with statement until the lock is released.
"""