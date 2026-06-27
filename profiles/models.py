from django.db import models
from accounts.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    university = models.CharField(max_length=200, default='KCA University')
    course = models.CharField(max_length=200, blank=True)
    year_of_study = models.PositiveIntegerField(null=True, blank=True)
    bio = models.TextField(blank=True)
    skills = models.TextField(blank=True, help_text="Comma-separated skills")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    portfolio = models.URLField(blank=True)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    total_earned = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    jobs_completed = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def skills_list(self):
        return [s.strip() for s in self.skills.split(',') if s.strip()]

    def __str__(self):
        return f"{self.user.get_full_name()} — Student Profile"

    def avg_rating(self):
        reviews = self.user.received_reviews.all()
        if reviews.exists():
            return round(sum(r.rating for r in reviews) / reviews.count(), 1)
        return None


class ClientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    company_name = models.CharField(max_length=200, blank=True)
    industry = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    website = models.URLField(blank=True)
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} — Client Profile"
