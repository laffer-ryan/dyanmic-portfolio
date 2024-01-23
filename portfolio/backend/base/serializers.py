from rest_framework.serializers import ModelSerializer
from base.models import UserProfile, University, TechnicalSkill, AcademicDegree, Occupation, Activity, CareerGoal, JobDescription, Accomplishment


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
        
class UniversitySerializer(ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
        
class TechnicalSkillSerializer(ModelSerializer):
    class Meta:
        model = TechnicalSkill
        fields = '__all__'
        
class AcademicDegreeSerializer(ModelSerializer):
    class Meta:
        model = AcademicDegree
        fields = '__all__'
        
    def create(self, validated_data):
        university_name = validated_data.pop('university_name')
        university, created = University.objects.get_or_create(name=university_name)
        validated_data['institution'] = university
        return super().create(validated_data)
        
class OccupationSerializer(ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'
        
class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'
        
class CareerGoalSerializer(ModelSerializer):
    class Meta:
        model = CareerGoal
        fields = '__all__'
        
class JobDescriptionSerializer(ModelSerializer):
    class Meta: 
        model = JobDescription
        fields = '__all__'
        
class AccomplishmentSerializer(ModelSerializer):
    class Meta: 
        model = Accomplishment
        fields = '__all__'