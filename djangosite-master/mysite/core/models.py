from django.db import models
from django import forms
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField




MY_CHOICES = (('java', 'java'),
              ('c++', 'c++'),
              ('python', 'python'),
              ('c#', 'c#'),
              ('php', 'php'),
              )
INTERPERSONAL_SKILLS = (('active listening','active listening'),('teamwork','teamwork'),('Responsibility','Responsibility'),
('Dependability','Dependability'),('Leadership','Leadership'),('Motivation','Motivation'),
('Flexibility','Flexibility'),('Patience','Patience'),('Empathy','Empathy'),
)

INTRAPERSONAL_SKILLS = (('self-esteem','self-esteem'),('discipline','discipline'),('brainstorming','brainstorming'),('writing','writing'),('communication','communication'),('team building','team building'))

              
 #gen_choice =(('male','male'),( 'female','female'),( 'other','other'))
    #mar_choice =(('single','single'),( 'married','married'),( 'widow','widow'),( 'divorced','divorced'))





class register(models.Model):
    name  = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

# takes the picture which user will submit in 

class profile(models.Model):
    profilepic= models.ImageField(upload_to='books/covers/', null=False, blank=False)


#takes contact information

class info(models.Model):
    Email_address = models.CharField(max_length=200)
    Phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    facebook= models.URLField(max_length=200 , null=False, blank=False, default='')
    linkedin= models.URLField(max_length=200, null=False, blank=False, default='')

    
#takes basic information

class Intro(models.Model):
    Applicants_name  = models.CharField(max_length=100)
    CNIC= models.CharField(max_length=15)
    Father_name  = models.CharField(max_length=100)
    Mother_name  = models.CharField(max_length=100)
    Gender = forms.ChoiceField(widget=forms.RadioSelect)
    Marital_status = forms.ChoiceField(widget=forms.RadioSelect)
    Domicile = forms.ChoiceField(widget=forms.RadioSelect)
    #Gender = models.CharField(max_length=30)
    #Marital_status =  models.CharField(max_length=30)
    #Domicile = models.CharField(max_length=50)
    Address = models.CharField(max_length=1000)
    Employment = models.CharField(max_length=50 , default='')
    Nationality = models.CharField(max_length=30)
    Religion =  models.CharField(max_length=30)
    Country =  models.CharField(max_length=30)
    City =  models.CharField(max_length=30)

#Takes basic documents

class mydoc(models.Model):
    name  = models.CharField(max_length=100, default="")
    cv = models.FileField(upload_to='books/pdfs/')
    picture= models.ImageField(upload_to='books/covers/', null=True, blank=True)
    certificate= models.FileField(upload_to='books/pdfs/')
    degree= models.ImageField(upload_to='books/covers/', null=True, blank=True)
    

    def __str__(self):
        return self.name

#takes skills record

class skills(models.Model):
    
    Interpersonal_skills = MultiSelectField(choices=INTERPERSONAL_SKILLS, default='')
    Intrapersonal_skills = MultiSelectField(choices=INTRAPERSONAL_SKILLS,default='')
    Hands_on_programming_languages  = MultiSelectField(choices=MY_CHOICES, default="")
    Additional_skills = models.CharField(max_length=50, default="")
    
    
#comment section

class Comment(models.Model):
    post = models.ForeignKey('skills' ,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Aboutyou(models.Model):
    start = models.CharField(max_length=1000, default='', null=False)