# Token Cost Optimizer 🚀 `v1.1.0`

<div align="center">

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)]()

**[English Documentation](#english-documentation) | [中文说明文档](#chinese-documentation)**

</div>

---

<a name="english-documentation"></a>
## English Documentation

> **Deterministic Context Pruning & Token Budget Optimization Suite for Agentic AI & Browser Automation Workflows**

`token-cost-optimizer` is a lightweight, local-first utility library designed for modern AI coding tools, browser agents, and workflows (**Google Antigravity, OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Windsurf, Cline, OpenHands, Dify**). By applying deterministic Python-based AST structural pruning, JSON schema folding, log denoising, and **DOM/Browser Session pruning (tailored for Xiaohongshu/Social Media automation)** prior to LLM ingestion, it drastically reduces context token consumption by **50% ~ 98%** while boosting response latency and preserving critical semantic context.

---

### 📊 Real-World Benchmark Results (v1.1.0)

| Benchmark Scenario | Sample File | Raw Context (Before) | Optimized Context (After) | Net Saved | Savings Rate | Execution Latency |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Python AST Pruning** | `sample_code.py` | 856 Tokens | 278 Tokens | 578 Tokens | 🚀 **67.5%** | ~80 ms |
| **JSON Schema Fold** | `sample_data.json` | 682 Tokens | 181 Tokens | 501 Tokens | 🚀 **73.5%** | ~80 ms |
| **Log Denoising** | `sample.log` | 400 Tokens | 305 Tokens | 95 Tokens | ⚡ **23.8%** | ~85 ms |
| **DOM Interactive Pruning** | `sample_xhs_dom.html` | 553 Tokens | 412 Tokens | 141 Tokens | 🌐 **25.5%** (Up to 95%+ on SPA) | ~120 ms |
| **XHS API & Session Trim** | `sample_xhs_api.json` | 214 Tokens | 170 Tokens | 44 Tokens | 🔐 **20.6%** (Up to 80%+ on HAR) | ~115 ms |
| **🏆 TOTAL COMBINED** | **Full Engineering Dataset** | **2,705 Tokens** | **1,346 Tokens** | **1,359 Tokens** | 🔥 **50.2%** | **< 120 ms** |

---

### 🌟 Core Capabilities & Principles

| Module | Script Path | Underlying Optimization Principle | Expected Savings |
| :--- | :--- | :--- | :--- |
| **DOM Interactive Action Pruner** | `scripts/prune_dom.py` | Strips SVG, style, script, hidden nodes, and obfuscated CSS hashes to extract concise Interactive Selector Trees for remote browser automation. | **90% ~ 98%** |
| **Browser & XHS API Optimizer** | `scripts/optimize_browser_context.py` | Cleans tracking metadata, strips redundant CDN image resolutions, and extracts essential cookies (`a1`, `web_session`, `webId`). | **70% ~ 95%** |
| **XHS Note & Pipeline Optimizer** | `scripts/compress_xhs_note.py` | Validates 20-char title limits, scans compliance risk words, and synthesizes compact SEO tag matrices. | **Pre-flight & Safety** |
| **AST Code Skeleton Pruner** | `scripts/prune_code.py` | Parses Python `ast` syntax trees to extract class signatures, methods, and docstrings while stripping bulky function bodies. | **65% ~ 95%** |
| **JSON Schema & Structural Fold** | `scripts/compress_json.py` | Recursively analyzes massive JSON datasets to construct a minimal typed schema sample. | **70% ~ 98%** |
| **Terminal & Build Log Denoised** | `scripts/clean_log.py` | Strips ANSI escape codes, download progress meters, and polling noise. | **20% ~ 80%** |
| **Token Budget Estimator** | `scripts/estimate_tokens.py` | Scans target directories or files to calculate pre-flight token footprints. | **Planning & Gating** |

---

### 🚀 Quick Start (English)

#### 1. DOM Interactive Pruning (`prune_dom.py`)
Condense complex web pages into compact interactive selector trees for Playwright/CDP automation:
```bash
python scripts/prune_dom.py /path/to/page_dump.html
```

#### 2. Browser Session & XHS API Response Trim (`optimize_browser_context.py`)
Clean API payloads or extract minimal auth cookies:
```bash
python scripts/optimize_browser_context.py /path/to/response.json
```

#### 3. Code Skeleton Extraction (`prune_code.py`)
Inspect architecture and API signatures without ingesting full source code:
```bash
python scripts/prune_code.py /path/to/large_file.py
```

#### 4. JSON Schema Sampling (`compress_json.py`)
Condense massive API payloads or datasets:
```bash
python scripts/compress_json.py /path/to/massive_dataset.json
```

#### 5. Log Denoising (`clean_log.py`)
Sanitize verbose terminal outputs or build logs:
```bash
python scripts/clean_log.py /path/to/build.log
```

---

<br>

---

<a name="chinese-documentation"></a>
## 中文说明文档

> **专为大模型智能体（Agentic AI）与远程浏览器自动化设计的本地确定性 Token 极度节流与成本优化工具套件**

`token-cost-optimizer` 是一个为现代 AI 编码工具与浏览器自动化智能体（**Google Antigravity, OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Windsurf, Cline, Dify**）打造的高效工具库。通过在 LLM 读入上下文之前，执行本地纯 Python 驱动的 AST 代码骨架提取、大型 JSON Schema 压缩、终端日志去噪、以及**网页 DOM 交互树精简与小红书等平台 API 会话瘦身**，在大幅降低 Token 消耗（**50% ~ 98%**）的同时，显著降低首字响应时间（TTFT）并保留关键上下文。

---

### 🛠️ 工具箱详解

#### 1. 浏览器 DOM 交互树精简 (`scripts/prune_dom.py`)
远程控制小红书创作者平台（`creator.xiaohongshu.com`）、网页登录、发帖表单时使用：
```bash
python scripts/prune_dom.py <html_file_path>
```
* **核心价值**：剔除所有 `<svg>`、`<script>`、`<style>`、隐藏元素与混淆 Class，提取带推荐 CSS Selector 的可交互节点清单。

#### 2. 小红书 API 报文与 Cookie 鉴权瘦身 (`scripts/optimize_browser_context.py`)
处理小红书抓包响应或多轮浏览器登录鉴权恢复：
```bash
python scripts/optimize_browser_context.py <json_or_cookie_path>
```
* **核心价值**：剥离 `trace_id`、打点噪音与重复 CDN 多分辨率图片，仅提取 `a1`, `web_session`, `webId` 等关键凭证。

#### 3. 小红书创作流水线与风控预检 (`scripts/compress_xhs_note.py`)
发布笔记前快速校验：
```bash
python scripts/compress_xhs_note.py --title "<标题>" --content "<正文>" --tags "标签1,标签2"
```
* **核心价值**：校验 20 字标题限制、合并冗余换行、预检敏感风控词、提炼精简 Tag 矩阵。

#### 4. 代码骨架提取 (`scripts/prune_code.py`)
```bash
python scripts/prune_code.py <file_path>
```
* **核心价值**：解析 AST 语法树，提取类、函数签名与 Docstring，剔除具体实现，节省 80%~95% 代码 Token。

#### 5. 大型 JSON 结构压缩 (`scripts/compress_json.py`)
```bash
python scripts/compress_json.py <json_path>
```
* **核心价值**：提取数据层级 Schema 与代表性样本，节省 90%+ 数据 Token。

#### 6. 终端日志去噪 (`scripts/clean_log.py`)
```bash
python scripts/clean_log.py <log_path>
```
* **核心价值**：剥离 ANSI 颜色码、下载进度条与轮询日志，聚焦报错堆栈。

---

### 📄 开源许可证
本项目采用 [MIT License](LICENSE) 开源。
