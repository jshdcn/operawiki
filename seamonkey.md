# SeaMonkey

SeaMonkey是一个免费的、跨平台的网页浏览器、邮件客户端、HTML编辑器和[IRC](irc.md)客户端。它完全符合HTML、[XML](xml.md)、CSS、DOM等现代标准，而且软件的源代码是完全开放的。官方版本可在[Linux](linux.md)、[Windows](windows.md)、[Mac](macos.md)下运行，也有志愿者将其移植到FreeBSD等平台。 与名声显赫的Netscape、Mozilla Suite一脉相承，是二者的后继产品。

## 分拆
Netscape自从1996年3月发布2.0版本起加入了电子邮件客户端，并且在3、4、（胎死腹中的5）、6、7版本中沿用了浏览器与客户端共用内核共用界面的产品模式。这一举动影响了相当一部分的浏览器，同年7月发布的[Opera](browser.md) 2.0也集成了简单的电邮客户端，并在7.0版本发扬光大成为[M2](m2.md)。而[Gecko](gecko.md)引擎最初的旗手Mozilla Suite同样采取了这种设计，Netscape的6、7两个版本就是基于Mozilla Suite。

网景最重要的竞争对手，微软，则是从一开始就分拆了Internet Explorer和Outlook Express。在IE强势时期兴起的浏览器厂商大多采用了这种模式，如KDE的Konqueror和KMail、GNOME的Galeon和Evolution、苹果的Safari和Mail、腾讯的TT浏览器和Foxmail。

网景方案的好处是明显的，浏览器和客户端具有很大的相似性，可以共享内核共享界面，节约磁盘空间和启动时间。但是微软方案则在灵活性上更胜一筹，人们可以自由选择采用相同或不同厂商的浏览器和客户端。

微软在浏览器大战中的胜利使得Mozilla这类产品必须同时面临两个强大对手的竞争。比这更严重的是，由于用户已经习惯于分开使用浏览器和客户端甚至根本不使用客户端，他们在遇到网络套件时往往会茫然不知所措。生不逢时，导致了Mozilla Suite叫好不叫座。在巨大压力面前，[Mozilla基金会](mozilla.md)终于决定分拆Mozilla Suite：

* 浏览器部分形成了[Mozilla Firefox](firefox.md)。还有一个使用Cocoa环境的Mac OS专版计划，名为[Camino](camino.md)；
* 邮件/新闻元件部分形成了[Mozilla Thunderbird](thunderbird.md)；
* 日历部分形成了Thunderbird的扩展Lightning；
* 此外还诞生了一些不由Mozilla提供官方支持的产品，包括网页编辑工具Nvu及其后继者KompoZer，以及Firefox的三个著名扩展：网页调试工具Firebug、IRC客户端ChatZilla和聚合器Sage。

## 独立
Firefox的快速发展影响了整个产业，也使得Mozilla基金会在短期内定下决心，抛弃Mozilla Suite。但是这个主张遭到了众多开发者和使用者的反对，在他们的坚持下，SeaMonkey专案诞生了。

由于Firefox已经大大完善了Gecko引擎和XUL扩展架构，SeaMonkey所要做的主要是将邮件客户端、网页编辑器和IRC客户端聚合进来，其中IRC部分直接采取了ChatZilla代码。2006年1月13日，SeaMonkey 1.0正式版面世。之后，由于Firefox进展神速，SeaMonkey陷入了1.0、1.1、1.5三个版本同时开发的苦战。1.5还处在Alpha阶段的时候，2.0又加入了进来。SeaMonkey最终只好决定跳过1.5直接开发2.0。

尽管Mozilla基金会不让他们使用Mozilla商标，SeaMonkey专案领导团体还是宣布：SeaMonkey 1.0就是Mozilla 1.8.0，SeaMonkey 1.1就是Mozilla 1.8.1，SeaMonkey 1.5即Mozilla 1.9，SeaMonkey 2.0即Mozilla 1.9.1。

Gecko大跃进之后，独立决策的SeaMonkey拒绝进行版本号的跃迁，但是在引入新内核方面却表现出了惊人的战斗力。在少获官方支持的情况下，还是快速地跟进了Firefox和Thunderbird的步伐。