# 📘 C 課程練習檔案說明

## assignment3.c
**主題：** 使用字元陣列讀取使用者輸入  
**內容：**  
- 宣告固定長度的字元陣列 (`char first[20]; char last[20];`)  
- 使用 `scanf("%s", &first)` 與 `scanf("%s", &last)` 接收名字與姓氏  
- 輸出格式化的歡迎訊息：`Hello 名字 姓氏!`  

## assignment3-extra.c
**主題：** 嘗試使用指標方式讀取字串  
**內容：**  
- 宣告 `char *first; char *last;` 作為指標  
- 使用 `scanf` 嘗試將輸入存入指標  
- 輸出格式化訊息：`Hello 名字 姓氏!`  
- 嘗試 `free(first)` 與 `free(last)`  
