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


urlpatterns = router.urls