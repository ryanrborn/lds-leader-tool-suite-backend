from django.db import models

class Organization(models.Model):
    owner = models.ForeignKey('auth.User',related_name="organizations")
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

class Household(models.Model):
    organization = models.ForeignKey(Organization,related_name="households")
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    moved = models.BooleanField(default=False)

class Member(models.Model):
    household = models.ForeignKey(Household, related_name="members")
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthday = models.DateField(blank=True)
    phone = models.CharField(blank=True, max_length=28)
    email = models.CharField(max_length=128)
    is_home_teacher = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

class District(models.Model):
    organization = models.ForeignKey(Organization, related_name="districts")
    leader = models.ForeignKey(Member, related_name="districts")
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)

class Companionship(models.Model):
    district = models.ForeignKey(District,related_name="companionships")
    created = models.DateTimeField(auto_now_add=True)

class Companion(models.Model):
    member = models.ForeignKey(Member, related_name="companionships")
    companionship = models.ForeignKey(Companionship, related_name="members")
    created = models.DateTimeField(auto_now_add=True)

class Assignment(models.Model):
    companionship = models.ForeignKey(Companionship, related_name="assignments")
    household = models.ForeignKey(Household, related_name="active_assignment")
    created = models.DateTimeField(auto_now_add=True)

class AssignmentHistory(models.Model):
    household = models.ForeignKey(Household, related_name="past_assignments")
    date = models.DateField()

class Visit(models.Model):
    household = models.ForeignKey(Household, related_name="visits")
    visitor1 = models.CharField(max_length=128)
    visitor2 = models.CharField(max_length=128, blank=True)
    date = models.DateField()
    notes = models.TextField(blank=True)


