from django.db import models


# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Project(models.Model):  # like category
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    text = models.TextField()
    labels = models.ManyToManyField(Label)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    date_added = models.DateTimeField()
    reviews_counter = models.IntegerField(default=0)
    link_url = models.URLField(default='')
    link_file = models.FileField(default=None, null=True)

    def __str__(self):
        return '{} — {}'.format(self.text[:100], self.project)
