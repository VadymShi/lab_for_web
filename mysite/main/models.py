from django.db import models


class Office(models.Model):
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
