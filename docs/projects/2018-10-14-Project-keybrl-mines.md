# keybrl-mines - 优雅的扫雷从此无处不在

**该项目未完成！！**

> 项目地址：[keybrl/keybrl-mines](https://github.com/keybrl/keybrl-mines/)

点击链接开始游戏 [https://mines.keybrl.com/](https://mines.keybrl.com/)

*通过浏览器，畅玩经典游戏，从雷区中清除隐藏的地雷*

---

我过去很多项目都是从我的爱好出发而开始的。 keybrl-mines 也不例外，扫雷非常有趣，而且它不像 Tetris （我特别喜欢的另一个游戏） 那么刺激，适合安静的时候玩，而且随时可以停止去干别的事情。所以，下载大的代码库，编译大的项目，往嵌入式设备刷写系统，上机前等待老师出现等无聊的时间，就非常适合玩扫雷。Tetris 我已经实现过一个了，C语言写的在 Windows 命令行运行的小游戏，很简陋，甚至不能 T-Spin ，但是我实现了。而扫雷我没有写过，就连C语言命令行版的扫雷都没有写过，这就很遗憾了。扫雷比 Tetris 容易太多，讲道理我应该要写一个的，所以现在它来了...

## 复刻 gnome-mines

> Clear hidden mines from a minefield

使用过 [Ubuntu Desktop](https://www.ubuntu.com/global) 的同学都知道，“常规安装”的情况下 Ubuntu Deskdop 自带一个 [GNOME](https://www.gnome.org/) 桌面的小游戏 `gnome-mines` ，中文一般叫“扫雷”。即使你的Linux发行版默认不安装这个游戏也没有关系，你可以使用 `apt` 轻松安装它（如果你的发行版使用apt作为包管理工具的话），只需在终端输入如下命令。

```bash
sudo apt install gnome-mines
```

即使你不能使用 apt ，你也可以通过求助你的社区获得解决方案，或者直接加入信奉 Debian 的阵营，比如换用 Ubuntu Desktop 作为你的桌面端 Linux 系统。

扫雷是非常有趣的。Microsoft Windows 已经在 Windows 10 中移除了原本在 Windows XP /7 中自带的扫雷游戏，而且现在在 Windows 平台已经很难找到一个外观上能看的扫雷游戏了。而 Ubuntu Desktop 默认安装的 gnome-mines 界面朴素优雅，交互动画丰富又恰到好处，成了我玩扫雷的最佳选择。

但是，我并不总是使用 Linux 的桌面系统，当我回到 Windows 的世界，问题仍然存在，我仍然找不到一个合适的扫雷游戏。

这就是我想要开启这个项目的原因，我想要实现一个跨平台的，像 gnome-mines 般优雅的扫雷游戏，我暂时把它起名叫 `keybrl-mines`。

当你看见这个游戏的成品，你可能会觉得他完全就是 gnome-mines 的样子。如果真是这样，那我就成功了，事实上，我从一开始就打算让我的项目完全复刻 gnome-mines 的体验，尽管平台不同，很多细节难以做到一模一样，但我还是尽可能让他们相似。甚至这个项目中很多图片、图标都是直接从 gnome-mines 的项目仓库中搬过来的（如果我没有错误理解 GPLv3 的含义的话，我这么做应该是完全合法的）。

![gnome-mines 和 keybrl-mines 的比较](//keybrl-webapp.oss-cn-shenzhen.aliyuncs.com/keybrl-mines/image/compare.png "gnome-mines 和 keybrl-mines 的比较")

无论如何，gnome-mines 是一个非常棒的游戏。不管你觉得我的 keybrl-mines 体验如何，我都建议你尝试一下 gnome-mines ，最简单的方法就如上面说的，安装一个 Ubuntu Desktop。或者看看这个项目，到它的Github仓库（[GNOME/gnome-mines](https://github.com/GNOME/gnome-mines)）中点个 Star。

## 为什么是 keybrl-mines

说实话，在我几乎还没有思考这个游戏的实现细节的时候，我首先思考的就是这个项目的名字，这十分有挑战性。我过去的项目大都十分无聊，仅仅为了满足我的某些奇怪癖好，而且只是写着玩玩，比如[keybrl/Coin](https://github.com/keybrl/Coin)。相比之下，我觉得扫雷这个项目不是无聊的，尽管它仍然是为了满足我的奇怪癖好，而且我有预感它会得到不少关注，因为我知道有很多人喜欢玩这个小游戏，而且像我一样在 Windows 平台很难找到合适的版本。所以起一个恰当的好名字就非常重要。

我不能简单地将它命名为 `Mine Sweeper` ，因为扫雷是一个历史悠久的游戏，多年来各种版本层出不穷，如果我简单的命名为 “Mine sweeper” 、 “扫雷” 或者 “Mines” 什么的，那我仿佛在宣称我的项目才是扫雷的标准，事实上这十分自以为是。所以首先我想到的是 `web-mines` 因为我几乎是打算复刻 gnome-mines ，而我的项目是运行在 Web 平台的，所以模仿 gnome-mines 的命名就非常合适。但是 “web” 是一个含义很广的词，看起来还不如 `www-mines` 明确。但不管是 “web-mines” 还是 “www-mines” ，都有一个问题， Web 不是我发明的，随随便便冠以 “Web” 的名头，是不是显得太自以为是，而且同样有企图宣称我的项目是 Web 平台上扫雷的标准的嫌疑。

所以，经过若干小时的思考，我认为 “gnome-mines” 的 “gnome” 除了是一个桌面平台，也可以理解为是作者（尽管作者不止一人），也就是 “gnome 写的 mines” 的意思。如果是这样，那我带上我的 id 似乎就非常不错，低调，而且万一以后火了大家还能轻易看出是谁写的，所以就有了目前这个项目名 `keybrl-mines`。
