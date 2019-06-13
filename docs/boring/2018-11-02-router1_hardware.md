# 软路由与NAS(1) - 硬件平台搭建

从大二下学期以来，一直梦想着拥有一个自己的软路由。千兆位局域网、透明代理、NAS、自建git私有仓库、...只要能运行Linux系统，就有无尽的乐趣。这种想法总会让我对各种奇奇怪怪的机子产生兴趣（也不知道我大三去了嵌入式方向是不是因为这个）

最初我有一个 Raspberry Pi 3B ，那也确实好玩，我还拿他刷过 OpenWrt ，做过一段时间的随身路由，上面配置有透明代理。可是 Raspberry Pi 最大的问题就是 I/O 性能太弱， USB 、内置无线网卡，都慢得不行。它本身的 SD 卡读写性能也是一个瓶颈。这就导致无论用它干什么都觉得不爽，无论是软路由还是文件共享，还是别的什么服务。也就有时需要一个东西在校园网内跑个长进程时需要他（比如大二期末用它跑了个成绩监视应用，有新成绩出来时通知我（项目仓库在这 [keybrl/xidian_grade_monitor](https://github.com/keybrl/xidian_grade_monitor) ）），它的体验甚至不如阿里云学生主机。所以后来也就很少玩了。开学初把它卖给了舍友，换了个 Raspberry Pi 3B+ ，一样没什么好玩。几周前，不小心短接了他 GPIO 的 VCC 5V 和 3.3V ，瞬间黑屏了。送修至今（发表这篇文章时已经等了 38 天了），了无音信，便不再牵挂。

大二下学期开学初，看了尹大人的几篇博客，了解了他与他的那个小小的软路由之间的有趣故事。比如这篇 [DIY NAS Project (1) Hardware and OpenWRT](https://www.yichya.dev/diy-nas-project-1/) ，这是他这个系列文章的第一篇。下面这是尹大人初代 NAS

![尹大人的初代](//blog-assets.keybrl.com/images/router/yichya_router.webp)

感觉，哇，太厉害了，我也想要一个！！于是乎心心念念到了现在，在又一个双十一的推波助澜下（虽然我买的这些东西都不会降价），我开始了我有生以来最具挑战的一次 DIY 之旅。

---

## Too Young!

电脑嘛，首先是 CPU 和 板子，因为 Raspberry Pi 给我的不好印象，我觉得只有 x86 好玩，兼容性也好，跑个什么系统都比较随意，其他平台都没意思（ARM 各种玄学）。开始也没多想，某宝搜个“工控主板”一大堆，挑了个比较小巧，好看的，像这个...

![n29](//blog-assets.keybrl.com/images/router/n29.png)


CPU 是 Intel&reg; Celeron&reg; J1800 ， TDP 只有 10W ，大小也只有 12cm * 12cm ，而且 CPU 我查了一下性能还可以。双以太网卡、一个 SATA 、一个 mSATA 、一个 mini PCI-E 、 USB 若干（甚至还有 USB3.0 ）。看起来无可挑剔了。

正当我准备买时（大概在我后来真正下单前 12h），我在群里问了一下尹大人。我获知了一个惊人的消息（其实一点也不惊人，因为我就没有想过）， **这个赛扬 J1800 是不支持 VT-d 的！**  
尹大人刚说时，其实我没有什么感觉，因为我也不知道什么是 VT-d ，反正尹大人也经常说一些奇奇怪怪的名词，估计是什么高级功能，没有就没有吧，反正就是个软路由。但是出于对尹大人的尊敬，我查了一下什么是 VT-d ...

> **Intel&reg; 官方说法：**  
> *Intel&reg; Virtualization Technology for Directed I/O (VT-d) continues from the existing support for IA-32 (VT-x) and Itanium&reg; processor (VT-i) virtualization adding new support for I/O-device virtualization. Intel VT-d can help end users improve security and reliability of the systems and also improve performance of I/O devices in virtualized environments.*
> 
> **中文：**  
> *英特尔&reg; 定向 I/O 虚拟化技术 (VT-d) 在现有对 IA-32（VT-x）和安腾&reg; 处理器 (VT-i) 虚拟化支持的基础上，还新增了对 I/O 设备虚拟化的支持。英特尔定向 I/O 虚拟化技术能帮助最终用户提高系统的安全性和可靠性，并改善 I/O 设备在虚拟化环境中的性能。*

嗯，看起来就是某种对 I/O 设备做专门优化的虚拟化技术。再 Google 一查，不得了，有 VT-d 的话，可以直接把一个 PCI-E 设备划分给虚拟机，可以大幅提高虚拟机的某些 I/O 性能。而且，按尹大人的说法， *“据我说知，这是目前让无线网卡穿进虚拟机的 **唯一方法** ”* 。

一语惊醒梦中人。如果按照我最初的设想，就是这机子上跑个 Ubuntu ， Ubuntu 里跑个 OpenWrt 虚拟机， Openwrt 承担软路由的功能， Ubuntu 上面还可以部署别的应用。可这如果无线网卡穿不进虚拟机，我还做个鬼无线路由啊（其实也是可以的，只是少了很多配置无线参数的空间，还要面临性能的大幅下降的窘迫）。所以如果要愉快玩耍，肯定要买个带支持 VT-d 的 CPU 的板子。

## 甚至有点绝望

多了一个要求的话，找板子还是很艰辛的。我甚至顺便去翻了翻 Intel&reg; 的产品线。工控板，供电和散热都有比较严格的限制，我还想没有风扇，这样 TDP 基本就限制在 10W 左右了。 Intel&reg; 目前满足这个要求的 CPU 只有 Celeron&reg; 和 Core&trade; m3 。想想都知道， m3 那么贵，不会有厂商愚蠢到把它用在工控机上的，所以只剩 赛扬&reg; 了。 赛扬&reg; 的芯片命名也很有趣，大致分 4 类：

- Gxxxx G 开头跟 4 个数字的， TDP 基本都 2、30W ，受不起；
- Jxxxx J 开头跟 4 个数字的， TDP 一般比较低， 10W 或以下，但是全都没有 VT-d；
- Nxxxx N 开头跟 4 个数字的，跟 Jxxxx 差不多，反正没有 VT-d；
- xxxxU 4 个数字开头跟一个字母 U 的， TDP 普遍是 15W ，稍高，但是支持 VT-d；

综合来看，别无选择，只能是 Celeron&reg; xxxxU 了。

把现有的几个 xxxxU CPU 的型号依次在某宝搜搜，最后，选择真是少得可怜。一个是尹大人的二代软路由用的板子，长这样

![3215U](//blog-assets.keybrl.com/images/router/3215U.png)

那是一块 Celeron&reg; 3215U ，四个以太网卡还是很诱人的，具体可以看尹大人这篇文章 [DIY NAS Project (3) Hardware Upgrade & Disaster](https://www.yichya.dev/diy-nas-project-3/) 。这块板子据说有 USB3.0 干扰网卡的情况，加上也比较贵，而且仔细一想， 4 以太网卡对我也没什么用，所以还是算了。

然后还有就是 Celeron&reg; 3855U 的有几块，大致是这样的

![3855U](//blog-assets.keybrl.com/images/router/3855U.png)

区别的话主要是，有的板子支持 DDR4 2133 内存条，有的板子支持 DDR3L 1333/1600 。考虑到 DDR4 内存可能比这板子都贵，就选了用 DDR3L 内存的，也就是上图那块。配置基本如下

- CPU: Intel&reg; Celeron&reg; 3855U
- NB/DDR3L 插槽 * 1，支持 DDR3L 1333/1600
- mini PCI-E 插槽 * 1，可以插无线网卡
- mSATA 插槽 * 1
- USB3.0 、 USB2.0 各 * 2
- 吉比特以太网卡 * 2
- SATA3.0 接口及 4pin 硬盘电源接口各 * 1
- VGA 、 HDMI 各 * 1
- GPIO 、 COM 、 FPI 、 PS/2 ...（除了GPIO都不认识...）

心一横，下单！！

## 买买买！！

下单了板子之后，就开始了各种配件的选购，因为不想双十一跟大家排队拿快递，加上主要配件早就看好了，所以多数都在当天下单了。

首先是内存、外存、无线网卡

![order1](//blog-assets.keybrl.com/images/router/order1.png)

内存没什么挑的，找了个比较便宜的大牌子，镁光的8G DDR3L 1600。原本我想的是一个小路由用不了多少内存，我主力笔记本也才8G内存，302一堆2G内存的旧机子都能算得上流畅运行，偶尔给他们插上4G内存就流畅得不行了，所以4G内存绝对足够。 **但是** ，在我下单之前，我又在群里问了一下，尹大人竟然回我了个“多多益善”，还说什么8G内存就能支持什么什么文件系统了（具体是什么我甚至都忘了）。加上我一看8G比4G也就贵了100多，这多4G跑个虚拟机什么的肯定更轻松，于是心一横又下单了。

外存嘛，本来我有一块1T的希捷酷鱼3.5"硬盘，也是我平时用来堆东西的盘，本来就够了。 **但是** ，尹大人见我要搞个软路由，在群里提议我买个SSD，说什么“系统装在SSD里，硬盘没事可以下下来”，“装个SSD可以显著提高系统性能的”，“反正一个几十G的拆机盘也不用几个钱”...有道理喔，赶紧淘宝搜索一下，一圈搜索下来，贵的太贵，受不起。便宜的看不上，那些几十块钱几十G的SSD，顺序写入150MB/s，顺序读220MB/s，这不就坑人嘛，我那块硬盘都随便上200MB/s，虽说这SSD访问速率和4K随机读取什么的比硬盘要好很多，但这挫成这样的SSD还真不想买。于是乎，心一横，挑了个不算很贵，也不算差的中档SSD...

无线网卡肯定得挑个好的。由于才疏学浅，开始只知道 Intel&reg; 无线网卡还不错，淘宝一搜，一大堆，随便挑个看起来还不错的，所谓 2.4GHz /5GHz 双频的，所谓支持千兆位无线局域网的，便宜的，五六十左右的，一块。 **但是** （又是但是），我还是在群里问了一下，尹大人直接说了个 **“QCA9880”** ，这可还行，都精确到型号了，赶紧 Google 一下。高通的的一块其貌不扬的无线网卡，看介绍好像是挺厉害，再看尹大人说“无线网卡，除了高通的方案都不用考虑”...后面尹大人说了一大堆，结合 Google ，大致理解了一下。就是，目前的技术，基本上只能做到单天线 450Mbps ，业界对千兆位无线局域网的解决方案都是 MIMO (Multi-input Multi-output, 多输入多输出) 也就是，多根天线在不同频段，同时传输，多根天线互不干扰。一般手机只有一根天线，那么就只能到 450Mbps ，笔记本一般有两根天线，就可以 2 * 2 MIMO ，达到 900Mbps 。苹果的笔记本比较厉害，他们是支持 3 * 3 MIMO 的，到 1300Mbps 。多天线除了可以 MIMO 提升单用户的传输速率，还可以通过 MU-MIMO （多用户多输入多输出）降低用户之间的冲突，提升整个无线局域网内的网络质量。所以这也是为什么现在很多路由器都有两根或者三根天线的原因。而回到网卡上， QCA9880 是有3个天线接口的，支持 3 * 3 MIMO，而 Intel&reg; 多数网卡都是 蓝牙 + 2天线 ，蓝牙对于软路由来说又没卵用，所以就性价比不怎么样。加上， MIMO 是需要收发两端同时支持而且共用同一套解决方案才能发挥作用的，也就是不同品牌之间甚至都不兼容，而高通在无线网卡方面市场占有率比较高，加上高通近年来在 MIMO 的研发方面投入了不少精力，颇有造诣，支持高通方案的设备也比较多，所以体验会好很多。最后，尹大人补充了一句 **“QCA9880是世界上最好的无线网卡，那些很牛的路由器都是好几块这个堆起来的”** ...反正也就贵几十块，好，买！

买完了大头，还得买些小东西，馈线、天线得买几根，随便下单了几条好看的

![order2](//blog-assets.keybrl.com/images/router/order2.png)

在这期间顺便 Google 了一下那些天线说的什么增益，什么 5dBi 、 6dBi 到底是些啥意思。天线增益嘛，大家直观感觉肯定是增强信号了，那那个多少多少 dBi 肯定是增益的单位嘛，那数值肯定是越大越好了。真的吗？当然不是。其实要说增益是增强信号也不是没有道理，但是这个增强不是通过增加功率做到的，输出功率是由网卡决定的，天线没有任何影响。天线增益的基本原理其实就是改变信号的形状，一般的WiFi天线就是把信号压扁，削弱竖直方向的信号，增强水平方向的信号。那么增益的多少就是由形变量实现的，其实下面这张图已经可以非常清楚地说明了

![dbi](//blog-assets.keybrl.com/images/router/dbi.jpg)

说了那么多，所以我应该挑选多少 dBi 的天线呢？不知道，我瞎挑的，最重要是好看。看了一些文章，看起来 5dBi 挺中规中矩，那就 5dBi 吧。买了3根， 3 * 3 MIMO 嘛。顺便看到一根 3dBi 的挺可爱，也许便携使用时会有用，反正也不贵，顺便买了一根。

最后是电源，电源这虽然技术含量不高，但是也很重要啊，就某宝随便搜个 DC12V ，然后选个合适的功率。功率可麻烦了，我去查了各种配件的文档，最后算起来最高应该不到 30W 。但是，这个电源不能省，特别是注意到 **硬盘的启动电流是 2A** ，正常工作电流是 0.8A （都是 12V），这里就会有一个大电流的冲击，如果随便买个 30W （也就是 2.5A ）的电源，那可能硬盘一启动，主板和其他配件就会突然欠压，轻则屏幕黑一下，重则直接关机了。所以我也懒得想了，直接 double ，买了个 60W 的电源。

那该买的差不多就买完了（个鬼了）...

## 拼积木

经过几天焦急的等待，东西陆续都到了。首先是某个风和日丽的早晨，内存和SSD到了。

![SSD&Memory](//blog-assets.keybrl.com/images/router/SSD&Memory.jpg)

![Memory](//blog-assets.keybrl.com/images/router/Memory.jpg)

![SSD](//blog-assets.keybrl.com/images/router/SSD.jpg)

甚至挺好看，但是好像除了吊我胃口，没有任何卵用。

所幸，内存和SSD到的那天的下午，板子也到了。那起码能开机、装个系统了。

毫无意外，板子长这样

![board front](//blog-assets.keybrl.com/images/router/board1.jpg)

![board back](//blog-assets.keybrl.com/images/router/board2.jpg)

真的毫无意外吗？太意外了好吧，我发现他居然没带散热器！！虽然我在淘宝上看的时候没有看见他有散热器的照片，但是他们家其他板子都有带散热器，我以为只是因为这块CPU在背面所以才看不见，结果一到货彻底傻眼了...赶紧一量尺寸下单了两个散热器，和硅脂

![cooler](//blog-assets.keybrl.com/images/router/cooler.jpg)

两个尺寸是一样的，之所以买两个是因为我看我这U 15W TDP ，人家 J1800 才 10W TDP 散热器都比这个大，这怕是得有风扇才能压住。所以买了个有风扇的（虽然风扇电源接口不合适），但还是不想放弃无风扇散热方案，所以两个都买来试试。硅脂在京东买的，因为刚好发现京东有卖，而且自营的话第二天就能到。

但是这板子、内存、SSD都齐了，总不能不让我玩吧，所以秉着好死也不能赖活着的原则（我记得原话好像是“好死不如赖活着”来着），在302四处踱步，寻找临时解决方案。功夫不负有心人，在302垃圾堆找到几块闲置的主板，上面有几块小散热片，估计是南桥芯片、北桥芯片什么的，果断拆下来，擦拭干净。

刚要高兴，发现，电源没到啊。找遍了302也没有发现接口合适的 DC12V 电源。但我看板子上有个奇怪的 4-pin 插座，在正常的电源接口旁边

![power](//blog-assets.keybrl.com/images/router/power.jpg)

而且这个接口和台式机电源引出来的一堆线中的一个看起来可以完美对接，就下面这个

![power](//blog-assets.keybrl.com/images/router/power-line.jpg)

那是不是可以用这个苟一下呢。

但是，电源可是大事，莽不得，特别是我看尹大人文章时了解了尹大人因为电源问题烧毁了一块塞满数据的硬盘的有趣故事（详情可以看尹大人这篇文章 [DIY NAS Project (3) Hardware Upgrade & Disaster](https://www.yichya.dev/diy-nas-project-3/) ）。于是我去找这板子的规格说明和用户手册，上面是这么说的

![power-info](//blog-assets.keybrl.com/images/router/power_info.jpg)

噢，才疏学浅的我，结合一下 Google 才知道，原来这个东西就是传说中的 ATX 12V 电源接口，那应该是能用的吧。保险起见，我还拿多用电表测了一下电源上几个针脚的电压，看是不是符合说明书上的定义。但其实这样接上还是通不了电的，因为电源上的主输出接口没有输出，电源会以为没有东西接上他。所以我还得在302垃圾堆找到一块没用的主板插上，电源开始工作，然后插上那根 ATX 12V 电源线。压上散热片，按下电源开关，哔~ 的一声...

![first-light](//blog-assets.keybrl.com/images/router/first_light.jpg)

之所以要这样鬼畜地压着散热片，是因为散热片是随便找了块主板拆下来的，规格是不合适的，不能自己固定在这块板子上，而且由于没有硅脂，所以接触非常不紧密，只能通过增加一点压力让他们接触没那么糟糕（事实上还是很糟糕，看后面就知道了）。

不管怎样，这样能开机了。首先进入 BIOS 看一眼。还行，没有坑我。BIOS 能设置的东西还挺丰富的，甚至主板某些组件的供电电压、时钟频率都可以设置（是不是意味着可以搞搞超频了）。由于过于兴奋，当时没有及时拍照，所以就这样吧，反正 BIOS 也没什么好看。比较有趣的是，BIOS 上可以看见CPU温度，我发现随随便便就能上60摄氏度，手松一点就上到70+，而且才没几分钟，温度还在以肉眼可见的速度缓慢上升，太可怕了。

看起来，散热就位之前也没法做什么了。但是好死也好过赖活着，作死为什么不做到底呢，怎么说也得让我装个系统看看吧，我还想看看 SSD 擦写次数呢（为了确定没有人坑我），我甚至还想编译个 OpenWrt 呢... 再次去 Intel&reg; 官网看了一眼对于 CPU 温度的描述

![temp-limit](//blog-assets.keybrl.com/images/router/temp_limit.jpg)

看起来只要没到100度就不会死，反正 CPU 也会自己启动保护措施。那么就快动手吧，插上 Ubuntu 装机盘，深吸一口气，开机...

![install-ubuntu](//blog-assets.keybrl.com/images/router/install_ubuntu1.jpg)

![install-ubuntu](//blog-assets.keybrl.com/images/router/install_ubuntu2.jpg)

呼，忍着手底的热度，终于完了，幸好是 SSD ，安装个系统不用半个钟。然后我还开机装了几个软件，期间感觉好像也没多热，松了一下手，没过多久，散热片甚至变凉了，凉了！！完全凉了。完全难以理解，我甚至以为是静息时就这个温度，但是很快，我发现我点什么都没有反应了，再过了一会鼠标都不能动了，赶紧强制关机，幸好还能再开机，于是便不敢再玩了。后来也没有想明白怎么回事，也许是 CPU 过热关机了，当时凉得不可思议，就好像关机时的温度一样，几十秒前还是温热的，但是为什么鼠标还可以动呢，难道外设通信不需要CPU干预？为什么没有瞬间黑屏呢，难道显卡还能自己工作？难道显示器有缓存？管他呢...

第二天，硅脂到了，因为是京东自营嘛，而且电源也在不久后到了，具体是哪一天就忘了。而且无线网卡也到了，无线网卡是最期待的，毕竟我还没摸过这所谓的神卡呢，网卡见下图。虽然散热器没有到，但是有硅脂的话，之前那个小小的散热片也能勉强撑着。甚至开始尝试编译 OpenWrt 。

![qca9880](//blog-assets.keybrl.com/images/router/qca9880.jpg)

虽然天线还没有到，但是，302有一块闲置的 PCI-E 无线网卡，上面有两根天线，而且非常巧，在一个机箱里找到一根悬空的馈线，拆下来，这样就可以接一根网线了。但是，天线怎么固定呢。总不能像尹大人那样随便找个地方拿包装带一扎就当固定了吧。这可是有3根天线，总得齐齐整整摆着吧。然后我发现 PCI-E 挡板非常好用，就这样的东西

![pcie-card](//blog-assets.keybrl.com/images/router/pcie_wlan.jpg)

赶紧拆下来，找个位置拧个螺丝固定住

![full1](//blog-assets.keybrl.com/images/router/full1.jpg)

蓝色的东西是电工胶布，因为会接触到主板上一堆焊点，所以缠点电工胶布避免短路。四个脚是铜柱，把板子垫高，避免压到正面的元件

![full2](//blog-assets.keybrl.com/images/router/full2.jpg)

这扳手、纸巾是编译OpenWrt时热得不行时想出来的方法，扳手下面压的纸巾是湿水的（甚至可以称之为水冷），之所以用扳手是因为那是我当时第一眼看见的最合适的可以压在上面的东西

![water cooler](//blog-assets.keybrl.com/images/router/water_cooler.jpg)

后来天线到了，但3孔位的 PCI-E 挡板没到，所以临时用了块纸板来固定天线（这里要感谢 [@Virtuoso](https://github.com/virtuoso00) 的创意）

![full3](//blog-assets.keybrl.com/images/router/full3.jpg)

![full4](//blog-assets.keybrl.com/images/router/full4.jpg)

散热器到了之后就可以把他反过来正面朝上了，天线挡板还是没有到，所以暂时用单天线，用一个回形针固定，还挺可爱

![full5](//blog-assets.keybrl.com/images/router/full5.jpg)

最后所有东西都到了之后，长这样

![full8](//blog-assets.keybrl.com/images/router/full8.jpg)

![full6](//blog-assets.keybrl.com/images/router/full6.jpg)

![full7](//blog-assets.keybrl.com/images/router/full7.jpg)

插上硬盘，找了个小角落将它安置下来

![full9](//blog-assets.keybrl.com/images/router/full9.jpg)

![full10](//blog-assets.keybrl.com/images/router/full10.jpg)

好了，硬件部分就先讲那么多吧，一篇文章太长也会把人看死，也会把我写死。软件部分也是坑巨多，有空我会再写一篇介绍一下这辛酸历程...

---

## 略显遗憾

最后最后，其实硬盘的固定方案还没有找到合适的，正如你看见的，硬盘就直接摆在旁边。我也有尝试过尹大人的光驱位硬盘架固定法，但是可能也是缺少材料，也不像尹大人那时那样有一堆星火杯小车，所以硬盘架买了我也没找到合适的固定方法。而且对于这个主板来说，硬盘架有点大，看起来不是那么般配。有思考过定制亚克力、定制木板、之类的方案，但是感觉还是略显麻烦，所以暂时也没有付诸实践，日后如果有优雅的方案了会再更...也欢迎大家留言板写下自己的创意...

---

2018.12.19更新

目前的解决方案，自己做了个木头的机箱，还能把硬盘架放里面，还有一个炫酷的开关

![wood1](//blog-assets.keybrl.com/images/router/wood1.jpg)

![wood2](//blog-assets.keybrl.com/images/router/wood2.jpg)

![wood3](//blog-assets.keybrl.com/images/router/wood3.jpg)

![wood4](//blog-assets.keybrl.com/images/router/wood4.jpg)

![wood5](//blog-assets.keybrl.com/images/router/wood5.jpg)

![wood6](//blog-assets.keybrl.com/images/router/wood6.jpg)

![wood7](//blog-assets.keybrl.com/images/router/wood7.jpg)

![wood8](//blog-assets.keybrl.com/images/router/wood8.jpg)
