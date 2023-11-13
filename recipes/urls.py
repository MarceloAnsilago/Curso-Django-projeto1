from django.urls import path
from recipes.views import home, sobre, contato

urlpatterns = [
    path('', home), # HOME
    path('sobre/', sobre), # SOBRE
    path('contato/', contato), #CONTATO

]
