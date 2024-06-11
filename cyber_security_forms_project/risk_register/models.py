from django.db import models

class Risk(models.Model):
    LIKELIHOOD_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    IMPACT_CHOICES = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High'),
    ]

    date_raised = models.DateField()
    description = models.TextField()
    likelihood = models.IntegerField(choices=LIKELIHOOD_CHOICES)
    impact = models.IntegerField(choices=IMPACT_CHOICES)
    owner = models.CharField(max_length=100)
    email = models.EmailField()
    mitigating_action = models.TextField()

    @property
    def severity(self):
        return self.likelihood * self.impact

    def __str__(self):
        return self.description


