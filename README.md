# tushare-models

## 项目概述

tushare-models 是一个使用 SQLAlchemy ORM 定义的 Tushare 数据接口模型集合。该项目提供了与 Tushare 金融数据服务 API 交互所需的数据模型定义，便于数据的查询、存储和分析。

## 核心组件

### 基础架构 (core/)

核心模块提供了各种 ORM 相关的基础功能：

#### base.py

定义了所有 Tushare 模型的基础类:

- `TushareModelMixin`: 包含所有 Tushare 相关的类属性，如 API ID、API 名称、权限需求等
- `Base`: 继承自 SQLAlchemy 的 `DeclarativeBase` 和 `TushareModelMixin`，为所有模型提供统一的基类

#### dialect.py

提供了对不同数据库方言的支持和定制:

- `TSDatabendDDLCompiler`: 为 Databend 数据库定制的 DDL 编译器
- `TSStarRocksDDLCompiler`: 为 StarRocks 数据库定制的 DDL 编译器
- 支持多种数据库引擎，包括 ClickHouse、DuckDB、MySQL 等

#### dml.py

提供了数据操作语言 (DML) 相关的功能扩展:

- `Replace`: 扩展了 `Insert` 操作，提供 `REPLACE INTO` 功能，用于数据更新或插入操作
- 提供链式调用接口，支持 `on` 子句的定制

### 数据类型

项目使用了多种数据类型:

- `Integer`: 整数类型
- `Float`: 浮点数类型
- `String`: 字符串类型
- `Date`: 日期类型
- `DateTime`: 日期时间类型

## 数据库适配支持

该项目支持多种数据库系统，使用 SQLAlchemy 的方言机制进行适配：

- **ClickHouse**: 面向列的高性能分析型数据库
- **Databend**: 云原生分析型数据库
- **StarRocks**: 分布式 MPP 数据库
- **MySQL**: 传统的关系型数据库
- **DuckDB**: 嵌入式分析型数据库
 
每种数据库都有专门的适配器，可根据实际需求选择合适的数据库后端。使用方法示例：

```python
# ClickHouse 连接
engine = create_engine('clickhouse+http://username:password@host:port/database')

# Databend 连接
engine = create_engine('databend://username:password@host:port/database')

# StarRocks 连接
engine = create_engine('starrocks://username:password@host:port/database')

# MySQL 连接
engine = create_engine('mysql+pymysql://username:password@host:port/database')

# DuckDB 连接
engine = create_engine('duckdb:///path/to/database.db')
```

## 模型示例

以下是项目中模型定义的示例:

```python
class FutMapping(Base):
    """期货主力与连续合约"""
    
    # Tushare API 相关信息
    __api_name__ = "fut_mapping"
    __api_title__ = "期货主力与连续合约"
    
    # 数据表字段定义
    ts_code = Column(String, comment='合约代码')
    trade_date = Column(Date, comment='交易日期')
    mapping_ts_code = Column(String, comment='映射合约代码')
    
    # 主键定义
    __table_args__ = (
        PrimaryKeyConstraint('ts_code', 'trade_date'),
        {}
    )
```

## 使用方法

### 初始化连接

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tushare_models.core import Base

# 创建数据库引擎
engine = create_engine('sqlite:///tushare_data.db')
# 创建所有表
Base.metadata.create_all(engine)
# 创建会话
Session = sessionmaker(bind=engine)
session = Session()
```

### 查询数据

```python
from sqlalchemy import select
from tushare_models import StockBasic

# 查询股票基本信息 (使用 SQLAlchemy 2.0 API)
stmt = select(StockBasic).where(StockBasic.market == '主板')
stocks = session.execute(stmt).scalars().all()
for stock in stocks:
    print(f"{stock.ts_code}: {stock.name}")
```

### 插入/更新数据

```python
from tushare_models.core.dml import upsert
from tushare_models import DailyPrice

# 使用upsert函数插入或更新数据
stmt = upsert(DailyPrice).values(
    ts_code='000001.SZ',
    trade_date='2023-01-01',
    open=10.5,
    high=11.2,
    low=10.3,
    close=11.0
)
session.execute(stmt)
session.commit()
```

## 项目扩展

可以通过继承 `Base` 类来创建自定义的数据模型:

```python
from tushare_models.core import Base, String, Float, Date
from sqlalchemy import Column, PrimaryKeyConstraint

class MyCustomModel(Base):
    """自定义模型"""
    __api_name__ = "custom_api"
    
    code = Column(String, comment='代码')
    value = Column(Float, comment='数值')
    date = Column(Date, comment='日期')
    
    __table_args__ = (
        PrimaryKeyConstraint('code', 'date'),
        {}
    )