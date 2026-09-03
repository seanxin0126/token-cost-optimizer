---
name: token-cost-optimizer
description: 极限节省与压缩 Token 开销工具库（Token Cost Optimizer）。支持 AST 代码骨架提取、大型 JSON 结构压缩、终端日志去噪、浏览器 DOM/网页可交互元素极致精简（专为小红书等平台远程浏览器控制打造）、网络 API 报文/Cookie 鉴权瘦身及 Token 预算评估。在处理长代码、大 JSON、大日志、复杂网页 DOM 及远程浏览器自动化任务前激活此技能。
metadata:
  builtin_skill_version: "1.1.0"
  version: "1.1.0"
  purpose: "Drastic Token Compression & Cost Optimization for Code, Data, Logs & Browser Automation"
---

# Token Cost Optimizer 极度节流与成本优化工具套件 (v1.1.0)

本技能专为在长任务、复杂工程及**远程浏览器自动化控制（如小红书创作者平台、电商及社交媒体自动化）**中实现 **50% ~ 98% 的 Token 压缩** 而设计，原生兼容 **Google Antigravity、OpenAI Codex、GitHub Copilot、Claude Code、Cursor、Windsurf、Cline、Dify** 等主流智能体，通过本地确定性 Python 工具替代盲目全量读入。

---

## 🛠️ 核心工具脚本规程

### 1. 浏览器 DOM 与网页交互树精简（节省 90%~98% 网页 Token）
在远程通过浏览器控制**小红书创作者平台（creator.xiaohongshu.com）**、网页登录、发帖、操作表单时，严禁将数万行庞大 HTML/DOM 直接塞入模型，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/prune_dom.py <html_file_path>
```
* **效果**：自动剥离所有 `<svg>`、`<script>`、`<style>`、隐藏元素与混淆 Class，精准提取带推荐 CSS Selector 的**高价值可交互元素清单（Interactive Action Map）**。

### 2. 浏览器会话、Cookies 鉴权与小红书 API 瘦身（节省 70%~95% 报文 Token）
当处理小红书抓包响应、发布接口 JSON 或恢复浏览器登录 Session 时，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/optimize_browser_context.py <json_or_cookie_path>
```
* **效果**：剔除 `trace_id`、打点、冗余 CDN 图片分辨率，仅保留核心鉴权 Token（`a1`, `web_session`, `webId`）与关键业务字段。

### 3. 小红书文案与发布流水线 Token 优化
在自动化发布小红书笔记前，进行字符限制、敏感风控词预检与 Token 预算评估：
```bash
python .agents/skills/token-cost-optimizer/scripts/compress_xhs_note.py --title "<标题>" --content "<正文>" --tags "标签1,标签2"
```
* **效果**：自动校验 20 字标题上限、合并冗余换行、预检违禁敏感词、提取精炼 SEO Tag 矩阵。

### 4. 代码骨架提取（节省 80%~95% 代码 Token）
在仅需了解模块架构、调用关系或接口签名时，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/prune_code.py <file_path>
```
* **效果**：自动解析 AST，提取模块 Docstring、类定义、方法签名与参数，剔除具体实现。

### 5. 大型 JSON 结构压缩（节省 90%+ 数据 Token）
当面对几十万行的复杂 JSON 数据文件时，严禁全量读入，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/compress_json.py <json_path>
```
* **效果**：自动提取数据层级 Schema、字段类型及典型 Sample，保留结构全貌同时压缩体积。

### 6. 终端与构建日志去噪（节省 50%+ 调试 Token）
当运行构建、测试或安装命令产生大量输出时，运行：
```bash
python .agents/skills/token-cost-optimizer/scripts/clean_log.py <log_file_or_text>
```
* **效果**：去除 ANSI 转义色彩码、下载进度条、轮询日志，保留错误堆栈与退出结论。

### 7. 任务 Token 预算精确评估
在执行长任务前，扫描目标文件或目录的 Token 占用：
```bash
python .agents/skills/token-cost-optimizer/scripts/estimate_tokens.py <path>
```
* **效果**：提供准确的 Token 消耗预估，辅助 `autonomous-meta-workflow` 做出准入决策。
