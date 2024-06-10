from django.db import models

class Risk(models.Model):
    date_raised = models.DateField(editable=True)
    description = models.TextField()
    likelihood = models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')])
    impact = models.IntegerField(choices=[(1, 'low'), (2, 'medium'), (3, 'high')])
    owner = models.CharField(max_length=100)
    email = models.EmailField()
    mitigating_action = models.TextField()

    @property
    def severity(self):
        severity_score = self.likelihood * self.impact
        if severity_score <= 2:
            return 'low'
        elif severity_score <= 4:
            return 'medium'
        else:
            return 'high'
    def __str__(self):
        return self.description
