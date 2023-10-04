from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import (create_item, dec_item, del_item, inc_item, login_user,
                        logout_user, register, show_html, show_json,
                        show_json_by_id, show_main, show_xml, show_xml_by_id)

app_name = 'main'

urlpatterns = [
    path('create-item', create_item, name='create_item'),
    path('', show_main, name='show_main'),
    path('del-item/<int:id>/', del_item, name='del_item'),
    path('inc-item/<int:id>/', inc_item, name='inc_item'),
    path('dec-item/<int:id>/', dec_item, name='dec_item'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)