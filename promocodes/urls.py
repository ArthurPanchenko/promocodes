from django.urls import path

from . import views


urlpatterns = [
    path('', views.BalanceDetail.as_view()),
    path('promo/', views.PromocodeList.as_view())
]