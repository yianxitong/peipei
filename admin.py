from django.contrib import admin

#Registeryourmodelshere.
from.models import Grades,Students

class GradesAdmin(admin.ModelAdmin):
 list_display=['pk','gname','gdate','ggirlnum','gboynum','isDelete']
list_filter=['gname']
search_fields=['gname']
list_per_page=5

#fields=['ggirlnum','gboynum','gname','gdate','isdelete']两种写法第二种分块了
fieldsets=[
("num",{"fields":['ggirlnum','gboynum']}),
("base",{"fields":['gname','gdate','isDelete']}),
]
admin.site.register(Grades,GradesAdmin)
admin.site.register(Students)