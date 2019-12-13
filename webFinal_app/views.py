from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from .models import Feedback, Car
from django.views.generic import TemplateView, ListView


def indexView(request):
    search_query = request.GET.get('search', '')
    if search_query:
        cars = Car.objects.filter(Q(model_of_car__icontains=search_query))
        return redirect('result.html')
    else:
        cars = Car.objects.all()
    return render(request, 'index.html')


def leave_feedback(request):
    try:
        f = Feedback.objects.all()

    except:
        raise Http404("You don't have feedbacks")

    txt1 = request.GET.get("name")
    txt2 = request.GET.get("email")
    txt3 = request.GET.get("message")

    feedback_res = Feedback(name_of_user=txt1, email_of_user=txt2, message_of_user=txt3)
    feedback_res.save()
    return render(request, "feedback_result.html", {'f': f})


@login_required()
def dashboardView(request):
    return render(request, 'dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def result(request):
    return render(request, 'result.html')


def carA(request):
    return render(request, 'A.html')
def carB(request):
    return render(request, 'B.html')
def carC(request):
    return render(request, 'C.html')
def carE(request):
    return render(request, 'E.html')
def carS(request):
    return render(request, 'S.html')
def carGLS(request):
    return render(request, 'GLS.html')
def carM(request):
    return render(request, 'Mayb.html')
def carAMG(request):
    return render(request, 'GT.html')


class ShowCarView(ListView):
    model = Car
    template_name = "car.html"
    context_object_name = 'cars'

    def get_context_data(self,  **kwargs):
        ctx = super(ShowCarView, self).get_context_data(**kwargs)
        ctx['title'] = "Mercedes OP"
        return ctx
#
#
# class CarDetailView(DetailView):
#     model = Characteristics
#     template_name = "car_detail.html"
#     context_object_name = "cars_d"


class HomePageView(TemplateView):
    template_name = 'index.html'


class SearchResultsView(ListView):
    model = Car
    template_name = 'search_engine.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Car.objects.filter(
            Q(model_of_car__icontains=query) | Q(about_car__icontains=query)
        )
        return object_list






