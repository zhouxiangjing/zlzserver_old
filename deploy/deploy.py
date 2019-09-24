import os
import tarfile
import datetime
import shutil
import subprocess
import configparser
from fabric import Connection, Config

_BASE_FILE = 'zlzserver'
_CONF_FILE = 'conf/conf.ini'
_TAR_FILE = 'dist-zlzserver.tar.gz'

_LOCAL_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

_LOCAL_DIST = _LOCAL_ROOT_DIR + '/deploy/dist/'
_LOCAL_TAR = _LOCAL_DIST + _TAR_FILE

_REMOTE_ROOT_DIR = '/zxj/'
_REMOTE_TMP_DIR = _REMOTE_ROOT_DIR + 'tmp/'
_REMOTE_TMP_TAR = _REMOTE_TMP_DIR + _TAR_FILE

conf = configparser.ConfigParser()
conf.read(_CONF_FILE, encoding="utf-8")
a = conf.get("remote_host","host")

nn = 0

def build():
    if not os.path.exists(_LOCAL_DIST):
        os.makedirs(_LOCAL_DIST)
    if os.path.exists(_LOCAL_TAR):
        os.remove(_LOCAL_TAR)

    cur_path = os.getcwd()
    tar = tarfile.open(_LOCAL_TAR, "w:gz")
    for root, dirs, files in os.walk(_LOCAL_ROOT_DIR):
        os.chdir(root)

        for file in files:
            full_file = os.path.join(root, file)
            tmp_file = os.path.relpath(full_file, start=_LOCAL_ROOT_DIR)
            if not (('.pyc' in tmp_file) or ('.idea' in tmp_file)):
                tar.add(full_file, arcname=tmp_file)

    tar.close()
    os.chdir(cur_path)


def deploy():

    # 重新收集static文件
    static_root = _LOCAL_ROOT_DIR + '/static/'
    if os.path.exists(static_root):
        shutil.rmtree(static_root)
    subproc = subprocess.run("python manage.py collectstatic", shell=True, cwd=_LOCAL_ROOT_DIR, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if not subproc.check_returncode():
        print('shell run succeeded.')
    else:
        print('shell run failed.')
        raise

    conf = configparser.ConfigParser()
    conf.read(_CONF_FILE, encoding="utf-8")
    remote_host = conf.get("remote_host", "host")
    remote_user = conf.get("remote_host", "user")
    remote_password = conf.get("remote_host", "password")

    fabric_config = Config(overrides={'run': {'warn': True}})
    with Connection(host=remote_host, user=remote_user, config=fabric_config, connect_kwargs={'password': remote_password}) as conn:
        with conn.cd(_REMOTE_ROOT_DIR):
            basedir = _BASE_FILE + "_" + datetime.datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
            conn.run('rm -rf tmp')
            conn.run('mkdir tmp')
            tar_tmp = _REMOTE_ROOT_DIR + 'tmp/' + _TAR_FILE;
            # 推送文件
            conn.put(_LOCAL_TAR, tar_tmp)
            # 创建新版本项目目录
            conn.run('mkdir %s' % basedir)
            # 解压文件
            with conn.cd(os.path.join(_REMOTE_ROOT_DIR, basedir)):
                conn.run('tar -xzvf %s' % _REMOTE_TMP_TAR)
            conn.run('rm -rf %s' % _BASE_FILE)
            conn.run('ln -s %s %s' % (basedir, _BASE_FILE))
            # user改为你的linux服务器上的用户名
            conn.run('chown root:root %s' % _BASE_FILE)
            conn.run('chown -R root:root %s' % basedir)

            # 替换nginx配置文件
            print('nginx start.')
            conn.run('sudo cp %s/deploy/nginx/zlzserver /etc/nginx/sites-available/zlzserver' % _BASE_FILE)
            conn.run('sudo rm -f /etc/nginx/sites-enabled/zlzserver')
            conn.run('sudo ln -s /etc/nginx/sites-available/zlzserver /etc/nginx/sites-enabled/zlzserver')
            conn.run('sudo service nginx restart')
            print('nginx end.')

            print('supervisord start.')
            conn.run('sudo cp %s/deploy/supervisord/zlzserver.conf /etc/supervisor/conf.d/zlzserver.conf' % _BASE_FILE)
            conn.run('sudo supervisorctl reload all')
            print('supervisord end.')


if __name__ == '__main__':
    print('start deploy.')
    build()
    deploy()
    # rollback()
    # backup()
    # restore2local()
    print('end deploy.')