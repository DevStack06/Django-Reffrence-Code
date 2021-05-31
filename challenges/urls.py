from django.urls import path
from . import views

urlpatterns = [
    # path("january", views.index),
    # path("<month>", views.get_Challenges)
    path("<int:month>", views.get_challenge_bynumber),
    path("<str:month>", views.get_Challenges)

]
