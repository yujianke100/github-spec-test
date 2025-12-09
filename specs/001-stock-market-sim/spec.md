
# Feature Specification: 股票市场数据统计网站

**Feature Branch**: `[001-stock-market-sim]`  
**Created**: 2025-12-09  
**Status**: Draft  
**Input**: User description: "搭建股票市场数据统计网站，包含本地虚拟数据库（模拟一周100用户对50股票买卖及价格波动），Web端支持时间区间、股票选择、查询与统计展示（价格曲线、买卖量、整体盈亏）。"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - 查询与统计展示 (Priority: P1)

用户在Web页面选择统计时间区间和股票后，点击查询按钮，系统丝滑展示该股票在区间内的价格变化曲线、所有用户的买入卖出量及整体盈亏。

**Why this priority**: 这是核心业务场景，直接体现产品价值。

**Independent Test**: 通过Web端输入时间区间和股票，点击查询，页面正确展示所有统计信息。

**Acceptance Scenarios**:

1. **Given** 数据库已生成模拟数据，**When** 用户选择时间区间和股票并点击查询，**Then** 页面展示该股票价格曲线、买卖量、整体盈亏。
2. **Given** 用户未选择股票，**When** 点击查询，**Then** 页面提示需选择股票。

---

### User Story 2 - 虚拟数据库生成 (Priority: P2)

开发者可一键生成本地虚拟数据库，包含一周内100用户对50只股票的买卖记录及价格波动。

**Why this priority**: 数据库是所有统计与展示的基础。

**Independent Test**: 运行生成脚本后，数据库内有完整模拟数据，结构与需求一致。

**Acceptance Scenarios**:

1. **Given** 无数据库，**When** 运行生成命令，**Then** 本地生成包含所需数据的数据库文件。
2. **Given** 已有数据库，**When** 重新生成，**Then** 数据被覆盖为新模拟数据。

---

### User Story 3 - 美观Web界面 (Priority: P3)

用户访问Web端，界面美观，交互流畅，支持输入时间、股票、查询，统计结果动画展示。

**Why this priority**: 良好体验提升用户满意度和产品竞争力。

**Independent Test**: 页面UI符合现代审美，交互无卡顿，统计结果有动画。

**Acceptance Scenarios**:

1. **Given** 页面加载，**When** 用户操作输入与查询，**Then** 页面无明显延迟，统计结果动画展示。
2. **Given** 页面异常，**When** 发生错误，**Then** 友好提示用户。

---

## Functional Requirements

1. 必须能在本地一键生成包含一周内100用户、50只股票、买卖记录与价格波动的数据库。
2. 必须提供API接口，支持按时间区间、股票查询价格曲线、买卖量、整体盈亏。
3. Web端需支持时间区间、股票选择输入，查询后丝滑展示统计结果（含动画）。
4. 所有数据与接口需有自动化测试，保证准确性。
5. 页面需有异常与无数据提示。

## Success Criteria

- 用户可在30秒内完成一次查询并看到统计结果。
- 统计结果准确率100%，与数据库一致。
- 页面交互无明显卡顿，动画展示流畅。
- 100%功能点有自动化测试覆盖。
- 用户反馈满意度高于80%（如有收集）。


## Key Entities

- 用户（user_id）
- 股票（stock_id, 名称）
- 买卖记录（user_id, stock_id, 时间, 类型[买/卖], 数量, 价格）
- 股票价格（stock_id, 时间, 价格）

## Assumptions

- 所有数据均为本地sqlite数据库模拟，无需真实外部数据。
- 统计时间区间、股票选择均由数据库内数据范围决定。
- Web端仅需支持单一页面展示，无需多端适配。

## Edge Cases

- 查询区间无数据时，页面应提示“无数据”而非报错。
- 用户输入非法时间区间（如结束早于开始）时，需有友好提示。
- 股票选择为空时，禁止查询并提示。
- 数据库文件丢失或损坏时，需有初始化或重建入口。

## Implementation Notes

- 数据库建议采用sqlite，结构简单，便于本地开发。
- 后端建议用Flask（或FastAPI）暴露API，接口简单明了。
- 前端建议用Vue或React，UI可用Antd、Element等常用组件库。
- 统计展示用echarts或chart.js，动画流畅。
- 不要求多用户登录、权限、复杂部署。
- 只需支持单页面查询与展示，界面美观简洁即可。

