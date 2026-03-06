# 开发报告

## 完成的任务
- [x] Task 1: 新增 `greet.py`，实现 `greet(name)` 与 `farewell(name)`。
- [x] Task 2: 新增 `test_greet.py`，覆盖两个函数的返回值。

## 修改的文件
- `greet.py`: 添加问候与告别函数。
- `test_greet.py`: 添加基于 `unittest` 的单元测试。
- `dev-log/dev-report.md`: 记录本次开发、自测与审查结果。

## 自测结果
- 测试命令: `python3 -m unittest test_greet.py`
- 测试结果: 通过（2 个测试全部通过）
- 测试命令: `make test`
- 测试结果: 通过（现有仓库检查通过）

## Self-Review 发现与修复
- `dev-log/plan.md` 在当前仓库中不存在；本次根据 issue 描述直接实现最小变更，无额外问题。

## 注意事项
- 当前仓库未提供 `dev-log/plan.md`，也未见现有 Python 项目结构，因此采用最小独立实现。
