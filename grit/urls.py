from django.urls import path
from django.conf.urls import include
from gritapi.views import register_user, login_user
from rest_framework import routers
from django.contrib import admin
from gritapi.views import NearEarthObjectView

# this parses the urls
# the register_user and login_user functions are imported into the module. Then they are used to map a route to that view.
router = routers.DefaultRouter(trailing_slash=False)
# /gametypes?label=blue
router.register(r'nearearthobjects', NearEarthObjectView, 'nearearthobject')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
]