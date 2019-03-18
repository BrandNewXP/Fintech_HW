# Fintech_HW1

## ETF_Crawler
### 1. 你選擇用甚麼樣的套件來做網路爬蟲?為什麼要用這個套件
* requests，因為要爬Yahoo Finance的資。YF提供自選時間段跟ETF類型的歷史資料下載，所以直接餵URL拿資料。
* jupyter notebook跟pandas分別拿來做coding和dataframe。 
### 2. 請用流程圖的方式告訴我們你是怎麼抓到你的目標資料，流程圖的畫法不拘，主要易懂就好
![image](https://github.com/BrandNewXP/Fintech_HW1/blob/master/files/Crawler.png)
* 更詳細的流程看程式註記。
### 3. 至少設想並列出 5 種當別人使用你的程式最有可能會遇到的錯誤情況，並提供解決辦法
#### 1. ipynb怎麼開？
* 下載ipython notebook，執行ipython notebook xxx.ipynb，或是下載jupyter notebook後執行。
#### 2. 歷史資料無法下載下來。
* 測試階段網址還沒出現過錯誤（雖然不保證不會出錯）可以先檢查網路連線
#### 3. 為什麼資料有NaN？
* 因為Yahoo Finance上沒有資料。
#### 4. 資料時間段有問題。
* 程式抓的是2015/12/31到現在系統時間的區段，你的系統時間可能不正確。 
#### 5. STEP 2的function好像沒有用到？
* 對，因為他只是測試抓資料沒問題的測試函式

## TED_Crawler
### 1. 如果用MAC OS遇到

    urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1056)
就要執行下面的指令，Python資料夾的名稱根據版本而定。HTTPError: HTTP Error 500: Internal Server Error

    Macintosh HD > Applications > Python3.7 > 執行Install Certificates.command
### 2. 如果遇到

    HTTPError: HTTP Error 500: Internal Server Error
關掉Chrome重新執行程式
