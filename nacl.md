# NaCl

Native Client是[Google](google.md)的虚拟机计划，提供了一套类POSIX环境，能够将本地程序植入网页，与[WAC](wac.md)、[WebAPI](webapi.md)有一定的竞争关系。

其特点是代码能够用C或C++编写（并分别执行在[Linux](linux.md)、[Mac](macos.md)、[Windows](windows.md)上），因此其实现依赖于Google公司对特定平台的支持。

Google Chrome从第14版起正式加入了NaCl支持。