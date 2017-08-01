from django.db import models


class PracticeCategory(models.Model):
    p_category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.p_category_name


class PracticeQuestion(models.Model):
    p_category_name = models.ForeignKey(PracticeCategory, on_delete=models.CASCADE)
    p_question_name = models.CharField(null=False, max_length=1000)
    p_question_files = models.FileField()
    p_question_description = models.TextField(max_length=10000)
    p_question_points = models.IntegerField(default=0)
    p_question_flag = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.p_question_name