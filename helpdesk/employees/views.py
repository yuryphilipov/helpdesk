from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Department


def index(request):
    from datetime import datetime

    num_persons = Person.objects.all().count()
    num_departments = Department.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    times_str = 'раза' if num_visits % 10 in [2,3,4] and not (12 <= num_visits <= 14) else 'раз'
    request.session['num_visits'] = num_visits + 1
    
    return render(request, 'index.html', context={'num_persons': num_persons, 'num_departments': num_departments,
                                                  'num_visits': num_visits, 'times_str': times_str})
    

class PersonListView(generic.ListView):

    model = Person

    def get_context_data(self, **kwargs):
        context = super(PersonListView, self).get_context_data(**kwargs)
        # context['fio'] = ' '.join((Person.last_name, Person.first_name, Person.middle_name))
        return context


class PersonDetailView(LoginRequiredMixin, generic.DetailView):

    model = Person
    permission_required = 'person.can_view'
    def get_context_data(self, **kwargs):
        context = super(PersonDetailView, self).get_context_data(**kwargs)
        # context['department'] = Department.objects.get(pk=1).name
        context['department'] = self.get_object().department.name
        return context
