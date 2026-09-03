# 📋 更新日志 (Changelog)

All notable changes to the `token-cost-optimizer` skill and repository will be documented in this file.

---

## [v1.1.0] - 2026-09-03

### 中文更新说明

#### 🚀 核心更新与功能特性（专为小红书与远程浏览器自动化深度强化）
1. **浏览器 DOM 与网页交互树极限精简器 (`prune_dom.py`)**：
   - 专为远程控制小红书创作者平台（`creator.xiaohongshu.com`）、自动化表单填写打造。
   - 自动剥离所有庞大 `<svg>`、`<script>`、`<style>`、隐藏节点、混淆 Class，精准提取带最简 CSS Selector 的**可交互操作元素树（Interactive Action Map）**，实现 **90%~98%** 的 HTML Token 压缩。
2. **小红书 API 报文与浏览器 Cookie 鉴权瘦身器 (`optimize_browser_context.py`)**：
   - 自动过滤小红书网络抓包中的 `trace_id`、打点、多分辨率冗余 CDN 图片数据。
   - 精简浏览器 Cookies，仅保留核心鉴权 Token（`a1`, `web_session`, `webId`），大幅降低多轮浏览器会话恢复时的 Token 开销。
3. **小红书创作流水线与风控敏感词预检器 (`compress_xhs_note.py`)**：
   - 实时校验小红书 20 字标题上限、正文字数与 Token 预算。
   - 内置风控敏感词/违禁词扫描及精炼 SEO Tag 话题矩阵提取。
4. **全套自动化测试套件与基准测试图表升级**：
   - 新增针对真实小红书 DOM 与 API 报文的测试样本和基准对比套件。

---

### English Release Notes

#### 🚀 Key Features & Improvements (Tailored for Xiaohongshu & Browser Automation)
1. **DOM & Web Page Interactive Action Pruner (`prune_dom.py`)**:
   - Designed specifically for remote browser control on complex Single Page Applications like Xiaohongshu Creator Center.
   - Strips SVG, scripts, styles, hidden containers, and obfuscated CSS classes to produce a lightweight Interactive Selector Tree, achieving **90%~98%** HTML token savings.
2. **Browser Session & Xiaohongshu API Response Optimizer (`optimize_browser_context.py`)**:
   - Filters bloated telemetry (`trace_id`, beacon trackers, redundant multi-res CDN images) from API payloads.
   - Condenses browser cookies to essential authentication tokens (`a1`, `web_session`, `webId`).
3. **Xiaohongshu Note & Creator Pipeline Token Optimizer (`compress_xhs_note.py`)**:
   - Enforces 20-character title constraints, monitors content token density, pre-scans compliance risk words, and synthesizes compact SEO tag matrices.
4. **Enhanced Benchmark Suite & Visual Metrics**:
   - Expanded real-world benchmark suite with browser automation datasets.

---

## [v1.0.1] - 2026-09-02

### 中文更新说明
- 跨平台控制台 UTF-8 兼容性增强（解决 Windows GBK 终端报错）。
- 智能目录与隐藏文件过滤优化。
- GitHub Actions 云端 7 天自动演进调度器集成。
- OpenAI Codex 与 GitHub Copilot 深度兼容规范。

---

## [v1.0.0] - 2026-09-02

### 中文说明
- 初始版本发布。
- 包含 4 大核心本地确定性压缩工具：AST 代码骨架提取、大型 JSON 数据压缩、终端日志去噪、以及 Token 预算评估。
