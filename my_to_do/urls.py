
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import (TodoListApis,completed_tasks,
                    delete_task
                    )

router = DefaultRouter()
router.register(r"todolist",TodoListApis)
urlpatterns = [
    path("",include(router.urls)),
    path("completed/", completed_tasks, name="completed-tasks"),
    path("delete-task/<int:task_id>/", delete_task, name="delete-task"),
]