# Pynecone

`Pynecone` 是一個全端框架，可以用來建立和部屬一個網頁apps。[官網](https://pynecone.io/docs/getting-started/introduction)


`Pynecone` 是一個基於純 python 的 web app 框架，他依賴 node.js，不需要另外寫前端的 code ，這對於沒接觸過前端的人非常友善。

### 安裝

- Prerequisites
    - [node.js](https://nodejs.org/en/)，下載 LTS 版本
    - [python](https://www.python.org/downloads/)


- 虛擬環境
    - [poetry](https://python-poetry.org/)
    - [venv](https://docs.python.org/3/library/venv.html)
    - 等...

### 這邊使用 `poetry` 進行安裝
- 本機為 win11, 64位元。

- 下載 WSL
    - 打開 power shell ``(不是 cmd 喔！)``，管理員模式。
    - 輸入 `wsl --install`  or `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
    - 等他下載好，重新開機即可

- 接著，下載 `poetry`
    - 本機安裝(power shell 管理員模式)。
    ```shell=
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
    ```
    - 更改路徑。
        - 打開環境變數，找到 path 接著把 `poetry` 的路徑貼上。
        ![](https://hackmd.io/_uploads/B1ZO5hmNh.png)

        - 打開 cmd ，輸入 `poetry --version`
    
    - WSL 安裝，先進入 WSL。
    ![](https://hackmd.io/_uploads/rkplyqm42.png)
    - 貼上這行。

    ```shell=
    curl -sSL https://install.python-poetry.org | python3 -
    ```
    - 接下來，更改一下路徑，依照提示輸入以下。
    ```shell=
     echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
    ```
    - 啟動它。
    ```shell=
    source ~/.bashrc
    ```
    - 確認。
    ```shell=
    poetry --version
    ```
### 開始啟用(本機)。
- 在本機裡使用。
- 接著，使用 `pip install pynecone`，按照官網，使用
```shell=
$ mkdir my_app_name
$ cd my_app_name
$ pc init
```
- 再下達。
```shell=
pc run
# or $ pc run --loglevel debug
```
就可以看見啟用了。

### 開始啟用(ubuntu)。
- 進入 WSL
```shell=
mkdir [project_name]

cd pyneconedemo

poetry init

poetry config virtualenvs.in-project true 

poetry env use python3.11
```

- 出問題？
```shell=
# python not found
sudo apt update && upgrade
sudo apt install python3 python3-pip ipython3

python3 --version
poetry env use python3.10.6
# 3.10.6 可以換，只是版本，不過還是得看 pyproject.toml 這個檔案裡的 python 版本。
```

- 加入套件
```shell=
poetry shell

poetry add pynecone
```

- 出問題？
```shell=
# node.js 下載，以及 nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash

# 依照提示關閉視窗，重新開啟。

nvm

node --version

nvm install node

node --version

nvm install 16[版本號]

# 查看版本有幾個
nvm ls

# 可以調轉版本，或不用
nvm alias default 16

# 要換回來的話，重複下指令就可以。
nvm alias default 20
```

### 好的，完成大部分了！
在 shell 裡下達指令就會自動下載 vscode 囉！
```shell=
code .
```

* 這裡要使用 `pc init` 進行初始化。
```shell=
pc init
```

* 如果看見 `FileNotFoundError: Pynecone requires unzip to be installed.`
就是說需要 unzip 這個包，下載就對了。
```shell=
sudo apt-get install unzip
```

沒問題的話就繼續 `pc init`。
就可以看見下圖囉！

![](https://hackmd.io/_uploads/SJWm52XNn.png)
