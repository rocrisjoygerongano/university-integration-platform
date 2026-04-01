from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Optional home page
def home(request):
    return JsonResponse({"message": "University Integration API is running!"})

urlpatterns = [
    path('', home),  # root URL
    path('admin/', admin.site.urls),
    path('api/student/', include('student_app.urls')),
    path('api/library/', include('library_app.urls')),
    path('api/payment/', include('payment_app.urls')),
]
