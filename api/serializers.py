# api/serializers.py
from rest_framework import serializers
from .models import User, UserRole, Year, Program, Module, Student, Lecturer, StudentAttendance, LecturerAttendance
from django.db import transaction
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
#         extra_kwargs = {'password': {'write_only': True}}
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_password_changed']
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# api/serializers.py
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password', 'is_password_changed', 'role']
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_password_changed', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = '__all__'

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'
#
# class LecturerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Lecturer
#         fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    program = serializers.PrimaryKeyRelatedField(queryset=Program.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'program', 'first_name', 'last_name', 'email']

    @transaction.atomic
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('email')

        username = f"{first_name.lower()}.{last_name.lower()}"
        user = User.objects.create_user(
            username=username,
            email=email,
            password='12345',
            first_name=first_name,
            last_name=last_name,
            role='student'
        )

        student = Student.objects.create(user=user, **validated_data)
        return student

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['first_name'] = instance.user.first_name
        representation['last_name'] = instance.user.last_name
        representation['email'] = instance.user.email
        return representation


# class LecturerSerializer(serializers.ModelSerializer):
#     first_name = serializers.CharField(write_only=True)
#     last_name = serializers.CharField(write_only=True)
#     email = serializers.EmailField(write_only=True)
#     modules = serializers.PrimaryKeyRelatedField(many=True, queryset=Module.objects.all(), required=False)
#
#     class Meta:
#         model = Lecturer
#         fields = ['id', 'staff_id', 'first_name', 'last_name', 'email', 'modules']
#
#     @transaction.atomic
#     def create(self, validated_data):
#         first_name = validated_data.pop('first_name')
#         last_name = validated_data.pop('last_name')
#         email = validated_data.pop('email')
#         modules = validated_data.pop('modules', [])
#
#         username = f"{first_name.lower()}.{last_name.lower()}"
#         user = User.objects.create_user(
#             username=username,
#             email=email,
#             password='12345',
#             first_name=first_name,
#             last_name=last_name,
#             role='lecturer'
#         )
#
#         lecturer = Lecturer.objects.create(user=user, **validated_data)
#         lecturer.modules.set(modules)
#         return lecturer
#
#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['first_name'] = instance.user.first_name
#         representation['last_name'] = instance.user.last_name
#         representation['email'] = instance.user.email
#         representation['modules'] = [module.id for module in instance.modules.all()]
#         return representation

class LecturerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    modules = serializers.PrimaryKeyRelatedField(many=True, queryset=Module.objects.all(), required=False)

    class Meta:
        model = Lecturer
        fields = ['id', 'staff_id', 'first_name', 'last_name', 'email', 'modules']

    @transaction.atomic
    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        email = validated_data.pop('email')
        modules = validated_data.pop('modules', [])

        username = f"{first_name.lower()}.{last_name.lower()}"
        user = User.objects.create_user(
            username=username,
            email=email,
            password='12345',  # You might want to generate a random password here
            first_name=first_name,
            last_name=last_name,
            role='lecturer'
        )

        lecturer = Lecturer.objects.create(user=user, **validated_data)
        lecturer.modules.set(modules)
        return lecturer

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['first_name'] = instance.user.first_name
        representation['last_name'] = instance.user.last_name
        representation['email'] = instance.user.email
        representation['modules'] = [module.id for module in instance.modules.all()]
        return representation
class StudentAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAttendance
        fields = '__all__'

class LecturerAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LecturerAttendance
        fields = '__all__'
