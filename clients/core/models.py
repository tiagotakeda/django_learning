from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='clientes')
    dt_birth = models.DateField(null=True, blank=True)

    def get_fullname(self):
        return self.name + ' ' + self.last_name

    def __str__(self) -> str:
        return self.get_fullname()