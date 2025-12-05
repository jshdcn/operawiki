# 排版引擎

排版引擎也被称为渲染引擎或样板引擎，它负责取得网页的内容（HTML、[XML](xml.md)、图像等）、版式信息（CSS、XSL等），以及计算网页的显示方式，然后会输出至显示器或打印机。所有网页浏览器、电子邮件客户端以及其它需要编辑、显示网络内容的应用程序都需要排版引擎。

## 历史

"排版引擎"这个词汇的广泛使用，源于Mozilla社团。网景开源之后，其赖以成功的排版技术被称为Mariner，而Mozilla放弃了Mariner，重新设计了自己的排版引擎Gecko。作为独立于浏览器的一个配件，除了Mozilla浏览器，其它浏览器也可以使用Gecko作自己排版引擎。IE也把自己的排版引擎称为Trident，用在很多Windows的应用程序上。

KDE率先将其脚本引擎和网页引擎相区别，分别称为KJS和KHTML。而到了苹果则更进一步，不仅区分开了JSCore和WebCore，还给它们起了一个总称WebKit。其他各家纷纷仿效，也将自己的脚本引擎单独命名，如Opera的Futhark、Google的V8等。

Opera则提出了三引擎的概念，即网页引擎、脚本引擎和图形引擎，并将其图形引擎命名为Vega。虽然Mozilla和KDE的图形引擎也有自己的名字，但他们并未采用三引擎的提法。

Mozilla最先提出四引擎，即网页引擎、样式引擎、脚本引擎和图形引擎，除脚本引擎是Monkey系列以外，另外三个Gecko、Stylo、cairo发音倒很相近。

## 功能

排版引擎的作用是相似的，将网页原始码通过运算组织成型得到人类可辨识的图像。但各家所采取的算法则各不相同，例如在低速网络环境下展现网页，Trident是按行从上至下显示，Gecko是按元素载入次序显示内容，Presto是先显示文字部分，再将多媒体内容插入文字之间，而KHTML则是在计算完成后，一股脑显示整页，WebCore与Presto相似，只是会预留多媒体元素的位置而不会打乱文字的排布。各家各派排版引擎的算法差异，也导致了用户体验和展现速度在不同位置取得平衡。

## 网页引擎

网页排版引擎是排版引擎的一种，用于对HTML代码进行版式编排使之以人类易于辨识的图像形式显示出来。

在旧时，因为网页基本上只包含HTML，所以网页排版引擎通常与排版引擎混用不分。直至KDE的Konqueror计划中开始区分KHTML和KJS，首次提出了脚本引擎的概念，但其时脚本引擎与网页引擎仍然基本上是一一对应的关系。再后来随着OmniWeb 5.5和Google Chrome的发布，才出现了网页排版引擎和脚本引擎的交互搭配。

下表列举了一些常见的网页排版引擎。

### 图形界面

* Cobra（基于Java）
* Lobo
* [Gecko](gecko.md)（[Mozilla Firefox](firefox.md)、[Camino](camino.md)、Mozilla和网景导航者 6.0及以上）
* GtkHTML（Novell Evolution及其他GTK+程序）
* HTMLayout（作为Windows Mobile的嵌入式组件）
* KHTML（Konqueror）
* WebCore（Safari、[Arora](arora.md)、[Midori](midori.md)、[OmniWeb](omniweb.md) 4.5及以上、Shiira、[iCab](icab.md)、Google Chrome和Epiphany 2.8及以上）
* Blink
* NetFront（爱可信NetFront）
* NetSurf
* [Presto](presto.md)（Opera 7.0及以上、Macromedia Dreamweaver MX & 2004（Mac）和Adobe Creative Suite 2）
* Prince XML
* Robin（The Bat!）
* Tasman（Mac OS版的Internet Explorer和Microsoft Outlook）
* [Trident](trident.md)（Internet Explorer、Internet Explorer shell和部分媒体播放器）
* EdgeHTML
* Tkhtml（hv3）

### 文字界面

* Lynx
* Links
* W3m

### 不复存在

* [Elektra](elektra.md)（Opera 3.5~6.1）
* Mariner（Netscape 1~5）
* iCab（iCab 1~3）

## 脚本引擎

脚本引擎则是自从Konqueror项目区分KHTML和KJS之后提出的概念，用于表示对网页中JavaScript及相关技术进行计算并展示的程序代码。一称JavaScript虚拟机。

下表展示了一些常见的脚本引擎。

* Carakan（Opera 10.5及以上）
* KJS（Konqueror）
* JavaScriptCore（OmniWeb 4.5及以上）
* SquirrelFish（Safari 4.0及以上）
* V8（Google Chrome）
* [SpiderMonkey](spidermonkey.md)（Mozilla Firefox 3.5及以上）

## 图形引擎

图形引擎的概念是由Opera首先提出，将其SVG渲染引擎称之为Vega。而Mozilla SVG Project则采用了开源的cairo图形引擎。

下表展示了一些常见的图形引擎。

* cairo（Mozilla Firefox 3.0及以上）
* KSVG（Konqueror）
* [Vega](vega.md)（Opera 10.1及以上）