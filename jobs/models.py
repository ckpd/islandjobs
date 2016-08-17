from django.db import models

class Company(models.Model):
    companyname = models.CharField(max_length=200)
    logo = models.FileField()
    ratings = models.IntegerField(default=0)
    
    def __str__(self):              # __unicode__ on Python 2
        return self.companyname
    
class Jobpost(models.Model):
    job = models.ForeignKey(Company, on_delete=models.CASCADE)
    jobTitle = models.CharField(max_length=200)
    jobCity = models.CharField(max_length=200)
    FullTime = 'FullTime'
    PartTime = 'PartTime'
    Contract = 'Contract'
    Freelance = 'Free Lance'
    jobType_choices = (
        (FullTime, 'full time'),
        (PartTime, 'part time'),
        (Contract, 'contract'),
        (Freelance, 'freelance'),
    )
    jobType = models.CharField(max_length=200, choices = jobType_choices )
    pubDate = models.DateField('date published')
    jobDetails = models.TextField(max_length=10000, default= '')
    
    
    class Meta:
        ordering = ["-pubDate"]
        
    def __str__(self):              # __unicode__ on Python 2
        return self.jobTitle