from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register('project', projectViewSet)
router.register('kamban', kambanViewSet)


urlpatterns = router.urls