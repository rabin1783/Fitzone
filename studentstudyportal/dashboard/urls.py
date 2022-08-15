from django.urls import path
from . import views

urlpatterns = [
    path('',views.front,name='front'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    
    path('notes/',views.notes,name='notes'), 
    path('delete_note/<int:pk>',views.delete_note,name='delete-note'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(),name='notes_detail'), 
    
    path('youtube/',views.youtube,name='youtube'),
    path('books/',views.books,name='books'),
    path('step/',views.step,name='step'),
    path('wiki/',views.wiki,name='wiki'),
    path('conversion/',views.Conversion,name='conversion'),
    path('admin_login/', views.admin_login, name="admin.login"),
    path('admin_register/', views.admin_register, name="admin.register"),
    path('login/', views.user_login, name="user.login"),
    path('create/',views.user_register,name="user.create"),
    path('logout/', views.logout, name="user.logout"),
    path('homework/',views.homework,name='homework'),
    path('update_homework/<int:pk>',views.update_homework,name='update_homework'),
    path('delete_homework/<int:pk>',views.delete_homework,name='delete_homework'),





    
    path('upload/', views.upload, name='upload'),
    path('steps/', views.step_list, name='step_list'),
    path('steps/upload/', views.upload_step, name='upload_step'),
    path('steps/<int:pk>/', views.delete_step, name='delete_step'),

    path('class/steps/', views.StepListView.as_view(), name='class_step_list'),
    path('class/steps/upload/', views.UploadStepView.as_view(), name='class_upload_step'),

    
    
]  