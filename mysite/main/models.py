from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
    on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    def __str__(self):
        return f'Profile of {self.user.username}'

class Office(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Поле для збереження інформації про користувача, який створив офіс
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.location})'

class Worker(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    offices = models.ManyToManyField(Office, related_name='workers', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Employment(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    hire_date = models.DateField()
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.worker} hired on {self.hire_date} as {self.position}'
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    hire_date = models.DateField()
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=8, decimal_places=2)

    def str(self):
        return f'{self.worker} hired on {self.hire_date} as {self.position}'
