# CentOS中通过Nginx和uWSGI部署Flask项目

> 部署Flask项目的新姿势
>
> date: 2017-08-01

---

在之前的很长一段时间里，我部署Flask项目都是使用Flask自带的服务器的。在开发环境中使用Flask自带的服务器还是相当方便的，但是在生产环境中使用这种简陋的服务器似乎并不大好（虽然我也不知道哪里不好）。不管怎么说，为了提高自己的知识水平，我也费了一天的时间稍微学习了一点人生的经验—— *Nginx和uWSGI*

那我们开始吧······

## 系统

我们不建议在Windows系统中搞这些事情，否则你可能会遇见各种奇怪而难以解决的问题，而且这将使你看起来很蠢。我没用过也不会用MacOS。所以我还是在Linux系统上搞事情，你可以在Ubuntu或CentOS这两种Linux发行版上尝试本文所列举的操作。

因为最近在尝试使用CentOS，所以本文主要讲解在CentOS上的操作，在Ubuntu上操作类似但略有不同，不同之处本文会作说明。

> 准确的说是 *CentOS 7.2 64位* 和 *Ubuntu 16.04 64位*

## 环境搭建

本文所诉操作依赖的环境主要包括：

1. Python 2.7
2. pip
3. uWSGI
4. Nginx
5. virtualenv（可选）

