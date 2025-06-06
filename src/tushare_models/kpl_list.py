# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class KplList(Base):
    """榜单数据(开盘啦)"""

    __tablename__: str = "kpl_list"
    __api_id__: ClassVar[int] = 347
    __api_name__: ClassVar[str] = "kpl_list"
    __api_title__: ClassVar[str] = "榜单数据(开盘啦)"
    __api_info_title__: ClassVar[str] = "开盘啦板单数据"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "打板专题数据", "榜单数据（开盘啦）"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 346, 347]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date", "tag"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "股票代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "tag": {"type": "str", "required": False, "description": "板单类型（涨停|炸板|跌停)"},
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
            "comment": "榜单数据(开盘啦)",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="代码")
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="名称")
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易时间",
    )
    lu_time = Column("lu_time", String(), nullable=False, default="", server_default=text("''"), comment="涨停时间")
    ld_time = Column("ld_time", String(), nullable=False, default="", server_default=text("''"), comment="跌停时间")
    open_time = Column("open_time", String(), nullable=False, default="", server_default=text("''"), comment="开板时间")
    last_time = Column(
        "last_time", String(), nullable=False, default="", server_default=text("''"), comment="最后涨停时间"
    )
    lu_desc = Column("lu_desc", String(), nullable=False, default="", server_default=text("''"), comment="涨停原因")
    tag = Column("tag", String(), nullable=False, default="", server_default=text("''"), comment="标签|类别")
    theme = Column("theme", String(), nullable=False, default="", server_default=text("''"), comment="板块")
    net_change = Column(
        "net_change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="主力净额(元)"
    )
    bid_amount = Column(
        "bid_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="竞价成交额(元)"
    )
    status = Column("status", String(), nullable=False, default="", server_default=text("''"), comment="状态")
    bid_change = Column(
        "bid_change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="竞价成交额(元|个)"
    )
    bid_turnover = Column(
        "bid_turnover", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="竞价换手)%"
    )
    lu_bid_vol = Column(
        "lu_bid_vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨停委买额(元|个)"
    )
    pct_chg = Column("pct_chg", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌幅%")
    bid_pct_chg = Column(
        "bid_pct_chg", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="竞价涨幅%"
    )
    rt_pct_chg = Column(
        "rt_pct_chg", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="实时涨幅%"
    )
    limit_order = Column(
        "limit_order", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="封单(元|个)"
    )
    amount = Column("amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交额(元|个)")
    turnover_rate = Column(
        "turnover_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="换手率%"
    )
    free_float = Column(
        "free_float", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="实际流通(元|个)"
    )
    lu_limit_order = Column(
        "lu_limit_order", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最大封单(元|个)"
    )
