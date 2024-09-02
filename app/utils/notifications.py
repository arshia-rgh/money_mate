import asyncio
from datetime import datetime

from fastapi import BackgroundTasks
from firebase_admin import auth

from app.firebase_config import realtime_db
from app.schemas.notification import Notification
from app.utils.send_mail import send_mail_async
from app.utils.serializers import serialize_item


class NotificationHandle:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.user_email = self.get_user_email()

    def get_user_email(self):
        try:
            user = auth.get_user(self.user_id)
            return user.email

        except auth.UserNotFoundError:
            pass

    async def new_notification(self, notification: Notification):
        notification.created_at = datetime.now()
        notification.updated_at = datetime.now()
        notification.user_id = self.user_id

        realtime_db.child("notifications").push(serialize_item(notification))

        subject = str(notification.title)
        body = str(notification.message)
        email_to = self.user_email

        await send_mail_async(subject=subject, body=body, email_to=email_to)

    async def get_notifications(self):
        notifications = []
        notifications_ref = realtime_db.child("notifications").order_by_child("user_id").equal_to(self.user_id).get()

        if notifications_ref:
            for k, v in notifications_ref.items():
                notifications.append(serialize_item(v))

        return notifications

    async def listen_notifications(self):
        def listener(event):
            if event.data:
                notification = Notification(**event.data)
                asyncio.create_task(self.new_notification(notification))

        realtime_db.child("notifications").order_by_child("user_id").equal_to(self.user_id).listen(listener)

    def start_listening(self, background_tasks: BackgroundTasks):
        background_tasks.add_task(self.listen_notifications)
