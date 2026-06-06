# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## 这个仓库是什么

一份**单文件、自包含、离线**的中文教程网页:`index.html`(约 2286 行 / 180K)。
内容是「Linux 命令 + Vim 从入门到进阶」,面向一位**每天在服务器上干活、但没系统学过 Linux** 的用户。

整个"代码库"就是这<strong>一个 HTML 文件</strong>。所有 CSS / JS 全部内联,**无任何外部依赖**(不引 CDN、字体、图片、库)。

> 关于"HTML 是否合适":对这个用途(一份可离线翻阅、可在浏览器排版精美呈现的讲解型手册)单文件 HTML 很合适。
> **不要**拆成多文件或引入构建工具——自包含、双击即开正是它的价值。下面的章节导航表就是为了让你**无需通读全文**即可定位编辑。

## 内容/风格约定(改动时遵守)

- **语言**:正文一律中文;命令、参数、代码标识符保持原样。
- **定位**:讲解型,**无互动测验/答题**。重点讲"命令怎么用、什么场景、易混点/坑",底层实现(内核、文件描述符细节)最多一两句带过。
- **深度基线**:读者会 `cd`/`ls` 等基础,但进阶参数(如 `ls -a`)要讲清。**每个用到的选项都要就近解释**(曾因漏解释被用户指出,如 `ls -l`、`ps aux`、`tmux -s`)。新增命令示例时,检查每个 flag 是否在附近注释或表格里说明。
- 带 `★` 的是用户特别看重的章节:管道重定向、grep/正则、find、远程传输、echo/变量/环境、组合配方、Shell 脚本、Vim、压缩归档、Git。

## 文件结构(行号会随编辑漂移,以锚点/标记为准)

| 区域 | 定位标记 | 约行号 |
|------|----------|--------|
| 内联 CSS(深色终端主题、变量在 `:root`) | `<style>` … `</style>` | 7–191 |
| 侧边栏目录导航 | `<nav id="toc">` | ~200 |
| 首屏 hero | `<header class="hero">` | ~230 |
| 各章正文 | `<!-- ===== N ===== -->` 注释分隔 | 见下表 |
| 内联 JS(复制按钮 / 目录滚动高亮 / 移动端菜单) | `<script>` … `</script>` | ~2244–2284 |

### 章节导航地图(改某章时直接按行号 Read,无需读全文)

| 章 | id | 标题 | 起始行 |
|----|----|------|--------|
| 1 | `c1` | 如何用这份教程 | 238 |
| 2 | `c2` | 文件与目录基础(含 ls 参数、**tree**、glob 通配符) | 296 |
| 3 ★ | `c3` | 管道与重定向 | 420 |
| 4 ★ | `c4` | grep 与正则 | 523 |
| 5 | `c5` | 文本三剑客与切分工具(cut/sort/uniq/sed/awk) | 613 |
| 6 ★ | `c6` | find 实战 | 662 |
| 7 | `c7` | 权限·进程·信号·磁盘(含 chmod/chown 归属、kill 信号、作业控制 `&`/`fg`) | 738 |
| 8 ★ | `c8` | 远程传输与打包(scp/rsync/curl/wget/tar,详见 c18) | 905 |
| 9 | `c9` | 会话保持与 Shell 效率(tmux 三层模型、history/Ctrl-R) | 980 |
| 10 | `c10` | SSH 进阶(config/免密/端口转发/跳板机) | 1075 |
| 11 | `c11` | 服务·日志·定时(systemctl/journalctl/crontab) | 1122 |
| 12 | `c12` | 排查类工具(ss/lsof/jq/watch/du) | 1162 |
| 13 ★ | `c13` | echo·变量·环境(`echo "..." >>`、引号、export、PATH) | 1200 |
| 14 ★ | `c14` | 组合命令实战配方 | 1274 |
| 15 ★ | `c15` | Shell 脚本基础 | 1353 |
| 16 ★ | `c16` | Vim 系统教学 | 1459 |
| 17 | `c17` | 速查附录(卡片式 cheatsheet,含 tar/zip、Git) | 1648 |
| 18 ★ | `c18` | 压缩与归档 tar/zip(gzip/bzip2/xz、管道传输、排除文件) | 1802 |
| 19 ★ | `c19` | Git 实战(含 worktree、分支/rebase、撤销、stash) | 1935 |

> 行号是编辑前的快照,可能漂移。精确定位用:`grep -n 'id="cN"' index.html`,或 `grep -n '<!-- ===== N' …`。

## 编辑这个 HTML 的约定

- **代码块语法高亮**靠 `<pre>` 里的 span class,改/加代码示例时沿用,保持配色一致:
  `.pr`=提示符 `$` · `.cm`=命令名 · `.fl`=选项/flag · `.st`=字符串 · `.op`=操作符(`| > >>`)· `.out`=模拟输出 · `.va`=变量 · `.cmt`=行内注释。
- **提示框**三种:`.box.warn`(⚠️ 坑)· `.box.tip`(💡 技巧)· `.box.note`(📖 原理)。表格用 `.tbl > table`;速查卡用 `.cards > .card`;纯 CSS 流程图用 `.flow`。
- **HTML 实体转义**:`<pre>`/`<code>` 里凡是字面的 `<` `>` `&` 必须写成 `&lt;` `&gt;` `&amp;`——重定向示例(`2>&1`、`>>`、`<`)最容易漏,漏了会破坏渲染。
- **新增章节**时三件事要同步:① 加 `<section class="chapter" id="cN">…</section>`;② 在 `<nav id="toc">` 加对应 `<a href="#cN">`;③ id 顺序连续。附录速查表(c17)也宜补上对应卡片。

## 校验(改完必跑)

无构建、无测试框架。改完用以下方式自检:

```bash
# ① 标签配对(开/闭数量必须相等)
for t in div pre table section; do echo "$t: $(grep -oc "<$t" index.html)/$(grep -oc "</$t>" index.html)"; done

# ② 确认仍无外部依赖(应无输出)
grep -noE 'src="http|href="http|cdn\.|googleapis|<script src|<link [^>]*href="http' index.html

# ③ 章节 id 与目录锚点一一对应(两行应一致)
grep -oE 'id="c[0-9]+"' index.html | grep -oE 'c[0-9]+' | sort -V | uniq | tr '\n' ' '; echo
grep -oE 'href="#c[0-9]+"' index.html | grep -oE 'c[0-9]+' | sort -V | uniq | tr '\n' ' '; echo
```

## 预览(WSL → Windows 浏览器)

本仓库在 WSL(Ubuntu-24.04)里,用户用 **Windows 浏览器**打开。地址:

```
\\wsl.localhost\Ubuntu-24.04\home\tallmessiwu\codes\linux-tutorial\index.html
```

或从 WSL 直接调起:`explorer.exe index.html`(资源管理器路径前缀同上)。
