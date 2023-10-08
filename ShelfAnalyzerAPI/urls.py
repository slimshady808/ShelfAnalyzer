from django.urls import path
from . import views
# analyze-shelf/
urlpatterns = [
    path('analyze-shelf/', views.analyze_shelf, name='analyze_shelf'),
]