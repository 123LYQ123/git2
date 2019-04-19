# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
#学院表
class Collage(models.Model):
    collage_id = models.IntegerField("学院id",primary_key=True)
    collage_name = models.CharField("学院名称",max_length=50)

    def __unicode__(self):
        return self.collage_name
    class Meta:
        verbose_name = '学院'
        verbose_name_plural = '学院'
#课程表
class Course(models.Model):
    course_id = models.IntegerField("课程编码",primary_key=True)
    course_name = models.CharField("课程名称",max_length=50)
    period = models.CharField("课程学时",max_length=50)
    cridit = models.CharField("课程学分",max_length=50)#课程学分
    collage = models.ForeignKey(Collage,on_delete=models.DO_NOTHING)
    course_type = models.IntegerField("课程类型")

    def __str__(self):
        return self.course_name
    class Meta:
        verbose_name = '课程'
        verbose_name_plural = '课程'
#职工表
class Teacher(models.Model):
    teacher_id = models.IntegerField("职工号",primary_key=True)
    teacher_name = models.CharField("教师姓名",max_length=50)
    collage = models.ForeignKey(Collage,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.teacher_id

    class Meta:
        verbose_name = '职工'
        verbose_name_plural = '职工'

#专业信息表
class Major(models.Model):
    major_id =models.IntegerField("专业编码",primary_key=True)
    major_name = models.CharField("专业名称",max_length=50)
    collage =models.ForeignKey(Collage,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.major_name

    class Meta:
        verbose_name = '专业'
        verbose_name_plural = '专业'

#年级表
class Grade(models.Model):
    grade_id = models.IntegerField("年级编码",primary_key=True)
    grade =models.CharField("年级",max_length=50)

    def __str__(self):
        return self.grade

    class Meta:
        verbose_name = '年级'
        verbose_name_plural = '年级'
    
#班级表
class Class(models.Model):
    class_id = models.IntegerField("班级id",primary_key=True)
    grade = models.ForeignKey(Grade,on_delete=models.DO_NOTHING)
    major = models.ForeignKey(Major,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.class_id

    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

#开课情况表
class curriculum(models.Model):
    curr_id = models.IntegerField("开课id",primary_key=True)
    course = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    class_id = models.ForeignKey(Class,on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey(Teacher,on_delete=models.DO_NOTHING)
    place = models.CharField("地点",max_length=50)
    time = models.CharField("时间",max_length=50)

    def __str__(self):
        return self.course

    class Meta:
        verbose_name = '已开课程'
        verbose_name_plural = '已开课程'

#资料表
class Material(models.Model):
    mate_id = models.IntegerField("资料id",primary_key=True)
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    mate_name = models.CharField("资料名称",max_length=50)
    end = models.CharField("文件类型",max_length=50)

    def __str__(self):
        return self.mate_name

    class Meta:
        verbose_name = '资料'
        verbose_name_plural = '资料'


 
    
    