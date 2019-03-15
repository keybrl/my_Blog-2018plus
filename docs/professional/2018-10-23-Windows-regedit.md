# Windows 常用注册表项

不知道为什么，每当涉及到 Windows 系统的的比较复杂的配置时，都会涉及注册表或者组策略的修改，由于 Windows10 Home 没有组策略编辑器，所以我们还是看看注册表吧

Windows 的注册表，有点像 Linux 的 `/etc` 文件夹，里面有各种奇奇怪怪的配置文件，而且 Windows 的明显要奇怪和反人类得多。所以才需要专门记录一下，以备不时之需

以下是本人平时遇到需要修改注册表时通过搜索引擎获得并搜集整理的一些注册表项的作用的记录，它们对于当时的 Windows 10 是有效的，理论上有可能会失效（特别是如果 Windows 10 还能苟很久的话）。如果你发现部分已经被移除了或者被永久转移了，可以在文章下方留言或者通过邮件联系我（邮箱在本站主页有）

---

首先是打开注册表编辑器的方法

- `Windows + R` 打开“运行”，输入 `regedit` ，回车
- 在“开始”菜单的搜索栏搜索“注册表编辑器”
- 问小娜

## 在文件资源管理器中的右键菜单

有时候可能因为安装无聊软件时忘了取消勾选什么，或者某些软件没卵用被卸载了，或者其他各种历史原因，右键菜单塞满了你不希望看见的选项，比如 “使用360强力删除”。修改或删除以下注册表项可以编辑你在文件资源管理器中的右键菜单。

- 右键文件 `HKEY_CLASSES_ROOT\`
  - 所有类型的文件 `*\shell\` 和 `*\shellex\ContextMenuHandlers\`
  - `.hhh` 类型的文件 `.hhh\shell\` 和 `.hhh\shellex\ContextMenuHandlers\` （一般不存在 `.hhh` ，这只是个代称，它可以是 `.mp4` 、 `.jpeg` ...）
- 右键文件夹 `HKEY_CLASSES_ROOT\Directory\`
  - 文件夹空白处 `Background\shell\` 和 `Background\shellex\ContextMenuHandlers\`
  - 文件夹图标 `shell\` 和 `shellex\ContextMenuHandlers\`

## 修改用户文件目录

Windows 默认的用户文件目录一般是这样的 C:\Users\username\ 。默认情况下这个 `username` ，如果是本地用户就是本地用户的用户名，创建用户时设置的；如果是 Windows 10 刚装好后第一次开机时按照指引登录了微软账户，那么会截取微软账户账号的前五个字母，比如说：我的微软账号是 `keyboard-l@outlook.com` 那么 Windows 10 会截取 `keybo` 作为用户目录的文件夹名，这十分扯淡。

开始的时候我是没什么所谓的，毕竟一般人也不会经常看见自己的用户目录，直到有一天我打开终端（CMD 或者 PowerShell）。终端的默认工作路径就在自己的用户目录（下图是已经改过来了）

![PowerShell](//blog-assets.keybrl.com/images/Windows-regedit/powershell.jpg)

那么如果用户目录不喜欢怎么办呢。首先需要修改注册表，修改系统的用户目录。

注册表路径 `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Profilelist` 下的各注册表的表项 `ProfileImagePath` 的值就是用户目录，找到自己用户那一个，修改为自己喜欢的，然后重启。重启后会提示用户目录不存在，因为原来的用户目录下的文件路径没变，去修改 C:\Users\ 下的文件夹名，再重启（或者注销），完成。

## 修改终端默认代码页

无论是使用 CMD 还是 PowerShell ，大家都会有一个烦恼，那就是中文时，默认字体是新宋体，虽然可以设置字体，但是可以选择的字体非常少。而且终端默认使用代码页 `936` ， GBK 编码，这时常导致麻烦。在终端输入 `chcp 65001` 可以将代码页切换到 UTF-8 编码的代码页，这时显示是英文，而且可以换各种英文字体，比如漂亮的 `Consolas` 。但是这样的修改是不可持久化的，下次再打开还是原来那样。所以有什么办法，修改默认的代码页呢，让它一启动就是代码页 `65001` 。

注册表 `HKEY_CURRENT_USER\Console\%SystemRoot%_System32_WindowsPowerShell_v1.0_powershell.exe` 下的 `CodePage` ，将 `936` 改为 `65001` 就可以了。不过这个只对 Windows + R 弹出“运行”对话框，输入 powershell ，这样打开的 PowerShell 有用。无论是对保存的 PowerShell 的快捷方式还是对右键 Windows 徽标中的 `Windows PowerShell` 都是无效的，目前我还没有找到解决方法。而且代码页 `65001` 也不是完美的，在 PowerShell 中，显示中文会只有一个字符宽（正常应该是两个字符宽），导致显示不全，在 CMD 中则没有这个问题，这个目前我也没有找到解决方法。
