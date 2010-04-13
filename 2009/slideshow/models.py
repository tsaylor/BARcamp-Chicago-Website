from django.db import models

TIME_CHOICES = (
    ('9','9 am'),
    ('10','10 am'),
    ('11','11 am'),
    ('12','12 pm'),
    ('13','1 pm'),
    ('14','2 pm'),
    ('15','3 pm'),
    ('16','4 pm'),
    ('17','5 pm'),
    ('18','6 pm'),
    ('19','7 pm'),
    ('20','8 pm'),
    ('21','9 pm'),
    ('22','10 pm'),
    ('23','11 pm'),
    ('24','12 am')
)

class room(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name

#class slide(models.Model):
#    name = models.CharField(max_length=100)
#    template = models.CharField(max_length=100)
#    
#    def __unicode__(self):
#        return self.name 
        
class talk(models.Model):
    name = models.CharField(max_length=100)
    day = models.DateField(auto_now=False, auto_now_add=True)
    time = models.CharField(max_length=2, choices=TIME_CHOICES)
    room = models.ForeignKey(room)
    
    def __unicode__(self):
        return "(%s-%s) %s" % (self.time, self.room, self.name)
        
class message(models.Model):
    content = models.TextField()
    msg_type = models.CharField(max_length=3, choices=(('ann','Announcement'),('spr','Sprint')))
    
    def __unicode__(self):
        return self.content