from django.db import models

# Create your models here.

class VCFUpload(models.Model):
    title = models.CharField(max_length=100)
    vcf = models.FileField(null=True, blank=True, upload_to="")

    def __str(self):
        return self.title
        