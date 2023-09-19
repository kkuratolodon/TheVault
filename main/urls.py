from django.urls import path

from main.views import (create_item, delete_item, show_html, show_json,
                        show_json_by_id, show_main, show_xml, show_xml_by_id)

app_name = 'main'

urlpatterns = [
    path('create-item', create_item, name='create_item'),
    path('', show_main, name='show_main'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('html/', show_html, name='show_html'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]