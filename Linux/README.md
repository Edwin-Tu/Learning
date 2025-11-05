# 使用 Windows 連線 Hack The Box 靶機指南

## 📘 背景說明

本專案記錄了在 **Windows 環境學習 Linux 與資安操作** 的過程。由於 Hack The Box (HTB) 平台提供了大量靶機（Target Machines）與教學實驗室，使用者需要透過 **VPN 連線 (.ovpn 檔案)** 才能進入 HTB 的私有網路。

由於我目前在 Windows 上進行練習，因此需安裝 **OpenVPN** 並使用 HTB 官方提供的 `.ovpn` 設定檔來建立連線，使本機能與 HTB 靶機互通。

---

## ⚙️ 操作流程

### 1. 下載並安裝 OpenVPN
1. 前往 [OpenVPN 官方網站](https://openvpn.net/community-downloads/)
2. 選擇適合你的 Windows 版本（通常為 64-bit Installer）
3. 下載後執行安裝，並確認勾選：
   - **OpenVPN GUI**
   - **Add OpenVPN to PATH**

---

### 2. 下載 HTB 的 `.ovpn` 檔案
1. 登入你的 [Hack The Box 帳號](https://app.hackthebox.com/)
2. 點擊右上角的個人頭像 → **VPN**
3. 在「Connection Packs」中選擇：
   - 伺服器地區（建議選擇距離自己最近的地區）
   - 連線方式：**Starting Point / Machines**
4. 點擊下載 `.ovpn` 檔案，儲存至任意資料夾（建議放在 `Documents\HTB\`）

---

### 3. 使用 OpenVPN 建立連線
1. 在桌面搜尋並執行 **OpenVPN GUI**
2. 右下角系統列會出現 OpenVPN 圖示（灰色）
3. 右鍵圖示 → **Import file...** → 選擇剛剛下載的 `.ovpn`
4. 匯入後，右鍵該設定檔 → **Connect**
5. 若顯示「Initialization Sequence Completed」，即成功連線

> 💡 成功連線後，可開啟 **CMD 或 PowerShell**，輸入：
> ```bash
> ping 10.10.10.10
> ```
> 若能成功回應，即表示你的本機已能連線到 HTB 內部網路。

---

### 4. 驗證連線狀態
你可以使用下列指令檢查 VPN 狀態與 IP：
```bash
ipconfig
在輸出中找到 TAP-Windows Adapter，若顯示 10.x.x.x 或 172.x.x.x 網段的 IP，即表示連線成功。