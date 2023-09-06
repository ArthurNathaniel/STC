from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from cms_app.views import login_view


urlpatterns = [
    path('', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('stats', views.stats, name='stats'),
    path('add_member', views.add_member, name='add_member'),
    path('view_member', views.view_member, name='view_member'),
    path('add_payment', views.add_payment, name='add_payment'),
    path('view_payment', views.view_payment, name='view_payment'),
    path('edit_payment/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('delete_payment/<int:payment_id>/',views.delete_payment, name='delete_payment'),
    path('payment_list/', views.payment_list, name='payment_list'),
    path('document', views.document, name='document'),
 
    # path('view_document/<int:document_id>/',
    #      views.view_document, name='view_document'),
         

    path('view_document', views.view_document, name='view_document'),

    # path('document/<int:document_id>/',views.view_document, name='view_document'),

]
