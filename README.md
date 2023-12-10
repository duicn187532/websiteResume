# 建立各種網站作品
# 作品在Flask資料夾中
# 內有開發歷程
* 進度規劃:
  * 股價爬蟲&網站建立(done)
  * 員工登入&註冊頁面(done)
  * 會員系統建立(in progress)
  * 購物車系統建立
  * 員工採購網站
  * 會員制電商網站
  * 股價資料分析
  * 股價技術分析圖表
  * 自動交易程式
  * 企業形象網站
  * 根據使用者消費紀錄、消費者資訊演算推薦商品的機器學習系統

# 請執行app.py並開啟虛擬網址
# 目前股價網站已完成前端AJAX→後端爬蟲發送API→前端接收排版階段
* 開發歷程：
    * 112/11/5 從0開始
    * 11/06 嘗試使用pyscript失敗
    * 11/14 將股價網站相關資源加入flask框架
    * 11/15 將股價爬蟲代入flask將api發送json到前端
    * 11/16 解決發送json資料無法寫入iframe的bug
    * 11/17 新增股票分類&進行網頁排版
    * 11/18 建立員工註冊畫面&POST取得資料
    * 12/03 使用MongoDB資料庫，並將註冊資料存入資料庫
    * 12/09 將登入的帳號及密碼與資料庫做比對
