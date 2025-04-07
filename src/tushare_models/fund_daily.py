# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FundDaily(Base):
    """基金行情(含ETF)"""

    __tablename__: str = "fund_daily"
    __api_id__: ClassVar[int] = 127
    __api_name__: ClassVar[str] = "fund_daily"
    __api_title__: ClassVar[str] = "基金行情(含ETF)"
    __api_info_title__: ClassVar[str] = "场内基金日线行情"
    __api_path__: ClassVar[List[str]] = ["数据接口", "公募基金", "基金行情（含ETF）"]
    __api_path_ids__: ClassVar[List[int]] = [2, 18, 127]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "ts_code": {"type": "str", "required": False, "description": "基金代码"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "基金行情(含ETF)",
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
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    pre_close = Column(
        "pre_close", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="昨收盘价(元)"
    )
    open = Column("open", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="开盘价(元)")
    high = Column("high", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最高价(元)")
    low = Column("low", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最低价(元)")
    close = Column("close", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="收盘价(元)")
    change = Column("change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌(元)")
    pct_chg = Column("pct_chg", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌幅(%)")
    vol = Column("vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交量(手)")
    amount = Column(
        "amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交金额(千元)"
    )
