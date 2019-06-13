# 在GitHub上通过Jekyll搭建个人博客

> 10分钟拥有一个自己的博客
>
> date: 2017-10-08

---

搭建和维护个人博客以及写博客是一件非常酷的事情，而且这也基本可以算是每个程序员的必备技能之一。一个个人博客既是自己的一张名片也可以作为自己学习的见证。

## 本节主要内容

搭建个人博客的方法有很多，而我们今天讲其中比较简单的一种。主要涉及以下内容

1. Git及GitHub的基本操作
2. Jekyll的浅显认识
3. 对Markdown的熟练应用
4. [可选]对Web前端的基本认识
5. [可选]域名的选购与解析

## Git和GitHub

**Git是一个分布式的版本控制软件** ，最初由林纳斯·托瓦兹（Linus Torvalds）创作

> "I'm an egotistical bastard, and I name all my projects after myself. First Linux, now git."

这个工具非常强大，当然幸运的是我们现在不需要用到很多高级的功能。我们先做第一件事

### 如何安装

1. Windows前往[下载](https://git-scm.com/)
2. Debian/Ubuntu在终端执行 `apt-get install git`

`git --version` 验证安装是否成功

---

好的，我们先把Git放一放，我们来看看[GitHub](https://github.com/)

**GitHub是一个通过Git进行版本控制的软件源代码托管平台** ，那是一个有趣的地方，多去逛逛。

![Welcome home, developers]({{ site.assets_url }}/images/SSSTA-Blog/welcome_home.png)

GitHub主要可以帮助你保管代码，协助你与小伙伴合作写项目以及为你提供大量优秀的开源项目（这样你就不用自己写了）

当然，我们今天使用他一个比较边缘的功能 ---- *GitHub Pages* ，他能为你提供静态网站服务，以及重要的是，他支持Jekyll。于是我们就可以愉快地搭博客了。

然后，同样的，我们先做点实际点的工作。

1. 注册并登陆GitHub账户
2. 创建一个公共仓库（如果你有钱你也可以用私有的）

---

前面提到，GitHub可以保管代码。所以我们现在开始做点有意义的事情。我们来试着管理自己的代码仓库，给GitHub仓库推代码。也就是一点简单的Git和GitHub操作。

首先查看仓库克隆地址

![仓库克隆地址]({{ site.assets_url }}/images/SSSTA-Blog/clone_url.png)

然后在本地克隆一份

```bash
cd .
git clone http://github.com/xxx/example.git
```

然后进入本地仓库目录

```bash
cd ./example
```

然后我们可以先对仓库里面的文件做些修改，比如写个README.md

然后我们试着提交修改并将修改后的仓库推到GitHub上

首先是将目前文件夹里的内容加到仓库中

```bash
git add .
```

然后提交修改

```bash
git commit -m 'summary
description'
```

> 如果此时弹出类似 `Please tell me who you are` 的字样，那你需要先写两行配置信息
>
> `git config --global user.name "{{ Your name }}"`
>
> `git config --global user.email "{{ Your email }}"`
>
> 两个大括号以及他们内部的内容用自己的真实信息替换

当然以上都是对本地仓库的操作，我们把修改后的仓库推到GitHub

```bash
git push origin master
```

现在我们可以刷新一下GitHub看看了

我们现在复习一下

1. 修改
2. add
3. commit
4. push

就是这样，很多事情就是这么枯燥乏味，但却很有趣。

## Jekyll

> "Transform your plain text into static websites and blogs."
>
>  ---- [Jekyll - Official Site](https://jekyllrb.com/)

Jekyll是个好东西，他非常神奇，对 **前端** 感兴趣的同学可以稍微深入研究一下。

但幸运的是，我们今天先不自己写，我们搬一个现成的。我们不用知道Jekyll怎么写，我们只需要知道怎么用别人写好的Jekyll模版。

我们随便百度一下 `Jekyll模版`

- [Jekyll Themes](http://jekyllthemes.org/)

然后我们只需要完成这么几步

1. 下载
2. 修改配置文件\[，以及对页面做一些个性化的修改(对前端感兴趣可选做)\]
3. 扔到自己的GitHub仓库

我们就说说修改配置文件

## GitHub Pages

GitHub Pages服务相当于为你提供一个静态网站服务器，对前端比较感兴趣的可能对此挺高兴，多数静态的前端作品都可以用这个展示出来。而且他还支持Jekyll，所以你用Jekyll写的（搬的）博客也可放在这上面。

你只需要在自己的仓库里，设置，选择一个分支，确定。

> Settings -> GitHub Pages -> Source

他会把一个叫 `index` 的文件作为索引，可以是 `index.html` ，也可以是 `index.md` 。

而且非常棒的是，你可以设置自己的域名，这样就不用用那个很长的https://username.github.io/project/了。

> 关于 **域名** 的问题后面选读

## Markdown

**我们一般用Markdown写博客**

Markdown是一种轻量化的标记语言，他非常适合写博客。除此之外，你们平时也可以用它写文档、写作业、写小论文、写报告（我经常这么干），他是一种非常适合阅读的标记语言。

标记只是决定一段文本的格式，比如说一级标题、二级标题、全局强调、局部强调、代码块、行内代码、超链接、图片、引用块、表格、......但是这些东西具体呈现出什么样子是由Markdown编辑器或者别的什么工具（比如Jekyll带的Markdown渲染引擎）渲染的。

这是非常优雅的东西，这份课案，上一份课案，以及你们见到的我的所有课案都是用Markdown写的。多数编辑器都可以将Markdown转换为pdf（打印和交流）、html（应用于网页）、图片（方便分享）。

> 好好学学，你们可以看看我的第一篇博客[《Markdown语法基础》](../professional/2016-11-13-The-base-of-grammar-in-Markdown.md)

## 最后的复习

我们借着推送一份文章的机会再最后复习一下Git和GitHub的操作

将文章按照要求写好，放在 `_post` 文件夹中

```bash
git add .
git commit -m 'push a new article'
git push origin master
```

我们刷新一下自己刚搭好的博客，会不会有一种感动

## 域名的选购与解析(选读)

> “如果没有自己的域名，人生还有什么意义”
>
>  ---- 没错，就是我说的

域名的用途有很多，可以解析到自己搭的Web服务器，方便别人访问自己的作品；解析到自己的邮件服务器，可以有自己独一无二的域名邮箱；所以当然，我们可以解析到自己的博客。这样别人可以用一种酷酷的方式访问自己的博客。

> 比如我的 `blog.keybrl.com`

不管你要用域名做什么，一般来所，你需要先买一个。推荐几个域名服务商

- [腾讯云](https://cloud.tencent.com/)
- [阿里云](https://cn.aliyun.com/)
- [Namecheap](https://www.namecheap.com/)

### 域名的分类

首先，域名有顶级域名、二级域名、三级域名，...

域名随便定的，就是个名字，只要可以解析。但是要能在世界上绝大部分地区能知道你的域名，获得你域名的解析，并访问解析的地址，那就需要有权威机构为你做这些事情。

首先已经有了一堆国际顶级域名，这是国际上承认的。比如 `.com` 、 `.cn` 、 `.org` 、......然后顶级域名还可以用二级域名细分，比如科协的 `sssta.org` 、我的 `keybrl.com` 、 `keyboard-l.com` 、 `keyboard-l.cn` 。顶级域名是由国际公认的，某些顶级域名服务商负责管理，然后他们会授权很多别的服务商去管理一部分带有二级域名的子域名。

> 不同顶级域名的一般用途可自行百度，比如 `.org` 一般用于组织， `.edu` 一般用于教育行业
>
> 选择什么看自己钱包以及需求
>
> 反正，尽量别选什么 `.中国` 就好

然后所谓买域名，其实就是买某个顶级域名的子域名，你在谁那买的，谁就会负责管理，他们会帮你记录这个域名的注册信息，并部分公示，记录在哪里解析，不过或许他们会帮你解析。

你可以选一个服务商，然后去那搜索一下自己意向的域名，如果没有被人注册，那你就可以把他买下来。

### 域名解析

然后你需要解析。其实域名很便宜，你花的钱多数是用于你的服务商为你提供的域名解析服务（DNS）。域名就像电话号码簿的某个人名，然后需要记录这个名字对应哪些电话号码。

关于域名解析的设置，其实腾讯云和阿里云都有比较详细的说明。

你一般需要为每条解析填写以下信息

`记录类型` 将域名解析为什么类型的值

`主机记录` 把域名以何种样子解析

`记录值` 域名解析为的值

`TTL` 解析被缓存的时间

详细，你们可以去试着买个域名解析一下，腾讯云和阿里云都会给出充足的提示，不懂还可以百度一下。以及实在不懂可以再找个学长问问（最起码，随便一个名片带 `web` 的学长应该都懂）

如果我们要解析到自己的GitHub Pages，那么你就选择 `CNAME` 记录类型，记录值填 `username.github.io.` ， `username` 是你的GitHub用户名，主机记录按自己喜好填，其他默认。然后在GitHub上再填上自己解析好的域名，确定，即可。

![腾讯云设置解析](//blog-assets.keybrl.com/images/SSSTA-Blog/tencentcloud_dns_set.png)

![GitHub设置自定义域名](//blog-assets.keybrl.com/images/SSSTA-Blog/github_domain_set.png)

然后就大功告成了，你可以试着访问一下。

> 确认无误后你就可以逢人便说：
>
> “嘿，你知道吗，我新搭了一个博客诶！...”
>
> “想看看吗？快拿你的手机试试访问 *blog.keybrl.com* 。”
>
> （虽然这样看起来很傻）

## 用SSH连接GitHub仓库(选读)

之前我们一直在使用HTTPS连接自己的GitHub仓库，这样你经常需要登录，很麻烦，而且并不很安全。所以GitHub提供了一种免密连接的方法，......

如果你有这样的追求，你一定不会畏惧于亲自寻找答案

> 参考阅读：
>
> [Connecting to GitHub with SSH](https://help.github.com/articles/connecting-to-github-with-ssh/)

## 写在最后

这次我们很幸运地遇到了更多奇怪的东西。不过千万不要有 `哇，好厉害诶，讲的是什么。我听不懂，我还是放弃吧。` 这样类似的想法。

我敢说，在我们接触这些时并没有比你们更多的基础，没有比你们更详细的指导，没有任何比你们更有利的条件。现在能将你们最终区分的只有*在虚无中快速构建根基并迅速扩展知识树的学习能力*。

> 好好学，这很有趣！

### 推荐阅读

> [git - 简易指南](http://www.bootcss.com/p/git-guide/)
>
> [GitHub Help](https://help.github.com/)
>
> [Coding 帮助文档](https://coding.net/help/)
>
> 虽然我不很喜欢Coding.net，但是刚开始我的确是用Coding指导我在GitHub的操作的。感谢睿神让我知道这个东西。
>
> [Jekyll - Official Site](http://jekyllcn.com/)
>
> 这回是中文的
>
> [Markdown语法基础 - Keyboard L](../professional/2016-11-13-The-base-of-grammar-in-Markdown.md)
>
> 我就是这么恬不知耻地推荐自己写的文章
>
> [W3School](http://www.w3school.com.cn/)
>
> 前端相关

### 各位强者的博客

请查看 [友链列表](../links.md)
