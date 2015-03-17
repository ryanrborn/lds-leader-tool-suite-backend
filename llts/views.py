from llts.models import Organization, Household, Member, District, Companionship, Assignment, Visit
from llts.serializers import UserSerializer, RegistrationSerializer, OrganizationSerializer, HouseholdSerializer, MemberSerializer, DistrictSerializer, CompanionshipSerializer, AssignmentSerializer, VisitSerializer
from llts import permissions as localpermissions
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, views, status, mixins
from rest_framework.response import Response


class UserList(generics.ListCreateAPIView):
	serializer_class = UserSerializer

	def get_queryset(self):
		if self.request.user.is_staff:
			return User.objects.all()
		else:
			return User.objects.filter(id=self.request.user.id)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAdminUser,)

class OrganizationList(generics.ListCreateAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user, households=[]);

	def get_queryset(self):
		"""
		This view should return a list of the organizations
		tied to the user. Admins see all
		"""
		if self.request.user.is_staff:
			return super(OrganizationList, self).get_queryset()
		else:
			return super(OrganizationList, self).get_queryset().filter(owner=self.request.user)

class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer
	permission_classes = (localpermissions.OrganizationOwner,)

class HouseholdList(generics.ListCreateAPIView):
	queryset = Household.objects.all()
	serializer_class = HouseholdSerializer

	def get_queryset(self):
		if self.request.user.is_staff:
			return super(HouseholdList, self).get_queryset()
		return super(HouseholdList, self).get_queryset().filter(organization__owner=self.request.user)

class HouseholdDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Household.objects.all()
	serializer_class = HouseholdSerializer
	permission_classes = (localpermissions.HouseholdOwner,)

class MemberList(generics.ListCreateAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer

	def get_queryset(self):
		if self.request.user.is_staff:
			return super(MemberList, self).get_queryset()
		return super(MemberList, self).get_queryset().filter(household__organization__owner=self.request.user)

class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Member.objects.all()
	serializer_class = MemberSerializer
	permission_classes = (localpermissions.MemberOwner,)

class DistrictList(generics.ListCreateAPIView):
	queryset = District.objects.all()
	serializer_class = DistrictSerializer

class DistrictDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = District.objects.all()
	serializer_class = DistrictSerializer

class CompanionshipList(generics.ListCreateAPIView):
	queryset = Companionship.objects.all()
	serializer_class = CompanionshipSerializer

class CompanionshipDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Companionship.objects.all()
	serializer_class = CompanionshipSerializer

class AssignmentList(generics.ListCreateAPIView):
	queryset = Assignment.objects.all()
	serializer_class = AssignmentSerializer

class AssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Assignment.objects.all()
	serializer_class = AssignmentSerializer

class VisitList(generics.ListCreateAPIView):
	queryset = Visit.objects.all()
	serializer_class = VisitSerializer

class VisitDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Visit.objects.all()
	serializer_class = VisitSerializer


class Register(views.APIView):
	"""
	Only allow registrations
	"""
	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):
		VALID_USER_FIELDS = [f.name for f in get_user_model()._meta.fields]
		DEFAULTS = {
			# you can define any defaults that you would like for the user, here
		}
		serialized = RegistrationSerializer(data=request.DATA)
		if serialized.is_valid():
			user_data = {field: data for (field, data) in request.DATA.items() if field in VALID_USER_FIELDS}
			user_data.update(DEFAULTS)
			user = get_user_model().objects.create_user(
				**user_data
			)
			return Response(UserSerializer(instance=user).data, status=status.HTTP_201_CREATED)
		else:
			return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
