from django.urls import path

from .views import CastView, MovieCastView, ActorCastView
urlpatterns = [
    path("", CastView.as_view()),
    path("movie/", MovieCastView.as_view()),
    path("actor/", ActorCastView.as_view())
]
