class YouTubeChannel:
    def __init__(self):
        self.video = None
        self.subscribers = []  # List to store subscribers

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)  # Add subscriber

    def upload_video(self, video):
        self.video = video
        self.notify_subscribers()  # Notify all subscribers when a video is uploaded

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.video)  # Directly notify each subscriber

class EmailSubscriber:
    def update(self, video):
        print(f"Email Subscriber: New video uploaded: {video}")

class SMSSubscriber:
    def update(self, video):
        print(f"SMS Subscriber: New video uploaded: {video}")

class PushNotificationSubscriber:  # New type of subscriber
    def update(self, video):
        print(f"Push Notification Subscriber: New video uploaded: {video}")


# Client Code
channel = YouTubeChannel()

# Subscribe existing subscribers
email_subscriber = EmailSubscriber()
sms_subscriber = SMSSubscriber()

# Add new type of subscriber without modifying YouTubeChannel class
push_subscriber = PushNotificationSubscriber()

# Subscribe to the channel
channel.subscribe(email_subscriber)
channel.subscribe(sms_subscriber)
channel.subscribe(push_subscriber)  # Adding the new subscriber

# Upload a new video
channel.upload_video("How to Design Patterns")



"""
Traditional Approach - Why It Is Bad:
- **Tightly Coupled Code**: In the traditional approach, the YouTubeChannel class is tightly coupled with specific types of subscribers (e.g., EmailSubscriber, SMSSubscriber). The YouTubeChannel class knows exactly how to notify each subscriber, which leads to **maintenance issues** when adding new subscriber types.
- **Scalability Issues**: As the number of subscriber types increases, the YouTubeChannel class grows increasingly complex. Every time you add a new subscriber type, you need to **modify** the YouTubeChannel class. This is cumbersome and violates the **Open/Closed Principle** (code should be open for extension, but closed for modification).
- **Manual Updates**: The YouTubeChannel class manually calls the `update()` method on each specific type of subscriber. This is repetitive and error-prone, especially when adding logic to handle new types of subscribers.
- **Hard to Extend**: If you want to add a new type of subscriber (e.g., PushNotificationSubscriber), you have to modify the YouTubeChannel class, which makes the system **less flexible** and harder to extend. New behavior cannot be added without modifying existing classes.

Why the Interface Is Needed:
- **Decoupling**: The interface abstracts the behavior of subscribers, ensuring that the YouTubeChannel only needs to know about the common method (i.e., `update()`). It doesn't need to know the specifics of how each subscriber handles the update, whether it sends an email, an SMS, or a push notification. This decouples the **subject** (YouTubeChannel) from the **observers** (subscribers).
- **Flexibility**: With the interface, new types of subscribers can be easily added without modifying the YouTubeChannel class. Subscribers simply implement the common interface and subscribe to the channel. The YouTubeChannel can notify them without caring about their specific type.
- **Maintainability**: The interface makes the system easier to maintain because it allows new subscribers to be added independently of the YouTubeChannel class. This leads to cleaner, more **modular** code.
- **Scalability**: As the number of subscriber types grows, the YouTubeChannel class remains **unchanged**, and you can simply add more subscriber classes that implement the interface. This ensures that the code remains flexible, extendable, and easy to scale.

"""
