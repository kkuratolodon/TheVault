from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import *

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
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_ajax, name='add_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)