# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class EcoCal(Base):
    """全球财经事件"""

    __tablename__: str = "eco_cal"
    __api_id__: ClassVar[int] = 233
    __api_name__: ClassVar[str] = "eco_cal"
    __api_title__: ClassVar[str] = "全球财经事件"
    __api_info_title__: ClassVar[str] = "财经日历"
    __api_path__: ClassVar[List[str]] = ["数据接口", "债券专题", "全球财经事件"]
    __api_path_ids__: ClassVar[List[int]] = [2, 184, 233]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["date", "time", "event"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "date": {"type": "str", "required": False, "description": "日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "currency": {"type": "str", "required": False, "description": "货币代码"},
        "country": {"type": "str", "required": False, "description": "国家"},
        "event": {"type": "str", "required": False, "description": "事件"},
        "is_new": {"type": "str", "required": False, "description": "是否最新"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "全球财经事件",
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

    date = Column("date", String(), nullable=False, default="", server_default=text("''"), comment="日期")
    time = Column("time", String(), nullable=False, default="", server_default=text("''"), comment="时间")
    currency = Column("currency", String(), nullable=False, default="", server_default=text("''"), comment="货币代码")
    country = Column("country", String(), nullable=False, default="", server_default=text("''"), comment="国家")
    event = Column("event", String(), nullable=False, default="", server_default=text("''"), comment="经济事件")
    value = Column("value", String(), nullable=False, default="", server_default=text("''"), comment="今值")
    pre_value = Column("pre_value", String(), nullable=False, default="", server_default=text("''"), comment="前值")
    fore_value = Column("fore_value", String(), nullable=False, default="", server_default=text("''"), comment="预测值")
