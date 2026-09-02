# 📋 更新日志 (Changelog)

All notable changes to the `token-cost-optimizer` skill and repository will be documented in this file.

---

## [v1.0.1] - 2026-09-02

### 中文更新说明

#### 🚀 核心更新与功能特性
1. **跨平台控制台 UTF-8 兼容性增强**：
   - 解决 Windows GBK 终端下输出 Emoji 与特殊字符时触发 `UnicodeEncodeError` 的问题。
   - 为全部核心脚本（`prune_code.py`、`compress_json.py`、`clean_log.py`、`estimate_tokens.py`）增加标准的 `sys.stdout.reconfigure(encoding='utf-8')` 安全输出包装。
2. **智能目录与文件过滤优化**：
   - 优化 `estimate_tokens.py` 的目录遍历逻辑，支持精准扫描以 `.` 开头的合法工程目录（如 `.agents`），同时智能忽略 `.git`、`__pycache__`、`.venv`、`node_modules`、`dist` 等无关大文件夹。
3. **GitHub Actions 云端 7 天自动演进调度器**：
   - 集成 `.github/workflows/weekly-research.yml`，实现每 7 天在 GitHub 云端自动触发前沿论文与开源技术检索。
   - 自动生成周报并分发 GitHub Issue，通知仓库所有者进行 Human-in-the-Loop 人工确认，完全无需本地电脑开机。
4. **OpenAI Codex 与 GitHub Copilot 深度兼容规范**：
   - 增加专用的 `.github/copilot-instructions.md` 与 `CODEX.md` 接入配置说明，帮助 Codex 模型聚焦高质量 AST 函数/类签名，减少歧义并提升代码补全精准度。
5. **防御性异常处理与超时保护**：
   - 为各脚本增添了优雅的异常降级处理，防止在解析异常格式文件时引发阻塞。

---

### English Release Notes

#### 🚀 Key Features & Improvements
1. **Cross-Platform UTF-8 Console Compatibility**:
   - Resolved `UnicodeEncodeError` issues on Windows terminals running non-UTF8 code pages (e.g., GBK/CP936) when outputting emojis and special characters.
   - Integrated robust `sys.stdout.reconfigure(encoding='utf-8', errors='replace')` across all core utility scripts (`prune_code.py`, `compress_json.py`, `clean_log.py`, `estimate_tokens.py`).
2. **Intelligent Directory & File Filtering**:
   - Enhanced directory traversal in `estimate_tokens.py` to seamlessly inspect valid hidden project paths (such as `.agents`) while properly excluding `.git`, `__pycache__`, `.venv`, `node_modules`, `build`, and `dist`.
3. **OpenAI Codex & GitHub Copilot Native Support**:
   - Added tailored instructions (`.github/copilot-instructions.md` & `CODEX.md`) to guide Codex-based agents to leverage AST skeletons for higher completion accuracy and zero token overflow.
4. **7-Day Cloud-Native Autonomous Evolution via GitHub Actions**:
   - Added `.github/workflows/weekly-research.yml` to automatically execute academic/open-source research every 7 days on GitHub cloud runners.
   - Automatically publishes weekly optimization reports and creates structured GitHub Issues for Human-in-the-Loop owner authorization without requiring local machine uptime.
5. **Defensive Error Handling & Graceful Fallback**:
   - Enhanced exception handling and timeout guarantees across all tools to prevent hanging or unexpected pipeline crashes.

---

## [v1.0.0] - 2026-09-02

### 中文说明
- 初始版本发布。
- 包含 4 大核心本地确定性压缩工具：AST 代码骨架提取、大型 JSON 数据压缩、终端日志去噪、以及 Token 预算评估。
- 提供标准 Antigravity `SKILL.md` 与中英文 `README.md`。

### English Release Notes
- Initial official release.
- Core local deterministic token optimization tools: AST Code Skeleton Pruner, JSON Schema Compressor, Terminal Log Cleaner, and Token Estimator.
- Standard Antigravity `SKILL.md` registration and complete documentation.
