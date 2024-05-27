from rest_framework.routers import DefaultRouter
from .views import EmpregadoViewSet

router = DefaultRouter()
router.register(r'empregados', EmpregadoViewSet)

urlpatterns = router.urls