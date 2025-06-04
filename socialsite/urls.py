from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from socialapp.forms import BootstrapAuthenticationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('socialapp.urls')),
    path('insightmint/', include('insightmint.urls')),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=BootstrapAuthenticationForm), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
