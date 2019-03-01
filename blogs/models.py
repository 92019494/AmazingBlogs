from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    phone_number = models.DecimalField(max_digits=15, decimal_places=0,  null=True)
    email = models.EmailField(null=True)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField(null=True)
    publish_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title





#add picture profile_image = ImageField(upload_to=get_image_path, blank=True, null=True)
# choose font
