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
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
