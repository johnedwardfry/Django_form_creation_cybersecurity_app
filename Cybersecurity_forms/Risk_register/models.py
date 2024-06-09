from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class RISK_MATRIX(models.Model):
    date_raised = models.DateField()
    RISK_NAME = models.CharField(max_length=200)
    RISK_OWNER = models.CharField(max_length=200)
    RISK_OWNER_EMAIL = models.CharField(max_length=200)
    RISK_DESCRIPTION = models.TextField()
    MITIGATING_ACTION = models.TextField()

    RISK_LIKELIHOOD = models.IntegerField(default=1,
                                          validators=[
                                              MaxValueValidator(3),
                                              MinValueValidator(1)
                                          ])

    RISK_IMPACT = models.IntegerField(default=1,
                                      validators=[
                                          MaxValueValidator(3),
                                          MinValueValidator(1)
                                      ])

    RISK_SEVERITY = models.IntegerField(editable=False, )

    def save(self, *args, **kwargs):
        # Calculate RISK_SEVERITY
        self.RISK_SEVERITY = self.RISK_LIKELIHOOD * self.RISK_IMPACT
        super().save(*args, **kwargs)

    @property
    def severity(self):
        return self.RISK_LIKELIHOOD * self.RISK_IMPACT
