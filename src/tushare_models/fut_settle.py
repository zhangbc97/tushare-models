# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FutSettle(Base):
    """每日结算参数"""

    __tablename__: str = "fut_settle"
    __api_id__: ClassVar[int] = 141
    __api_name__: ClassVar[str] = "fut_settle"
    __api_title__: ClassVar[str] = "每日结算参数"
    __api_info_title__: ClassVar[str] = "结算参数"
    __api_path__: ClassVar[List[str]] = ["数据接口", "期货数据", "每日结算参数"]
    __api_path_ids__: ClassVar[List[int]] = [2, 134, 141]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = "2012-01-04"
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "ts_code": {"type": "str", "required": False, "description": "合约代码"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "exchange": {"type": "str", "required": False, "description": "交易所代码"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "每日结算参数",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="合约代码")
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    settle = Column("settle", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="结算价")
    trading_fee_rate = Column(
        "trading_fee_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="交易手续费率"
    )
    trading_fee = Column(
        "trading_fee", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="交易手续费"
    )
    delivery_fee = Column(
        "delivery_fee", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="交割手续费"
    )
    b_hedging_margin_rate = Column(
        "b_hedging_margin_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="买套保交易保证金率",
    )
    s_hedging_margin_rate = Column(
        "s_hedging_margin_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="卖套保交易保证金率",
    )
    long_margin_rate = Column(
        "long_margin_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="买投机交易保证金率",
    )
    short_margin_rate = Column(
        "short_margin_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="卖投机交易保证金率",
    )
    offset_today_fee = Column(
        "offset_today_fee", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="平今仓手续率"
    )
    exchange = Column("exchange", String(), nullable=False, default="", server_default=text("''"), comment="交易所")
