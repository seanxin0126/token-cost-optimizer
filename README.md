# Token Cost Optimizer 🚀 `v1.0.1`

<div align="center">

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)]()

**[English](#english-documentation) | [中文说明](#chinese-documentation)**

</div>

---

<a name="english-documentation"></a>
## English Documentation

> **Deterministic Context Pruning & Token Budget Optimization Suite for Agentic AI Workflows**

`token-cost-optimizer` is a lightweight, local-first utility library designed for modern AI coding tools and agents (**Google Antigravity, OpenAI Codex, GitHub Copilot, Claude Code, Cursor, Windsurf, Cline, OpenHands, Dify**). By applying deterministic Python-based AST structural pruning, JSON schema folding, and log denoising prior to LLM ingestion, it drastically reduces context token consumption by **50% ~ 95%** while boosting response latency and preserving critical semantic context.

---

### 🌟 Core Capabilities & Metrics

| Module | Script Path | Underlying Optimization Principle | Expected Token Savings |
| :--- | :--- | :--- | :--- |
| **AST Code Skeleton Pruner** | `scripts/prune_code.py` | Utilizes Python `ast` syntax tree parsing to extract class signatures, functions, types, and docstrings while stripping bulky function bodies. | **80% ~ 95%** |
| **JSON Schema & Structural Fold** | `scripts/compress_json.py` | Recursively analyzes massive JSON datasets to construct a minimal typed schema sample, preventing full-dump token blowups. | **90% ~ 98%** |
| **Terminal & Build Log Denoised** | `scripts/clean_log.py` | Strips ANSI escape sequences, download progress meters, and polling noise, retaining only critical error traces and status conclusions. | **50% ~ 80%** |
| **Token Budget Estimator** | `scripts/estimate_tokens.py` | Scans target directories or files to calculate pre-flight token footprints and assist task gating decisions. | **Analysis & Planning** |

---

### 🚀 Quick Start (English)

#### 1. Code Skeleton Extraction (`prune_code.py`)
Inspect architecture and API signatures without ingesting full source code:
```bash
python scripts/prune_code.py /path/to/large_file.py
```

#### 2. JSON Schema Sampling (`compress_json.py`)
Condense massive API payloads or datasets:
```bash
python scripts/compress_json.py /path/to/massive_dataset.json
```

#### 3. Log Denoising (`clean_log.py`)
Sanitize verbose terminal outputs or build logs:
```bash
python scripts/clean_log.py /path/to/build.log
```

#### 4. Token Footprint Estimation (`estimate_tokens.py`)
Estimate token budget across target folders or projects:
```bash
python scripts/estimate_tokens.py ./src
```

---

### 🧩 Integration with AI Agents

Place this repository under `.agents/skills/token-cost-optimizer` in your workspace. AI Agents will automatically discover `SKILL.md` and invoke the scripts to minimize context overhead.

---

<br>

---

<a name="chinese-documentation"></a>
## 中文说明文档

> **专为大模型智能体（Agentic AI）设计的本地确定性 Token 极度节流与成本优化工具套件**

`token-cost-optimizer` 专为 **Google Antigravity、OpenAI Codex、GitHub Copilot、Claude Code、Cursor、Windsurf、Cline、OpenHands 及 Dify** 等主流 Vibe Coding 与智能体系统设计。通过在上下文灌入大模型之前，先行在本地利用 Python 确定性工具进行 AST 代码骨架提取、JSON 结构采样和终端日志降噪，实现 **50% ~ 95%** 的 Token 消耗削减与响应提速。

---

### 🌟 核心特性与节流收益

| 工具模块 | 脚本路径 | 优化原理 | 预期 Token 节省 |
| :--- | :--- | :--- | :--- |
| **AST 代码骨架提取** | `scripts/prune_code.py` | 基于 Python `ast` 语法树，提取类结构、函数签名、类型标注与 Docstring，剔除函数实现体。 | **80% ~ 95%** |
| **大型 JSON 结构压缩** | `scripts/compress_json.py` | 递归分析巨型 JSON 数据集，提取字段类型架构（Schema）与代表性样本采样，避免全量读入。 | **90% ~ 98%** |
| **终端日志智能降噪** | `scripts/clean_log.py` | 自动剥离 ANSI 转义颜色码、下载进度条、轮询重试信息，仅保留关键错误堆栈与执行摘要。 | **50% ~ 80%** |
| **Token 预算精确评估** | `scripts/estimate_tokens.py` | 预先扫描文件或目录并估算 Token 消耗，为长任务准入决策与上下文窗口管理提供量化支撑。 | **分析决策辅助** |

---

### 🚀 快速上手 (中文)

#### 1. 代码骨架提取 (`prune_code.py`)
无需修改函数内部实现、仅需了解系统架构与接口定义时使用：
```bash
python scripts/prune_code.py /path/to/large_file.py
```

#### 2. JSON 数据压缩 (`compress_json.py`)
处理几十万行复杂 JSON 数据集或 API 响应：
```bash
python scripts/compress_json.py /path/to/massive_dataset.json
```

#### 3. 日志降噪 (`clean_log.py`)
清洗冗长的构建、测试或终端执行日志：
```bash
python scripts/clean_log.py /path/to/build.log
```

#### 4. Token 预算评估 (`estimate_tokens.py`)
扫描工程或指定目录的 Token 占用：
```bash
python scripts/estimate_tokens.py ./src
```

---

## 🧩 集成至 Antigravity / AI Agent

将本仓库置于工作区 `.agents/skills/token-cost-optimizer` 目录下，AI 智能体将自动识别 `SKILL.md` 并自主调度脚本以优化自身交互开销。

---

## 📄 License & Changelog
- **License**: [MIT License](LICENSE)
- **Changelog**: 详细版本履历请参阅 [CHANGELOG.md](CHANGELOG.md)
