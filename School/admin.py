from django.contrib import admin
from .models import Teacher, Avarages


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name_teacher',
        'school',
    )


@admin.register(Avarages)
class AvaragesAdmin(admin.ModelAdmin):
    list_display = (
        'created',
        'update',
        'active',
        'name',
        'teacher',
        'matter',
        'behavior',
        'evaluation1_grade',
        'evaluation2_grade',
        'evaluation3_grade',
        'evaluation4_grade',
        'evaluation5_grade',
        'evaluation6_grade',
        'evaluation7_grade',
        'evaluation8_grade',
        'work1_note',
        'work2_note',
        'work3_note',
        'work4_note',
        'work5_note',
        'work6_note',
        'work7_note',
        'work8_note',
        'monthly1_average',
        'monthly2_average',
        'monthly3_average',
        'monthly4_average',
        'monthly5_average',
        'monthly6_average',
        'monthly7_average',
        'monthly8_average',
        'bimonthly1_average',
        'bimonthly2_average',
        'bimonthly3_average',
        'bimonthly4_average',
        'semester1_average',
        'semester2_average',
        'annual_average',
        'status',
    )
