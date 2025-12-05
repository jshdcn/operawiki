# Yoono

Yoono是一个社交扩展，现可用于Chrome、Firefox、[SeaMonkey](seamonkey.md)（称附加组件）和IE（称加载项）。就浏览器而论，粗略地说它安装在Firefox上的效果可以相当于Flock；就扩展而论，Yoono大约是Meebo、[Xmarks](xmarks.md)、Twitterfox、Facebook Toolbar等的集合体。在一个侧边栏中支持多种聊天协议、微博客、社交网站乃至书签同步。曾在很长时间内成为Firefox官方推荐的社交扩展。

无论是否注册帐号，其数据流量皆需通过Yoono服务器。非注册用户也会由网站分配给Cookie帐号，但有些功能如书签同步，还是只有注册用户能够享受得到。

Yoono声称尽可能地不将用户信息存放于服务器端，如果一项服务提供第三方登录系统，如Facebook、Twitter，他们就会采用。虽然如此，在IM等功能中，Yoono仍然需要将帐号密码在服务器端进行设置，因此上线时与浏览器本身被认为是不同客户端。即使是提供第三方登录系统的服务，也不能实现自动同步登录，这点类似Facebook Toolbar，而与Flock的处理逻辑是正好相反的。禁止多点登录的通讯协议如AIM，会禁止Yoono和浏览器同时登录，但浏览器登出后，Yoono可以继续在线，这是它已经把帐号密码寄存在服务器的缘故。

Yoono的另一项功能是搜索，使用方法与IE8的加速器类似。搜索结果来源于维基百科、Google自定义搜索、OneRiot等，OneRiot是一个实时搜索引擎，也提供自己的浏览器扩展。Yoono的搜索可以在当前页面用一个iframe预览，更多结果用新建页面打开，不影响正在进行的操作。

Yoono功能以AJAX技术为主，可以不依赖Adobe Flash Player，但启动时会被Flashblock报出。