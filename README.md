# Token Cost Optimizer 🚀 `v1.0.1`

<div align="center">

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)]()

**[English Documentation](#-english-documentation) | [中文说明文档](#-中文说明文档)**

</div>

---

<a name="english-documentation"></a>
## 🇬🇧 English Documentation

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
| **7-Day Autonomous Evolution** | `scripts/check_updates.py` | Scans academic literature and open-source ecosystems every 7 days via GitHub Actions for continuous self-evolution. | **Self-Evolving** |

---

### 📦 Repository Structure

```text
token-cost-optimizer/
├── SKILL.md                  # Standard Antigravity Agent Skill Definition
├── README.md                 # Bilingual documentation & architecture guide
├── CHANGELOG.md              # Bilingual version history & release notes
├── .github/workflows/        # GitHub Actions 7-day autonomous scheduler
├── scripts/
│   ├── prune_code.py         # AST syntax tree code skeleton extractor
│   ├── compress_json.py      # JSON schema sampling & structural compressor
│   ├── clean_log.py          # Terminal/build log noise stripper
│   ├── estimate_tokens.py    # Directory/file token footprint estimator
│   └── check_updates.py      # Weekly research discovery & report generator
```

---

### 🤖 OpenAI Codex & GitHub Copilot Compatibility

`token-cost-optimizer` is **100% compatible with OpenAI Codex, GitHub Copilot (Codex Agent), and OpenCode**. Codex thrives when provided with clean AST signatures rather than verbose implementation bodies.

#### 1. Setup for GitHub Copilot (VS Code / JetBrains)
Create `.github/copilot-instructions.md` in your workspace root:
```markdown
# Instructions for GitHub Copilot / Codex
- **Token Efficiency First**: Do not load raw code files (>100 lines) directly into context.
- Run `python .agents/skills/token-cost-optimizer/scripts/prune_code.py <file>` to extract class/function signatures.
- For large JSON datasets (>50KB), run `python .agents/skills/token-cost-optimizer/scripts/compress_json.py <file>` to inspect the minimal schema.
- Sanitize terminal outputs with `python .agents/skills/token-cost-optimizer/scripts/clean_log.py <log>`.
```

#### 2. Setup for OpenAI Codex CLI / Custom Agent Pipelines
In your agent system prompt or `CODEX.md`:
```markdown
# Codex Agent Directives
Always execute deterministic local tools in `token-cost-optimizer/scripts/` prior to multi-file refactoring to stay well within token limits and rate thresholds.
```

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

### 🔄 7-Day Cloud-Native Autonomous Evolution

Managed by GitHub Actions (`.github/workflows/weekly-research.yml`), this repository automatically:
1. **Scans** global LLM context pruning and prompt compression literature every Monday (01:00 UTC).
2. **Evaluates** algorithm efficiency and local deterministic execution metrics.
3. **Dispatches** a structured GitHub Issue report requiring explicit repository owner confirmation before merging any PRs.

---

<br>

---

<a name="中文说明文档"></a>
## 🇨🇳 中文说明文档

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
| **7 天云端自主演进** | `scripts/check_updates.py` | 配合 GitHub Actions 每 7 天自动追踪全球最新上下文剪裁与压缩前沿技术。 | **自进化中枢** |

---

### 🤖 OpenAI Codex 与 GitHub Copilot 兼容与配置说明

`token-cost-optimizer` 与 **OpenAI Codex、GitHub Copilot（Codex 智能体模式）及 OpenCode 具备 100% 的原生兼容性**。由于 Codex 对结构清晰的类型标注与函数签名极其敏感，提供剪裁后的 AST 骨架不仅大幅节省 Token，还能显著提升 Codex 代码生成的准确率。

#### 1. 配置 GitHub Copilot（VS Code / IDE 插件）
在项目根目录创建 `.github/copilot-instructions.md`：
```markdown
# GitHub Copilot / Codex 专属优化指南
- **Token 节流原则**：严禁直接全量读取超过 100 行的大型源代码文件。
- 优先在终端执行 `python .agents/skills/token-cost-optimizer/scripts/prune_code.py <file>` 提取函数/类签名。
- 处理大于 50KB 的 JSON 数据时，执行 `python .agents/skills/token-cost-optimizer/scripts/compress_json.py <file>` 提取 Schema。
- 排查终端报错时，使用 `python .agents/skills/token-cost-optimizer/scripts/clean_log.py <log>` 过滤干扰字符。
```

#### 2. 配置 OpenAI Codex CLI / 终端 Agent
在您的 Prompt 指令或 `CODEX.md` 中声明：
```markdown
# Codex Agent 执行守则
在重构与跨文件分析时，优先调度 `token-cost-optimizer/scripts/` 中的确定性工具，防止突破上下文窗口与触发 API 限额。
```

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

### 🔄 定期演进与人工决策机制 (Weekly Auto-Evolution)

本项目受自动化调度器（GitHub Actions）管理，按照 **每 7 天一次** 的周期自主运作：
1. **自动检索**：云端自动检索全球最新的 LLM 上下文剪裁、AST 分析、结构化采样技术。
2. **本地评估**：验证新方案的 Token 节省率与本地确定性执行表现。
3. **人工确认 (Human-in-the-Loop)**：自动在 GitHub 创建带有周报的 Issue，必须获得仓库所有者显式勾选确认后，才执行代码合并。

---

## 🧩 集成至 Antigravity / AI Agent

将本仓库置于工作区 `.agents/skills/token-cost-optimizer` 目录下，AI 智能体将自动识别 `SKILL.md` 并自主调度脚本以优化自身交互开销。

---

## 📄 License & Changelog
- **License**: [MIT License](LICENSE)
- **Changelog**: 详细版本履历请参阅 [CHANGELOG.md](CHANGELOG.md)
