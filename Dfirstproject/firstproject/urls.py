"""
URL configuration for firstproject project.

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
from community.views import *
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List, name="main"),
    path('<int:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('delete/<int:pk>', delete, name="delete"),
    path('update_page/<int:pk>', update_page, name="update_page"),
    path('update/<int:pk>', update,name="update"),
    path('<int:pk>/comment', add_comment,name="add_comment"),
    path('<int:pk>/comment/delete/<int:comment_pk>', comments_delete,name="comments_delete"),
    path('<int:pk>/likes', likes, name='likes'),
    # path('<int:pk>/recommend', add_recommend,name="add_recommend"),

    path('accounts/login', accounts.views.login_view, name='login'),
    path('accounts/logout', accounts.views.logout_view, name='logout'),
    path('accounts/signup', accounts.views.signup_view, name='signup'),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
