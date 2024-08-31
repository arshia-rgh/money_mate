from datetime import datetime

from app.firebase_config import realtime_db
from app.schemas.notification import Notification
from app.utils.send_mail import send_mail_async


class NotificationCRUD:
    def __init__(self, user_id: str, user_email: str):
        self.user_id = user_id
        self.user_email = user_email

    async def new_notification(self, notification: Notification):
        notification_data = notification.model_dump()
        notification_data["created_at"] = datetime.now()
        notification_data["updated_at"] = datetime.now()
        notification_data["user_id"] = self.user_id

        await realtime_db.child("notifications").push(notification_data)

        subject = notification.title
        body = notification.message
        email_to = self.user_email

        await send_mail_async(subject, email_to, body)

    async def get_notifications(self):
        notifications = []
        notifications_ref = realtime_db.child("notifications").order_by_child("user_id").equal_to(self.user_id).get()

        if notifications_ref:
            for k, v in notifications_ref.items():
                notifications.append(v)

        return notifications

    async def listen_notifications(self):
        pass
