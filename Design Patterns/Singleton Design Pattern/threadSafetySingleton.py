import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:  # Ensures thread safety when creating the instance
                if cls._instance is None:  # Double-check to avoid race conditions
                    cls._instance = super().__new__(cls)
                    cls._instance.cache = {}  # Initialize cache
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


"""
Above code ensures that the Singleton class is thread-safe, meaning that even if multiple threads try to create an instance at the same time, only one instance will be created. 
Double-check locking is used to ensure that the instance is created only once, even if multiple threads reach the `__new__` method simultaneously.

Normal Lock always acquires the lock, leading to higher overhead but ensuring thread safety.

Double Lock optimizes performance by checking first (without the lock) and acquiring the lock only when necessary, making it more efficient in multithreaded environments.

"""


"""
_lock: A lock is created to ensure that only one thread can enter the critical section of code (where the instance is created).

with cls._lock:: This acquires the lock, and ensures that other threads cannot access the block of code inside the with statement until the lock is released.
"""