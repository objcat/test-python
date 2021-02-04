# 1.安装django
```
pip install django
```

# 2.创建项目
```
django-admin startproject my_site
```
```
'django-admin.py was deprecated in Django 3.1 and removed in Django '
'4.0. Please manually remove this script from your virtual environment '
'and use django-admin instead.'
```

# 3.创建模块
```
django-admin startapp app01
```

# 启动
```
python manage.py runserver 0.0.0.0:8000
```


# 渲染html
```
setting设置
'DIRS': [BASE_DIR / 'html']

渲染
def index(request):
    return render(request, 'index.html')
```

