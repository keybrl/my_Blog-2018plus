# Nginx常用配置套路

我们都知道， Nginx 是一个强大的 Web 服务器。只需要简单配置，它就能承载你的 Web 应用。轻易实现诸如负载均衡、反向代理、重定向、HTTPS证书配置、静态资源托管、......这一切只需要填写几个配置文件

我第一次使用 Nginx 是用它部署我的 Python Flask 应用，当时的情景可以看看这篇文章（ [CentOS中通过Nginx和uWSGI部署Flask项目](2017-08-01-Nginx_uWSGI_Flask_in_CentOS.md) ）作为回顾。其实后来我发现 Nginx 太好用了，我经常用它重定向或者搭建静态站点什么的。但是背配置文件实在太痛苦啦，每次都要借助 Google 的帮助，而且还不是特别容易一下子找到我想要的东西。所以我不如把我常用的配置记下来吧，找自己博客总还是比瞎搜快很多的。

## 初始配置

在 Ubuntu 上， Nginx 可以通过 `apt install nginx` 安装。如果是那样，那么默认配置文件是 `/etc/nginx/nginx.conf` 。初始内容是这样的

```conf
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
    worker_connections 768;
    # multi_accept on;
}

http {

    ##
    # Basic Settings
    ##

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    # server_tokens off;

    # server_names_hash_bucket_size 64;
    # server_name_in_redirect off;

    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    ##
    # SSL Settings
    ##

    ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
    ssl_prefer_server_ciphers on;

    ##
    # Logging Settings
    ##

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    ##
    # Gzip Settings
    ##

    gzip on;

    # gzip_vary on;
    # gzip_proxied any;
    # gzip_comp_level 6;
    # gzip_buffers 16 8k;
    # gzip_http_version 1.1;
    # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

    ##
    # Virtual Host Configs
    ##

    include /etc/nginx/conf.d/*.conf;
    include /etc/nginx/sites-enabled/*;
}


#mail {
#    # See sample authentication script at:
#    # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#    # auth_http localhost/auth.php;
#    # pop3_capabilities "TOP" "USER";
#    # imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#    server {
#        listen     localhost:110;
#        protocol   pop3;
#        proxy      on;
#    }
#
#    server {
#        listen     localhost:143;
#        protocol   imap;
#        proxy      on;
#    }
#}

```

一般来说这个文件是不需要修改的，其中有一行是 `include /etc/nginx/conf.d/*.conf;` ，说明，它会自动把 `/etc/nginx/conf.d/` 下面所有 `.conf` 文件引入到 `http {}` 里面，一般我们通过这种方式就可以达到目的。

!!! note "值得注意"
    `http {}` 内有一句 `include /etc/nginx/sites-enabled/*;` 会让你的 Nginx 成功安装、启动后，被访问时，显示 Nginx 的欢迎页面，像下面这样

    ![Nginx 的欢迎页面](//blog-oss.keybrl.com/2018/images/nginx-configure/nginx_welcome_page.png)

    而且无论你设置什么别的配置，80 端口都会被这个页面占用，所以需要先加个井号注释掉这行。

    ![Nginx 配置文件注释掉某行](//blog-oss.keybrl.com/2018/images/nginx-configure/nginx_command.png)

然后剩下的配置可以写在 `/etc/nginx/conf.d/` 里

## 静态文件服务器

最简单最基础的就是配置一个静态文件服务器，它可以托管你的静态站点（比如这个博客），或者为别的什么静态资源提供一个简单的可通过 http 访问的接口。

我们在 `/etc/nginx/conf.d/static_website.conf` 写下如下配置（当然，文件名可以是任意的，只要路径和文件名后缀一样就行）

```conf
server {
    # 服务器监听的端口号
    listen      80;
    # 服务的ip地址或者域名
    # 一般可以为 0.0.0.0 ，表示接受通过任意网卡任意域名的访问
    server_name 0.0.0.0;

    # 可选的日志文件路径，如果不设置则记录到 Nginx 的主日志文件中，其设置见 `/etc/nginx/nginx.conf`
    access_log /home/someone/logs/neinx_static_files.log;
    error_log  /home/someone/logs/nginx_static_files_error.log;

    # 静态文件根目录
    root        /home/someone/static_files/;
    
    # 通过从头部开始能完整匹配 '/' 的 url访问的“路由”
    location / {
        autoindex on;
    }
}
```
