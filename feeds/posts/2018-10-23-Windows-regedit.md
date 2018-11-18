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

- 右键文件 ``HKEY_CLASSES_ROOT\`
  - 所有类型的文件 `*\shell\` 和 `*\shellex\ContextMenuHandlers\`
  - `.hhh` 类型的文件 `.hhh\shell\` 和 `.hhh\shellex\ContextMenuHandlers\` （一般不存在 `.hhh` ，这只是个代称，它可以是 `.mp4` 、 `.jpeg` ...）
- 右键文件夹 `HKEY_CLASSES_ROOT\Directory\`
  - 文件夹空白处 `Background\shell\` 和 `Background\shellex\ContextMenuHandlers\`
  - 文件夹图标 `shell\` 和 `shellex\ContextMenuHandlers\`
