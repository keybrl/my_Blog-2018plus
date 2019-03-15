hero: 9分钟拥有一个自己的博客

# 通过MkDocs搭建个人博客

> date: 2018-05-19

---

搭建和维护个人博客以及写博客是一件非常酷的事情，这也是每个程序员生活的一部分。一个个人博客既是自己的一张名片也是自己学习的见证。

搭建和托管博客的方法有很多，很久以前我曾经推荐过通过GitHub托管Jekyll项目，并通过GitHub Pages服务展示博客的方法。

> 详见，[《在GitHub上通过Jekyll搭建个人博客》](../sssta/2017-10-08-SSSTA-Blog.md)

Jekyll是一个强大的静态网站生成器，结合GitHub Pages的完美支持，非常便于你展示你的想法。但是，他并不易于操作，如果没有前端的知识你甚至没法操作，你只能被动接受Jekyll主题设计者在设计中加入的一大堆垃圾。

如果你只是想好好地写写文章，并让他们优雅地展示出来，那用Jekyll肯定是不合适的，或者至少是不方便的。很快我将为你介绍一个更优雅的方式应该具备的特性。

## 0. MkDocs概述

> MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation.
>
> MkDocs是一个致力于构建项目文档的快速、简单和绝对优雅的静态网站生成器。

MkDocs是被设计用于构建文档的，所以它特别适于注重内容的静态站点，它至少有以下优雅之处

- 清晰的文章分级目录
- 文章内标题导航
- 全站文本搜索
- 全部Python Markdown扩展
- 优雅、易于阅读的Markdown渲染

