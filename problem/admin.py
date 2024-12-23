from django.contrib import admin

from problem.models import Problem, ProblemList, Solution, SolutionComment, StudyPlan, Tag

# Register your models here.
admin.site.register(Problem)
admin.site.register(ProblemList)
admin.site.register(Solution)
admin.site.register(SolutionComment)
admin.site.register(StudyPlan)
admin.site.register(Tag)