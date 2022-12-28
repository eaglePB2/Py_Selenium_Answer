
# Selenium 全自動答案輸入系統 （非100%準確率）
可以把它當成針對[http://etabc.tw/etest/](http://etabc.tw/etest/)的漏洞來自動輸入的測試系統，但目前沒有想要把它做到很完美的意思，僅供參考用，本人不對因使用該系統而發生的各種事情（包括但不限於：被其他人發現，因某問題導致你成績直接爆炸等）負責，我只是以教育性質和回報漏洞為目的而寫這份程式的。

**當然，等相關部門想到怎麼防這個系統的時候，我自然會直接存檔處理。 **

## 假設範圍
介於本人不是要把所有範圍都抓上來（畢竟漏洞捕捉方式也都差不多一摸一樣），因此這個系統只針對以下範圍：
- 測試網站為：http://etabc.tw/etest/default.asp?dt=1&db=3012 （是的，後面的dt和db都很重要）
- 默認資料如下（會魔改的自然會怎麼改，對吧awa）：
	- 班級：122；
	- 名字：測試用；
	- 座號：36 ；
	- 章節範圍：1-3012；
	- 挑選：100題；
	- 測驗時間：10分鐘；

## 前置安裝
你需要pip 安裝兩個bundle：
Selenium — 就是這個程式的重大核心，也是用來打開網頁，找關鍵字，輸入答案，按按鈕的重要工具
`pip install selenium`

webdriver-manager — 用來支援Selenium可以打開Chrome, Firefox, Internet Explorer, Opera, Brave, 和 Edge遊覽器
`pip install webdriver-manager`

## 效果預覽
https://youtu.be/zrECA0TBI4M

## 參考文獻

_How to automate filling in web forms with python using selenium_. LambdaTest. (2022, November 7). Retrieved December 28, 2022, from https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/

Muthukadan, B. (2018). _7. Webdriver API¶_. 7. WebDriver API - Selenium Python Bindings 2 documentation. Retrieved December 28, 2022, from https://selenium-python.readthedocs.io/api.html
