from django.urls import path
from .views import index, blog, about, get_category, loginauth, signup, userlogout, account
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('', index, name="home"),
                  path('articles/<int:article_id>/', blog, name="blog"),
                  path('about/', about, name="about"),
                  path('category/<int:category_id>/', get_category),
                  path('loginauth/', loginauth, name="loginauth"),
                  path('signup/', signup, name="signup"),
                  path('logout/', userlogout, name="logout"),
                  path('account/', account, name="account")
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
