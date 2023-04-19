from django.db import models

# Create your models here.

class Fcuser(models.Model):
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀 번호')
    register_data = models.DateTimeField(auto_now=True, verbose_name='등록 일자')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fast_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'