#!/usr/bin/env python3
"""自动扫描 index.html 的章节/结构行号，更新 AGENTS.md 中对应的数值。

用法：
    python3 update_agents_md.py           # 预览变更（dry-run）
    python3 update_agents_md.py --write   # 实际写入
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HTML = ROOT / "index.html"
MD = ROOT / "AGENTS.md"


def scan_html(path: Path) -> dict:
    """扫描 index.html，返回结构行号字典。"""
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    def line_of(pattern: str) -> int:
        for i, ln in enumerate(lines, 1):
            if re.search(pattern, ln):
                return i
        return 0

    # 结构元素
    style_end = line_of(r"</style>")
    nav_toc = line_of(r'<nav id="toc">')
    hero = line_of(r'<header class="hero">')
    script_start = line_of(r"<script>")
    script_end = line_of(r"</script>")

    # 章节起始行
    chapters = {}
    for i, ln in enumerate(lines, 1):
        m = re.match(r"<!-- ============ (\d+) ============ -->", ln)
        if m:
            chapters[int(m.group(1))] = i

    return {
        "style_end": style_end,
        "nav_toc": nav_toc,
        "hero": hero,
        "script_start": script_start,
        "script_end": script_end,
        "chapters": chapters,
        "total_lines": len(lines),
    }


def format_chapter_row(ch_num: int, ch_id: str, title: str, info: dict) -> str:
    """格式化章节表格的一行。"""
    line = info["chapters"].get(ch_num, 0)
    star = " ★" if ch_num in (3, 4, 6, 8, 13, 14, 15, 16, 18, 19) else ""
    return f"| {ch_num}{star} | `{ch_id}` | {title} | {line} |"


def update_agents_md(info: dict, dry_run: bool = True) -> str:
    """根据扫描结果生成更新后的 AGENTS.md 内容。"""
    text = MD.read_text(encoding="utf-8")
    lines = text.split("\n")
    new_lines = []
    i = 0

    while i < len(lines):
        ln = lines[i]

        # 更新总行数/大小描述
        if "单文件、自包含、离线" in ln and "index.html" in ln:
            size_kb = round(HTML.stat().st_size / 1024)
            ln = re.sub(
                r"约 \d+ 行 / \d+K",
                f"约 {info['total_lines']} 行 / {size_kb}K",
                ln,
            )
            new_lines.append(ln)
            i += 1
            continue

        # 更新 CSS 行号范围
        if "内联 CSS" in ln and "|" in ln and "7–" in ln:
            ln = re.sub(r"\d+–\d+", f"7–{info['style_end']}", ln)
            new_lines.append(ln)
            i += 1
            continue

        # 更新 nav#toc 行号
        if "侧边栏目录导航" in ln and "~" in ln:
            ln = re.sub(r"~\d+", f"~{info['nav_toc']}", ln)
            new_lines.append(ln)
            i += 1
            continue

        # 更新 hero 行号
        if "首屏 hero" in ln and "~" in ln:
            ln = re.sub(r"~\d+", f"~{info['hero']}", ln)
            new_lines.append(ln)
            i += 1
            continue

        # 更新 JS 行号范围
        if "内联 JS" in ln and "|" in ln and "~" in ln:
            ln = re.sub(
                r"~\d+–\d+",
                f"~{info['script_start']}–{info['script_end']}",
                ln,
            )
            new_lines.append(ln)
            i += 1
            continue

        # 更新章节表格行
        # 匹配模式: | 数字 | `c数字` | 标题 | 行号 |
        chapter_match = re.match(
            r"^\| (\d+)( ★)? \| `(c\d+)` \| (.+?) \| (\d+) \|$", ln
        )
        if chapter_match:
            ch_num = int(chapter_match.group(1))
            ch_id = chapter_match.group(3)
            title = chapter_match.group(4)
            new_line = format_chapter_row(ch_num, ch_id, title, info)
            # 保持一致的缩进
            new_lines.append(new_line)
            i += 1
            continue

        new_lines.append(ln)
        i += 1

    return "\n".join(new_lines)


def main():
    write = "--write" in sys.argv
    info = scan_html(HTML)

    print(f"扫描结果: {info['total_lines']} 行, {len(info['chapters'])} 章")
    for ch in sorted(info["chapters"]):
        print(f"  c{ch}: 第 {info['chapters'][ch]} 行")

    new_content = update_agents_md(info)

    if write:
        MD.write_text(new_content, encoding="utf-8")
        print(f"\n✅ 已写入 {MD}")
    else:
        # 对比差异
        old = MD.read_text(encoding="utf-8")
        if old == new_content:
            print("\n✅ 无需更新，行号已是最新。")
        else:
            print("\n📋 预览变更（运行 --write 实际写入）：")
            old_lines = old.split("\n")
            new_lines = new_content.split("\n")
            for i, (o, n) in enumerate(zip(old_lines, new_lines), 1):
                if o != n:
                    print(f"  L{i}:")
                    print(f"    - {o.strip()}")
                    print(f"    + {n.strip()}")


if __name__ == "__main__":
    main()
