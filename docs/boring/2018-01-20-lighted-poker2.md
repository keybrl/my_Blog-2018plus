# IKBC Poker2 加灯历程

> 记录我为我的Poker2加上背光的过程，作为纪念
>
> date: 2018-01-20

---

首先我特别想安利一波Poker2，Poker2是非常优雅的一款键盘。

![键盘展示1](//blog-oss.keybrl.com/2018/images/lighted-poker2/1.jpg)

一般来说，一款功能完整的键盘应该是87键的，104键比87键多了可有可无的小键盘，而61键是将87键的 `F1` ~ `F12` ，9个功能键，4个方向键和一个 `ESC` 键去掉。非常的小巧、便捷，而且除了精简的键外键盘布局和传统键盘布局基本一样，不像Filco的Minila那样拥挤。

![键盘展示1](//blog-oss.keybrl.com/2018/images/lighted-poker2/2.jpg)

原装加厚的PBT键帽和比一代Poker多的钢板让其拥有上乘的击打手感。

![键盘展示1](//blog-oss.keybrl.com/2018/images/lighted-poker2/3.jpg)

我买的是红轴，红轴的轻盈配合Poker2紧凑的外型，可以说是十足的优雅了。

缺少的功能键、方向键都可以通过 `Fn` 加一个键实现，如果将 `Fn` 键改到左 `Alt` 处，就能实现一只左手完成上下左右，右手可以拿着鼠标，打字时移动光标也很方便。最重要的是，Poker2是硬件支持全键可编程的，而且可编程的不同编程层多达3层。这就意味着你可以个性化自己键盘的键位。将所有功能集中在键盘核心的61键区是非常优雅的做法，你在打字时调用各种功能键都毫不别扭，而且非常流畅方便。

USB Type-C的接口为其赋予了便携和通用性，带到外面只需要一根手机数据线就可以连接（前提是你的手机是Type-C接口的）

如果一定要说Poker2有什么缺点的话，那就是你用它用久了之后，打字时你就会下意识地去够Fn键。还有就是，他没有蓝牙，这一点很伤，不过优雅的东西总会有一点缺憾美的。

---

Poker2是一款很低调的键盘，他只有黑白两种颜色，也没有什么RGB背光。但是，适当的背光其实也是有助于提高在低光照环境中的办公效率的，所以我萌生了为我的Poker2加背光的想法。

其实最终打动我的，让我决定为其加灯的，是Poker2主板预留了灯位，每个灯都有配套的灯阻，而且自带8级亮度调节和8种灯效，可以通过 `Fn` + `C` / `V` / `B` 来切换，只需要把led灯珠插上就能亮。一个没有灯的键盘，居然帮你把灯效写好了，如此良心，岂能不心动。于是我打算加个灯。

## 0. 工具准备

首先我们来看看加灯所需的工具

![加灯所需工具1](//blog-oss.keybrl.com/2018/images/lighted-poker2/4.jpg)  
![加灯所需工具2](//blog-oss.keybrl.com/2018/images/lighted-poker2/5.jpg)

- **笔记本电脑** ，调试时为键盘供电的设备，直接把键盘插在手机充电器或者移动电源上是不工作的。必须是一个可以输入的设备，手机加OTG也可以；
- **数据线**，调试时连接键盘用的，只要是Type-C数据线都可以；
- **IKBC Poker2**，要加灯的键盘；
- **螺丝刀**，用于拆卸键盘；
- **拔键器**，用于拔键；
- 【可选】吸锡器，用于吸除多余的焊锡；
- **电焊枪/笔**，用于焊接LED灯珠；
- **焊枪架、松香、吸水海绵、焊锡**，焊接工具；
- **LED灯珠 * 61**，LED有很多种，可以自行选择，我用的是‘3mm圆头无边白光LED’；
- **3V电子**，用于测试LED是否正常，买薄的那种，我是用CR2025的；
- 【可选】多用电表，检查电路；
- **剪线钳**，用于剪短LED管脚，没有也可以用指甲剪或普通剪刀。

看起来准备充分，可以开始搞事情了。

## 1. 键盘拆解

首先需要把键帽都拔下来，如果有一把优秀的钢丝拔键器那就非常爽了。

![钢丝拔键器](//blog-oss.keybrl.com/2018/images/lighted-poker2/6.jpg)  
![拆好键帽](//blog-oss.keybrl.com/2018/images/lighted-poker2/7.jpg)

有没有觉得一排排的红轴很可爱呢

其实这个时候就可以试着把一个灯珠插上看看会不会亮

插上电，按一下大写锁定键，看到大写指示灯亮了，说明键盘此时正常工作

![大写灯](//blog-oss.keybrl.com/2018/images/lighted-poker2/8.jpg)

拿出一个LED，用电子测试一下，会亮说明LED正常

电子是平的那面是正极。LED是长脚是正极，其实还有一个特征，灯珠里面两块金属不一样大，小的那边是正极（这个特征后面会用到）

![led](//blog-oss.keybrl.com/2018/images/lighted-poker2/9.jpg)  
![试灯](//blog-oss.keybrl.com/2018/images/lighted-poker2/10.jpg)

把管脚剪平（别剪短，把正极剪到和负极一样长就可以了），然后插进轴上预留的灯孔里。注意，标A的那边是正极，或者说，当正视‘Cherry’字样时（为了上灯位，Poker2将轴反着装的。上灯位适合正刻，下灯位适合侧刻），正极在左手边。

![红轴](//blog-oss.keybrl.com/2018/images/lighted-poker2/11.jpg)

插进去之后按一下 `Fn` + `C` 切换灯效或者 + `V` / `B` 调节亮度，看看灯珠是否会亮。要注意用手压着灯珠，不然接触不良。（我是因为刚好放正了位置，不用用手压着）

![键盘试灯](//blog-oss.keybrl.com/2018/images/lighted-poker2/12.jpg)

看见亮光异常兴奋呢

好了继续拆解吧。把键都拔出来之后可以看到钢板上有 **六颗** 固定螺丝，全部拧下来，收好。

![拧螺丝](//blog-oss.keybrl.com/2018/images/lighted-poker2/13.jpg)

然后想办法把板子弄出来，我的方法是拿螺丝刀挂住大写锁定键左边那个空洞然后往上板，固定得还是挺稳的，要用点力。然后就可以把整个钢板连同下面的PCB板一起拿出来了，电源是固定在外壳上的，注意别瞎扯。

![彻底拆开](//blog-oss.keybrl.com/2018/images/lighted-poker2/14.jpg)

仔细观察PCB板上每个轴的位置，都有两个小的焊盘，一个方的一个圆的，跟上面插灯的位置是对应的。就是焊接LED的位置，方的是正极。

![PCB板1](//blog-oss.keybrl.com/2018/images/lighted-poker2/15.jpg)  
![PCB板2](//blog-oss.keybrl.com/2018/images/lighted-poker2/16.jpg)  
![板上试灯](//blog-oss.keybrl.com/2018/images/lighted-poker2/17.jpg)

**拔掉PCB板的供电线** ，准备进入下一环节。

## 焊接

差不多了，可以开始进入到最困难的阶段了。焊接可是技术活，对自己技术不够有信心的最好还是不要自己尝试了。

![一堆led](//blog-oss.keybrl.com/2018/images/lighted-poker2/18.jpg)  
![焊接套装](//blog-oss.keybrl.com/2018/images/lighted-poker2/19.jpg)

注意到焊盘上已经有锡了，为了防氧化，所以，理论上讲，最方便的方法就是拿一个刀头焊咀同时熔两个，然后灯珠顺势从背面（钢板那面）插进来，然后固定住。但是我没有刀头焊咀

然后网上的教程一般都是用吸锡器吸掉正极的锡，然后熔了负极时可以把灯插进来。因为LED是正极脚长嘛，去掉正极的锡容易插进来。然后固定好后再补上正极的锡。看起来非常完美，不过可能我操作吸锡器不够娴熟，或者吸锡器不合适，试了好几次都洗不干净正极，果断放弃了。

然后最后我采取了一套完美的方案，先给两边补点锡，把他们连起来...

![补锡](//blog-oss.keybrl.com/2018/images/lighted-poker2/20.jpg)

然后把焊咀放中间就可以一次熔两块了，然后把LED顺势插入，将中间的锡拨掉，整一整两个焊点的形状，完工。由于没有三只手，所以没有焊接时的照片...焊好后是这样的

![一个焊好](//blog-oss.keybrl.com/2018/images/lighted-poker2/21.jpg)

有几个注意事项。钢板和PCB板是有一段空隙的，所以两边的孔不能保证一插通过，要反复调整角度才能插进去，运气好时几秒，运气不好时半分钟，期间焊锡要保持熔化状态，会氧化。氧化太严重的话，就变得很粘稠，还有点想掉渣的感觉，就不容易弄出完美的形状，再想拿松香还原一下又很麻烦，所以动作尽量快。将管脚剪平似乎可以明显缩短摸索插入的时间，但是注意别为此弄反了正负极（还记得前面说过的判断正负的方法吗）

非常累，全部弄完长这样

![全部焊好](//blog-oss.keybrl.com/2018/images/lighted-poker2/22.jpg)

然后拿剪线钳把多余的管脚都剪了，注意剪的时候拿手指按住管脚末端或捏住，避免剪断瞬间断管脚飞起（否则你可能需要护目镜，10倍于断指甲的杀伤力）】

焊点真丑

![全部剪好](//blog-oss.keybrl.com/2018/images/lighted-poker2/23.jpg)

接上电源，翻过来试试能不能全部点亮

![全部剪好](//blog-oss.keybrl.com/2018/images/lighted-poker2/24.jpg)

看到一排排的灯，没有一个不亮的，异常兴奋呢。装上，拧好螺丝把！

![全部装好](//blog-oss.keybrl.com/2018/images/lighted-poker2/25.jpg)

## 完工

有了灯，怎么能不换一套透光键帽呢是吧

![键帽](//blog-oss.keybrl.com/2018/images/lighted-poker2/26.jpg)  
![完工](//blog-oss.keybrl.com/2018/images/lighted-poker2/27.jpg)

其实我还换了10颗彩色增补键，更可爱了

![完工](//blog-oss.keybrl.com/2018/images/lighted-poker2/28.jpg)

最后是灯效演示环节

<video controls="" preload="metadata" width="100%">
    <source src="//blog-oss.keybrl.com/2018/images/lighted-poker2/29.webm" type="video/webm">
    <p>Your user agent does not support the HTML5 Video element.</p>
</video>
