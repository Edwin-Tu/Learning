
# 🧭 虛擬化與駭客攻防環境建置 README

> 匯整自上傳的六份簡報（虛擬化網路管理、Kali 環境簡介、Linux CLI、駭客攻擊工具、駭客攻擊演練、攻防 Lab 演練）。

---

## 📘 一、虛擬化網路管理 (摘錄)
參考來源：虛擬化網路管理【12†虛擬化網路管理】

- 四種 VirtualBox 網路模式：NAT、Bridged、Host-Only、Internal Network  
- 常用檢查指令：
  - Windows：`ipconfig`、`ping <IP/網址>`、`tracert <網址>`
  - Linux：`ip a`、`ping -c 3 <IP/網址>`、`tracepath <網址>`

---

## 🐉 二、Kali 環境快速上手 (摘錄)
參考來源：Kali 環境簡介【13†Kali 環境簡介】

- 原則：**僅在授權環境進行測試**，記錄操作，避免違法。
- 快速測試指令範例：
  - `ping 8.8.8.8`
  - `ip a` / `ifconfig`
  - `traceroute google.com`
  - `nslookup yahoo.com`

---

## 🧩 三、Linux 與 CLI 重點 (摘錄)
參考來源：Linux 環境與 CLI 介面【14†Linux 環境與 CLI 介面】

- 基本檔案/資料夾操作：`mkdir`、`mv`、`cp`、`rm`、`ls -a`
- 管線與文字處理：`sort`、`uniq`、`wc -l`、`less`
- 權限與 sudo：`sudo apt update`、`sudo cat /etc/shadow`（需權限）
- 編輯器：`nano` (Ctrl+O 存檔, Ctrl+X 退出)、`vim` (`:wq`)

---

## 🧰 四、駭客攻擊工具 (摘錄)
參考來源：駭客攻擊工具【15†駭客攻擊工具】

- 推薦在 Lab 內建立兩台 VM：Kali (攻擊機)、Ubuntu (靶機)，兩台 VM 加入 Host-Only 網卡 做內網測試。
- Kali 常用安裝指令：
```bash
sudo apt update
sudo apt install -y zaproxy netcat-openbsd wireshark john wordlists
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz || true
sudo usermod -aG wireshark $USER
```
- Ubuntu (靶機) 建立簡單受保護的測試網頁：
```bash
sudo apt update
sudo apt install -y apache2 openssh-server apache2-utils
sudo mkdir -p /var/www/html/secure_folder
sudo htpasswd -bc /var/www/html/secure_folder/.htpasswd testuser password123
echo "<h1>This is a secure page.</h1>" | sudo tee /var/www/html/secure_folder/index.html
sudo systemctl restart apache2
```

---

## ⚔️ 五、駭客攻擊演練 — 完整指令總覽（詳細版）
參考來源：駭客攻擊演練【16†駭客攻擊演練】

> 下列內容為實作步驟與範例指令。**請務必只在授權環境或實驗網段上執行。**

### A. 虛擬機與網路準備
- 在 VirtualBox 建立兩台 VM（Kali、Ubuntu）。
- Network 設定建議：
  - 介面卡1：NAT（VM 可上網，用於更新套件）
  - 介面卡2：Host-Only（實驗網段，用於攻防互測）
- 建立 Host-Only 網卡（VirtualBox → 檔案 → 主機網路管理員），啟用 DHCP 或手動設定 IP：
  - 範例手動設定（在 Ubuntu/Kali 內）：
```bash
sudo ip addr add 192.168.56.105/24 dev enp0s3    # ubuntu (靶機)
sudo ip addr add 192.168.56.106/24 dev enp0s3    # kali (攻擊機)
```

### B. Kali 基本安裝與環境調整
```bash
# 更新與安裝常用工具
sudo apt update
sudo apt install -y zaproxy netcat-openbsd wireshark john hydra dirb nikto

# rockyou 字典（若為壓縮檔）
sudo gzip -d /usr/share/wordlists/rockyou.txt.gz || true

# 允許非 root 使用 wireshark（登入後重新啟動 session）
sudo dpkg-reconfigure wireshark-common
sudo usermod -aG wireshark $USER
newgrp wireshark
```

### C. Ubuntu (靶機) 服務設定（示範 Apache + Basic Auth）
```bash
sudo apt update
sudo apt install -y apache2 apache2-utils
sudo mkdir -p /var/www/html/secure_folder
sudo htpasswd -bc /var/www/html/secure_folder/.htpasswd testuser password123
sudo sh -c 'echo "<h1>Secure page</h1>" > /var/www/html/secure_folder/index.html'

# 建立 Apache 設定（可選）
sudo sh -c 'cat <<EOF > /etc/apache2/sites-available/secure_folder.conf
<VirtualHost *:80>
    DocumentRoot /var/www/html
    <Directory /var/www/html/secure_folder>
        AuthType Basic
        AuthName "Restricted Content"
        AuthUserFile /var/www/html/secure_folder/.htpasswd
        Require valid-user
    </Directory>
</VirtualHost>
EOF'

sudo a2dissite 000-default.conf || true
sudo a2ensite secure_folder.conf
sudo a2enmod auth_basic
sudo systemctl restart apache2
```

