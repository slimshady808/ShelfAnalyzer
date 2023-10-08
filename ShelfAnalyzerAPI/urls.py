from django.urls import path
from . import views
# analyze-shelf/
urlpatterns = [
    path('', views.analyze_shelf, name='analyze_shelf'),
]