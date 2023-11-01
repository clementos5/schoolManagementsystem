from django.contrib import admin
from django.urls import path, include
from apps.corecode import admin as corecode_admin
from apps.corecode import admin as corecode_admin

urlpatterns = [    
    # Include the Django admin URLs
    path('admin/', admin.site.urls),
     # school_app/urls.py
    # Include your custom admin URLs
    #path('admin/', corecode_admin.custom_admin_site.urls),

    # Your other app URLs go here
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("apps.corecode.urls")),
    path("student/", include("apps.students.urls")),
    path("staff/", include("apps.staffs.urls")),
    path("finance/", include("apps.finance.urls")),
    path("result/", include("apps.result.urls")),
]
