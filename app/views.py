from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Create your views here.

@login_required
def index(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html',{'user':request.user})

def get_next_number(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'get_next_number.html')

def get_number_status(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'get_number_status.html')

def reports(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'reports.html')

def manage_range(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'manage_range.html')


def mangae_report(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'mangae_report.html')


def manage_reservation(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'manage_reservation.html')

def manage_rule(request):
    #context = {'latest_question_list': latest_question_list}
    return render(request, 'manage_rule.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
