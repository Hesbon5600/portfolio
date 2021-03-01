from django_better_admin_arrayfield.models.fields import ArrayField
from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField


class BaseModel(models.Model):
    """
    The common field in all the models are defined here
    """
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp representing when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # add deleted option for every entry
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class Category(BaseModel):
    """
    Category model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    description = HTMLField()
    icon = models.CharField(max_length=50, blank=True, null=True)

    experience = models.IntegerField(blank=False, null=False)

    def __str__(self):
        """
        Returns a string representation of this `Category`.

        This string is used when a `Category` is printed in the console.
        """
        return f"<Category - {self.name}>"


class Project(BaseModel):
    """
    Project model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    slug = models.CharField(max_length=50, db_index=True,
                            blank=True, null=True)
    client = models.CharField(max_length=50, db_index=True,
                              blank=False, null=False)
    team_size = models.IntegerField(blank=False, null=False)

    description = HTMLField()
    icon = models.CharField(max_length=50, blank=True, null=True)
    category_style = models.CharField(max_length=100, blank=True, null=True)
    completion_date = models.DateField(max_length=50, db_index=True,
                                       blank=False, null=False)
    technologies = ArrayField(models.TextField(null=True, blank=True),
                              null=True, blank=True, default=list)
    roles = ArrayField(models.TextField(null=True, blank=True),
                       null=True, blank=True, default=list)
    success = ArrayField(models.TextField(null=True, blank=True),
                         null=True, blank=True, default=list)
    is_feature = models.BooleanField(default=False)
    ongoing = models.BooleanField(default=False)
    url = models.CharField(max_length=250, db_index=True,
                           blank=False, null=False)
    github_url = models.CharField(max_length=250,
                                  db_index=True, blank=False, null=False)
    image_url = models.CharField(max_length=250,
                                 db_index=True, blank=False, null=False)
    background_image_url = models.CharField(max_length=250,
                                            db_index=True, blank=False, null=False)
    thumbnail_image_url = models.CharField(max_length=250,
                                           db_index=True, blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        """
        Returns a string representation of this `Project`.

        This string is used when a `Project` is printed in the console.
        """
        return f"<Project - {self.name}>"

    def create_name_slug(self):
        """This method automatically slugs the name before saving"""
        slug = slugify(self.name)
        new_slug = slug
        n = 1
        while Project.objects.filter(slug=new_slug).exists():
            new_slug = '{}-{}'.format(slug, n)
            n += 1

        return new_slug

    def save(self, *args, **kwargs):
        """This method ensures that the project is saved with a slug"""
        if not self.slug:
            self.slug = self.create_name_slug()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-completion_date']


class Client(BaseModel):
    """
    Client model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    slug = models.CharField(max_length=50, db_index=True,
                            blank=True, null=True)
    description = HTMLField()
    fade_style = models.CharField(max_length=50, blank=False, null=False)
    description_style = models.CharField(
        max_length=50, blank=True, null=True)
    start_date = models.DateField(max_length=50, db_index=True,
                                  blank=False, null=False)
    end_date = models.DateField(max_length=50, db_index=True,
                                blank=True, null=True)
    background_image_url = models.CharField(max_length=250,
                                            db_index=True, blank=False, null=False)
    projects = models.ManyToManyField(
        Project, related_name="%(app_label)s_%(class)s_related")

    def __str__(self):
        """
        Returns a string representation of this `Client`.

        This string is used when a `Client` is printed in the console.
        """
        return f"<Client - {self.name}>"

    def create_name_slug(self):
        """This method automatically slugs the name before saving"""
        slug = slugify(self.name)
        new_slug = slug
        n = 1
        while Client.objects.filter(slug=new_slug).exists():
            new_slug = '{}-{}'.format(slug, n)
            n += 1

        return new_slug

    def save(self, *args, **kwargs):
        """This method ensures that the client is saved with a slug"""
        if not self.slug:
            self.slug = self.create_name_slug()
        super().save(*args, **kwargs)

    @property
    def skills(self):
        skills = []
        for i in self.projects.all():
            skills = [*skills, *i.category.all()]
        return list(set(skills))

    class Meta:
        ordering = ['-end_date']


class Email(BaseModel):
    """
    Client model
    """
    name = models.CharField(max_length=50, db_index=True,
                            blank=False, null=False)
    email = models.CharField(max_length=50, db_index=True,
                             blank=True, null=True)
    subject = models.TextField(
        max_length=50, blank=True, null=True)
    message = models.TextField(
        max_length=5000, blank=True, null=True)

    def __str__(self):
        """
        Returns a string representation of this `Email`.

        This string is used when a `Email` is printed in the console.
        """
        return f"<Email - {self.name}>"
