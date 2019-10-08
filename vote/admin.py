from django.contrib import admin
from .models import Food,Price,Choice
# Register your models here.
admin.site.site_header='Menu  rater'
admin.site.site_title='Let the rating began'
admin.site.index_title='Aao ji khao ji'
class ChoiceInline(admin.TabularInline):
    model= Choice
    extra=3
class QuestionAdmin(admin.ModelAdmin ):
    fieldsets=[(None,{'fields':['Question_txt']}),
    # ('Price',{'fields':['rupees'],'classes':['Collapse']}),
    # ('Price',{'fields':[''],'classes':['Collapse']})
    (None,{'fields':['pub_dates']}),
    ]
    inlines=[ChoiceInline]

admin.site.register(Food,QuestionAdmin)
# admin.site.register(Choice)