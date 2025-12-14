# Opera蜻蜓

[Opera浏览器](browser.md)内置的网页调试工具，与Firebug相似。可以帮助用户分析网页结构，计算渲染效果。

蜻蜓是[Opera](asa.md)历史上第一个核心的开源组件，但是本地端功能有限，初次使用时需要从网络上下载配套组件才能使用。其alpha版随[Opera](browser.md) 9.5释出，并在此后保持了与浏览器不同的发行周期。Opera蜻蜓可以自更新。

Opera蜻蜓和Opera浏览器之间的接口叫作Scope传输协议。理论上[Presto](presto.md) 2.1以上的浏览器都可以与蜻蜓配合使用，但是至今尚未在[Opera Mobile](opera-mobile.md)上找到合适的UI设计方案。

转投Blink后，Opera不再开发蜻蜓，代之以[Chromium](chromium.md)自带的DevTools。