# Implementation Plan: 股票市场数据统计网站

**Branch**: `001-stock-market-sim` | **Date**: 2025-12-09 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-stock-market-sim/spec.md`

## Summary

本项目旨在快速搭建一个本地股票市场数据统计网站，包含：
- 本地sqlite数据库，模拟一周内100用户对50只股票的买卖及价格波动。
- Flask API，提供按时间区间和股票查询统计数据的接口。
- Vue/React前端，支持时间区间、股票选择，丝滑展示价格曲线、买卖量、盈亏。
- 只需单页面展示，界面美观简洁，动画流畅。

## Technical Context

**Language/Version**: Python 3.13（后端），JavaScript/TypeScript（前端）  
**Primary Dependencies**: Flask, sqlite3, pandas, Vue3 或 React, ECharts/Chart.js, Axios  
**Storage**: 本地sqlite数据库  
**Testing**: pytest（后端），Jest/Vitest（前端）  
**Target Platform**: Linux本地开发环境，现代浏览器  
**Project Type**: web  
**Performance Goals**: 查询响应<1s，页面渲染<1s  
**Constraints**: 单机本地运行，界面美观，动画流畅  
**Scale/Scope**: 100用户、50股票、一周数据，单页面Web端

## Constitution Check

- 必须本地数据库优先，API化，Web端展示，测试驱动，数据安全。
- 不引入多余复杂度，不做多用户登录、权限、分布式等。
- 所有功能均需有自动化测试。
- 代码需经Code Review。

## Project Structure

### Documentation (this feature)

```
specs/001-stock-market-sim/
├── plan.md              # 本文件
├── research.md          # 研究与选型
├── data-model.md        # 数据模型
├── quickstart.md        # 快速上手
├── contracts/           # API接口定义
└── tasks.md             # 任务分解
```

### Source Code (repository root)

```
backend/
  ├── app.py             # Flask主程序
  ├── db.py              # 数据库生成与操作
  ├── api.py             # API路由
  ├── tests/             # 后端测试
frontend/
  ├── src/
  │   ├── App.vue/jsx    # 主页面
  │   ├── components/    # 组件
  │   ├── api/           # API请求
  │   └── utils/         # 工具
  ├── public/
  └── tests/             # 前端测试
```

---

## Phase 0: Outline & Research

### 需明确/研究点（已明确）
- 虚拟数据生成逻辑：
  - 股票初始价格为[20, 200]区间随机，后续每5分钟波动一次，涨跌幅服从正态分布（均值0，标准差1%），保证价格不为负。
  - 100个用户，每人每天随机买入/卖出1~5次，买卖股票、数量、价格均随机。
  - 买卖记录与价格表均带时间戳，时间范围为一周。
- 前端选型：Vue3 + Vite + ECharts，轻量、易用、动画丰富。
- API接口格式与数据结构：
  - /api/stocks  获取所有股票列表
  - /api/query   POST，参数：start_time, end_time, stock_id，返回：
    - 价格曲线（[{time, price}]）
    - 买入量/卖出量（[{time, buy_volume, sell_volume}]）
    - 盈亏（总买入金额、总卖出金额、净盈亏）

### 研究任务（已定案）
- 虚拟数据生成采用正态分布波动+均匀分布买卖行为，简单易实现。
- 前端采用Vue3+ECharts，开发效率高，动画丰富。
- API接口采用RESTful风格，数据结构清晰，便于前后端分离。

---

## Phase 1: Design & Contracts

- sqlite表结构：
  - users(user_id INTEGER PRIMARY KEY)
  - stocks(stock_id INTEGER PRIMARY KEY, name TEXT)
  - prices(id INTEGER PRIMARY KEY, stock_id INTEGER, time DATETIME, price REAL)
  - trades(id INTEGER PRIMARY KEY, user_id INTEGER, stock_id INTEGER, time DATETIME, type TEXT, volume INTEGER, price REAL)
- API接口：
  - GET /api/stocks  → [{stock_id, name}]
  - POST /api/query  → {价格曲线, 买卖量, 盈亏}
    - 请求参数：{start_time, end_time, stock_id}
    - 返回：{
        prices: [{time, price}],
        volumes: [{time, buy_volume, sell_volume}],
        pnl: {total_buy, total_sell, net_profit}
      }
- 前端页面结构：
  - 输入区：时间区间选择、股票下拉框、查询按钮
  - 展示区：价格曲线图、买卖量柱状图、盈亏数字/图表
  - 交互：查询时loading动画，结果丝滑展示，异常友好提示
- 测试用例：
  - 数据库生成后，数据量、分布、时间范围正确
  - API接口返回结构、数据准确
  - 前端输入、查询、展示流程无误，边界情况有提示

---

## 质量门槛
- 只需本地sqlite+Flask+Vue/React，结构简单，易于维护
- 不引入多余依赖与复杂度
- 代码、接口、页面均需有自动化测试
- UI需美观、交互流畅

---

## 备注
- 后续可根据实际需求扩展多用户、权限、部署等功能，但本期不做
