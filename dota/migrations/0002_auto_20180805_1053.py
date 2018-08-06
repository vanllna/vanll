# Generated by Django 2.0.7 on 2018-08-05 02:53

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('dota', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ad_one', models.ImageField(upload_to='ad/', verbose_name='广告图1')),
                ('Ad_two', models.ImageField(upload_to='ad/', verbose_name='广告图2')),
                ('Ad_there', models.ImageField(upload_to='ad/', verbose_name='广告图3')),
            ],
            options={
                'verbose_name_plural': '关于我们广告图',
            },
        ),
        migrations.CreateModel(
            name='ContactDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AD_one', models.ImageField(upload_to='contactad/', verbose_name='广告图1')),
                ('top_title', models.CharField(max_length=120, verbose_name='顶部标题')),
                ('top_detail', tinymce.models.HTMLField(verbose_name='顶部详情')),
                ('AD_two', models.ImageField(upload_to='contactad/', verbose_name='广告图2')),
                ('mid_title', models.CharField(max_length=120, verbose_name='中部标题')),
                ('mid_info', models.CharField(max_length=120, verbose_name='中部小标')),
                ('mid_detail', tinymce.models.HTMLField(verbose_name='中部详情')),
            ],
            options={
                'verbose_name_plural': '联系我们 ',
            },
        ),
        migrations.CreateModel(
            name='CultuerDetaul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('culture_one', models.ImageField(upload_to='culture/', verbose_name='广告图1')),
                ('top_title', models.CharField(max_length=120, verbose_name='顶部标题')),
                ('top_detail', tinymce.models.HTMLField(verbose_name='顶部详情')),
                ('culture_two', models.ImageField(upload_to='culture/', verbose_name='广告图2')),
                ('mid_title', models.CharField(max_length=120, verbose_name='中部标题')),
                ('mid_detail', tinymce.models.HTMLField(verbose_name='中部详情')),
                ('culture_there', models.ImageField(upload_to='culture/', verbose_name='广告图3')),
                ('button_title', models.CharField(max_length=120, verbose_name='底部标题')),
                ('button_detail', tinymce.models.HTMLField(verbose_name='底部详情')),
            ],
            options={
                'verbose_name_plural': '文化',
            },
        ),
        migrations.AlterModelOptions(
            name='banerimg',
            options={'verbose_name_plural': '广告图片'},
        ),
        migrations.AlterModelOptions(
            name='footinfo',
            options={'verbose_name_plural': '底部二维码'},
        ),
        migrations.AlterModelOptions(
            name='indexmodels',
            options={'verbose_name_plural': '首页内容'},
        ),
        migrations.AlterModelOptions(
            name='newinfo',
            options={'verbose_name_plural': '新闻'},
        ),
        migrations.AlterModelOptions(
            name='teaminfo',
            options={'verbose_name_plural': '团队'},
        ),
        migrations.AlterField(
            model_name='footinfo',
            name='lerfqrcode',
            field=models.ImageField(upload_to='qrcode/', verbose_name='左侧二维码'),
        ),
        migrations.AlterField(
            model_name='footinfo',
            name='rightqrcode',
            field=models.ImageField(upload_to='qrcode/', verbose_name='后侧二维码'),
        ),
    ]
