from blog_app.views import*
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',registerPage,name='registerPage'),
    path('loginPage/',loginPage,name='loginPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    
    path('homePage/',homePage,name='homePage'),
    path('addPage/',addPage,name='addPage'),
    path('postPage/',postPage,name='postPage'),
    
    path('postDlt/<int:id>',postDlt,name='postDlt'),
    path('postEdit/<int:id>',postEdit,name='postEdit'),
    path('publish_status/<int:id>',publish_status,name='publish_status'),
    
    path('reject_status/<int:id>',reject_status,name='reject_status'),
    
    path('pending_status/<int:id>',pending_status,name='pending_status'),
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
