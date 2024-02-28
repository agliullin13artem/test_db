from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=199)
    start_date = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def distribute_users_to_group(self):
        groups = Group.objects.filter(product=self).order_by('min_students')
        students = User.objects.all().exclude(group__in=groups)

        for student in students:
            suitable_group = groups[0]
            suitable_group.students.add(student)
            if suitable_group.students.count() == suitable_group.max_students:
                groups = groups[1:]



class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=199)
    video_link = models.URLField()


class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(User)
    min_students = models.IntegerField()
    max_students = models.IntegerField()
