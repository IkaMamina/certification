from django.db import models


class Network(models.Model):
    LEVEL = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.IntegerField()
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Клиенты')
    debt_to_supplier = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Сети"


class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    release_date = models.DateField()
    products = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='Продукты')

    def __str__(self):
        return f'{self.name} ({self.model})'

    class Meta:
        verbose_name_plural = "Продукты"


