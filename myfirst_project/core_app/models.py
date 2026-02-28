from django.db import models

class Category(models.Model):
    name = models.CharField("Санат атауы", max_length=100)
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Тақырыбы", max_length=200)
    content = models.TextField("Мәтіні")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField("Сурет", upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Ad(models.Model):
    title = models.CharField("Жарнама атауы", max_length=100)
    image = models.ImageField("Жарнама суреті", upload_to='ads/')
    link = models.URLField("Сілтеме", blank=True)

    def __str__(self):
        return self.title