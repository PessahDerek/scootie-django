"""
URL configuration for scootie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework import routers
from bikes import views as bike_views
from content import views as content_views
from cart import views as cart_views
from scootie import settings

router = routers.DefaultRouter()
router.register(r'bikes', bike_views.BikeViewSet)
router.register(r'category', bike_views.CategoryViewSet)
router.register(r'content', content_views.ContentViewSet)
router.register(r'reviews', content_views.ReviewsViewSet)
router.register(r'videos', content_views.VideoViewSet)
router.register(r'faqs', content_views.FaqViewSet)
router.register(r'contacts', content_views.ContactViewSet)
router.register(r'cart', cart_views.CartViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('bikes/by-category-page/<category>/<page>/', bike_views.BikeViewSet.by_category),
    # path('bikes/<category>/', bike_views.BikeViewSet.as_view({'get': 'retrieve'})),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# else:
#     urlpatterns += static(settings.MEDIA_URL,)