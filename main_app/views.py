from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Investment, Source, Prediction

from .forms import PredictionForm

def home(request):
    return render(request, 'home.html')

def list(request):
  investments = Investment.objects.all()
  return render(request, 'investments/index.html', { 'investments': investments })

def detail(request, id):
  investment = Investment.objects.get(id=id)
  sources = Source.objects.exclude(id__in=investment.sources.all().values_list('id')).all()
  prediction_form = PredictionForm()
  return render(request, 'investments/detail.html', {
    'investment': investment,
    'prediction_form': prediction_form,
    'sources': sources
  })

class InvestmentCreate(CreateView):
  model = Investment
  fields = ['name', 'amount', 'description']

class InvestmentUpdate(UpdateView):
  model = Investment
  fields = ['amount', 'description']

class InvestmentDelete(DeleteView):
  model = Investment
  success_url = '/investments/'

def add_prediction(request, id):
  form = PredictionForm(request.POST)
  if form.is_valid():
    prediction = form.save(commit=False)
    prediction.investment_id = id
    prediction.save()
  return redirect('detail', id=id)

def remove_prediction(request, prediction_id):
  prediction = Prediction.objects.get(id=prediction_id)
  investment_id = prediction.investment.id
  prediction.delete()
  return redirect('detail', id=investment_id)

class SourceList(ListView):
  model = Source

class SourceDetail(DetailView):
  model = Source

class SourceCreate(CreateView):
  model = Source
  fields = '__all__'

class SourceUpdate(UpdateView):
  model = Source
  fields = ['name', 'amount', 'payment_method']

class SourceDelete(DeleteView):
  model = Source
  success_url = '/sources/'

def assoc_source(request, id, source_id):
  Investment.objects.get(id=id).sources.add(source_id)
  return redirect('detail', id=id)

def unassoc_source(request, id, source_id):
  Investment.objects.get(id=id).sources.remove(source_id)
  return redirect('detail', id=id)
