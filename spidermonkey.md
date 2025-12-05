# SpiderMonkey

众所周知，JavaScript是1995年由网景发明的语言。最早的脚本引擎，自然也可以追溯到网景浏览器。

但早期的JavaScript，不管网景的原版还是微软的山寨版，都是解释执行的，这给人留下了JavaScript是一门解释型语言的根深蒂固的印象。作为开源社区，自然也没有动力去改变什么。

直到2008年，Google用V8引擎告诉我们，JS是可以编译执行的。整个浏览器界忽然茅塞顿开，纷纷将JIT引入自己的脚本引擎。而Mozilla的SpiderMonkey也是在这个时候浮出水面，尽管它作为内部开发代号可能已经存在了12年。在JavaScript原作者布兰登·艾克的领导下，Mozilla仅用了10个月就随Gecko 1.9.1发布了带有JIT的SpiderMonkey，内部代号TraceMonkey。

有了更快的JavaScript之后，Mozilla相继启动了众多项目，如：

* popcorn.js，一个HTML5视频播放框架；

* orbx.js，一个HTML5视频解码器；

* vtt.js，一个WebVTT实现，看视频的时候有字幕；

* pdf.js，用浏览器打开PDF文件而无需安装插件；

* asm.js，将高级语言编译为可执行的JavaScript，后来被标准化成了WebAssembly。

相当一部分功能，已经被内化到了Firefox等软件中，这大大改变了浏览器的开发模式，一些原本需要通过原生代码或XUL开发的功能，可直接用JS编写并获得还不错的执行效率。从而大大削弱了老牌浏览器的生态优势，轻便而独特的新一代浏览器雨后春笋般涌现出来。