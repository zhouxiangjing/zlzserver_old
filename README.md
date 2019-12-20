# zlzserver
个人网站

常用命令
    
    // 依赖文件生成与安装
    pip freeze > requirements.txt
    pip install -r requirement.txt      // 安装
    pip install -Ur requirements.txt    // 安装
    // 项目管理
    python django-admin.py startproject zlzserver // 初始化项目
    python manage.py startapp blog      // 创建APP
    python manage.py runserver          // 开始运行项目
    python manage.py collectstatic      // 收集静态文件
    python manage.py createsuperuser    // 创建超级管理员
    
    //数据库管理
    python manage.py makemigrations     // 迁移数据库
    python manage.py migrate            // 执行迁移
    
    python manage.py showmigrations     // 显示迁移历史
    python manage.py migrate --fake-initial // 重新初始化数据库
    
    或者
    python manage.py inspectdb

    
项目生命周期

    Django生命周期:
    前端发送请求-->Django的wsgi-->中间件-->路由系统-->视图-->ORM数据库操作-->模板-->返回数据给用户
    
    django rest framework生命周期：
    发送请求-->Django的wsgi-->中间件-->路由系统_执行CBV的as_view()，就是执行内部的dispath方法-->在执行dispath之前，
    有版本分析 和 渲染器-->在dispath内，对request封装-->版本-->认证-->权限-->限流-->视图-->如果视图用到缓存
    ( request.data or   request.query_params )就用到了 解析器-->视图处理数据，用到了序列化(对数据进行序列化或验证) -->
    视图返回数据可以用到分页
