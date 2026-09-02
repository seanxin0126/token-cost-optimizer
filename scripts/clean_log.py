#!/usr/bin/env python3
"""
Token Cost Optimizer - Terminal & Build Log Denoised Filter
清洗终端命令输出，移除 ANSI 颜色码、进度条、重复下载日志，只保留错误关键堆栈与结论。
"""

import sys
import re
from pathlib import Path

# 确保 Windows 终端 UTF-8 兼容输出
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def clean_log_text(text: str) -> str:
    # 移除 ANSI 转义序列 (包括实际字节与字面量转义)
    ansi_escape = re.compile(r'(\x1B|\\u001b|\\033)(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    clean = ansi_escape.sub('', text)
    
    lines = clean.splitlines()
    filtered_lines = []
    
    skip_patterns = [
        re.compile(r'^\s*[\d\.]+\s*kB\s*[\d\.]+\s*kB/s'), # 下载速度
        re.compile(r'^\s*[-/\\]\s*fetching', re.IGNORECASE),
        re.compile(r'^\s*npm\s+http\s+fetch', re.IGNORECASE),
        re.compile(r'^\s*Downloading\s+', re.IGNORECASE),
        re.compile(r'\[=*>*-*\]'), # 进度条 [=====>------]
        re.compile(r'\[PROGRESS\]', re.IGNORECASE),
        re.compile(r'^\s*\[\s*\d+%\s*\]'), # 进度百分比
        re.compile(r'^\s*[\d\.]+\s*%\s*\(\d+/\d+\s*modules?\s*downloaded\)', re.IGNORECASE)
    ]
    
    for line in lines:
        if any(p.search(line) for p in skip_patterns):
            continue
        filtered_lines.append(line)
        
    # 去除连续空行
    result = []
    last_empty = False
    for line in filtered_lines:
        if not line.strip():
            if not last_empty:
                result.append(line)
                last_empty = True
        else:
            result.append(line)
            last_empty = False
            
    # 如果仍然很长，保留前 100 行和后 100 行（聚焦开始与结尾报错）
    if len(result) > 250:
        truncated = result[:100] + [f"\n... [已自动省略中间 {len(result) - 200} 行重复日志以节省 Token] ...\n"] + result[-100:]
        return "\n".join(truncated)
        
    return "\n".join(result)

def main():
    if len(sys.argv) < 2:
        print("Usage: python clean_log.py <log_file_or_text>")
        sys.exit(1)
        
    target = sys.argv[1]
    p = Path(target)
    if p.exists() and p.is_file():
        raw = p.read_text(encoding="utf-8", errors="replace")
    else:
        raw = target
        
    original_size = len(raw)
    cleaned = clean_log_text(raw)
    cleaned_size = len(cleaned)
    ratio = (1 - (cleaned_size / original_size)) * 100 if original_size > 0 else 0
    
    print(f"# === [日志去噪结果] 原始: {original_size} 字符 -> 压缩后: {cleaned_size} 字符 (节省 {ratio:.1f}%) ===")
    print(cleaned)

if __name__ == "__main__":
    main()
