from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class HRRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("hr representative")
        verbose_name_plural = _("hr representatives")

    def __str__(self):
        return f"{self.user}"
    
    def get_absolute_url(self):
        return reverse("hrrepresentative_detail", kwargs={"pk": self.pk})


class MeetingReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hr_representative = models.ForeignKey(HRRepresentative, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        verbose_name = _("meeting reservation")
        verbose_name_plural = _("meeting reservations")

    def __str__(self):
        return f"{self.user} - {self.start_time} to {self.end_time}"
    
    def get_absolute_url(self):
        return reverse("meetingreservation_detail", kwargs={"pk": self.pk})