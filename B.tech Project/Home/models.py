from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
# Information About Users..................

class user(models.Model):
	user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)

class chat(models.Model):
    Username=models.CharField(max_length=100)
    Messege=models.CharField(max_length=200)
    Time=models.DateTimeField(default=timezone.now)
    deleted_chats = models.ForeignKey(user,related_name="deleted_chat",null=True,blank=True,on_delete = models.CASCADE)
    def __str__(self):
        return self.Username

class AlumniInfo(models.Model):
    Enrollment_Number=models.IntegerField(unique=True)
    Profile_Image=models.FileField(null=True,blank=True)
    Campus=models.CharField(max_length=80,default='BHU (Varansi)')
    Department=models.CharField(max_length=200,choices=(("Ceramic Engineering","Ceramic Engineering"),("Chemical Engineering and Technology","Chemical Engineering and Technology"),("Civil Engineering","Civil Engineering"),("Computer Science and Engineering","Computer Science and Engineering"),("Electrical Engineering","Electrical Engineering"),("Electronics Engineering","Electronics Engineering"),("Mechanical Engineering","Mechanical Engineering"),("Metallurgical Engineering","Metallurgical Engineering"),("Mining Engineering","Mining Engineering"),("Pharmaceutics","Pharmaceutics"),("Biochemical Engineering","Biochemical Engineering"),("Biomedical Engineering","Biomedical Engineering"),("Materials Science and Technology","Materials Science and Technology"),("Chemistry","Chemistry"),("Mathematical Sciences","Mathematical Sciences"),("Humanistic Studies","Humanistic Studies"),("Physics","Physics"),("Other","Other")),default='Computer Science and Engineering')
    Program=models.CharField(max_length=100,choices=(("M.Pharm.","M.Pharm."),("Ph.D.","Ph.D."),("M.Tech.","M.Tech."),("IDD","IDD"),("B.Tech.","B.Tech."),("B.Pharm.","B.Pharm."),("IMD","IMD"),("Post Doctoral Fellow","Post Doctoral Fellow"),("Other","Other")),default='B.Tech.')
    Passout_Year=models.IntegerField(default=2016)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10,choices=(('Male','Male'),('Male','Female')),default='Male')
    Martial_Status=models.CharField(max_length=50,choices=(('UnMarried','UnMarried'),('Married','Married')),default='UnMarried')
    Date_of_Birth=models.DateField()
    Mobile_Number=models.IntegerField(unique=True)
    Email_Id=models.CharField(max_length=150,primary_key=True)
    Current_Status=models.CharField(max_length=15)
    Organization=models.CharField(max_length=150)
    Designation=models.CharField(max_length=100)
    Address_Line1=models.CharField(max_length=150)
    Address_Line2=models.CharField(max_length=150,default='IIT BHU')
    City=models.CharField(max_length=150,default='Varanasi')
    State=models.CharField(max_length=50,default='Uttar Pradesh')
    Country=models.CharField(max_length=50,choices=(('India','India'),('Other','Other')),default='India')
    Pin_Code=models.IntegerField(default=221005)
    def __str__(self):
        return self.First_Name+' '+self.Last_Name

class StaffInfo(models.Model):
    Campus=models.CharField(max_length=80,default='BHU (Varanasi)')
    Year_of_Join=models.IntegerField(default=1999)
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10,choices=(('Male','Male'),('Male','Female')),default='Male')
    Martial_Status=models.CharField(max_length=50,choices=(('UnMarried','UnMarried'),('Married','Married')),default='UnMarried')
    Date_of_Birth=models.DateField()
    Mobile_Number=models.IntegerField(unique=True)
    Email_Id=models.CharField(max_length=150,primary_key=True)
    Current_Status=models.CharField(max_length=15)
    Organization=models.CharField(max_length=150)
    Designation=models.CharField(max_length=100)
    Address_Line1=models.CharField(max_length=150)
    Address_Line2=models.CharField(max_length=150,default='IIT BHU')
    City=models.CharField(max_length=150,default='Varanasi')
    State=models.CharField(max_length=50,default='Uttar Pradesh')
    Country=models.CharField(max_length=50,choices=(('India','India'),('Other','Other')),default='India')
    Pin_Code=models.IntegerField(default=221005)
    def __str__(self):
        return self.First_Name+' '+self.Last_Name
    
class StudentInfo(models.Model):
    Enrollment_Number=models.IntegerField(unique=True)
    Campus=models.CharField(max_length=80,default='BHU (Varanasi)')
    Department=models.CharField(max_length=200,choices=(("Ceramic Engineering","Ceramic Engineering"),("Chemical Engineering and Technology","Chemical Engineering and Technology"),("Civil Engineering","Civil Engineering"),("Computer Science and Engineering","Computer Science and Engineering"),("Electrical Engineering","Electrical Engineering"),("Electronics Engineering","Electronics Engineering"),("Mechanical Engineering","Mechanical Engineering"),("Metallurgical Engineering","Metallurgical Engineering"),("Mining Engineering","Mining Engineering"),("Pharmaceutics","Pharmaceutics"),("Biochemical Engineering","Biochemical Engineering"),("Biomedical Engineering","Biomedical Engineering"),("Materials Science and Technology","Materials Science and Technology"),("Chemistry","Chemistry"),("Mathematical Sciences","Mathematical Sciences"),("Humanistic Studies","Humanistic Studies"),("Physics","Physics"),("Other","Other")),default='Computer Science and Engineering')
    Program=models.CharField(max_length=100,choices=(("M.Pharm.","M.Pharm."),("Ph.D.","Ph.D."),("M.Tech.","M.Tech."),("IDD","IDD"),("B.Tech.","B.Tech."),("B.Pharm.","B.Pharm."),("IMD","IMD"),("Post Doctoral Fellow","Post Doctoral Fellow"),("Other","Other")),default='B.Tech.')
    Year_of_Join=models.IntegerField(default='2015')
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10,choices=(('Male','Male'),('Male','Female')),default='Male')
    Date_of_Birth=models.DateField()
    Mobile_Number=models.IntegerField(unique=True)
    Email_Id=models.CharField(max_length=150,primary_key=True)
    Current_Status=models.CharField(max_length=15)
    Address_Line1=models.CharField(max_length=150)
    Address_Line2=models.CharField(max_length=150,default='IIT BHU')
    City=models.CharField(max_length=150,default='Varanasi')
    State=models.CharField(max_length=50,default='Uttar Pradesh')
    Country=models.CharField(max_length=50,choices=(('India','India'),('Other','Other')),default='India')
    PinCode=models.IntegerField(default=221005)
    def __str__(self):
        return self.First_Name+' '+self.Last_Name

class Gift(models.Model):
    Name=models.CharField(max_length=100,null=True)
    Relation=models.CharField(max_length=100,null=True)
    Designation=models.CharField(max_length=100,null=True)
    Address=models.CharField(max_length=600,null=True)
    Email=models.CharField(max_length=100,null=True)
    Contact=models.CharField(max_length=100,null=True)
    Money=models.CharField(max_length=100,null=True)
        