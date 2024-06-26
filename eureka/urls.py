"""
URL configuration for eureka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import main_site.views as views
import main_site.api_views as api_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registration_view, name='registration'),
    path('new_idea/', views.new_idea_view, name='new_idea'),
    path('profile/', views.profile_view, name='profile'),
    path('add_like/<int:id>/', api_views.add_like),
    path('add_dislike/<int:id>/', api_views.add_dislike),
    path('delete_idea/<int:id>/', api_views.delete_idea),
    path('api/index/', api_views.get_ideas),
    path('add_request/', api_views.add_request)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
