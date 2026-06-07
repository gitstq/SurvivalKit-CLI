<!-- Language Selector -->
<div align="center">

**[简体中文](#-简体中文) | [繁體中文](#-繁體中文) | [English](#-english)**

</div>

---

# 🆘 SurvivalKit-CLI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Cross--Platform-lightgrey?style=flat-square)

**輕量級終端應急知識庫與離線生存工具箱**

*Lightweight Terminal Emergency Knowledge Base & Offline Survival Toolkit*

</div>

---

## 简体中文

### 项目介绍

**SurvivalKit-CLI** 是一款专为应急场景设计的轻量级终端工具。在自然灾害、野外探险、突发事故等紧急情况下，网络可能中断，手机可能没电，但只要有终端，你就能获得专业的急救指导和生存技能。

**灵感来源**：本项目灵感来自 GitHub Trending 上的 [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)（离线生存计算机），但我们采用了**差异化轻量路线**——不做庞大的全功能系统，而是聚焦在**最实用、最轻量、最易用**的CLI工具箱，让任何人都能零门槛使用。

### 核心特性

| 特性 | 说明 |
|------|------|
| 急救知识库 | 心肺复苏、止血、骨折固定、烧伤处理、气道梗阻、休克应对 |
| 野外生存技能 | 取水、取火、避难所搭建、食物获取、野外定向、求救信号 |
| 摩斯电码工具 | 实时编解码、视觉表示、发送时长估算、完整对照表 |
| 坐标转换工具 | DD/DMS/UTM 互转、两点距离与方位角计算 |
| 应急清单生成器 | 地震、洪水、野外、停电等场景的完整检查清单 |
| 零依赖 | 纯 Python 标准库，无需安装任何第三方包 |
| 完全离线 | 无需网络，随时随地可用 |
| 跨平台 | Windows、macOS、Linux 全兼容 |
| 彩色终端UI | 美观的终端界面，支持自动颜色检测 |

### 快速开始

#### 环境要求
- **Python 3.8** 或更高版本

#### 安装方式

**方式一：pip 安装（推荐）**
```bash
pip install survivalkit-cli
```

**方式二：源码运行**
```bash
git clone https://github.com/gitstq/SurvivalKit-CLI.git
cd SurvivalKit-CLI
python -m survivalkit
```

**方式三：直接下载运行**
```bash
# 下载源码后直接进入目录运行
python -m survivalkit
```

#### 启动命令
```bash
# 主命令
survivalkit

# 快捷命令
sk

# 模块方式
python -m survivalkit
```

### 详细使用指南

#### 主菜单导航
启动后，你会看到彩色终端主菜单：

```
1. 急救知识      - 6大类急救指南
2. 野外生存      - 6大生存技能
3. 实用工具      - 摩斯电码 + 坐标转换
4. 应急清单      - 6种场景检查清单
5. 关于          - 项目信息
```

#### 急救知识示例
选择 `1. 急救知识` → `1. 心肺复苏 (CPR)`，即可查看完整的CPR操作步骤：
- 判断意识 → 呼叫救援 → 检查呼吸
- 胸外按压（位置、深度、频率）
- 开放气道 → 人工呼吸
- 持续循环直到救援到达

#### 摩斯电码工具示例
```
原文: SOS HELP
编码: ... --- ... / .... . .-.. .--.
视觉: ■ ■■■ ■   ■■■■ ■ ■− ■−− ■−−
时长: ~3.42秒
```

#### 坐标转换示例
```
输入: 39.9042, 116.4074 (北京天安门)
DMS:  39°54′15.12″N, 116°24′26.64″E
UTM:  Zone 50S, Easting 447xxx, Northing 4418xxx
```

### 设计思路与迭代规划

#### 为什么做这个项目？
1. **真实痛点**：现有应急APP都需要网络，灾难时往往无法使用
2. **技术空白**：您的GitHub账号下已有80+项目，但**没有离线应急工具**
3. **轻量哲学**：参考 project-nomad 的灵感，但走差异化路线——更轻、更快、更易用

#### 技术选型原因
- **Python**：跨平台、标准库丰富、人人会写
- **零依赖**：确保在任何环境下都能运行
- **终端UI**：最低资源占用，最高兼容性

#### 后续迭代计划
- [ ] 增加更多急救场景（中毒、溺水、触电）
- [ ] 增加野外植物图鉴数据库
- [ ] 增加应急计算器（净水片用量、食物配给）
- [ ] 增加多语言知识库（英文、日文）
- [ ] 增加导出PDF功能

### 打包与部署

本项目为**CLI工具/脚本类项目**，无需打包为可执行文件。

#### 安装到系统
```bash
# 开发安装
pip install -e .

# 全局安装
pip install .
```

#### 卸载
```bash
pip uninstall survivalkit-cli
```

### 贡献指南

欢迎提交 Issue 和 PR！

- **Bug 反馈**：请描述复现步骤和环境信息
- **功能建议**：请说明使用场景和预期行为
- **代码贡献**：遵循 PEP 8 规范，保持零依赖原则

### 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 繁體中文

### 專案介紹

**SurvivalKit-CLI** 是一款專為應急場景設計的輕量級終端工具。在自然災害、野外探險、突發事故等緊急情況下，網路可能中斷，手機可能沒電，但只要有終端，你就能獲得專業的急救指導和生存技能。

**靈感來源**：本專案靈感來自 GitHub Trending 上的 [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad)（離線生存電腦），但我們採用了**差異化輕量路線**——不做龐大的全功能系統，而是聚焦在**最實用、最輕量、最易用**的CLI工具箱，讓任何人都能零門檻使用。

### 核心特性

| 特性 | 說明 |
|------|------|
| 急救知識庫 | 心肺復甦、止血、骨折固定、燒傷處理、氣道梗阻、休克應對 |
| 野外生存技能 | 取水、取火、避難所搭建、食物獲取、野外定向、求救信號 |
| 摩斯電碼工具 | 即時編解碼、視覺表示、發送時長估算、完整對照表 |
| 座標轉換工具 | DD/DMS/UTM 互轉、兩點距離與方位角計算 |
| 應急清單產生器 | 地震、洪水、野外、停電等場景的完整檢查清單 |
| 零依賴 | 純 Python 標準庫，無需安裝任何第三方套件 |
| 完全離線 | 無需網路，隨時隨地可用 |
| 跨平台 | Windows、macOS、Linux 全相容 |
| 彩色終端UI | 美觀的終端介面，支援自動顏色檢測 |

### 快速開始

#### 環境要求
- **Python 3.8** 或更高版本

#### 安裝方式

**方式一：pip 安裝（推薦）**
```bash
pip install survivalkit-cli
```

**方式二：原始碼執行**
```bash
git clone https://github.com/gitstq/SurvivalKit-CLI.git
cd SurvivalKit-CLI
python -m survivalkit
```

**方式三：直接下載執行**
```bash
# 下載原始碼後直接進入目錄執行
python -m survivalkit
```

#### 啟動命令
```bash
# 主命令
survivalkit

# 快捷命令
sk

# 模組方式
python -m survivalkit
```

### 詳細使用指南

#### 主選單導航
啟動後，你會看到彩色終端主選單：

```
1. 急救知識      - 6大類急救指南
2. 野外生存      - 6大生存技能
3. 實用工具      - 摩斯電碼 + 座標轉換
4. 應急清單      - 6種場景檢查清單
5. 關於          - 專案資訊
```

#### 急救知識範例
選擇 `1. 急救知識` → `1. 心肺復甦 (CPR)`，即可查看完整的CPR操作步驟：
- 判斷意識 → 呼叫救援 → 檢查呼吸
- 胸外按壓（位置、深度、頻率）
- 開放氣道 → 人工呼吸
- 持續循環直到救援到達

#### 摩斯電碼工具範例
```
原文: SOS HELP
編碼: ... --- ... / .... . .-.. .--.
視覺: ■ ■■■ ■   ■■■■ ■ ■− ■−− ■−−
時長: ~3.42秒
```

#### 座標轉換範例
```
輸入: 39.9042, 116.4074 (北京天安門)
DMS:  39°54′15.12″N, 116°24′26.64″E
UTM:  Zone 50S, Easting 447xxx, Northing 4418xxx
```

### 設計思路與迭代規劃

#### 為什麼做這個專案？
1. **真實痛點**：現有應急APP都需要網路，災難時往往無法使用
2. **技術空白**：您的GitHub帳號下已有80+專案，但**沒有離線應急工具**
3. **輕量哲學**：參考 project-nomad 的靈感，但走差異化路線——更輕、更快、更易用

#### 技術選型原因
- **Python**：跨平台、標準庫豐富、人人會寫
- **零依賴**：確保在任何環境下都能執行
- **終端UI**：最低資源佔用，最高相容性

#### 後續迭代計劃
- [ ] 增加更多急救場景（中毒、溺水、觸電）
- [ ] 增加野外植物圖鑑資料庫
- [ ] 增加應急計算器（淨水片用量、食物配給）
- [ ] 增加多語言知識庫（英文、日文）
- [ ] 增加匯出PDF功能

### 打包與部署

本專案為**CLI工具/腳本類專案**，無需打包為可執行檔案。

#### 安裝到系統
```bash
# 開發安裝
pip install -e .

# 全域安裝
pip install .
```

#### 解除安裝
```bash
pip uninstall survivalkit-cli
```

### 貢獻指南

歡迎提交 Issue 和 PR！

- **Bug 回報**：請描述復現步驟和環境資訊
- **功能建議**：請說明使用場景和預期行為
- **程式碼貢獻**：遵循 PEP 8 規範，保持零依賴原則

### 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## English

### Introduction

**SurvivalKit-CLI** is a lightweight terminal tool designed for emergency scenarios. During natural disasters, wilderness adventures, or sudden accidents, when the internet may be down and phones may be dead, as long as you have a terminal, you can access professional first aid guidance and survival skills.

**Inspiration**: This project is inspired by [project-nomad](https://github.com/Crosstalk-Solutions/project-nomad) from GitHub Trending (an offline survival computer), but we took a **differentiated lightweight approach** — instead of building a massive all-in-one system, we focused on creating the **most practical, lightweight, and user-friendly** CLI toolkit that anyone can use with zero barriers.

### Core Features

| Feature | Description |
|---------|-------------|
| First Aid Knowledge Base | CPR, bleeding control, fracture immobilization, burn treatment, choking, shock management |
| Wilderness Survival Skills | Water procurement, fire making, shelter building, food foraging, navigation, emergency signals |
| Morse Code Tool | Real-time encode/decode, visual representation, timing estimation, full reference chart |
| Coordinate Converter | DD/DMS/UTM conversion, distance and bearing calculation between two points |
| Emergency Checklist Generator | Complete checklists for earthquake, flood, wilderness, power outage scenarios |
| Zero Dependencies | Pure Python standard library, no third-party packages required |
| Fully Offline | Works anytime, anywhere without internet |
| Cross-Platform | Compatible with Windows, macOS, and Linux |
| Colorful Terminal UI | Beautiful terminal interface with automatic color detection |

### Quick Start

#### Requirements
- **Python 3.8** or higher

#### Installation

**Method 1: pip install (Recommended)**
```bash
pip install survivalkit-cli
```

**Method 2: Run from source**
```bash
git clone https://github.com/gitstq/SurvivalKit-CLI.git
cd SurvivalKit-CLI
python -m survivalkit
```

**Method 3: Direct download and run**
```bash
# Download source code and run directly
python -m survivalkit
```

#### Launch Commands
```bash
# Main command
survivalkit

# Shortcut command
sk

# Module mode
python -m survivalkit
```

### Detailed Usage Guide

#### Main Menu Navigation
After launching, you will see a colorful terminal main menu:

```
1. First Aid      - 6 major first aid guides
2. Wilderness     - 6 survival skills
3. Tools          - Morse code + Coordinate conversion
4. Checklists     - 6 scenario-based checklists
5. About          - Project information
```

#### First Aid Example
Select `1. First Aid` → `1. CPR`, and you can view the complete CPR procedure:
- Check responsiveness → Call for help → Check breathing
- Chest compressions (position, depth, rate)
- Open airway → Rescue breaths
- Continue cycles until help arrives

#### Morse Code Tool Example
```
Text:   SOS HELP
Encoded: ... --- ... / .... . .-.. .--.
Visual:  ■ ■■■ ■   ■■■■ ■ ■− ■−− ■−−
Duration: ~3.42 seconds
```

#### Coordinate Conversion Example
```
Input: 39.9042, 116.4074 (Beijing Tiananmen)
DMS:   39°54′15.12″N, 116°24′26.64″E
UTM:   Zone 50S, Easting 447xxx, Northing 4418xxx
```

### Design Philosophy & Roadmap

#### Why this project?
1. **Real Pain Point**: Existing emergency apps all require internet, which is often unavailable during disasters
2. **Technical Gap**: Your GitHub account has 80+ projects, but **no offline emergency tools**
3. **Lightweight Philosophy**: Inspired by project-nomad, but taking a differentiated route — lighter, faster, easier to use

#### Technology Choices
- **Python**: Cross-platform, rich standard library, easy for everyone
- **Zero Dependencies**: Ensures it runs in any environment
- **Terminal UI**: Lowest resource usage, highest compatibility

#### Future Roadmap
- [ ] Add more first aid scenarios (poisoning, drowning, electrocution)
- [ ] Add wilderness plant identification database
- [ ] Add emergency calculators (water purification tablets, food rationing)
- [ ] Add multilingual knowledge base (English, Japanese)
- [ ] Add PDF export functionality

### Packaging & Deployment

This project is a **CLI tool/script project** and does not need to be packaged as an executable.

#### Install to System
```bash
# Development install
pip install -e .

# Global install
pip install .
```

#### Uninstall
```bash
pip uninstall survivalkit-cli
```

### Contributing

Issues and PRs are welcome!

- **Bug Reports**: Please describe reproduction steps and environment info
- **Feature Suggestions**: Please describe use cases and expected behavior
- **Code Contributions**: Follow PEP 8 standards, maintain zero-dependency principle

### License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Made with ❤️ by Lobster Daily Incubator**

*In emergency situations, knowledge is power.*

</div>
