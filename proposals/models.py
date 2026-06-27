from django.db import models
from accounts.models import User
from projects.models import Project

class Proposal(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
        ('withdrawn', 'Withdrawn'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='proposals')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitted_proposals')
    cover_letter = models.TextField()
    proposed_price = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_days = models.PositiveIntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']
        unique_together = ['project', 'student']

    def __str__(self):
        return f"{self.student.get_full_name()} → {self.project.title}"
