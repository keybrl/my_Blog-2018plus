# 使用Python的smtplib和email发送邮件

> 关于如何使用Python发送邮件的一点学习总结
>
> date: 2017-04-09

---

> *smtplib* 和 *email* 是 *Python* 的两个官方库

花了一天时间了解了一下在Python中如何发送电子邮件，了解不深，基本只稍微知道如何使用，在此做个总结以作备忘。

发送电子邮件对于服务器来说是十分重要的，邮箱验证、邮件通知等都涉及到服务器自动发送邮件，除了可以购买各大云服务器厂商的邮件服务，也可以自己写邮件收发的应用，本文首先讲讲邮件的发送。

## smtplib

> smtplib即SMTP的Library

> SMTP( *Simple Mail Transfer Protocol* )
>
> 简单的 基于文本的 用于规范邮件发送的 协议

简单地讲SMTP就是一种对邮件的纯文本格式和传输的规定。它通过指定的端口，加密方式，用指定账号、密码登录的SMTP服务器，收件方地址等传输邮件的纯文本格式。

Python的smtplib主要负责传输部分，使用smtplib发送邮件仅需要短短几行代码。

```python
import smtplib

server = smtplib.SMTP(host, port)  # 创建一个SMTP类
server.starttls()  # 使用STARTTLS对明文进行加密，明文通信时应去掉该行
server.set_debuglevel(False)  # 调试等级，即是否显示发送过程的某些信息
server.login(user, password)  # 登录SMTP服务器
server.sendmail(from_addr, to_addr, msg.as_string())  # 发送邮件
server.quit()  # 关闭SMTP服务器
```

`host`即SMTP服务器的地址，常见的如

* smtp-mail.outlook.com  *Outlook邮箱*
* smtp.qq.com  *QQ邮箱*
* smtp.163.com  *163邮箱*

`port`即SMTP服务器端口，一般情况下，25为明文通信，587为加密通信。部分SMTP服务器，如Outlook邮箱，不支持明文通信。

`user`和`password`即登陆SMTP服务器的用户名和密码，一般情况下，其与你登录该邮箱时的用户名和密码相同，但有些服务器有不同，如QQ邮箱使用QQ号和邮箱授权码登录。

`from_addr`和`to_addr`即发件方和收件方的邮箱地址

`msg`即该邮件的内容，具体见下文

## email

由于SMTP设计之初是基于ASCII的纯文本的，对二进制文件处理得并不好，因此并不适合传输文件。由此产生了MIME扩展。

> MIME(*Multipurpose Internet Mail Extensions*)
>
> MIME使邮件几乎可以包含任何内容

MIME是一套把各种文件编码为ASCII的规范，他使得用邮件传输各种*附件*成为可能。

不过事实上，你并不需要具体知道MIME和SMTP所规定的邮件格式。

在Python中你可以使用email来构建一个邮件，像这样

```python
from email.mime.text import MIMEText

msg = MIMEText(text, subtype, charset)
```

可以看到`msg`即上文中SMTP所发送的那个`msg`

`text`即邮件的文本内容，可为一般文本或HTML文本等

`subtype`即文本的格式，若为一般文本则为`'plain'`，若为HTML文本则为`'html'`

`charset`即文本的文字编码，默认为`'us-ascii'`，如果邮件中含有中文内容，为了保证其对中文字符最大程度的支持，应将其设为`'utf-8'`

当然，如果你直接发送该邮件，你会发现邮件缺少发件人、收件人、主题等信息，这些信息其实是构建在邮件的`header`中的，你可以这样设置

```python
from email.header import Header
from email.utils import formataddr

msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))
msg['To'] = formataddr((Header(to_name.decode(), 'utf-8').encode(), to_addr))
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()
```

`Header()`函数用于构建email的头部，传入该函数的参数应为`unicode`格式的

`formataddr()`可以将发件人名和发件地址组合成类似于`Keyboard <keyboard-l@outlook.com>`的标准格式，传入该函数的参数应为`utf-8`格式

> 对呀，所以上面才要进行一堆麻烦的`decode()`和`encode()`操作

所以们来发几个邮件试试吧

#### 发送文本邮件

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_name = 'dalao'  # 收件人名
to_addr = 'aaaaaa@qq.com'  # 收件地址
subject = '试试发个邮件'  # 邮件主题
text = '这是一份无聊的邮件的正文'  # 邮件正文

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器

msg = MIMEText(text, 'plain', 'utf-8')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['To'] = formataddr((Header(to_name.decode(), 'utf-8').encode(), to_addr))  # 收件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

嫌一个人不够？

#### 群发邮件

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_addr = ['aaaaaa@qq.com', 'bbbbbb@qq.com', 'cccccc@qq.com', 'dddddd@qq.com', 'eeeeee@qq.com']  # 收件地址
subject = '群发邮件'  # 邮件主题
text = '这是一份无聊的邮件的正文'  # 邮件正文

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器

msg = MIMEText(text, 'plain', 'utf-8')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

好像没什么不同

#### 发送HTML邮件

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr

from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_name = 'dalao'  # 收件人名
to_addr = 'aaaaaa@qq.com'  # 收件地址
subject = '一份HTML'  # 邮件主题
# 邮件正文
text = """\
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<style>
		h1{  color: red;  }
		a{  color: blue;  }
		p{  color: purple;  }
		em{  color: grey;  }
		/* 哇，好神奇的配色啊 */
	</style>
</head>

<body>
	<h1>一个超无聊的页面</h1>
	<p>这个页面真的<em>超无聊<em>啊</p>
	<p>还很丑</p>
	<p>From <a href="https://keyboard-l.github.io/Keyboard-L">Keyboard</a></p>
</body>
</html>
"""

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器

