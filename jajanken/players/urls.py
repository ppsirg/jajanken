from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from players import views

urlpatterns = [
    path('', views.PlayerListView.as_view()),
    path('<int:pk>', views.PlayerDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
