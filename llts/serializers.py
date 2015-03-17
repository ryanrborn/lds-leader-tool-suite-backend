from rest_framework import serializers
from llts.models import Organization, Household, Member, District, Companionship, Assignment, Visit
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
	organizations = serializers.PrimaryKeyRelatedField(many=True, queryset=Organization.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'organizations')

class RegistrationSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name')

class OrganizationSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')
	households = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

	class Meta:
		model = Organization
		fields = ('id','owner','name','created','households')

class HouseholdSerializer(serializers.ModelSerializer):

	class Meta:
		model = Household
		fields = ('id', 'organization', 'name', 'address', 'notes', 'created')

class MemberSerializer(serializers.ModelSerializer):
	moved = serializers.ReadOnlyField(source="household.moved")

	class Meta:
		model = Member
		fields = ('id', 'household', 'moved', 'first_name', 'last_name', 'birthday', 'phone', 'email', 'is_home_teacher', 'created')

class DistrictSerializer(serializers.ModelSerializer):

	class Meta:
		model = District
		fields = ('id','organization', 'leader', 'name', 'created')

class CompanionshipSerializer(serializers.ModelSerializer):

	class Meta:
		model = Companionship
		fields = ('member1', 'member2', 'district', 'created')

class AssignmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Assignment
		fields = ('companionship', 'household', 'created')

class VisitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Visit
		fields = ('household', 'date', 'notes')