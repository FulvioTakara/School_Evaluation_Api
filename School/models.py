from optparse import check_choice
from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Teacher(Base):
    name_teacher = models.CharField(max_length=300)
    school = models.CharField(max_length=300)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'

    def __str__(self) -> str:
        return self.name_teacher


class Studants(Base):
    name = models.CharField
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    matter = models.CharField(max_length=200)
    behavior = models.TextField()
    evaluation1_grade = models.FloatField()
    evaluation2_grade = models.FloatField()
    evaluation3_grade = models.FloatField()
    evaluation4_grade = models.FloatField()
    evaluation5_grade = models.FloatField()
    evaluation6_grade = models.FloatField()
    evaluation7_grade = models.FloatField()
    evaluation8_grade = models.FloatField()
    work1_note = models.FloatField()
    work2_note = models.FloatField()
    work3_note = models.FloatField()
    work4_note = models.FloatField()
    work5_note = models.FloatField()
    work6_note = models.FloatField()
    work7_note = models.FloatField()
    work8_note = models.FloatField()

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self) -> str:
        return self.name


class Avarages(Studants):
    monthly1_average = models.FloatField()
    monthly2_average = models.FloatField()
    monthly3_average = models.FloatField()
    monthly4_average = models.FloatField()
    monthly5_average = models.FloatField()
    monthly6_average = models.FloatField()
    monthly7_average = models.FloatField()
    monthly8_average = models.FloatField()
    bimonthly1_average = models.FloatField()
    bimonthly2_average = models.FloatField()
    bimonthly3_average = models.FloatField()
    bimonthly4_average = models.FloatField()
    semester1_average = models.FloatField()
    semester2_average = models.FloatField()
    annual_average = models.FloatField()
    status = models.CharField(default='A', check_choice=('C', 'Calculando, ainda não acabou o ano letivo'), null=True, blank=True, choices=(
        ('A', 'Aprovado'),
        ('C', 'Calculando, ainda não acabou o ano letivo'),
        ('O', 'Observação em recuperação'),
        ('R', 'Reprovado'),
    ))

    def monthly1_average(self) -> float:
        average_monthly1 = (self.evaluation1_grade + self.work1_note) / 2
        return average_monthly1

    def monthly2_average(self) -> float:
        average_monthly1 = (self.evaluation2_grade + self.work2_note) / 2
        return average_monthly1

    def monthly3_average(self) -> float:
        average_monthly1 = (self.evaluation3_grade + self.work3_note) / 2
        return average_monthly1

    def monthly4_average(self) -> float:
        average_monthly1 = (self.evaluation4_grade + self.work4_note) / 2
        return average_monthly1

    def monthly5_average(self) -> float:
        average_monthly1 = (self.evaluation5_grade + self.work5_note) / 2
        return average_monthly1

    def monthly6_average(self) -> float:
        average_monthly1 = (self.evaluation6_grade + self.work6_note) / 2
        return average_monthly1

    def monthly7_average(self) -> float:
        average_monthly1 = (self.evaluation7_grade + self.work7_note) / 2
        return average_monthly1

    def monthly8_average(self) -> float:
        average_monthly1 = (self.evaluation8_grade + self.work8_note) / 2
        return average_monthly1

    def bimonthly1_average(self) -> float:
        average_bimonthly1 = (self. monthly1_average +
                              self.monthly2_average) / 2
        return average_bimonthly1

    def bimonthly2_average(self) -> float:
        average_bimonthly2 = (self. monthly3_average +
                              self.monthly4_average) / 2
        return average_bimonthly2

    def bimonthly3_average(self) -> float:
        average_bimonthly3 = (self. monthly5_average +
                              self.monthly6_average) / 2
        return average_bimonthly3

    def bimonthly4_average(self) -> float:
        average_bimonthly4 = (self. monthly7_average +
                              self.monthly8_average) / 2
        return average_bimonthly4

    def semester1_average(self) -> float:
        average_semester1 = (self.bimonthly1_average +
                             self.bimonthly2_average) / 2
        return average_semester1

    def semester2_average(self) -> float:
        average_semester2 = (self.bimonthly3_average +
                             self.bimonthly4_average) / 2
        return average_semester2

    def annual_average(self) -> float:
        average_annual = (self.semester1_average + self.semester2_average) / 2
        return average_annual

    class Meta:
        verbose_name = 'avarage'
        verbose_name_plural = 'avarages'

    def __str__(self) -> str:
        return self.status
