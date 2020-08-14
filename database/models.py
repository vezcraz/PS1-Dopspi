from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# class Chapter_Data(models.Model):
#     Year_Published = models.CharField(max_length=100)
#     Chapter_Number = models.CharField(max_length=100)
#     Table_Number = models.CharField(max_length=100)
#     Table_Content = models.CharField(max_length=100)
#     Excel_File = models.FileField()
#     Pdf_File = models.FileField()

#     def __str__(self):
#         return 'Year : {0} Chapter : {1} Table Number : {2}'.format(self.Year_Published, self.Chapter_Number, self.Table_Number)

# class Section_Data(models.Model):
#     Year_Published = models.CharField(max_length=100)
#     Section_Number = models.CharField(max_length=100)
#     Chapter_Number = models.CharField(max_length=100)
#     Content = models.TextField()
#     SubChapter(Yes_No) =  


#     def __str__(self):
#         return '  {0}  {1}'.format(self.Year_Published, self.Content)

# class Index_Data(models.Model):
#     Year_Published = models.CharField(max_length=100)
#     Section_Number = models.CharField(max_length=100)
#     Content = models.TextField()
#     Icon = models.FileField()


#     def __str__(self):
#         return '  {0}  {1}'.format(self.Year_Published, self.Content)


# class Ext_Link(models.Model):
#     Year_Published = models.CharField(max_length=100)
#     Name = models.CharField(max_length=100)
#     Icon = models.FileField()
#     Link = models.URLField()

#     def __str__(self):
#         return '{0} {1}'.format(self.Year_Published, self.Name)


# class Year_Data(models.Model):
#     Year_Published = models.CharField(max_length=100)
#     Cover_Page = models.FileField()
#     def __str__(self):
#         return 'Year : {0} '.format(self.Year_Published)


# class Navbar(models.Model):
#     Year_Published = models.CharField(max_length=4)
#     Name = models.CharField(max_length=10)
#     Link = models.FileField()

#     def __str__(self):
#         return '{0} {1} '.format(self.Year_Published,self.Name)

		





    