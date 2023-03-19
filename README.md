# Selenium 全自動答案輸入系統 （100%準確率）
可以把它當成針對[http://etabc.tw/etest/](http://etabc.tw/etest/)的漏洞來自動輸入的測試系統，但目前沒有想要把它做到很完美的意思，僅供參考用，本人不對因使用該系統而發生的各種事情（包括但不限於：被其他人發現，因某問題導致你成績直接爆炸等）負責，我只是以教育性質和回報漏洞為目的而寫這份程式的。

**當然，等相關部門想到怎麼防這個系統的時候，我自然會直接存檔處理。 **

## 假設範圍
介於本人不是要把所有範圍都抓上來（畢竟漏洞捕捉方式也都差不多一摸一樣），因此這個系統只針對以下範圍：
- 測試網站為：http://etabc.tw/etest/default.asp?dt=1 （是的，後面的dt很重要）
- 目前支援輸入題庫（僅限2000和3000）、名字、班級、座號、最大範圍、作答時間以及題目數量。


## 前置安裝
你需要pip 安裝兩個bundle：  
Selenium — 就是這個程式的重大核心，也是用來打開網頁，找關鍵字，輸入答案，按按鈕的重要工具  
```
pip install selenium
```

webdriver-manager — 用來支援Selenium可以打開Chrome, Firefox, Internet Explorer, Opera, Brave, 和 Edge遊覽器  
```
pip install webdriver-manager
```

## 效果預覽
https://youtu.be/zrECA0TBI4M

## 延伸想法
~~1. 有沒有辦法用別的方式，來提高準確率呢？
（提示：測驗頁面有一個 “🔈” 按鈕，當你滑鼠經過的時候就會發音的那種。 但我發現到他的檔案名居然就是答案，有沒有辦法用Selenium把那個喇叭的html tag挖出來，並且採用split原理抓出那個答案，然後直接丟進答案欄裡面呢？ 而且這樣也完全不需要brute force攻擊了，時間複雜度瞬間優化成`O(1)`。）~~  
~~2. 如果有錯誤的話，該如何自動化訂正的頁面呢？~~

**上述問題我已經解決並釋出解答了，各位可以參考參考。**

## 參考文獻

_How to automate filling in web forms with python using selenium_. LambdaTest. (2022, November 7). Retrieved December 28, 2022, from https://www.lambdatest.com/blog/how-to-automate-filling-in-web-forms-with-python-using-selenium/

Muthukadan, B. (2018). _7. Webdriver API¶_. 7. WebDriver API - Selenium Python Bindings 2 documentation. Retrieved December 28, 2022, from https://selenium-python.readthedocs.io/api.html

## 一些酷酷的……徽章？
虽然我没拿过任何的软体来检测各种安全病毒什么鬼的，但还是谢咯  
[![Security Status](https://www.murphysec.com/platform3/v3/badge/1609745945815502848.svg)](https://www.murphysec.com/accept?code=7591fc7a6d5fa48571ada882d2d1348d&type=1&from=2&t=1)
