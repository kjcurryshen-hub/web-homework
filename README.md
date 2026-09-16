# 自我介紹網頁與 Docker / Git 作業

先完成、再複習。現在先做第 1 步，其他步驟可以稍後跟著教學完成。

## 作業與檔案對照

| 教材要求 | 提供的檔案 | 還要自己操作的部分 |
| --- | --- | --- |
| 自我介紹網頁 | `index.html`：含 HTML、CSS、JavaScript | 確認介紹符合自己、開啟網頁 |
| GitHub Pages | 本專案可直接發布的靜態網頁 | 在自己的 GitHub 建立 repo、push、設定 Pages |
| Docker Practice 1 | `practice-1/main.py` | 在容器執行 Hello World |
| Docker Practice 2 | `practice-2/` 原始程式、圖片、套件與 Dockerfile | 建置並執行 |
| Docker Practice 3 / Jupyter Demo | `practice-3/Dockerfile`、`hello.ipynb` | 啟動容器，在瀏覽器執行 notebook |
| Docker 基本指令問答 | 本文件第 6 步 | 說明指令並實際操作 |

根目錄的 Dockerfile 是「用 Docker 提供網頁」的延伸示範，不取代教材指定的 Practice 2。
教材沒有明列截圖繳交格式；下方驗收項目是自我檢查建議，不是額外作業規定。

## 1. 現在先開啟網頁

1. 將 ZIP 完整解壓縮。
2. 找到有 `index.html` 和 `README.md` 的 `web-homework` 資料夾。不要在 ZIP 內直接操作。
3. 雙擊 `index.html`，用 Chrome 或 Edge 開啟。
4. 確認能看到「你好，我是楷鈞」，並試按「Docker」「Git」頁籤。

到這裡只代表網頁可以開啟，尚未在你的電腦執行 Docker 或發布 GitHub Pages。

修改介紹：用 VS Code 開啟這個資料夾，編輯 index.html 中的「關於我」區塊。姓名先使用「楷鈞」，未填入學號、聯絡方式或未確認的個人經歷。興趣文字先依這次課程主題撰寫，可換成你實際的興趣；代表圖片使用教材的 Hello 圖片，可換成自己的照片。外部連結已放課程與 GitHub 專案連結，也可加上自己的 GitHub 個人頁。

## 2. 用 Docker 跑網頁（延伸示範）

先打開 Docker Desktop，等待引擎啟動。在 VS Code 開啟專案根目錄，再開啟 PowerShell 終端機。以下指令逐行執行：

```powershell
docker version
docker build -t web-homework .
docker run -d --name web-homework-site -p 127.0.0.1:8080:8000 web-homework
docker ps
```

瀏覽器開啟 http://localhost:8080。這裡的 8080 是 Windows 端，8000 是容器端。

```powershell
docker stop web-homework-site
docker start web-homework-site
```

`run` 建立新容器；已建立過同名容器時，用 `start` 重新啟動。
這個示範使用 COPY，修改 HTML 後需重新 build，並以新映像建立新容器才會更新。初次練習先不必處理更新。
若 8080 已被使用，可改成 `-p 127.0.0.1:8081:8000`，網址也改用 8081。
這裡的 Python HTTP server 用於課堂本機示範；對外靜態網站使用第 5 步的 Pages。

## 3. Docker Practice 1：在容器執行程式

對照 docker_2026.pdf 第 18 頁。從專案根目錄執行：

```powershell
cd practice-1
docker pull python:3.12-slim
docker images
docker run -dit --name homework-python -v "${PWD}:/app" -w /app python:3.12-slim bash
docker exec -it homework-python python main.py
```

預期第一行輸出 `Hello Docker!`。
這裡另取容器名 `homework-python`，避免與你可能已建立的 `practice_1` 同名。
使用固定的 Python 次版本方便教學；教材中的 `python` 未指定版本。

試著用 VS Code 修改 main.py 第一行 print 的文字，再執行一次 `docker exec`。因為 `-v` 連接了 Windows 資料夾和容器的 /app，修改會直接反映在容器讀到的檔案。

```powershell
docker exec -it homework-python bash
```

進入容器後執行 `pwd`、`ls`、`python main.py`；使用 `exit` 回到 PowerShell。
接著執行：

```powershell
docker stop homework-python
cd ..
```

## 4. Docker Practice 2 與 Practice 3

### Practice 2：指定專案部署

對照 docker_2026.pdf 第 19 頁；詳細操作請開啟 `practice-2/README.md`。必須使用教師指定專案，不能只用本網頁代替。

### Practice 3：Jupyter 與連接埠

對照 docker_2026.pdf 第 20–21 頁。從專案根目錄執行：

