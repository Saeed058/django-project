from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": {"cmspages": CMSSitemap}}),
    path('', include('eshoper.django_login.urls')),
    path('', include('eshoper.search.urls')),
    path('', include('eshoper.paginator.urls')),
    path('en/api/', include('eshoper.api.urls')),
    path('', include('eshoper.cart.urls')),
    path('en/login/', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}),
    path('logout/', auth_views.LogoutView.as_view()),
]


urlpatterns += i18n_patterns(path("admin/", admin.site.urls), path("", include("cms.urls")),)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

