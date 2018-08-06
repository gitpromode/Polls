from django.urls import path, include

from rest_framework import routers

from . import viewset

router = routers.DefaultRouter()
router.register(r'Question', viewset.QuestionViewSet, base_name='questions')
router.register(r'Choice', viewset.ChoiceViewSet, base_name='choices')

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	]