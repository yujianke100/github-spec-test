# 快速上手：股票市场数据统计网站

## 环境准备
- Python 3.11
- Node.js 16+
- mamba/conda、npm

## 后端启动
```sh
mamba create -n stocksite python=3.11
mamba activate stocksite
mamba install flask pandas sqlite
cd backend
python db.py   # 生成数据库
python app.py  # 启动API服务
```

## 前端启动
```sh
cd ../frontend
npm install
npm run dev
# 浏览器访问 http://localhost:5173
```

## 运行测试
- 后端：pytest backend/tests/
- 前端：cd frontend && npx vitest run

## 常见问题
- 如前端无法获取API数据，请确认vite.config.js已配置API代理并重启前端服务。
- 数据库损坏可删除 backend/stocksite.db 后重新生成。

## 目录说明
- backend/  后端API与数据生成
- frontend/ 前端页面与组件
- specs/    需求、计划、测试文档
