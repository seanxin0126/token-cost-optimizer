---
name: token-cost-optimizer
description: 极限节省与压缩 Token 开销工具库（Token Cost Optimizer）。提供 AST 代码骨架提取（剔除庞大函数体提取接口签名）、大型 JSON 结构压缩（提取 Schema 样本）、终端日志去噪（过滤进度条与重复日志）及 Token 精确预算估算。在处理超长代码文件、分析大型 JSON 数据、审查大日志或任务准入前激活此技能。
metadata:
  builtin_skill_version: "1.0.1"
  version: "1.0.1"
  purpose: "Drastic Token Compression & Cost Optimization"
---

# Token Cost Optimizer 极度节流与成本优化工具套件

本技能专为在长任务与复杂工程中实现 **50% ~ 90% 的 Token 压缩** 而设计，原生兼容 **Google Antigravity、OpenAI Codex、GitHub Copilot、Claude Code、Cursor、Windsurf、Cline、Dify** 等主流智能体，通过本地确定性 Python 工具替代盲目全量读入。

---

## 🛠️ 核心工具脚本规程

### 1. 代码骨架提取（节省 80%~95% 代码 Token）
在不需要修改函数内部实现、仅需了解模块架构、调用关系或接口签名时，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/prune_code.py <file_path>
```
* **效果**：自动解析 AST，提取模块 Docstring、类定义、方法签名与参数，剔除具体实现。

### 2. 大型 JSON 结构压缩（节省 90%+ 数据 Token）
当面对几十万行的复杂 JSON 数据文件时，严禁全量读入，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/compress_json.py <json_path>
```
* **效果**：自动提取数据层级 Schema、字段类型及典型 Sample，保留结构全貌同时压缩体积。

### 3. 终端与构建日志去噪（节省 50%+ 调试 Token）
当运行构建或安装命令产生大量输出时，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/clean_log.py <log_file_or_text>
```
* **效果**：去除 ANSI 转义色彩码、下载进度条、npm/pip 轮询日志，保留错误堆栈与退出结论。

### 4. 任务 Token 预算精确评估
在执行长任务前，扫描目标文件或目录的 Token 占用：
```bash
python .agents/skills/token-cost-optimizer/scripts/estimate_tokens.py <path>
```
* **效果**：提供准确的 Token 消耗预估，辅助 `autonomous-meta-workflow` 做出准入决策。

---

## 🔄 每 7 天自主前沿检索与进化规程
1. **定时周期**：每 7 天自主触发一次网络深度检索（聚焦最新的 Prompt 压缩、AST 剪枝、上下文缓存、日志采样技术）。
2. **三级风控确认（L3 拦截）**：
   - 本地自动验证与对比新算法的 Token 节省率。
   - 向用户输出《周度 Token 节流技术优化报告与代码变动提案》。
   - **严禁擅自直接推送**：必须经用户显式确认同意后，方可将新特性合并并推送至 GitHub 仓库。

