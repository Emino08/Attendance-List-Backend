# # api/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import UserViewSet, UserRoleViewSet, YearViewSet, ProgramViewSet, ModuleViewSet, StudentViewSet, LecturerViewSet, StudentAttendanceViewSet, LecturerAttendanceViewSet
#
# router = DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'user-roles', UserRoleViewSet)
# router.register(r'years', YearViewSet)
# router.register(r'programs', ProgramViewSet)
# router.register(r'modules', ModuleViewSet)
# router.register(r'students', StudentViewSet)
# router.register(r'lecturers', LecturerViewSet)
# router.register(r'student-attendance', StudentAttendanceViewSet)
# router.register(r'lecturer-attendance', LecturerAttendanceViewSet)
#
#
# urlpatterns = [
#     path('', include(router.urls)),
# ]

# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, UserRoleViewSet, YearViewSet, ProgramViewSet, ModuleViewSet,
    StudentViewSet, LecturerViewSet, StudentAttendanceViewSet, LecturerAttendanceViewSet,
    LoginView, ChangePasswordView
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-roles', UserRoleViewSet)
router.register(r'years', YearViewSet)
router.register(r'programs', ProgramViewSet)
router.register(r'modules', ModuleViewSet)
router.register(r'students', StudentViewSet)
router.register(r'lecturers', LecturerViewSet)
router.register(r'student-attendance', StudentAttendanceViewSet)
router.register(r'lecturer-attendance', LecturerAttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]