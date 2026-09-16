# Practice 2：指定專案部署

來源：https://github.com/jefffang19/python_helloworld/tree/main

本資料夾的 main.py、requirements.txt、hello.jpg 來自教師指定專案；Dockerfile 依你提供的 Dockerfile.docx 轉出。
程式透過 OpenCV 讀取 hello.jpg、轉為灰階，再逐像素以 o 與空白印出圖案。

從專案根目錄，在 PowerShell 逐行執行：

```powershell
cd practice-2
docker build -t homework-deployment .
docker run --rm homework-deployment
cd ..
```

預期先輸出圖片尺寸，再輸出字元組成的 Hello 圖案。--rm 會在程式結束後自動移除這次的臨時容器，映像仍保留。

成功條件：映像建置成功、程式正常印出尺寸與圖案；不能用首頁可以開啟取代這一題。

此 Dockerfile 保留教材的 Python 3.8.13，配合指定專案的 numpy 1.23.1 和 OpenCV 4.6.0.66。此處沒有 Docker 引擎，尚未驗證容器建置。若 apt-get 或套件安裝失敗，請保留錯誤訊息再修正。

若老師要求練習 clone，可另外在空白資料夾執行：

```powershell
git clone https://github.com/jefffang19/python_helloworld.git
```

不要在已有檔案的 practice-2 資料夾覆蓋下載。
