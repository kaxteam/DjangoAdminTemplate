from django.conf.urls import include, url
from panel import views

panelurl = [
    url(r'^', views.panel)
]

urlpatterns = [
    url(r'^/', views.root),
    url(r'^panel/', include(panelurl)),
]
