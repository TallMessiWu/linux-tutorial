# Linux 命令 + Vim · 从入门到进阶

一份**单文件、自包含、离线可用**的中文教程网页。覆盖 Linux 常用命令和 Vim 系统教学，面向每天在服务器上干活、但没系统学过 Linux 的用户。

## 特点

- **零依赖** — 不引 CDN、字体、图片、库，双击即开
- **离线可用** — 下载到本地即阅，无需网络
- **深色主题** — 模仿终端风格，护眼易读
- **侧边栏导航** — 快速跳转各章节
- **速查附录** — 卡片式 cheatsheet，方便快速查阅
- **代码高亮** — 命令/参数/输出各用不同颜色区分

## 内容概览

| 章节 | 内容 |
|------|------|
| 1 | 如何用这份教程 |
| 2 | 文件与目录基础（ls、tree、glob 通配符） |
| 3 ★ | 管道与重定向 |
| 4 ★ | grep 与正则 |
| 5 | 文本三剑客与切分工具（cut/sort/uniq/sed/awk） |
| 6 ★ | find 实战 |
| 7 | 权限·进程·信号·磁盘（chmod、kill、作业控制） |
| 8 ★ | 远程传输与打包（scp/rsync/curl/wget/tar） |
| 9 | 会话保持与 Shell 效率（tmux、history/Ctrl-R） |
| 10 | SSH 进阶（config/免密/端口转发/跳板机） |
| 11 | 服务·日志·定时（systemctl/journalctl/crontab） |
| 12 | 排查类工具（ss/lsof/jq/watch/du） |
| 13 ★ | echo·变量·环境 |
| 14 ★ | 组合命令实战配方 |
| 15 ★ | Shell 脚本基础 |
| 16 ★ | Vim 系统教学 |
| 17 | 速查附录 |

> ★ 为用户特别看重的重点章节

## 使用方式

### 直接打开

```bash
# WSL 下用 Windows 浏览器打开
explorer.exe index.html

# 或用路径直接访问
# \\wsl.localhost\Ubuntu-24.04\home\tallmessiwu\codes\linux-tutorial\index.html
```

### GitHub Pages

访问 `https://tallmessiwu.github.io/linux-tutorial/` 在线阅读。

## 面向读者

- 每天在服务器上操作，但没系统学过 Linux
- 会 `cd`/`ls` 基础，想掌握进阶用法
- 想系统学 Vim 但不想啃厚书
- 需要一本离线可查的命令速查手册

## 技术细节

整个教程是一个约 1800 行的单 HTML 文件，所有 CSS/JS 全部内联，无任何外部依赖。代码块使用 `<pre>` + `<span>` 实现语法高亮，配色统一为深色终端主题。
