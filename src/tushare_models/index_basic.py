# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class IndexBasic(Base):
    """指数基本信息"""

    __tablename__: str = "index_basic"
    __api_id__: ClassVar[int] = 94
    __api_name__: ClassVar[str] = "index_basic"
    __api_title__: ClassVar[str] = "指数基本信息"
    __api_info_title__: ClassVar[str] = "指数基本信息"
    __api_path__: ClassVar[List[str]] = ["数据接口", "指数专题", "指数基本信息"]
    __api_path_ids__: ClassVar[List[int]] = [2, 93, 94]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "指数代码"},
        "market": {"type": "str", "required": False, "description": "交易所或服务商"},
        "publisher": {"type": "str", "required": False, "description": "发布商"},
        "category": {"type": "str", "required": False, "description": "指数类别"},
        "name": {"type": "str", "required": False, "description": "指数名称"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "指数基本信息",
            # MySQL引擎
            "mysql_engine": "InnoDB",
            # StarRocks引擎
            "starrocks_primary_key": ",".join(__primary_key__),
            "starrocks_order_by": ",".join(__primary_key__),
            # Apache Doris引擎
            "doris_unique_key": __primary_key__,
            # Databend引擎
            "databend_cluster_by": __primary_key__,
        },
    )

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="TS代码")
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="简称")
    fullname = Column("fullname", String(), nullable=False, default="", server_default=text("''"), comment="指数全称")
    market = Column("market", String(), nullable=False, default="", server_default=text("''"), comment="市场")
    publisher = Column("publisher", String(), nullable=False, default="", server_default=text("''"), comment="发布方")
    index_type = Column(
        "index_type", String(), nullable=False, default="", server_default=text("''"), comment="指数风格"
    )
    category = Column("category", String(), nullable=False, default="", server_default=text("''"), comment="指数类别")
    base_date = Column(
        "base_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="基期"
    )
    base_point = Column("base_point", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="基点")
    list_date = Column(
        "list_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="发布日期"
    )
    weight_rule = Column(
        "weight_rule", String(), nullable=False, default="", server_default=text("''"), comment="加权方式"
    )
    desc = Column("desc", String(), nullable=False, default="", server_default=text("''"), comment="描述")
    exp_date = Column(
        "exp_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="终止日期"
    )
