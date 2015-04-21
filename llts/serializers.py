from rest_framework import serializers
from llts.models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	organizations = serializers.PrimaryKeyRelatedField(many=True, queryset=Organization.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'organizations')

class FullUserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'organizations')

class RegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

class HouseholdSerializer(serializers.ModelSerializer):

	class Meta:
		model = Household
		fields = ('id', 'organization', 'name', 'address', 'notes', 'created')

class DistrictSerializer(serializers.ModelSerializer):

	class Meta:
		model = District
		fields = ('id','organization', 'leader', 'name', 'created')

class OrganizationSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	households = HouseholdSerializer(many=True, required=False, read_only=True)
	districts = DistrictSerializer(many=True, required=False, read_only=True)

	class Meta:
		model = Organization
		fields = ('id','owner','name','created','households', 'districts')

class MemberSerializer(serializers.ModelSerializer):
	moved = serializers.ReadOnlyField(source="household.moved")

	class Meta:
		model = Member
		fields = ('id', 'household', 'moved', 'first_name', 'last_name', 'birthday', 'phone', 'email', 'is_home_teacher', 'created')

class CompanionSerializer(serializers.ModelSerializer):
	member = MemberSerializer()

	class Meta:
		model = Companion
		fields = ('id', 'member', 'created')

class AssignmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Assignment
		fields = ('companionship', 'household', 'created')

class CompanionshipSerializer(serializers.ModelSerializer):
	companions = CompanionSerializer(many=True)
	assignments = AssignmentSerializer(many=True)

	class Meta:
		model = Companionship
		fields = ('companions', 'assignments', 'district', 'created')

class VisitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Visit
		fields = ('household', 'date', 'notes')