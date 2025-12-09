
# Local Database & Web API Constitution


## Core Principles

### I. 本地数据库优先
所有核心数据必须首先存储于本地数据库，保证数据完整性、可控性与高可用。
*本地数据为一切业务与统计的基础。*

### II. API化
本地数据库的数据必须通过标准API接口对外暴露，接口需文档化、可测试、支持权限控制。
*API是系统集成与扩展的唯一入口。*

### III. Web端统计展示
必须开发Web端，调用API并展示数据库统计信息，界面需简洁、交互友好，统计逻辑清晰。
*Web端是数据价值的直接体现。*

### IV. 测试驱动开发（TDD）
所有数据库、API、Web端功能均需先编写测试用例，测试通过后方可上线。
*测试保障系统质量与可维护性。*

### V. 数据安全与隐私
所有数据传输与存储必须符合安全规范，敏感信息加密，接口需鉴权。
*安全是系统运行的底线。*


## 附加约束

- 技术栈建议：Python/Node.js + SQLite/PostgreSQL + FastAPI/Express + Vue/React。
- API需有OpenAPI/Swagger文档。
- Web端需支持基础图表与导出功能。
- 部署需支持本地与云端两种模式。


## 开发流程与质量门槛

- 需求评审后，先设计数据库结构与API接口。
- 所有代码需经Code Review，重点关注数据一致性与接口安全。
- 每次提交需通过自动化测试。
- 统计展示需有用户反馈环节。


## 治理规则

1. 本宪法高于其他开发规范，所有开发、评审、上线流程必须遵循。
2. 宪法修订需经团队讨论并记录修订理由与迁移方案。
3. 版本号采用MAJOR.MINOR.PATCH，原则调整为MAJOR，新增原则为MINOR，表述修订为PATCH。
4. 每次合并/发布前需检查与宪法一致性。


**Version**: 1.0.0 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09

<!--
Sync Impact Report
- Version change: N/A → 1.0.0
- 新增原则：本地数据库优先、API化、Web端统计展示、测试驱动开发、数据安全与隐私
- 新增约束与开发流程说明
- 所有模板需检查与新原则一致性（plan-template.md、spec-template.md、tasks-template.md）
- 无历史版本，Ratified/Amended均为今日
-->
