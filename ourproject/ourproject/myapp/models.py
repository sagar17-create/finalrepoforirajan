from django.db import models

class Product(models.Model):
    Quality = [
        ('brand_new','brand_new'),
        ('good','good'),
        ('average','average'),
        ('bad','bad')
    ]
    name = models.CharField(max_length= 250)
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='pictures')
    quality = models.CharField(max_length = 250, choices = Quality)
    description = models.TextField()
    
    def __str__(self):
        return self.name+" "+str(self.price)

    class Meta:
        ordering = ['price']

class Brand(models.Model):
    brand_name = models.CharField(max_length = 250)
    brand_logo = models.ImageField()
    brand_description = models.TextField()
    brand_moto = models.SlugField(max_length=50)

    def __str__(self):
        return self.brand_name

    class Meta:
        ordering = ['brand_name']


# class testing(models.Model):
#     firstName = models.CharField(max_length=250)
#     num = models.IntegerField()
#     def __str__(self):
#         return self.firstName

# #One to one
# class Home(models.Model):
#     Home = models.CharField(max_length=250)
#     def __str__(self):
#         return self.Home
# class Family(models.Model):
#     family_name =  models.CharField(max_length=250)
#     home = models.OneToOneField(Home, on_delete=models.SET_NULL, null=True)
#     def __str__(self):
#         return self.family_name

# #one to one
# class Room(models.Model):
#     room = models.IntegerField()
# class Person(models.Model):
#     totalPerson =  models.IntegerField()
#     Room = models.OneToOneField(Room, on_delete=models.CASCADE)

# #one to many
# class Parents(models.Model):
#     parents_cast = models.CharField(max_length=250)
#     def __str__(self):
#         return self.parents_cast
# class Children(models.Model):
#     child_name = models.CharField(max_length=250)
#     belongs_to = models.ForeignKey(Parents,on_delete=models.CASCADE, null=True)
#     def __str__(self):
#         return self.child_name

# #many to many
# class Item(models.Model):         
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
# class Tag(models.Model):
#     tag_name = models.CharField(max_length=200)
#     tag_belongs_to = models.ManyToManyField(Item) # , on_delete=models.SET_NULL, null=True
#     def __str__(self):
#         return self.tag_name