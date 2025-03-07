# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FutWeeklyDetail(Base):
    """期货主要品种交易周报"""

    __tablename__: str = "fut_weekly_detail"
    __api_id__: ClassVar[int] = 216
    __api_name__: ClassVar[str] = "fut_weekly_detail"
    __api_title__: ClassVar[str] = "期货主要品种交易周报"
    __api_info_title__: ClassVar[str] = "期货主要品种交易周报"
    __api_path__: ClassVar[List[str]] = ["数据接口", "期货数据", "期货主要品种交易周报"]
    __api_path_ids__: ClassVar[List[int]] = [2, 134, 216]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["week", "prd"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "week": {"type": "str", "required": False, "description": "周期"},
        "prd": {"type": "str", "required": False, "description": "期货品种"},
        "start_week": {"type": "str", "required": False, "description": "开始周期"},
        "end_week": {"type": "str", "required": False, "description": "结束周期"},
        "exchange": {"type": "str", "required": False, "description": "交易所"},
        "offset": {"type": "int", "required": False, "description": ""},
        "limit": {"type": "int", "required": False, "description": ""},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "期货主要品种交易周报",
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

    exchange = Column(
        "exchange",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="交易所代码",
    )
    prd = Column(
        "prd",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="期货品种代码",
    )
    name = Column(
        "name",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="品种名称",
    )
    vol = Column(
        "vol",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="成交量(手)",
    )
    vol_yoy = Column(
        "vol_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="同比增减(%)",
    )
    amount = Column(
        "amount",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="成交金额(亿元)",
    )
    amout_yoy = Column(
        "amout_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="同比增减(%)",
    )
    cumvol = Column(
        "cumvol",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="年累计成交总量(手)",
    )
    cumvol_yoy = Column(
        "cumvol_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="同比增减(%)",
    )
    cumamt = Column(
        "cumamt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="年累计成交金额(亿元)",
    )
    cumamt_yoy = Column(
        "cumamt_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="同比增减(%)",
    )
    open_interest = Column(
        "open_interest",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="持仓量(手)",
    )
    interest_wow = Column(
        "interest_wow",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="环比增减(%)",
    )
    mc_close = Column(
        "mc_close",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="本周主力合约收盘价",
    )
    close_wow = Column(
        "close_wow",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="环比涨跌(%)",
    )
    week = Column(
        "week",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="周期",
    )
    week_date = Column(
        "week_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="周日期",
    )
