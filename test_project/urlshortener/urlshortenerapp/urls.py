from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('url/<str:short_code>/', views.redirect_original_url),
    path('url/', views.create_short_url),

    # ...
]