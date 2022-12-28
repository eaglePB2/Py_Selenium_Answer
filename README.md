# Selenium 全自动答案输入系统 （非100%准确率）
可以把它当成针对[http://etabc.tw/etest/](http://etabc.tw/etest/)的漏洞来自动输入的测试系统，但目前没有想要把它做到很完美的意思，仅供参考用，本人不对因使用该系统而发生的各种事情（包括但不限于：被其他人发现，因某问题导致你成绩直接爆炸等）负责，我只是以教育性质和回报漏洞为目的而写这份程式的。

**当然，等相关部门想到怎么防这个系统的时候，我自然会直接存档处理。**

## 假设范围
介于本人不是要把所有范围都抓上来（毕竟漏洞捕捉方式也都差不多一摸一样），因此这个系统只针对以下范围：
- 测试网站为：http://etabc.tw/etest/default.asp?dt=1&db=3012 （是的，后面的dt和db都很重要）
- 默认资料如下（会魔改的自然会怎么改，对吧awa）：
	- 班级：122；
	- 名字：测试用；
	- 座号：36 ；
	- 章节范围：1-3012；
	- 挑选：100题；
	- 测验时间：10分钟；

## 前置安装
你需要pip 安装两个bundle：
Selenium — 就是这个程式的重大核心，也是用来打开网页，找关键字，输入答案，按按钮的重要工具
`pip install selenium`

webdriver-manager — 用来支援Selenium可以打开Chrome, Firefox, Internet Explorer, Opera, Brave, 和 Edge游览器
`pip install webdriver-manager`
