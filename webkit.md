# WebKit

WebKit是[Mac OS X](macos.md) v10.3及以上版本所包含的软件框架（对v10.2.7及以上版本也可通过软件更新获取）。 同时，WebKit也是Mac OS X的Safari的基础。WebKit是一个开源项目，主要由[KDE](https://userbase.kde.org/What_is_KDE/zh-cn)的[KHTML](https://userbase.kde.org/Glossary/zh-cn#KHTML)修改而来并且包含了一些来自苹果公司的一些组件。

传统上，WebKit包含一个网页引擎WebCore和一个脚本引擎JavaScriptCore，它们分别对应的是KDE的[KHTML](https://userbase.kde.org/Glossary/zh-cn#KHTML)和[KJS](https://userbase.kde.org/Glossary/zh-cn#KJS)。不过，随着[JavaScript](javascript.md)引擎的独立性越来越强，现在WebKit和WebCore已经基本上混用不分（例如[Chromium](chromium.md)和[Maxthon 3](maxthon.md)采用[V8](v8.md)引擎，却仍然宣称自己是WebKit内核）。

## 跨平台之路
苹果公司在设计WebKit之时加入了太多Mac OS X平台的独有事物，这给向其它系统的移植造成了很大障碍。不过，由于WebKit出色的开源特性，这些障碍正在被不断克服。

### Symbian
2005年，[诺基亚](nokia.md)的S60团队成为手机端WebKit的先驱，他们将WebKit框架移植到了Symbian S60平台，作为S60第三版的浏览器内核。

尽管这一浏览器颇为人诟病，但S60WebKit仍然是整个Symbian平台最重要的WebKit项目。

### iOS
2007年6月29日，iPhone上市，WebKit进入[iOS](ios.md)平台。按照苹果公司的规定，iOS平台所有浏览器均必须采用该[排版引擎](engine.md)。

包括[UC浏览器](ucweb.md)、[Opera Mini](opera-mini.md)、Firefox Home在内的后装浏览器为了打入iOS市场，均屈从了苹果公司这一规定。

直至2024年，为满足数字市场法案，iOS的17.4版本，才对欧盟地区开放了排版引擎选择权。

### Windows
2008年3月18日，Safari 3.1 for Windows转正，解决了[Windows](windows.md)平台下WebKit一直存在的部分兼容性问题。同年9月3日推出的Google Chrome使得这一平台进一步成熟。傲游浏览器自第3版开始使用WebCore和[Trident](trident.md)双内核设计，是首个采用这种设计的主流浏览器，其内核基于官方支持版本汇编。而[世界之窗](theworld.md)、[搜狗浏览器](sogouie.md)、[QQ浏览器](qqbrowser.md)、[360浏览器](360.md)等也纷纷跟随这一步伐，在自己的Windows版本中添加了WebKit引擎。

而在Windows Mobile战线，领先推出稳定版的是RIM旗下拓驰公司的Iris Browser。

Windows是除Mac OS X外另一个得到WebKit官方支持的版本。

### Linux
2008年10月22日投入市场的[Android]，其内置浏览器Google Chrome Lite是第一款[Linux](linux.md)平台的稳定版WebKit浏览器，能够与之并驾齐驱的是[webOS](webos.md)的内置浏览器。而到晚些时候，三星的bada，以及Android下浩如烟海的壳浏览器，也都是使用了WebKit内核。

而在桌面Linux战线，[Midori](midori.md)是多年来Linux下WebCore的主要开发者，自从GNOME和Google踏入这一领域后其地位饱受挑战。GNOME的[Epiphany](epiphany.md)自2.8版起采用了WebCore组件，而Google Chrome的Linux版也于2009年11月23日如期进入Beta，从而改变了Midori孤身奋战的局面。此后，[Flock](flock.md)也转向了WebKit内核。

尽管WebKit的原型K内核是由[Qt](qt.md)写成，但Linux下Chrome采用的却是GNU网络对象模型环境领导的WebKit/Gtk+（这种现象的原因之一在于[Objective-C](objective-c.md)和GTK+都是基于C语言，而Qt是基于C++）。随着奇趣科技于2008年6月被诺基亚收购，Qt方面也加快了WebKit的“回归”进程。[Arora](arora.md)和[Rekonq](https://userbase.kde.org/Rekonq/zh-cn)便是用QtWebKit写就。

## 应用
作为最早的WebCore浏览器，Safari长期保持Mac OS下最快浏览器的桂冠，它与新科状元Chrome的龙争虎斗也是WebCore世界最受瞩目的焦点。Google Chrome自2009年起已超过Safari成为WebCore内核市占率最高的浏览器，成为WebCore平台事实上的领导者，并且经常提出有益的修改。其首创的V8引擎和扩展机制大大丰富了WebCore阵营的选择。这使得2013年Blink的分叉变得顺理成章。