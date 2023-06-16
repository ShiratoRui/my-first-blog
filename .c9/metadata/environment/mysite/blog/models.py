{"filter":false,"title":"models.py","tooltip":"/mysite/blog/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.db import models","","# Create your models here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":17,"column":25},"action":"insert","lines":["from django.conf import settings","from django.db import models","from django.utils import timezone","","","class Post(models.Model):","    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)","    title = models.CharField(max_length=200)","    text = models.TextField()","    created_date = models.DateTimeField(default=timezone.now)","    published_date = models.DateTimeField(blank=True, null=True)","","    def publish(self):","        self.published_date = timezone.now()","        self.save()","","    def __str__(self):","        return self.title"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":6,"column":40},"end":{"row":6,"column":55},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"77e9b0244c0e5a64a2220e02674a6f39e09a7386","timestamp":1686809324004}