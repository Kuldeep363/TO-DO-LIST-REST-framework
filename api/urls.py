from django.urls import path
from . import views as apiView
# from rest_framework.urlpatterns import format_suffix_patterns # urls used for default class based views

urlpatterns = [
    path('',apiView.apiUrls,name='apiHome'),
    path('task-list',apiView.taskList,name='taskList'),
    # path('task-detail/<slug:slug>',apiView.taskDetail,name='taskDetail'),
    path('task-create',apiView.taskCreate,name='taskCreate'),
    path('task-update/<slug:slug>',apiView.taskUpdate,name='taskUpdate'),
    path('task-delete/<slug:slug>',apiView.taskDelete,name='taskDelete')
]


'''
    urls used for default class based views
'''

# urlpatterns = [
#     path('',apiView.taskList,name='apiHome'),
#     path('/<int:id>',apiView.taskDetail,name='detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns) 

'''
    used for mixins based and generic  class views
'''

# urlpatterns = [
#     path('',apiView.taskList,name='apiHome'),
#     path('/<int:pk>',apiView.taskDetail,name='detail'),
# ]