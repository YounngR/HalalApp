from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'halalapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('/goods', views.goods, name='goods'),
    path('/recipe', views.recipe, name='recipe'),
    path('/event', views.event, name='event'),
    path('/recipe_registration', views.recipe_registration, name='recipe_registration'),
    path('/sign_up', views.Sign_up, name='Sign_up'),
    path('/login', views.login, name='login'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
