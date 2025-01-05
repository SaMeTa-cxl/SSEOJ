from django.db import models


class SysConfigs(models.Model):
    key = models.CharField(max_length=25, unique=True, db_index=True)
    value = models.JSONField()

    def __str__(self):
        return self.key