除此之外，MkDocs的多数主题都没有多余的内容，只专注于展示文章，正如[该站点](https://blog.keybrl.com/)所呈现的。而且，你需要做的也只是写文章，其他细节都能很便捷地设置。这比Jekyll还简单，而且更优雅。  
**酷炸了不是吗？**

接下来我将分部分逐步介绍通过MkDocs构建、部署个人博客的过程。点击列表中的超链接可以直接跳转到相应章节。

1. [环境搭建和MkDocs的安装](#1)
2. [构建一个最简单的网站](#2)
3. [通过Markdown写自己的文章](#3)
4. [选择主题](#4)
5. [完善配置文件](#5)
6. [站点托管与部署](#6)

!!! Tip "阅读提示"
    本篇旨在从一个大的视角了解通过MkDocs构建站点的过程，而不是作为指导工作的手册、文档

    对于上述的部分内容，本篇可能只会作简要描述，并引导读者前去阅读[MkDocs的官方文档](https://www.mkdocs.org/)或另一篇更详尽的文章

    [本文最后](#_1)有一个列表，列出了全部在本文出现的建议阅读的相关的官方文档和其它文章，它们对于读者建立完善、准确的认识将更有帮助。

## 1. 准备工作

MkDocs 是一个以 Python 实现的轻量化静态网站生成器

所以，首先我们需要安装 Python ，在 Debian/Ubuntu 下只需要通过 apt 安装即可

```bash
apt install python
```

!!! Warning "兼容的Python版本"
    > 官方文档的说明是：MkDocs supports Python versions 2.7, 3.3, 3.4, 3.5 and pypy.

    但事实上我用 Python 3.6 也没有任何问题，所以我建议首先尝试 Python 的最新稳定版，如果存在兼容问题再参考官方推荐

安装Python的第三方包管理器 pip

```bash
apt install python-pip
```

在Windows环境下安装 Python 和 pip 请参考 [python.org](https://www.python.org)

然后通过 pip 安装 MkDocs

```bash
pip install mkdocs
```

检查安装情况

```bash
pip show mkdocs
```

如果有出现对 MkDocs 的简要描述即安装成功

!!! Tip "强烈推荐WSL"
    在 Windows 环境下进行与 Web 相关的开发经常都很不方便，如果既不喜欢虚拟机，又不习惯长时间在 Linux 下工作，又不想来回切换系统，那你一定要试试 WSL

    > WSL: Windows Subsystem for Linux

    WSL 是 Windows 的 Linux 子系统，可以在 Windows 中运行 Linux 应用，它只能通过命令行进行交互，有兴趣自行 Google

## 2. 好的开端

MkDocs 给我们提供了一种简单的创建 MkDocs 项目的方式

```bash
mkdocs new hhh
```

!!! Tip "备选方案"
    基于我还不清楚的原因，某些情况下，这样的命令可能不能工作

    尝试替换为 `python -m mkdocs new hhh` ，以下涉及 mkdocs 的命令都可以作类似替换


在终端 cd 到合适的目录，执行上述命令，即可在当前目录创建一个最简单的 MkDocs 项目文件夹，在此他的文件夹名为 `hhh` ，你可以将其换成任何你喜欢的名字，只要他符合文件夹命名规范

进入新建的目录

```bash
cd hhh
```

使用 `ls` 命令或直接在文件资源管理器打开可以看见里面有这些文件

```
- docs
  |- index.md
- mkdocs.yml
```

其中 `mkdocs.yml` 是项目配置文件， `docs/` 是默认用于存放文档的文件夹，目前里面只有一个 `index.md` 是文档主页的文档

在上面所说的目录下，即 `hhh/` 内，输入以下命令即可呈现文档

```bash
mkdocs serve
```

输入完之后终端会提示通过 URL http://127.0.0.1:8000 访问，在浏览器地址栏输入它，回车，你就能看见默认的主页

这是一个开发用的服务器，当你修改项目中的配置文件或文章，他会自动更新并使打开的页面刷新以保持同步。除此之外，使用 `mkdocs build` 可以构建网站并将静态文件放入配置文件设置的某目录内，，默认是 `site/` 里面就是一些简单的如 `.html` 、 `.css` 、 `.js` 等静态文件，它们完全可以直接通过如 GitHub Pages 等静态网站服务展示出来，只需要将生成的 `site/` 目录下的文件放进 GitHub 仓库，开启 GitHub Pages 服务即可。不过先不要急着这么做， MkDocs 有更优雅的方式，我将在该篇最后一节介绍这些部署技巧。

## 3. 跃动的思想

一个博客，或者文档，最重要的是里面的内容。和多数博客、文档或别的什么静态网站生成器一样 MkDocs
支持将用 Markdown 写就的文章转换为具有好看样式的 HTML 页面，而且 MkDocs 只支持 Markdown。只需要将 `.md` 文件放在 `docs/` 目录内， MkDocs 会自动转换他们，按 `docs/` 内的目录结构生成静态页面树，并尽可能将这种结构展现在页面中

!!! Tip "关于文档结构"
    MkDocs会尽量自动展现文档结构，你也可以通过修改 `mkdocs.yml` 文件来自定义文档结构，详见 [5. 尽在掌控](#5) 中关于修改配置文件的说明

    不同的 MkDocs 主题对文档结构的呈现能力不同，但他们一般都不能呈现超过两层的文件目录

MkDocs 对 Markdown 的转换是通过 [Python-Markdown](https://github.com/Python-Markdown/markdown) （一个 Python 的第三方库）实现的，所以除了支持标准的 Markdown 语法 （见[Daring Fireball: Markdown Syntax Documentation](https://daringfireball.net/projects/markdown/syntax)），也支持 Python-Markdown 支持的多数 Markdown 扩展 （详见其[官方文档](https://python-markdown.github.io/extensions/)）

## 4. 颜值即正义

一个博客，或者文档，最重要的是里面的内容。但是这不意味着我们将容忍外观的丑陋，而且我们还应该有极致追求

MkDocs 有一个简单的基础主题，就是你刚刚看见那个。除此之外，你还可以在十几种第三方主题中选择一个或自己自定义主题

在 `mkdocs.yml` 中加入以下内容

```yml
theme: 'readthedocs'
```

这将将主题切换至 Read the Docs 的主题，或许你会发现这个主题十分熟悉，因为很多文档都是这么构建的。更多第三方主题详见 [社区wiki](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Themes)

> 我个人推荐 [**Material**](https://squidfunk.github.io/mkdocs-material/)

自定义主题的相关内容已经远远超出本篇所能描述的范畴，详见 [Custom themes - MkDocs](https://www.mkdocs.org/user-guide/custom-themes/)

## 5. 尽在掌控

对 MkDocs 很多细节的设置是通过其项目配置文件 `mkdocs.yml` 达成的，由于内容繁琐不便于叙述，所以我建议通过参阅相关官方文档了解这部分内容 [Configuration - MkDocs](https://www.mkdocs.org/user-guide/configuration/)

## 6. 锋芒毕露

无论怎么样，博客总是要给人看的。前面我已经介绍了如何在开发环境预览自己的 MkDocs 项目和在 GitHub Pages 部署 `site/` 目录。在此，我将介绍 MkDocs 一个更方便、优雅的部署技巧。

GitHub Pages 不只能简单地展示 master 分支内的内容，他还能部署任意一个分支或者 master branch /docs folder 。所以如果我们要在一个 GitHub 仓库中展示 MkDocs 项目并部署其生成的静态网站，我们可以将它们分在两个分支中。将 MkDocs 项目的全部文件放在 master 分支，按照正常方法管理。创建一个专门用于部署静态网站的分支，比如我设置的是 `gh-pages` ，在里面放置 `site/` 中的文件，并在该分支开启 GitHub Pages 服务即可。

不要急着复制 `site/` 中的文件， MkDocs 提供了 gh-deploy 工具，他可以帮你一键 build、commit、push

在 `mkdocs.yml` 文件中加入以下内容

```yml
remote_branch: gh-pages
remote_name: origin
```

第一个是用于开启 GitHub Pages 的分支名，第二项是仓库地址名，如果你打算设置成上述样子，那你就可以省略他们，因为他们是默认设置

然后在终端执行

```bash
mkdocs gh-deploy
```

MkDocs 会自动 build 该项目并 commit、push 到该项目仓库的指定分支，第一次使用该功能可能需要登录，按提示操作即可

如果分支设置、 GitHub Pages 设置、 gh-deploy 设置都正确的话，理论上讲你就已经把最新构建的网站部署了

!!! Danger "谨慎行事"
    在您决定公开部署你的 MkDocs 项目之前，请确保项目中的全部内容符合您所在国家、地区的相关法律法规，避免冒犯您所在国家或地区的常见宗教信仰、风俗习惯，并尽量尊重可能的读者。

    即使你确保符合上述要求，我个人仍然额外地建议您，当您在您的 MkDocs 项目中公开谈论政治时保持谨慎

---

## 建议阅读

- MkDocs官方文档 [MkDocs](https://www.mkdocs.org/)
- Python-Markdown的GitHub仓库 [Python-Markdown](https://github.com/Python-Markdown/markdown)
- 标准 Markdown 语法规范文档 [Daring Fireball: Markdown Syntax Documentation](https://daringfireball.net/projects/markdown/syntax)
- [MkDocs社区wiki](https://github.com/mkdocs/mkdocs/wiki/)
- [《在GitHub上通过Jekyll搭建个人博客》](../sssta/2017-10-08-SSSTA-Blog.md)
