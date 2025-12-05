# XMPP

eXtensible Messaging and Presence Protocol，是一个已成为IETF标准，全球使用人口最多的即时通讯协议。最初由Jabber公司（被思科收购）开发，在标准化以前称为Jabber协议，后公开发布并由XMPP标准基金会实现标准化。主要由RFC 6120定义，IETF的标准都是可以免费使用的。

XMPP的特点是其数据完全由XML编写，并可以充分扩展。由于XMPP具有实时通知的能力，Google使用它作为技术基础为旗下的Android用户提供C2DM消息推送服务。

每个域名都可以开放XMPP服务并分发登录ID，客户端凭借此ID登录，通过服务器之间的互通与其它域名下的ID进行对谈，甚至不采用XMPP协议的通讯网络也可以通过XMPP网关与XMPP网络通讯。更有趣的是，每个域名都可以自由选择实现或不实现其中的某项功能。

尽管2004年即成为国际标准，但在Google Talk大面积推广之前，只有不到100万用户。Gtalk的出现不仅使XMPP用户迅速扩张到千万级、亿级，更使得许多新兴科技公司争相效法，包括Facebook、VKontakte、校内发布的即时聊天工具都采用了XMPP。目前服务商对XMPP的实现主要分以下几种：

支持泛Jabber登录，支持泛Jabber互通：站长开放泛Jabber互通的Gtalk（如Gmail域名）、LiveJournal、WordPress、[Nimbuzz](nimbuzz.md)、Ovi Chat（已废弃）

支持泛Jabber登录，但不与其它网络互通：Facebook Chat、VKontakte IM、校内通、Zoho Chat

不支持泛Jabber登录，只能与选定的Jabber网络互通：网易泡泡（与Gmail域名互通）、站长不开放泛Jabber互通的纯Gtalk（如AppSpot域名，与Gtalk互通）

本身不是Jabber协议，但能与选定的Jabber网络互通：AIM（与Gtalk互通）、雅虎通（与Ovi互通）

本身不是即时通讯网络，但经过配置能够通过XMPP网络传输：Twitter DM、新浪微博私信

XMPP最有希望继万国邮政、PSTN、Email之后，成为第四个十亿级用户网络。