# Generated by Django 2.0.7 on 2018-08-04 11:29

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BanerImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerimg', models.ImageField(upload_to='bannerimg/', verbose_name='广告图')),
                ('imgad', models.ImageField(upload_to='bannerimg/', verbose_name='缩略图')),
                ('adtext', models.CharField(max_length=120, verbose_name='banner标题')),
                ('adtextinfo', models.CharField(max_length=120, verbose_name='banner详情')),
            ],
        ),
        migrations.CreateModel(
            name='Footinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lerfqrcode', models.ImageField(upload_to='qrcode/', verbose_name='二维码')),
                ('rightqrcode', models.ImageField(upload_to='qrcode/', verbose_name='二维码')),
            ],
        ),
        migrations.CreateModel(
            name='IndexModels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='media/', verbose_name='logo')),
                ('title', models.CharField(max_length=120, verbose_name='网站标题')),
            ],
            options={
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Newinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newtitle', models.CharField(max_length=120, verbose_name='新闻标题')),
                ('newdetails', tinymce.models.HTMLField(verbose_name='新闻详情')),
                ('addtime', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updatetime', models.DateTimeField(verbose_name='修改时间')),
                ('isdelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TeamInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamimg', models.ImageField(upload_to='teamimg/', verbose_name='团队图片')),
                ('teamdetail', models.CharField(max_length=120, verbose_name='详情介绍')),
            ],
        ),
    ]
