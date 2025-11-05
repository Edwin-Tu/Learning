# 📘 C 課程練習檔案說明

## assignment9.c
**主題：** 使用命令列引數  
**內容：**  
- 主函式宣告為 `int main(int argc, char *argv[])`  
- 程式檢查 `argc` 是否等於 3  
  - 若不是，顯示使用方式提示：`Usage: ./assignment9 Firstname Lastname`  
  - 若正確，輸出格式化訊息：`Hello, 名字 姓氏`  

---

## 編譯與執行方式

### Linux / MacOS
```bash
# 編譯
gcc assignment9.c -o assignment9

# 執行 (需帶參數)
./assignment9 Amber Lin

### Windows

# 編譯
gcc assignment9.c -o assignment9.exe

# 執行 (需帶參數)
assignment9.exe Amber Lin