### D. 掃描 (nmap) 範例與解讀
- 快速 TCP SYN 掃描（無 ping）：  
```bash
sudo nmap -sS -Pn -T4 -oN scan_quick.txt 192.168.56.105
```
- 服務與 OS 偵測（詳細）：  
```bash
sudo nmap -sS -sV -O --osscan-guess -oN scan_ver_os.txt 192.168.56.105
```
- UDP 掃描特定埠：  
```bash
sudo nmap -sU -p 53,123,161 -oN scan_udp.txt 192.168.56.105
```
**說明**：
- `-sS`：SYN stealth 掃描  
- `-Pn`：不執行 ping 掃描（對防火牆環境有用）  
- `-T4`：加速掃描（注意網路影響）  
- `-sV`：服務版本偵測，協助找已知漏洞  
- `-O`：作業系統指紋偵測

### E. 目錄掃描 (dirb / nikto)
- 使用 dirb 掃 common paths：
```bash
dirb http://192.168.56.105 /usr/share/dirb/wordlists/common.txt -o dirb_report.txt
```
- 使用 nikto 做 web vuln 掃描：
```bash
nikto -h http://192.168.56.105 -output nikto_report.txt
```

### F. 密碼破解 (hydra) 範例
- HTTP basic auth 爆破（將 `-s` 改成實際 port，若為 80 可省略）：  
```bash
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt 192.168.56.105 http-get /secure_folder/
```
- SSH 爆破（範例）：  
```bash
hydra -L users.txt -P /usr/share/wordlists/rockyou.txt ssh://192.168.56.105 -t 4
```
**注意**：大規模爆破會對網路與主機造成負擔，實驗時請控制速率與並行數 (`-t`)，並取得授權。

### G. 手動驗證 / curl 測試
- 未驗證頁面（GET）：
```bash
curl -i http://192.168.56.105/secure_folder/
```
- Basic Auth 驗證：
```bash
curl -i --user testuser:password123 http://192.168.56.105/secure_folder/
```

### H. 封包擷取 (tshark / wireshark)
- 使用 tshark 抓取 HTTP 的封包：
```bash
sudo tshark -i any -f "host 192.168.56.105 and tcp port 80" -w http_traffic.pcapng
```
- 在 Wireshark GUI 中選擇 interface `any` 或 `vboxnet0`，使用 `http` 或 `tcp.port==80` 過濾器觀察資料。

### I. 自動掃描工具 (ZAP)
- 使用 ZAP CLI 做快速掃描並輸出報告：
```bash
zaproxy -cmd -quickurl http://192.168.56.105/secure_folder/ -quickout ~/zap_report.html
```
或帶 Basic Auth 的 URL：
```bash
zaproxy -cmd -quickurl http://testuser:password123@192.168.56.105/secure_folder/ -quickout ~/zap_report.html
```

### J. 記錄與截圖
- 每個主要步驟請截圖保存（nmap 輸出、hydra 結果、tshark pcap、ZAP 報告等），並歸檔於 `/home/<user>/LabResult/`。

### K. 常見問題與排除
- 若 nmap 沒有回應，檢查 Host-Only IP 是否正確 (`ip a`) 並確認防火牆（`sudo ufw status`）。
- 若 web 頁面顯示 403/401，檢查 `.htpasswd` 是否正確與 Apache/Nginx 設定。
- 若 Wireshark 無封包，確認抓取介面是否為 `vboxnet0` / VirtualBox host-only 網卡。

---

## 🧾 六、攻防 Lab 演練（摘錄）【17†攻防 Lab 演練】
- 建議在 NAT 網路上統一管理（用於上網），並將 Host-Only 做為內網攻防測試網段。  
- Kali 建議分配多核心（電腦核心的一半以上）以加速工具運作。

---

## 🔒 法律與倫理注意事項
- 僅在有**明確授權**的環境（課程靶機、企業資安測試網段、實驗室）執行上述測試。  
- 未經許可掃描或攻擊第三方系統可能觸犯法律。

---

## ✅ 檔案來源（節錄）
- 虛擬化網路管理（上傳簡報）【12†虛擬化網路管理】  
- Kali 環境簡介（上傳簡報）【13†Kali 環境簡介】  
- Linux 環境與 CLI（上傳簡報）【14†Linux 環境與 CLI 介面】  
- 駭客攻擊工具（上傳簡報）【15†駭客攻擊工具】  
- 駭客攻擊演練（上傳簡報）【16†駭客攻擊演練】  
- 攻防 Lab 演練（上傳簡報）【17†攻防 Lab 演練】

---

請妥善保存此 `README.md` 作為實驗指引與繳交說明。
