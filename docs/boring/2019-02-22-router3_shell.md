# 软路由与NAS(3) - 外壳

2018年秋冬之交（双十一前后），用工控主板搭了一个软路由和 NAS ，详见这两篇文章 [软路由与NAS(1) - 硬件平台搭建](./2018-11-02-router1_hardware.md) 和 [软路由与NAS(2) - 软件平台搭建](./2019-02-18-router2_software.md)

当时刚弄好是这个样子的

![full9](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/full9.jpg)

可以看到硬盘单独放置在旁边，十分不美观，而且零零散散不容易移动，还很容易积灰。于是寻思着要给他搞一个机箱

虽然这块板子说是 “Nano-ITX” ，但是一查好像也就是个概念，并没有什么统一的标准，所以自然也买不到刚好合适的机箱。然后我开始想能不能自己做一个机箱，首先我想到的是亚克力板。但是亚克力很硬，一般人用一般的工具很难精确加工，去查某宝，有定制切割亚克力的服务

![full9](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/ykl.jpg)

但是定制就意味着我必须提前设计好，而我更希望是一边做一边想，而且我也不知道商家能够做到的多高的精度，万一最后到货发现差一些，装不上，那就不好了。排除了这个之后我搜了我能想到的所有材料，看看供应商们能给我一些什么解决方案。最后我感觉还是木板容易一些，据说用裁纸刀就能切，而且我感觉也算是比较好看，木头具有一定的弹性，木板之间嵌合的宽容度就比较高。

随便估算了一下用量，买回来十张这样 3mm 厚的椴木层板

![shell1](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell1.jpg)

![shell2](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell2.jpg)

图中的小裁纸刀和铅笔尺子也是主要的加工工具。

主要的加工方法就是画好线，然后拿裁纸刀慢慢划开，根据力道不同，要划十几到几十下才能划透，从两面往中间划比从一面划穿到另一面要容易一点，还是相当累的。除了裁纸刀，我也有一些辅助工具

![shell3](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell3.jpg)

一个小小的电钻，可以装锯片、麻花钻头、磨砂轮之类的东西，加工木板还是比较容易的，只是不太容易操控，抖动什么的误差也很大，所以精细的还是要用裁纸刀

然后先讲讲设计吧

首先考虑的是最外面6块板（如果做成四棱柱的话）如何固定，我不想使用螺丝什么的，所以就用了一种小时候拼插玩具很喜欢用的结构，我也不知道如何形容，看图

![shell4](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell4.jpg)

插入、横着移一下就能卡住。

他们被设计为这样的方向：左右两块是往下移动锁死，这样只要不让左右两块往上移动就可以了，于是底板往后移动锁死左右两块板，上板往左移动锁死前后两块板，这样只要不水平推动上下两块板，整个结构就不会散。而且这些拼插结构加工得也是比较紧的，不容易松动。

![shell5](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell5.jpg)

![shell6](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell6.jpg)

![shell7](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell7.jpg)

然后再考虑内部的结构。首先我需要他能放下一个3.5寸硬盘，为此我买了一个台式机箱的光驱位硬盘架。

![shell8](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell8.jpg)

![shell9](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell9.jpg)

那为了不头重脚轻，应该是硬盘架和硬盘在下面，上面放主板，为了固定方便，中间用木板间隔。大概像这样

![shell10](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell10.jpg)

因为主板比硬盘架小很多，所以，主板必然不能前后两侧都靠边，于是我选择让主板上接口比较多的一侧靠边。但是正面还有4个 USB 接口啊，总不能浪费了吧，于是我买了3根延长线（两根 USB3.0 ，一根双头 USB2.0 ，没办法，找不到规格统一的 USB3.0 和 USB2.0 延长线），把他们延长到后面。大概就这样， USB2.0 延长线从主板下方 CPU 散热器边上过，两个 USB3.0 从主板上方过

（其实正面还有一个很像网线接口的接口是串口，不重要，所以没有做处理）

![shell11](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell11.jpg)

因为机箱比较封闭，原来的被动散热看起来也不是很行，于是选择在 CPU 下方的隔板挖个洞放个 8cm 的风扇，风扇是卡在那的，并没有什么胶水、螺丝。隔板上还有一个小洞是用来通下面硬盘的 SATA 和电源线的。

![shell12](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell12.jpg)

背板按照主板上的接口挖有洞，侧板右2左1共3个洞用来固定天线。

![shell13](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell13.jpg)

![shell14](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell14.jpg)

正面挖有一个硬盘架开口的洞，一个固定电源按钮的洞

![shell15](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell15.jpg)

还有一些适当位置的螺丝孔用来固定内部部件。

下面看一下装配过程吧

将天线馈线、电源开关固定到相应的洞上

![shell16](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell16.jpg)

嵌好侧板、背板、中间隔板

![shell17](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell17.jpg)

用螺丝固定好 USB 延长线、固定主板的铜柱，固定好风扇，将 SATA 和硬盘电源线穿好

![shell18](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell18.jpg)

插上主板底部的风扇控制线

![shell19](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell19.jpg)

理清线，把主板塞进合适的位置，拧上固定螺丝

![shell20](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell20.jpg)

嵌入前板，将各种线插到主板上，理好线

![shell21](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell21.jpg)

嵌入上板，翻转，可以看到底部

![shell22](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell22.jpg)

![shell23](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell23.jpg)

置入硬盘架，插上 SATA 和硬盘电源线，拧好硬盘架两侧的8颗固定螺丝

![shell24](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell24.jpg)

![shell25](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell25.jpg)

嵌入底板，翻转，装上天线，完工（这些做好的板看起来和原来的板色泽不太一样是因为我刷了木油，防潮、防蛀、防腐用的）

![shell26](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell26.jpg)

![shell27](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell27.jpg)

---

本来这事就结束了，但是吧，我觉得这个还是太大了，不够便携。而且我寒假还要拿回家，这么大不好带。于是我又做了一个更小的，不包含硬盘架的机箱。

拆卸后可以和主板和所有配件一起塞进这个小盒子里（不包括电源）

![shell30](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell30.jpg)

这个的制作方式和组合基本原理和上面那个差不多，就不详细说明了，放几张图吧

![shell31](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell31.jpg)

![shell32](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell32.jpg)

![shell33](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell33.jpg)

![shell34](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell34.jpg)

![shell35](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell35.jpg)

明显可爱多了不是吗，而且也更像一个路由器了！

如果需要接硬盘的话，侧边有一个隐蔽的开口可以把 SATA 和硬盘电源线透出来

![shell36](//keybrl-my-blog.oss-cn-shenzhen.aliyuncs.com/2018/images/router/shell36.jpg)

完美

---

这篇文章主要就是讲一下设计思路，大致的加工工艺，给需要的同学一点参考。具体的设计细节就不说了，如果想自己做一个类似的机箱的话，我主要有下面一些提醒

首先是做之前要有一个总体的安装过程的思路，不能只是按照想象安装好什么样子来设计，因为有可能会产生各部件之间冲突、活动受限，导致根本安装不起来

设计可以按自己喜欢的来，但是，加工其实很困难的，一定要结合材料的理化性质和自己的加工能力来设计。像镂空、云纹、雕花什么的，我只能说祝您好运了。

还有就是，加工真的很难，切这个需要手臂、手腕以一个不算小的力气，持续、稳定地做功。想象一下举着哑铃，往前伸直手，持续一天，手臂会非常酸的。非常劝退

好了，没了。
