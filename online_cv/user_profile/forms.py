
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ("picture",)