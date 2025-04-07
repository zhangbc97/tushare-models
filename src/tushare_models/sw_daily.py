# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class SwDaily(Base):
    """申万行业指数日行情"""

    __tablename__: str = "sw_daily"
    __api_id__: ClassVar[int] = 327
    __api_name__: ClassVar[str] = "sw_daily"
    __api_title__: ClassVar[str] = "申万行业指数日行情"
    __api_info_title__: ClassVar[str] = "申万行业日线行情"
    __api_path__: ClassVar[List[str]] = ["数据接口", "指数专题", "申万行业指数日行情"]
    __api_path_ids__: ClassVar[List[int]] = [2, 93, 327]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "行业代码"},
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
            "comment": "申万行业指数日行情",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="指数代码")
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="指数名称")
    open = Column("open", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="开盘点位")
    low = Column("low", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最低点位")
    high = Column("high", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最高点位")
    close = Column("close", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="收盘点位")
    change = Column("change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌点位")
    pct_change = Column(
        "pct_change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌幅"
    )
    vol = Column("vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交量(万股)")
    amount = Column("amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交额(万元)")
    pe = Column("pe", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="市盈率")
    pb = Column("pb", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="市净率")
    float_mv = Column(
        "float_mv", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="流通市值(万元)"
    )
    total_mv = Column(
        "total_mv", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="总市值(万元)"
    )
    weight = Column("weight", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="权重")
