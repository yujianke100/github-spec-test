# 股票市场数据统计网站

本项目为本地虚拟股票市场数据统计与可视化演示，支持一键生成数据、API查询、Web端动画展示。

## 技术栈
- 后端：Python 3.11 + Flask + sqlite3 + pandas
- 前端：Vue3 + Vite + ECharts + axios
- 测试：pytest、@vue/test-utils、Vitest

## 快速上手

1. 克隆仓库并进入目录
2. 创建Python虚拟环境并安装依赖
	```sh
	mamba create -n stocksite python=3.11
	mamba activate stocksite
	mamba install flask pandas sqlite
	cd backend && python db.py  # 生成数据库
	python app.py  # 启动后端
	```
3. 前端安装依赖并启动
	```sh
	cd ../frontend
	npm install
	npm run dev
	# 浏览器访问 http://localhost:5173
	```
4. 运行测试
	- 后端：`pytest backend/tests/`
	- 前端：`cd frontend && npx vitest run`

## 目录结构
- backend/  后端API与数据生成
- frontend/ 前端页面与组件
- specs/    需求、计划、测试文档

## 主要功能
- 一键生成本地虚拟股票数据（100用户、50股票、一周）
- 支持按股票与时间区间查询，返回价格曲线、买卖量、盈亏
- Web端动画展示统计结果，交互流畅

## 贡献与反馈
欢迎提交issue或PR改进本项目。
# github-spec-test