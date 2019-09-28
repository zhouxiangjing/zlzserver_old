
sudo apt-get install supervisor

默认配置文件路径 /etc/supervisor/supervisord.conf

常用命令:
sudo vim /etc/supervisor/conf.d/zlz.conf
supervisorctl help # 查看帮助
sudo supervisorctl status # 查看程序状态
sudo supervisorctl stop zlz # 关闭 指定的程序
sudo supervisorctl start zlz # 启动 指定的程序
sudo supervisorctl restart zlz # 重启 指定的程序
sudo supervisorctl tail -f zlz # 查看 该程序的日志
sudo supervisorctl update # 重启配置文件修改过的程序（修改配置必须执行的命令，通过这个命令加载新的配置)
sudo supervisorctl start all
sudo supervisorctl stop all
sudo supervisord -c /etc/supervisor/conf.d/zlz.conf # 指定配置文件目录


更新配置:
1. 替换/etc/supervisor/conf.d 文件夹下面的配置文件zlzserver.conf
2. 重启所有应用
sudo supervisorctl start all
sudo supervisorctl stop all