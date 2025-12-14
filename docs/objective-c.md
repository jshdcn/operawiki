# Objective-C

**Objective-C**，通常写作**Obj-C**，是扩充C的面向对象编程语言。它主要使用于[Mac OS X](macos.md)和GNUstep这两个使用OpenStep标准的系统，而在NeXTSTEP和OpenStep中它更是基本语言。Objective-C可以在gcc运作的系统写和编译，因为gcc含Objective-C的编译器。

## 历史

1980年代初布莱德·确斯在其公司Stepstone发明Objective-C。他对软体设计和编程里的真实可用度问题十分关心。

对Objective-C最主要的描述是他1986年出版的《Object-oriented Programming, An Evolutionary Approach》。

## 语言分析

Objective-C是非常「实际」的语言。它使用一个用C写成、很小的运行库，只会令应用程式的大小增加很小，与此相比，大部分OO系统需要极大的运行时虚拟机来执行。ObjC写成的程式通常不会比其原始码和函式库（通常无需包含在软体发行版本中）大太多，不会像Smalltalk系统，即使只是打开一个窗口也需要大量的容量。由于Obj-C的动态类型特征，Obj-C不能对方法进行内联一类的优化，使得Obj-C的应用程序一般比类似的C或C++程序更大。

Obj-C可以在现存C编译器基础上实现（在GCC中，Obj-C最初作为预处理器引入，后来作为模块存在），而不需要编写一个全新的编译器。这个特性使得Obj-C能利用大量现存的C代码、库、工具和编程思想等资源。现存C库可以用Obj-C包装器来提供一个Obj-C使用的OO风格界面包装。

以上这些特性极大地降低了进入Obj-C的门槛，这是1980年代Smalltalk在推广中遇到的最大问题。

Objective-C的最初版本并不支持垃圾回收。在当时这是争论的焦点之一，很多人考虑到Smalltalk回收时有漫长的「死亡时间」，令整个系统失去功用，Objective-C为避免此问题才不拥有这个功能。某些第三方版本加入了这个功能（尤是GNUstep）, Apple也在其[Mac OS X](macos.md) 10.5 中提供了实现。

另一个广受批评的问题是ObjC不包括命名空间机制（namespace mechanism）。取而代之的是程式设计师必须在其类别名称加上前缀，由于前缀往往较短（相比命名空间），这时常引致冲突。在2007年，在Cocoa编程环境中，所有Mac OS X类别和函式均有「NS」作为前缀，例如NSObject或NSButton来清楚分辨它们属于Mac OS X核心；使用「NS」是由于这些类别的名称在NeXTSTEP开发时定下。

虽然Objective-C是C的严格超集，但它也不视C的基本型别为第一级的对象。

和C++不同，Objective-C不支持运算子多载（它不支持ad-hoc多型）。亦与C++不同，但和Java相同，Objective-C只容许物件继承一个类别（不设多重继承）。Categories和protocols不但可以提供很多多重继承的好处，而且没有很多缺点，例如额外执行时间过重和二进制不兼容。

由于Obj-C使用动态运行时类型，而且所有的方法都是函数调用（有时甚至连系统调用(syscalls)也如此），很多常见的编译时性能优化方法都不能应用于Obj-C（例如：内联函数、常数传播、交互式优化、纯量取代与聚集等）。这使得Obj-C性能劣于类似的对象抽象语言（如C++）。不过Obj-C辩护者认为既然Obj-C运行时消耗较大， Obj-C本来就不应应用于C++或Java常见的底层抽象。