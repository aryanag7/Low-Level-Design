from abc import ABC, abstractmethod

# Observer Interface
class Subscriber(ABC):
    @abstractmethod
    def update(self, video):
        pass


# Concrete Subscriber 1: Email Subscriber
class EmailSubscriber(Subscriber):
    def update(self, video):
        print(f"Email: A new video has been uploaded: {video}")

# Concrete Subscriber 2: SMS Subscriber
class SMSSubscriber(Subscriber):
    def update(self, video):
        print(f"SMS: A new video has been uploaded: {video}")

# Concrete Subscriber 3: Push Notification Subscriber
class PushNotificationSubscriber(Subscriber):
    def update(self, video):
        print(f"Push Notification: A new video has been uploaded: {video}")



class YouTubeChannel:
    def __init__(self):
        self.video = None
        self.subscribers = []  # List to store subscribers (observers)

    def subscribe(self, subscriber: Subscriber):
        self.subscribers.append(subscriber)  # Add a subscriber

    def unsubscribe(self, subscriber: Subscriber):
         self.subscribers.remove(subscriber) 

    def upload_video(self, video):
        self.video = video
        self.notify_subscribers()  # Notify all subscribers when a video is uploaded

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.video)  # Call update() on each subscriber


# Client Code
channel = YouTubeChannel()

# Subscribe existing subscribers
email_subscriber = EmailSubscriber()
sms_subscriber = SMSSubscriber()

# Add new subscriber (Push Notification)
push_subscriber = PushNotificationSubscriber()

# Subscribe to the channel
channel.subscribe(email_subscriber)
channel.subscribe(sms_subscriber)
channel.subscribe(push_subscriber)  # Add the new subscriber


# Upload a new video (this will trigger notifications to all subscribers)
channel.upload_video("How to Design Patterns")



channel.unsubscribe(push_subscriber)  


channel.upload_video("How to Design Patterns Part 2")



"""
each subscriber can have all the 3 types of notifications without modifying the YouTubeChannel class. Alice has Email, SMS, and Push Notification subscribers, while Bob has only Email and SMS subscribers. This demonstrates the flexibility of the Observer Design Pattern rather than the traditional approach where the YouTubeChannel class is tightly coupled with specific subscriber types.
"""


"""
Good Code (Using Observer Pattern):
- The `YouTubeChannel` class is decoupled from specific subscriber types by using a `Subscriber` interface.
- The `YouTubeChannel` only knows that it has a list of `Subscriber` objects which is of type Subscriber and calls their `update()` method, making it flexible and extensible.
- New subscriber types (e.g., `PushNotificationSubscriber`) can be added easily without modifying the `YouTubeChannel` class.
- This implementation adheres to the **Open/Closed Principle**: the code is open for extension but closed for modification.
- The system is **modular** and **scalable**, as new behavior (subscribers) can be added without affecting existing code.
"""


"""
Real Use Case Examples (Observer Pattern):
- **Weather Monitoring System**: The **WeatherStation** (subject) notifies various **observers** (e.g., mobile app, desktop app, and weather website) when the temperature changes. New observers can be added without modifying the **WeatherStation** class, making the system scalable.
- **Social Media Updates**: A **SocialMediaPlatform** (subject) notifies **users** (observers) about new posts, comments, or messages. Different types of notifications (email, SMS, in-app) can be added by creating new observer classes without changing the platform’s core logic.
"""
