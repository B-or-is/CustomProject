"""CustomProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include
# from django.conf.urls import include

from custom_1.views import CreateUser
from custom_2.views import UpdateProfile
from user_app import views
from user_app.views import Index

from django.conf.urls.static import static
# from .settings import MEDIA_ROOT, MEDIA_URL
from CustomProject.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    # path('', views.index),
    path('', Index.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('all_users/', include('custom_1.urls')),
    path('all_users2/', include('custom_2.urls')),
    # path('all_users3/', include('custom_3.urls')),
    path('signup/', CreateUser.as_view(), name="signup"),
    path('signup2/', CreateUser.as_view(), name="signup2"),
    path('profile/<pk>', UpdateProfile.as_view(), name='profile'),
    path('profile/', Index.as_view(), name="index"),
    # path('grappelli/', include('grappelli.urls')),
    ] + static(MEDIA_URL, document_root=MEDIA_ROOT)

# обработку - см.views.py в ЭТОМ каталоге
handler404 = "CustomProject.views.page_not_found_view"

