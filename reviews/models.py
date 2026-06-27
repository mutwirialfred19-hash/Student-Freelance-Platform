from django.db import models
from accounts.models import User
from projects.models import Project

class Review(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='reviews')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='given_reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_reviews')
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['project', 'client', 'student']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.rating}★ — {self.student.get_full_name()} by {self.client.get_full_name()}"
