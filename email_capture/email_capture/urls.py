from django.urls import path
from email_app.views import landing_page, capture_email_route

urlpatterns = [
   path('', landing_page, name='landing_page'),
   path('capture_email', capture_email_route, name='capture_email')
]
