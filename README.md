# demo-notes

一个用来管理读书笔记的小工具。命令行录入，SQLite 存储，支持按标签检索和导出 Markdown。

## 功能

- 快速录入：一行命令记一条读书笔记
- 标签检索：按标签、按书名单条件筛选
- 一键导出：把选中笔记导出成 Markdown 文件

## 快速开始

```bash
pip install -r requirements.txt
python src/notes.py add "《原则》第 3 章：痛苦 + 反思 = 进步" --tag 认知
python src/notes.py list --tag 认知
python src/notes.py export --tag 认知 --out notes.md
```

## 目录结构

```
src/        命令行入口与核心逻辑
docs/       设计文档与路线图
tests/      单元测试
```

## 状态

MVP 阶段，本地可用，导出功能还在打磨。
