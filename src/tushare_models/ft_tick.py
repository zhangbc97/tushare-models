# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FtTick(Base):
    """期货期权tick数据"""

    __tablename__: str = "ft_tick"
    __api_id__: ClassVar[int] = 235
    __api_name__: ClassVar[str] = "ft_tick"
    __api_title__: ClassVar[str] = "期货期权tick数据"
    __api_info_title__: ClassVar[str] = "期货期权tick数据"
    __api_path__: ClassVar[List[str]] = ["期货期权tick数据"]
    __api_path_ids__: ClassVar[List[int]] = []
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["symbol", "trade_time"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "symbol": {"type": "str", "required": True, "description": "期货期权代码"},
        "start_date": {"type": "datetime", "required": False, "description": "开始时间"},
        "end_date": {"type": "datetime", "required": False, "description": "结束时间"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "期货期权tick数据",
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

    symbol = Column("symbol", String(), nullable=False, default="", server_default=text("''"), comment="交易代码")
    trade_time = Column(
        "trade_time", String(), nullable=False, default="", server_default=text("''"), comment="交易时间"
    )
    trade_ms = Column("trade_ms", String(), nullable=False, default="", server_default=text("''"), comment="交易毫秒数")
    price = Column("price", String(), nullable=False, default="", server_default=text("''"), comment="当前价")
    vol = Column("vol", String(), nullable=False, default="", server_default=text("''"), comment="成交量")
    amount = Column("amount", String(), nullable=False, default="", server_default=text("''"), comment="成交金额")
    ask_p1 = Column("ask_p1", String(), nullable=False, default="", server_default=text("''"), comment="申卖价一")
    ask_v1 = Column("ask_v1", String(), nullable=False, default="", server_default=text("''"), comment="申卖量一")
    bid_p1 = Column("bid_p1", String(), nullable=False, default="", server_default=text("''"), comment="申买价一")
    bid_v1 = Column("bid_v1", String(), nullable=False, default="", server_default=text("''"), comment="申买量一")
    oi = Column("oi", String(), nullable=False, default="", server_default=text("''"), comment="持仓量")
