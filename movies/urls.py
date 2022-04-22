from django.urls import include, path

from .views import MovieListAPIView
from .routers import router
urlpatterns = [
    path("", include(router.urls)),
    path("movies-list/", MovieListAPIView.as_view())
]
