from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, default='💼')
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, default='#6366f1')

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    BUDGET_TYPE_CHOICES = [
        ('fixed', 'Fixed Price'),
        ('hourly', 'Hourly Rate'),
    ]

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_projects')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='projects')
    title = models.CharField(max_length=300)
    description = models.TextField()
    skills_required = models.TextField(blank=True, help_text="Comma-separated skills")
    budget_type = models.CharField(max_length=10, choices=BUDGET_TYPE_CHOICES, default='fixed')
    budget_min = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    budget_max = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, blank=True, help_text="Leave blank for remote")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='open')
    is_approved = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def skills_list(self):
        return [s.strip() for s in self.skills_required.split(',') if s.strip()]

    def proposal_count(self):
        return self.proposals.count()