所以我们首先安装python。可以通过 `python --version` 命令查看是否安装python及python版本，如果不是python 2.7请先安装或升级至Python 2.7版本。具体操作见[Python-Official Site](https://www.python.org/)

然后安装Python的包管理器pip，当然，其他包管理器原则上也可以，但是我还是推荐使用pip。通过 `pip --version` 查看是否安装及版本。具体安装或更新操作见[PyPI-get pip](https://pip.pypa.io/en/latest/installing/)

### 安装uWSGI

首先你可能需要安装一些乱七八糟的依赖

```
yum groupinstall "Development Tools"
yum install zlib zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel
```

for Python/WSGI support

```
yum install python-devel
```

然后安装uWSGI

```
pip install uwsgi
```

通过 `uwsgi --version` 检验是否安装成功。

\*Ubuntu下是

```
apt-get install python-dev
apt-get install python3-dev
pip install uwsgi
```

### 安装Nginx

据说Nginx不在yum安装源软件里，所以添加上

```
rpm -ivh http://nginx.org/packages/centos/6/noarch/RPMS/nginx-release-centos-6-0.el6.ngx.noarch.rpm
yum install nginx
```

然后通过 `nginx -v` 检验是否安装成功。

\*Ubuntu直接使用apt即可

```
apt-get install nginx
```

## Flask项目

> 如果你成功完成了上面的步骤，那你终于可以开始一些有意义的工作了，比如写个"Hello World!"

首先我们需要建立一个Flask项目，并为其指定一个项目文件夹，这很简单

**/root/myProject/Hello/manage.py**

```python
#!/usr/bin/python2
# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

@app.route('\')
def hello():
	return 'Hello World!'

if __name__ == "__main__":
    app.run()

```

该项目文件夹为/root/myProject/Hello/，你可以将项目放置在任何你喜欢的地方，但是下文都将按照该地址进行说明。

## 配置uWSGI

uWSGI是一个实现了WSGI协议的Web服务器，我们用它来联系Flask应用与Nginx服务器。

> 了解更多关于uWSGI的信息，可以查看[uWSGI的文档](http://uwsgi-docs.readthedocs.io/en/latest/)（或者[中文文档](http://uwsgi-docs-cn.readthedocs.io/zh_CN/latest/)）

经过前面的操作，你已经安装了uWSGI，下面我们为uWSGI创建一个配置文件以避免输入一堆的参数

**/root/myProject/Hello/uwsgiconfig.ini**

```
[uwsgi]

socket = 127.0.0.1:8001
//启动程序时所监听的地址和端口，通常在本地运行flask项目，
//地址和端口是127.0.0.1:5000,
//不过在服务器上是通过uwsgi设置端口，通过uwsgi来启动项目，
//也就是说启动了uwsgi，也就启动了项目。

chdir = /root/myProject/Hello
//项目目录

wsgi-file = manage.py
//flask程序的启动文件，通常在本地是通过运行python manage.py runserver 来启动项目的

callable = app
//程序内启用的application变量名

stats = 127.0.0.1:9191
//获取uwsgi统计信息的服务地址
```

*以上代码中的所有注释都需删去*

配置文件可以放在任何位置，我放置在项目文件夹内是为了方便使用。配置文件写好后就可以通过 `uwsgi uwsgiconfig.ini` 启动uWSGI及Flask项目

> 当然，如果你此时试图通过浏览器访问上述监听地址是不能成功的，因为 `socket` 表示是通过套接字进程通讯而非http通讯，如果只使用uWSGI而不使用Nginx的话，可以将 `socket=127.0.0.1:5000` 改成 `http=0.0.0.0:80`

实际上uWSGI支持多种配置文件格式，xml、json、ini等。

## 配置Nginx

Nginx是一个高性能的http、反向代理或IMAP/POP3/SMTP服务器。我们拿他来直接接收和处理外网的请求。

> 了解更多关于Nginx的信息，可以访问[Nginx-Official Site](http://nginx.org/)

Nginx的命令参数不多，常用的有一下几种

- 启动： `nginx`
- 停止： `nginx -s stop`
- 查看Nginx是否应用配置文件： `nginx -t`
- 查看版本： `nginx -v`

Nginx主要依靠配置文件配置。我们打开Nginx的默认配置文件，一般是/etc/nginx/nginx.conf。具体文件位置可以通过 `nginx -t` 命令查看。默认配置文件大部分是加注释的，我们修改一部分。

```conf
http {
    server {
        listen       80;
        # 默认的web访问端口
        server_name  0.0.0.0;
        # 你的公网ip

        access_log  /root/myProject/Hello/logs/access.log;
        # 服务器接收的请求日志
        # 需要在项目文件夹下创建
        # logs文件夹，下同。
        error_log  /root/myProject/Hello/logs/error.log;
        # 错误日志

        location / {

            include        uwsgi_params;
            # 这里是导入的uwsgi配置

            uwsgi_pass     127.0.0.1:8001;
            # 需要和uwsgi的配置文件里socket项的地址
            # 相同,否则无法让uwsgi接收到请求。

            uwsgi_param UWSGI_PYHOME /root/myProject/Hello;
            # python的位置(如果有虚拟环境则是虚拟环境下)

            uwsgi_param UWSGI_CHDIR  /root/myProject/Hello;
            # 项目根目录

            uwsgi_param UWSGI_SCRIPT manage:app;     
            # 启动项目的主程序(在本地上运行
            # 这个主程序可以在flask内置的
            # 服务器上访问你的项目)
        }
    }
}
```

> 其实你只需要在/etc/nginx/conf.d中新建一个配置文件将增加的部分填入即可，并不一定要修改默认配置文件。
>
> 记得注释掉默认配置文件中的 `include /etc/nginx/sites-enabled/*;`

*Ubuntu和CentOS中的Nginx的默认配置文件不完全相同，所以重要的是见机行事。

## 启动和停止

1. `nginx` ，启动Nginx
2. `uwsgi uwsgiconfig.ini` ，启动uWSGI

然后你就可以尝试访问你的项目了

如果你需要关闭服务器，只需要关闭Nginx和uWSGI即可。你可以通过 `nginx -s stop` 来关闭Nginx。但如果你要关闭uWSGI则略显麻烦。

### 关闭uWSGI

uWSGI似乎并没有什么命令关闭，如果你不慎使其在后台运行而无法通过 `Ctrl+C` 来终止的话，那么你需要进行下面的操作。

查看uWSGI的PID

```
ps -e
```

根据PID杀掉相应进程

```
kill -9 PID
```
