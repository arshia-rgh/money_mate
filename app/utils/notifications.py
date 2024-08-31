import asyncio
from datetime import datetime

from fastapi import BackgroundTasks
from firebase_admin import auth

from app.firebase_config import realtime_db,
from app.schemas.notification import Notification
from app.utils.send_mail import send_mail_async


class NotificationCRUD:
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
        def listener(event):
            if event.data:
                notification = Notification(**event.data)
                asyncio.create_task(self.new_notification(notification))

        realtime_db.child("notifications").order_by_child("user_id").equal_to(self.user_id).listen(listener)

    def start_listening(self, background_tasks: BackgroundTasks):
        background_tasks.add_task(self.listen_notifications)
