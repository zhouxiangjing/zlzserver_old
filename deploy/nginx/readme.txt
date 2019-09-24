

更新Nginx配置
1.替换/etc/nginx/sites-available/下的配置文件zlzserver
2.进入目录 /etc/nginx/sites-enabled建立软连接：
sudo ln -s /etc/nginx/sites-available/zlzserver .
3.重启Nginx
service nginx restart

root与alias主要区别在于nginx如何解释location后面的uri，这会使两者分别以不同的方式将请求映射到服务器文件上。
root的处理结果是：root路径＋location路径
alias的处理结果是：使用alias路径替换location路径