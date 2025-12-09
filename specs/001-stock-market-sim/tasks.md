---
description: "Tasks for 股票市场数据统计网站"
---

# Tasks: 股票市场数据统计网站

**Input**: Design documents from `/specs/001-stock-market-sim/`
**Prerequisites**: plan.md, spec.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: 项目初始化与基础结构

- [ ] T001 创建 backend/ 与 frontend/ 目录结构
- [ ] T002 使用 mamba/conda 创建 Python 虚拟环境（如：mamba create -n stocksite python=3.11）
- [ ] T003 在虚拟环境中安装 Flask、pandas、sqlite3（mamba install flask pandas sqlite）
- [ ] T004 安装 Node.js（如未安装，建议用 nvm 安装 LTS 版本）
- [ ] T005 初始化前端项目（Vue3 + Vite + ECharts），如需可先安装 yarn（npm i -g yarn）
- [ ] T006 [P] 配置后端与前端的 lint/format 工具

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: 所有用户故事前置的基础能力

- [ ] T005 设计并实现 sqlite 数据库结构于 backend/db.py
- [ ] T006 [P] 实现虚拟数据生成脚本于 backend/db.py
- [ ] T007 [P] 编写数据库生成与重建的自动化测试于 backend/tests/test_db.py
- [ ] T008 [P] 实现基础 Flask 启动与健康检查接口于 backend/app.py

---

## Phase 3: [US2] 虚拟数据库生成

**Goal**: 一键生成本地虚拟数据库，含一周100用户50股票买卖及价格波动
**Independent Test Criteria**: 运行生成脚本后，数据库结构与数据量、分布、时间范围均正确

- [ ] T009 [US2] 完善虚拟数据生成逻辑（价格正态波动、用户买卖行为）于 backend/db.py
- [ ] T010 [P] [US2] 生成初始数据并写入数据库，支持重建
- [ ] T011 [P] [US2] 自动化测试：数据分布、时间范围、边界情况于 backend/tests/test_db.py

---

## Phase 4: [US1] 查询与统计展示

**Goal**: 支持按时间区间、股票查询统计，返回价格曲线、买卖量、盈亏
**Independent Test Criteria**: Web端输入后，能正确展示所有统计信息

- [ ] T012 [US1] 设计并实现 /api/stocks 与 /api/query 接口于 backend/api.py
- [ ] T013 [P] [US1] 编写接口自动化测试于 backend/tests/test_api.py
- [ ] T014 [US1] 前端实现股票、时间区间选择与查询表单于 frontend/src/components/QueryForm.vue
- [ ] T015 [P] [US1] 前端实现价格曲线、买卖量、盈亏展示组件于 frontend/src/components/StatsCharts.vue
- [ ] T016 [P] [US1] 前后端联调，确保查询与展示流程丝滑
- [ ] T017 [P] [US1] 前端边界与异常提示（无数据、参数非法等）于 frontend/src/components/QueryForm.vue

---

## Phase 5: [US3] 美观Web界面

**Goal**: 单页面美观、交互流畅，动画展示统计结果
**Independent Test Criteria**: UI现代美观，交互无卡顿，动画流畅

- [ ] T018 [US3] 设计并实现主页面布局于 frontend/src/App.vue
- [ ] T019 [P] [US3] 优化UI样式与动画效果于 frontend/src/components/StatsCharts.vue
- [ ] T020 [P] [US3] 前端自动化测试：UI渲染、交互、动画于 frontend/tests/

---

## Phase 6: Polish & Cross-Cutting

- [ ] T021 优化数据库与API性能，确保查询<1s
- [ ] T022 [P] 增加README与快速上手文档于 specs/001-stock-market-sim/quickstart.md
- [ ] T023 [P] 代码Review与最终验收

---

## Dependencies

- Phase 1、2为所有后续任务基础，需先完成
- US2（数据库生成）可与US1（API与前端）并行推进，US3（美观UI）可与US1后期并行
- Polish阶段可与部分测试、文档并行

## Parallel Execution Examples

- T004、T006、T007、T010、T011 可并行
- T013、T015、T017、T019、T020 可并行

## Implementation Strategy

- 先实现MVP：数据库生成+API+基础前端查询与展示
- 后续增量完善UI、动画、测试与文档
