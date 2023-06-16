from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.urls import reverse
import uuid
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.db import models
from django.utils import timezone


User = get_user_model()


class WorkExperience(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name = "work_experiences", on_delete=models.CASCADE)
    cv = models.ForeignKey("CV", verbose_name=_("cv"), on_delete=models.CASCADE)
    workplace_name = models.CharField(_("workplace_name"), max_length=100, db_index=True)
    date_from = models.DateField(_("date_from"), default=timezone.now)
    date_until = models.DateField(_("date_until"), default=timezone.now)
    duties = models.CharField(_("duties"), max_length=100, db_index=True)

    class Meta:
        verbose_name = _("work experience")
        verbose_name_plural = _("work experiences")

    def __str__(self):
        return f"{self.workplace_name} | {self.duties} | From: {self.date_from} Until: {self.date_until}"
    
    def get_absolute_url(self):
        return reverse("workexperience_detail", kwargs={"pk": self.pk})
    

class Education(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name = "educations", on_delete=models.CASCADE)
    cv = models.ForeignKey("CV", verbose_name=_("cv"), on_delete=models.CASCADE)
    program = models.CharField(_("program"), max_length=100, db_index=True)
    date_from = models.DateField(_("date_from"), default=timezone.now)
    date_until = models.DateField(_("date_until"), default=timezone.now)
    
    
    SCHOOL_CHOICES = (
        ("middle", _("Middle School")),
        ("high", _("High School")),
        ("home", _("Home Schooling")),
        ("vocational", _("Vocational School")),
        ("university/college", _("University/College")),
        ("certificate", _("Certificate"))
    )

    school = models.CharField(_("school"), default="middle", max_length=100, choices=SCHOOL_CHOICES, db_index=True)
    # school_name = models.CharField(_("school_name"), max_length=100, db_index=True)


    class Meta:
        verbose_name = _("education")
        verbose_name_plural = _("educations")

    def __str__(self):
        return f"{self.user} | {self.school} | {self.program} | From: {self.date_from} Until: {self.date_until}"

    def get_absolute_url(self):
        return reverse("education_detail", kwargs={"pk": self.pk})
    

class Skill(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name = "skills", on_delete=models.CASCADE)
    cv = models.ForeignKey("CV", verbose_name=_("cv"), on_delete=models.CASCADE)
    skill = models.CharField(_("skill"), max_length=100, db_index=True)

    class Meta:
        verbose_name = _("skill")
        verbose_name_plural = _("skills")

    def __str__(self):
        return f"{self.user} | {self.skill}"

    def get_absolute_url(self):
        return reverse("skill_detail", kwargs={"pk": self.pk})
    

class Summary(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name = "summaries", on_delete=models.CASCADE)
    cv = models.ForeignKey("CV", verbose_name=_("cv"), on_delete=models.CASCADE)
    about_user = models.TextField(_("about_user"), max_length=500)

    class Meta:
        verbose_name = _("summary")
        verbose_name_plural = _("summaries")

    def __str__(self):
        return f"{self.user}"

    def get_absolute_url(self):
        return reverse("summary_detail", kwargs={"pk": self.pk})


class CV(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name = "certificates", on_delete=models.CASCADE)
    first_name = models.CharField(_("first_name"), max_length=100)
    last_name = models.CharField(_("last_name"), max_length=100, db_index=True)
    email = models.CharField(_("email"), max_length=100, db_index=True)
    # country_code = models.CharField(_("code"), max_length=10)
    # extention = models.IntegerField(_("phone_number"), max_length=20)
    city = models.CharField(_("city"), max_length=100, db_index=True)
    picture = models.ImageField(_("picture"), upload_to="online_cv/media/ptu12_cv/cv_pictures", null=True, blank=True)
    title = models.CharField(_("title"), max_length=100)
    # scope = models.CharField(_("scope"), max_length=150)

    class Meta:
        verbose_name = _("CV")
        verbose_name_plural = _("CVs")

    def __str__(self):
        return f"{self.user} {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("cv_detail", kwargs={"pk": self.pk})



    


    


