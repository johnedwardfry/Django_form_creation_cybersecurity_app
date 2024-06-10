from django.db import models

class Risk(models.Model):
    date_raised = models.DateField(auto_now_add=True)
    description = models.TextField()
    likelihood = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])
    impact = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])
    owner = models.CharField(max_length=100)
    email = models.EmailField()
    mitigating_action = models.TextField()

    @property
    def severity(self):
        return self.likelihood * self.impact

    def __str__(self):
        return self.description
