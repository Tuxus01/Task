from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('project', projectViewSet)
router.register('kamban', kambanViewSet)
router.register('comment', CommentViewSet)
router.register('task', TaskViewSet)
router.register('profile', UserProfileViewSet)

#Usuario

router.register('users', UserViewSet)
router.register('groups', GroupViewSet)



##Seccion para agregar informacion###
router.register('commentAdd',CommentAddViewSet )
router.register('files',Comment_FileViewSet )
router.register('members',MembersViewSet )

urlpatterns = router.urls