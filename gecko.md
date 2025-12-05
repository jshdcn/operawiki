# Gecko

Gecko是[Mozilla](mozilla.md)全系产品及Netscape 6.0以上版本所使用的网页[排版引擎](engine.md)。

其最重要特色是完美支持XUL扩展系统。由于网景系一向喜欢把各种功能集成在统一界面，所以他们花费了很大精力构建了可扩展的内核架构。因此尽管Gecko不是最快的内核，却能够吸引到大批用户。由于其高扩展性，连媒体播放器Songbird和聊天软件Instantbird也采用了Gecko引擎，甚至它们还模仿了Mozilla的产品命名方式。

尽管理论上其它引擎也可以集成XUL或相似的扩展系统，但总不如Gecko设计精巧，至今没有生成真正的挑战者。反过来，Gecko引擎也可以不提供扩展系统。除了通用Gecko浏览器[Mozilla Firefox](firefox.md)和[Flock](flock.md)之外，为三个主要平台量身定制的浏览器——Linux的Galeon、Mac的[Camino](camino.md)和Windows的K-Meleon就不提供或只有象征性的扩展系统，但是却因为强化了速度和系统整合而受到了不少用户的青睐。

Gecko发展到1.9版本时，采用了[cairo](cairo.md)作为图形引擎，cairo是一个功能强大但系统要求很高的程序。这导致了使用这一版本Gecko引擎的软件无法支持当时市场占有率还超过1%的Windows 2000以下、Mac OS X v10.4以下所有版本。

Gecko发展到1.9.1版本时，更换了所采用的脚本引擎。引入了JIT的SpiderMonkey使JS执行效率倍增，是正式发布以来最显著的一次飞升。

近年来，随着[WebKit](webkit.md)内核的快速成长，Flock、[Epiphany](epiphany.md)等传统Gecko浏览器纷纷转投WebKit阵营。除了无人维护的几个小项目以外，Gecko基本上成为Mozilla的私家玩具。

痛定思痛的Mozilla于2011年掀起了大跃进运动。Gecko版本号从2.0直接升至5.0并高速向6.0、7.0、8.0演进。其目标似乎是效法Chrome的成功案例，但也导致Gecko阵营进一步分化，除Firefox、[Thunderbird](thunderbird.md)和[SeaMonkey](seamonkey.md)三大王牌之外的Gecko程序全部脱轨，为数众多的XUL扩展无法跟上最新版本的发布。

在城头变幻大王旗的移动市场，Gecko是最后一个到达的重量级玩家。Minimo已经与其赖以生存的WinMo双双归西。Fennec在Maemo出师得利，但Maemo却已日薄西山。在[Android](android.md)市场上只有用NDK写的Firefox孤军奋战，其主要竞争对手是用SDK写的[Opera Mobile](opera-mobile.md)。

在KHTML为世人所知时，Gecko已经开源并做到了更高的完成度。尽管如此，在需要一个浏览器内核的时候，苹果和Google仍然选择了分叉KHTML，理由是它拥有更清晰的代码架构。为了弥补这一不足，提升开发者吸引力以跟上Blink社团的节奏，Mozilla决定启动Servo项目重写内核，并为重写Servo内核专门创造了一门编程语言。这门语言的名字，叫作Rust。后来的故事众所周知，Rust成了编程界的当红小生，为包括Linux内核、AOSP在内的许多项目所接纳，Vivo的蓝河OS更是提出用Rust构建整个操作系统。而Servo却是门前冷落车马稀，它对Firefox Quantum的影响，仅限于贡献了CSS样式引擎Stylo，之后便无人问津了。