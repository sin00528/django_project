from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('accountapp:login'))
def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))

    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list': data_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

# CBV이기 때문에 login_required decorator를 쓸 수 없음
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    # detail.html로 가야하나, key을 전달할수 있는 방법이 없으므로 일단은 hello_world로 돌아간다
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


# CBV이기 때문에 login_required decorator를 쓸 수 없음
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'