msg = MIMEText(text, 'html', 'utf-8')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['To'] = formataddr((Header(to_name.decode(), 'utf-8').encode(), to_addr))  # 收件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

可以看到，跟上一份代码比，这不过是更换了邮件正文内容和`msg`的`subtype`

#### 发送带图片的HTML邮件

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr

from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_name = 'dalao'  # 收件人名
to_addr = 'aaaaaa@qq.com'  # 收件地址
subject = '带图片的HTML'  # 邮件主题
# 邮件正文
text = """\
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<style>
		h1{  color: red;  }
		a{  color: blue;  }
		p{  color: purple;  }
		em{  color: grey;  }
		/* 哇，好神奇的配色啊 */
	</style>
</head>

<body>
	<h1>一个超无聊的页面</h1>
	<img src="cid:image1">
	<p>这个页面真的<em>超无聊<em>啊</p>
	<p>还很丑</p>
	<p>From <a href="https://blog.keybrl.com/">KeybrL's Blog</a></p>
</body>
</html>
"""

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器

msg = MIMEMultipart('related')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['To'] = formataddr((Header(to_name.decode(), 'utf-8').encode(), to_addr))  # 收件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 构造正文
msgText = MIMEText(text, 'html', 'utf-8')
msg.attach(msgText)

# 导入图片
fp = open('G:\\User\\Pictures\\qwe.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

看起来复杂多了？慢慢捋捋吧。

#### 发送带有附件的邮件

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
import os


from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_name = 'dalao'  # 收件人名
to_addr = 'aaaaaa@qq.com'  # 收件地址
subject = '带附件的文本'  # 邮件主题
text = '这是一份无聊的邮件的正文'  # 邮件正文
atta_url = 'G:\\a.png'  # 附件地址

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器


msg = MIMEMultipart('alternative')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['To'] = formataddr((Header(to_name.decode(), 'utf-8').encode(), to_addr))  # 收件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 构造正文
msgText = MIMEText(text, 'plain', 'utf-8')
msg.attach(msgText)

# 构造附件
msgAtta = MIMEText(open(atta_url, 'rb').read(), 'base64', 'utf-8')
msgAtta["Content-Type"] = 'application/octet-stream'
msgAtta["Content-Disposition"] = 'attachment; filename="%s"' % (os.path.basename(atta_url),)
msg.attach(msgAtta)


# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

其实不是很难，不是吗？

#### 来玩一票大的吧

> 发送各种东西

```python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr
import os


from_name = 'Keyboard L'  # 发件人名
from_addr = 'xxxxxx@outlook.com'  # 发件地址
to_addr = ['aaaaaa@qq.com', 'bbbbbb@qq.com', 'cccccc@qq.com', 'dddddd@qq.com', 'eeeeee@qq.com']  # 收件地址
subject = '一票大的'  # 邮件主题
# 邮件正文
text = '这仍是一份无聊的邮件的正文'
html = """\
<html lang="zh">
<head>
	<meta charset="UTF-8">
	<style>
		h1{  color: red;  }
		a{  color: blue;  }
		p{  color: purple;  }
		em{  color: grey;  }
		/* 哇，好神奇的配色啊 */
	</style>
</head>

<body>
	<h1>一个超无聊的页面</h1>
	<img src="cid:image1">
	<p>这个页面真的<em>超无聊<em>啊</p>
	<p>还很丑</p>
	<p>From <a href="https://blog.keybrl.com/">KeybrL's Blog</a></p>
</body>
</html>
"""
atta_url = ['G:\\a.py', 'G:\\User\\Pictures\\asd.png']  # 附件地址

password = '********'  # 邮箱密码
smtp_server = 'smtp-mail.outlook.com'  # 邮件服务器

msg = MIMEMultipart('alternative')  # 创建邮件
msg['From'] = formataddr((Header(from_name.decode(), 'utf-8').encode(), from_addr))  # 发件人
msg['Subject'] = Header(subject.decode('utf-8'), 'utf-8').encode()  # 主题

# 构造正文
msgText = MIMEText(text, 'plain', 'utf-8')
msg.attach(msgText)
msgHTML = MIMEText(html, 'html', 'utf-8')
msg.attach(msgHTML)

# 导入图片
fp = open('G:\\User\\Pictures\\qwe.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
msgImage.add_header('Content-ID', '<image1>')
msg.attach(msgImage)

# 构造附件
for url in atta_url:
    msgAtta = MIMEText(open(url, 'rb').read(), 'base64', 'utf-8')
    msgAtta["Content-Type"] = 'application/octet-stream'
    msgAtta["Content-Disposition"] = 'attachment; filename="%s"' % (os.path.basename(url),)
    msg.attach(msgAtta)

# 发送
server = smtplib.SMTP(smtp_server, 587)
server.starttls()
server.set_debuglevel(False)
server.login(from_addr, password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()

```

## 做点总结

看了几份代码，基本上应该能发现使用smtplib发送邮件的步骤是一样的，变的只是使用email构造邮件的方法。而且，构造邮件也是有一定相似之处的，首先创建邮件，然后加入头部的信息，然后将正文文本、HTML以及附带的图片、附件通过`.attach()`方法逐一加入到创建的邮件中去，如此便能构建出一份完整的邮件。

> 所以说还是挺简单的嘛
