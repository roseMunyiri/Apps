from django.urls import path
from .views import CreateViewPage, HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("upload/", CreateViewPage.as_view(), name="upload_post")
]