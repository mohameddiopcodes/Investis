from django.db import models

from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

PAYMENTS = (
  ('CC', 'Credit Card'),
  ('CA', 'Cash'),
  ('WT', 'Wire Transfer'),
  ('CR', 'Cryptocurrency')
)

class Source(models.Model):
  name = models.CharField(max_length=100)
  amount = models.IntegerField()
  date = models.DateField('Bought on')
  payment_method = models.CharField(
    'Payment Method',
    max_length=2,
    choices=PAYMENTS,
    default=PAYMENTS[0][0]
  )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('list_source')

  class Meta:
    ordering = ['-date']

class Investment(models.Model):
  name = models.CharField(max_length=100)
  amount = models.IntegerField()
  description = models.TextField(max_length=500)
  sources = models.ManyToManyField(Source)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'id': self.id})

  def has_sources(self):
    return len(self.sources.all()) > 0 

class Prediction(models.Model):
  date = models.DateField('Predicted on')
  amount = models.IntegerField()
  investment = models.ForeignKey(Investment, on_delete=models.CASCADE)

  def __str__(self):
    return self.amount

  def get_absolute_url(self):
    return reverse('detail', kwargs={'id': self.id})

  class Meta:
    ordering = ['-date']