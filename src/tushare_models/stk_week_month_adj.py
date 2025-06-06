# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class StkWeekMonthAdj(Base):
    """周/月线复权行情(每日更新)"""

    __tablename__: str = "stk_week_month_adj"
    __api_id__: ClassVar[int] = 365
    __api_name__: ClassVar[str] = "stk_week_month_adj"
    __api_title__: ClassVar[str] = "周/月线复权行情(每日更新)"
    __api_info_title__: ClassVar[str] = "股票周/月线行情(复权--每日更新)"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "行情数据", "周/月线复权行情(每日更新)"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 15, 365]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "TS代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "freq": {"type": "str", "required": True, "description": "频率week周，month月"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "周/月线复权行情(每日更新)",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="股票代码")
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    freq = Column(
        "freq", String(), nullable=False, default="", server_default=text("''"), comment="频率(周week,月month)"
    )
    open = Column("open", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)开盘价")
    high = Column("high", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)最高价")
    low = Column("low", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)最低价")
    close = Column("close", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)收盘价")
    pre_close = Column(
        "pre_close",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="上一(周/月)收盘价【除权价，前复权】",
    )
    open_qfq = Column(
        "open_qfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="前复权(周/月)开盘价"
    )
    high_qfq = Column(
        "high_qfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="前复权(周/月)最高价"
    )
    low_qfq = Column(
        "low_qfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="前复权(周/月)最低价"
    )
    close_qfq = Column(
        "close_qfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="前复权(周/月)收盘价"
    )
    open_hfq = Column(
        "open_hfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="后复权(周/月)开盘价"
    )
    high_hfq = Column(
        "high_hfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="后复权(周/月)最高价"
    )
    low_hfq = Column(
        "low_hfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="后复权(周/月)最低价"
    )
    close_hfq = Column(
        "close_hfq", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="后复权(周/月)收盘价"
    )
    vol = Column("vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)成交量")
    amount = Column("amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)成交额")
    change = Column("change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="(周/月)涨跌额")
    pct_chg = Column(
        "pct_chg",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="(周/月)涨跌幅 【基于除权后的昨收计算的涨跌幅：(今收-除权昨收)/除权昨收 】",
    )
