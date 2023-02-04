from django.db import models
from datetime import datetime,date

# Create your models here.
def age(year, month, day):
    today = date.today()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age



class Profile(models.Model):

    name                = models.CharField(max_length=255)
    job_title           = models.CharField(max_length=255)
    summary             = models.CharField(max_length=255)
    father_name         = models.CharField(max_length=255)
    mother_name         = models.CharField(max_length=255)
    date_of_birth       = models.DateField()
    gender              = models.CharField(max_length=255)
    mobile_number       = models.CharField(max_length=12)
    email               = models.EmailField()
    marital_status      = models.CharField(max_length=255)
    nationality         = models.CharField(max_length=255)
    nid_no              = models.CharField(max_length=255)
    religion            = models.CharField(max_length=255)
    permanent_address   = models.TextField()
    present_address     = models.TextField()
    present_salary      = models.IntegerField()
    expected_salary     = models.IntegerField()
    preferred_job       = models.CharField(max_length=255, null=True, blank=True)
    carrieer_obj        = models.TextField()
    current_degree      = models.CharField(max_length=12)
    freelance           = models.BooleanField(default=True)
    image1              = models.ImageField(upload_to='upload/profile')
    image2              = models.ImageField(upload_to='upload/profile', null= True,blank=True)
    image3              = models.ImageField(upload_to='upload/profile', null= True,blank=True)
    video               = models.FileField(upload_to='upload/video', null= True,blank=True)

    def __str__(self):
        return self.name
    

    def main_job_title(self):
        return self.job_title.split(",")[0]

    def age(self):
        dob = str( self.date_of_birth )
        year = int (dob.split("-")[0])
        month = int (dob.split("-")[1])
        day = int (dob.split("-")[-1])
        get_age = age(year, month, day)
        return get_age



class Education(models.Model):

    profile_name        = models.ForeignKey(Profile, on_delete=models.CASCADE)
    exam_name           = models.CharField(max_length=255)
    institute           = models.CharField(max_length=255)
    cgpa                = models.FloatField()
    passing_year        = models.CharField(max_length=255)
    major               = models.CharField(max_length=255)
    duration            = models.CharField(max_length=255)

    def __str__(self):
        return self.exam_name

class Course(models.Model):

    profile_name        = models.ForeignKey(Profile, on_delete=models.CASCADE)
    institute           = models.CharField(max_length=255)
    location            = models.CharField(max_length=255)
    start_date          = models.DateField()
    end_date            = models.DateField()
    certificate         = models.FileField(upload_to="upload/certificate" , null=True,blank=True)


class Experience(models.Model):
    profile_name        = models.ForeignKey(Profile, on_delete=models.CASCADE)
    company_name        = models.CharField(max_length=255)
    company_address     = models.CharField(max_length=255)
    start_date          = models.CharField(max_length=255)
    end_date            = models.CharField(max_length=255, blank=True, null=True)
    duties              = models.TextField(blank=True, null=True)


class Project(models.Model):
    profile_name        = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_title       = models.CharField(max_length=255)
    project_desc        = models.TextField(max_length=255)
    project_cat         = models.TextField(max_length=255)
    project_url         = models.CharField(max_length=255)
    project_image1      = models.ImageField(upload_to='upload/project',)
    project_image2      = models.ImageField(upload_to='upload/project', null= True,blank=True)
    project_image2      = models.ImageField(upload_to='upload/project', null= True,blank=True)

class Service(models.Model):
    profile_name            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    services_title          = models.CharField(max_length=255)
    services_desc           = models.TextField(max_length=255)
    services_image1         = models.ImageField(upload_to='upload/services',blank=True, null=True)

class Testimonial(models.Model):
    profile_name            = models.ForeignKey(Profile, on_delete=models.CASCADE)
    test_by                 = models.CharField(max_length=255)
    test_company            = models.CharField(max_length=255)
    test_desig              = models.CharField(max_length=255)
    testimonial             = models.TextField()
    test_image              = models.ImageField(upload_to='upload/testimonial',blank=True, null=True)


