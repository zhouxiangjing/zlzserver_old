
sudo apt-get install supervisor

默认配置文件路径 /etc/supervisor/supervisord.conf

更新配置

1. 替换/etc/supervisor/conf.d 文件夹下面的配置文件zlzserver.conf
2. 重启所有应用
sudo supervisorctl start all
sudo supervisorctl stop all