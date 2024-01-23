from django.contrib import admin

# Register your models here.
from .models import UserProfile, University, TechnicalSkill, AcademicDegree, Occupation, Activity, CareerGoal, JobDescription, Accomplishment

admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(TechnicalSkill)
admin.site.register(AcademicDegree)
admin.site.register(Occupation)
admin.site.register(Activity)
admin.site.register(CareerGoal)
admin.site.register(JobDescription)
admin.site.register(Accomplishment)
