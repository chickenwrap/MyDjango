from typing import Type

from django.db import models

# Create your models here.
from django.utils.html import format_html
from pymysql import NULL


class Type(models.Model):
    id = models.AutoField('序号', primary_key=True)
    type_name = models.CharField('产品类型', max_length=20)

    def __str__(self):
        return self.type_name

class Product(models.Model):
    id = models.AutoField('序号', primary_key=True)
    name = models.CharField('名称', max_length=50)
    weight = models.CharField('重量', max_length=20)
    size = models.CharField('尺寸', max_length=20)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='产品类型')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '产品信息'
        verbose_name_plural = '产品信息'
        permissions = (
            ('visit_Product', 'Can visit Product'),
        )

    def colored_type(self):
        if '手机' in self.type.type_name:
            color_code = 'red'
        elif '平板电脑' in self.type.type_name:
            color_code = 'blue'
        elif '智能穿戴' in self.type.type_name:
            color_code = 'green'
        else:
            color_code = 'yellow'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.type,
        )

    colored_type.short_description = '带颜色的产品类型'

