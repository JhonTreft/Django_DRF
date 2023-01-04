from django.urls import path

from .views import people_list

urlpatterns=[
        path('list_people/',people_list.as_view(),name="list-people"),
        ]
