"""
URL configuration for tourism project.

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
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularRedocView, SpectacularAPIView

from tourism_app.views import SubmitData, ListMountainPasses, DetailMountainPass


urlpatterns = [
    path('admin/', admin.site.urls),
    path('filterData/', ListMountainPasses.as_view(), name='filter_pass'),

    path('submitData/', include(
            [
                path('<int:pk>/', DetailMountainPass.as_view(), name='update_pass'),
                path('', SubmitData.as_view(), name='create_pass'),
            ]
        )
    ),
    path('api/schema/', include(
            [
                path('', SpectacularAPIView.as_view(), name='schema'),
                path('swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                path('documentation/', SpectacularRedocView.as_view(url_name='schema'), name='documentation'),
            ]
        )
    )
]
