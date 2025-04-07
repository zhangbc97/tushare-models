# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class GgtDaily(Base):
    """港股通每日成交统计"""

    __tablename__: str = "ggt_daily"
    __api_id__: ClassVar[int] = 196
    __api_name__: ClassVar[str] = "ggt_daily"
    __api_title__: ClassVar[str] = "港股通每日成交统计"
    __api_info_title__: ClassVar[str] = "港股通每日成交统计"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "行情数据", "港股通每日成交统计"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 15, 196]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["daily"]
    __primary_key__: ClassVar[List[str]] = ["trade_date"]
    __start_date__: ClassVar[str | None] = "2014-11-17"
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "港股通每日成交统计",
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

    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    buy_amount = Column(
        "buy_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="买入成交金额(亿元)"
    )
    buy_volume = Column(
        "buy_volume", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="买入成交笔数(万笔)"
    )
    sell_amount = Column(
        "sell_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="卖出成交金额(亿元)"
    )
    sell_volume = Column(
        "sell_volume", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="卖出成交笔数(万笔)"
    )
