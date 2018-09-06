from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonListView.as_view(), name='persons'),
    path('persons/<int:pk>', views.PersonDetailView.as_view(), name='person-detail'),
]
