from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_friend_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_friend_requests')
    status = models.CharField(choices=(
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ), default='pending', max_length=20)

    def __str__(self):
        return f"Friend request from {self.sender.username} to {self.receiver.username}"
