# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class LimitCptList(Base):
    """涨停最强板块统计"""

    __tablename__: str = "limit_cpt_list"
    __api_id__: ClassVar[int] = 357
    __api_name__: ClassVar[str] = "limit_cpt_list"
    __api_title__: ClassVar[str] = "涨停最强板块统计"
    __api_info_title__: ClassVar[str] = "最强板块统计"
    __api_path__: ClassVar[List[str]] = [
        "数据接口",
        "沪深股票",
        "打板专题数据",
        "涨停最强板块统计",
    ]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 346, 357]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "trade_date": {
            "type": "str",
            "required": False,
            "description": "交易日期(格式：YYYYMMDD，下同)",
        },
        "ts_code": {"type": "str", "required": False, "description": "板块代码"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {
            "type": "int",
            "required": False,
            "description": "请求数据的开始位移量",
        },
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "涨停最强板块统计",
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

    ts_code = Column(
        "ts_code",
        String(16),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="板块代码",
    )
    name = Column(
        "name",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="板块名称",
    )
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    days = Column(
        "days",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="上榜天数",
    )
    up_stat = Column(
        "up_stat",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="连板高度",
    )
    cons_nums = Column(
        "cons_nums",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="连板家数",
    )
    up_nums = Column(
        "up_nums",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="涨停家数",
    )
    pct_chg = Column(
        "pct_chg",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="涨跌幅%",
    )
    rank = Column(
        "rank",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="板块热点排名",
    )
