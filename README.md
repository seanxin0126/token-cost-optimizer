# Token Cost Optimizer 🚀 `v1.0.1`

[![Version](https://img.shields.io/badge/version-1.0.1-blue.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

> **Drastic Token Compression & Context Cost Optimizer for Agentic AI Workflows**

`token-cost-optimizer` 是一个为大模型智能体（Agentic AI / Antigravity / OpenHands / Claude Code）设计的本地确定性 Token 节流与压缩工具库。通过本地 Python 脚本先行对超长上下文进行结构化剪裁与清洗，实现 **50% ~ 95%** 的 Token 开销削减与响应提速。

---

## 🌟 核心特性 (Features)

| 工具模块 | 脚本路径 | 优化原理 | 预期 Token 节省 |
| :--- | :--- | :--- | :--- |
| **AST 代码骨架提取** | `scripts/prune_code.py` | 利用 Python `ast` 解析语法树，提取类结构、函数签名、类型标注与 Docstring，剔除函数实现体。 | **80% ~ 95%** |
| **大型 JSON 结构压缩** | `scripts/compress_json.py` | 递归分析巨型 JSON 数据集，提取字段类型架构（Schema）与代表性样本采样，避免全量读入。 | **90% ~ 98%** |
| **终端日志智能降噪** | `scripts/clean_log.py` | 自动剥离 ANSI 转义颜色码、下载进度条、轮询重试信息，仅保留关键错误堆栈与执行摘要。 | **50% ~ 80%** |
| **Token 预算精确评估** | `scripts/estimate_tokens.py` | 预先扫描文件或目录并估算 Token 消耗，为长任务准入决策与上下文窗口管理提供量化支撑。 | **分析决策辅助** |

---

## 📦 项目结构 (Repository Structure)

```text
token-cost-optimizer/
├── SKILL.md                  # Antigravity Agent 标准技能注册描述
├── README.md                 # 仓库详细使用说明
├── CHANGELOG.md              # 中英文版本更新日志
├── .github/workflows/        # GitHub Actions 7天云端自动演进工作流
├── scripts/
│   ├── prune_code.py         # AST 代码骨架提取器
│   ├── compress_json.py      # JSON 数据结构采样与压缩
│   ├── clean_log.py          # 终端/构建日志去噪与错误提取
│   ├── estimate_tokens.py    # 文件与目录 Token 预算评估器
│   └── check_updates.py      # 每周前沿技术检索与演进规程
```

---

## 🔄 定期演进与更新规程 (Weekly Auto-Evolution)

本项目受自动化调度器（Scheduler）管理，按照 **每 7 天一次** 的周期自主运作：
1. **自动检索**：检索全球最新的 LLM 上下文剪裁、AST 分析、结构化采样技术。
2. **本地评估**：验证新方案的 Token 节省率与本地确定性执行表现。
3. **人工确认 (Human-in-the-Loop)**：严格执行三级风控（L3 Interception），生成变动报告向所有者发起审批，在获得明确授权后才执行 GitHub 仓库推送与代码同步。

---

## 🚀 快速上手 (Quick Start)

### 1. 代码骨架提取 (`prune_code.py`)
无需修改函数实现、只需理解系统架构与接口定义时使用：
```bash
python scripts/prune_code.py /path/to/large_source_file.py
```

### 2. JSON 数据压缩 (`compress_json.py`)
处理巨型 API 返回或数据集：
```bash
python scripts/compress_json.py /path/to/massive_dataset.json
```

### 3. 日志降噪 (`clean_log.py`)
清洗冗长的构建、测试或终端执行日志：
```bash
python scripts/clean_log.py /path/to/build.log
```

### 4. Token 预算评估 (`estimate_tokens.py`)
扫描工程或指定目录：
```bash
python scripts/estimate_tokens.py ./src
```

---

## 🧩 集成至 Antigravity / AI Agent

将本仓库置于智能体工作区的 `.agents/skills/token-cost-optimizer` 路径下，AI Agent 将自动识别 `SKILL.md` 并自主调度脚本以优化自身交互开销。

---

## 📄 License
MIT License
