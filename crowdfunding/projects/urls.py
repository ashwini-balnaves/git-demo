from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<uuid:code>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('', views.HelloWorld.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)