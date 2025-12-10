from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # 1. Admin Panel
    path('admin/', admin.site.urls),

    # 2. Authentication (Login, Signup, etc.)
    # This connects to your 'accounts' app. 
    # Ensure accounts/urls.py has path('login/', ...)
    path('auth/', include('accounts.urls')),

    # 3. Explicit Logout 
    # We define this here so {% url 'logout' %} works globally.
    # NEXT_PAGE redirects to login after logout
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # 4. The Dashboard (Home Page)
    # We place this at the bottom to handle the root URL ''.
    # This allows your Sales dashboard to be the homepage.
    path('', include('dashboard.urls')),
]