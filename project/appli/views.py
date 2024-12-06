from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request,'home.html')



def list(request):
    return render(request,'list.html')

# ----------------------create------------------------------------

from django.views.generic.edit import CreateView

class Createproject(CreateView):
    model = addproject
    template_name = 'add.html'
    fields = '__all__'
    success_url = reverse_lazy('home')

    def form_valid(self, form):         
        return super().form_valid(form)
    
# ----------------list-----------------------------------------

from django.views.generic import ListView

class listproject(ListView):
    model = addproject
    template_name = 'list.html'
    context_object_name = 'blg'
    ordering = ['-end_date'] #ascending order


# -----------------update view-------------

from django.views.generic.edit import UpdateView,DeleteView

from django.urls import reverse_lazy
class UpdateView(UpdateView):
    model =addproject
    template_name = 'update.html'
    fields ='__all__'

    def get_success_url(self): 
        return reverse_lazy('blg')#,kwargs ={'pk':self.object.id})


# -----------delete view-------------------
class DeleteView(DeleteView):
    model = addproject
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


    # ==================fetailed=======================


from django.views.generic.detail import DetailView
class Detailproject(DetailView):
    model=addproject
    template_name='detailes.html'
    context_object_name='blg'

# --------------------forms-----------------------------


from .forms import CreatingForm

def task(request):
    if request.method == "POST":
        form = CreatingForm(request.POST)
        if form.is_valid():
            form.save()
    form = CreatingForm()
    dict_form = {
        'form':form
    }
    return render(request,'add.html',dict_form)