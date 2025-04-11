# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class LimitListThs(Base):
    """同花顺涨跌停榜单"""

    __tablename__: str = "limit_list_ths"
    __api_id__: ClassVar[int] = 355
    __api_name__: ClassVar[str] = "limit_list_ths"
    __api_title__: ClassVar[str] = "同花顺涨跌停榜单"
    __api_info_title__: ClassVar[str] = "涨跌停榜单(同花顺)"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "打板专题数据", "同花顺涨跌停榜单"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 346, 355]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = '2023-11-01'
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "trade_date": {"type": "str", "required": False, "description": "交易日期(格式：YYYYMMDD，下同)"},
        "ts_code": {"type": "str", "required": False, "description": "股票代码"},
        "limit_type": {
            "type": "str",
            "required": False,
            "description": "涨停池、连扳池、冲刺涨停、炸板池、跌停池，默认：涨停池",
        },
        "market": {"type": "str", "required": False, "description": "HS-沪深主板 GEM-创业板 STAR-科创板"},
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
            "comment": "同花顺涨跌停榜单",
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
    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="股票代码")
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="股票名称")
    price = Column("price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最近价格(元)")
    pct_chg = Column("pct_chg", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨跌幅%")
    open_num = Column("open_num", String(), nullable=False, default="", server_default=text("''"), comment="打开次数")
    lu_desc = Column("lu_desc", String(), nullable=False, default="", server_default=text("''"), comment="涨停原因")
    limit_type = Column(
        "limit_type", String(), nullable=False, default="", server_default=text("''"), comment="板单类别"
    )
    tag = Column("tag", String(), nullable=False, default="", server_default=text("''"), comment="涨停标签")
    status = Column(
        "status", String(), nullable=False, default="", server_default=text("''"), comment="涨停状态(N连板、一字板)"
    )
    first_lu_time = Column(
        "first_lu_time", String(), nullable=False, default="", server_default=text("''"), comment="首次涨停时间"
    )
    last_lu_time = Column(
        "last_lu_time", String(), nullable=False, default="", server_default=text("''"), comment="最后涨停时间"
    )
    first_ld_time = Column(
        "first_ld_time", String(), nullable=False, default="", server_default=text("''"), comment="首次跌停时间"
    )
    last_ld_time = Column(
        "last_ld_time", String(), nullable=False, default="", server_default=text("''"), comment="最后涨停时间"
    )
    limit_order = Column(
        "limit_order", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="封单量(元|个)"
    )
    limit_amount = Column(
        "limit_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="封单额(元|个)"
    )
    turnover_rate = Column(
        "turnover_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="换手率%"
    )
    free_float = Column(
        "free_float", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="实际流通(元|个)"
    )
    lu_limit_order = Column(
        "lu_limit_order", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最大封单(元|个)"
    )
    limit_up_suc_rate = Column(
        "limit_up_suc_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="近一年涨停封板率",
    )
    turnover = Column("turnover", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="成交额")
    rise_rate = Column("rise_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="涨速")
    sum_float = Column(
        "sum_float", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment=" 总市值 亿元"
    )
    market_type = Column(
        "market_type",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="股票类型：HS沪深主板、GEM创业板、STAR科创板",
    )
