from django.db import models
from datetime import datetime


class Base(models.Model):

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        default=datetime.now,
        blank=True
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class Assignment(Base):

    title = models.CharField(max_length=250, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    status = models.CharField(max_length=250, null=True, blank=True)
    def __str__(self):
        return {
                "title": self.title,
                "balance": self.description,
                "status": self.status,
                "created_at": self.created_at
                }

