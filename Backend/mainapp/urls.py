from django.urls import path
from mainapp import views

urlpatterns = [
    path('get-mastodon/', views.get_mastodon, name='get-mastodon-data'),
    path('get-immigration/', views.get_immigration, name='get-immigration'),
    path('get-state/', views.get_state, name='get-state-data')
]