```powershell
cd practice-3
docker build -t homework-jupyter .
docker run -d --name homework-notebook -p 127.0.0.1:8888:8888 -v "${PWD}:/app" homework-jupyter
docker logs homework-notebook
```

第一次啟動可能需要數秒，若尚未看到網址，再執行一次 logs。找出含 `token=` 的網址，在瀏覽器開啟其中的 `http://127.0.0.1:8888/...`。若顯示容器主機名稱，改成 localhost，保留其餘路徑與 token。
也可以開啟 http://localhost:8888，貼上 logs 裡的 token 登入。保留預設 token 驗證。

開啟 `hello.ipynb` → 選取程式儲存格 → 按 Shift + Enter。預期輸出：

```text
Hello Docker from Jupyter!
```

按 Ctrl + S 儲存。因為有掛載資料夾，notebook 修改會保存在 Windows 的 practice-3 中。

```powershell
docker stop homework-notebook
cd ..
```

下次啟動用 `docker start homework-notebook`，再用 `docker logs homework-notebook` 查看本次登入資訊。

## 5. Git 與 GitHub Pages

此處沒有代你上傳 GitHub。先在自己的 GitHub 建立空白 repo，例如 `web-homework`；為了配合以下第一次 push 的流程，先不要在 GitHub 勾選建立 README、license 或 gitignore。

回到本機專案根目錄。先確認 Git 已安裝：

```powershell
git --version
git init
```

如果尚未設定提交身分，執行以下兩行，務必把引號中的範例改成自己的值。這是目前 repo 的設定：

```powershell
git config user.name "你的姓名或暱稱"
git config user.email "你的 GitHub 電子郵件或 GitHub noreply 電子郵件"
```

接著建立提交：

```powershell
git add .
git commit -m "Add personal introduction website and Docker exercises"
git branch -M main
```

下一行的 YOUR-USERNAME 要替換為自己的 GitHub 帳號；repo 名稱也要和你建立的一致。第一次操作 GitHub 可能會要求登入。

```powershell
git remote add origin https://github.com/YOUR-USERNAME/web-homework.git
git push -u origin main
```

在 GitHub repo 打開 **Settings → Pages**，Source 選 **Deploy from a branch**，選 **main** 和 **/ (root)**，然後 Save。等待部署成功，開啟 Pages 顯示的實際網址。

驗收：網址可以從瀏覽器開啟，並顯示自己的介紹。GitHub Pages 只負責這個靜態網頁，不會執行 Docker 或 Jupyter。
如果只是把檔案用 GitHub 網頁上傳，仍需另外練習本機 Git 指令，才涵蓋這堂課的版本控制操作。

## 6. 做完後的複習順序

每次只看一題，用已完成的專案回答，不用一次背完。

1. 在 HTML 找到 h1，把姓名改一下。CSS 的 color 改變什麼？JavaScript 的頁籤切換又做什麼？
2. Dockerfile 是建置說明，Image 是建置產物，Container 是依 Image 建立的實例。請指出各自對應哪個檔案／指令。
3. `-v` 把什麼資料夾連起來？為何 Practice 1 改檔不必重新 build？
4. `-p 127.0.0.1:8888:8888` 哪一端屬於電腦、哪一端屬於容器？
5. `git add` 是暫存修改，`commit` 是記錄版本，`push` 是送到遠端。三個動作發生在哪裡？

| 指令 | 用途 |
| --- | --- |
| docker images | 列出本機映像 |
| docker ps | 列出執行中的容器 |
| docker ps -a | 包含已停止的容器 |
| docker pull | 下載映像 |
| docker build | 依 Dockerfile 建置映像 |
| docker run | 建立並啟動新容器 |
| docker start / stop | 啟動／停止既有容器 |
| docker exec -it | 在執行中的容器裡執行互動指令 |
| docker logs | 查看容器輸出 |
| docker rm | 移除容器，操作前先確認資料與目標 |
| docker rmi | 移除映像 |
| git status / log / diff | 查看檔案狀態／提交歷史／修改差異 |

## 教材來源與驗證界線

- 使用者提供的 `index.html`、`Dockerfile.docx`、`docker_2026.pdf`、`2026Git.pdf`。
- [HTML 課程講義](https://hackmd.io/@Eric0413/2025-html5_orientation)：Homework 為自我介紹、Git Page、Docker 指令與 Jupyter Demo。Django 是補充內容，未列為該段作業的必做項目。
- [Docker 連接埠說明](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)
- [GitHub Pages 設定](https://docs.github.com/en/pages/quickstart)
- [Python HTTP server](https://docs.python.org/3/library/http.server.html)

本次環境沒有 Docker 引擎，無法實際建置 Docker 映像或驗證容器啟動；GitHub Pages 也尚未發布。這些需要在你的電腦與帳號實際完成。網頁本身的驗證另見 `VALIDATION.md`。
