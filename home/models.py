from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    email = models.CharField(max_length=255)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name
    
class SessionYear(models.Model):
    id = models.AutoField(primary_key = True)
    sessionStartYear = models.DateField()
    sessionEndYear = models.DateField()
    objects = models.Manager()
    
class Students(models.Model):
    id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
        
    # class  Meta:
    
    #         permissions = (
    #             ("Student" , "Student"),
    #         )    
    
    def __str__(self):
        return (self.email)
    
class Staff(models.Model):
    id = models.AutoField(primary_key = True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=16)
    address = models.CharField(max_length=255)   
    
    # class  Meta:
    
    #         permissions = (
    #             ("Staff" , "Staff"),
    #         )    
    
    def __str__(self):
        return (self.email)

class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
 
    def __str__(self):
        return (self.course_name)
 
 
class Subjects(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)
     
    # need to give default course
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return (self.subject_name)
    
