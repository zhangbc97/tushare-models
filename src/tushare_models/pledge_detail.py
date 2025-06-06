# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class PledgeDetail(Base):
    """股权质押明细数据"""

    __tablename__: str = "pledge_detail"
    __api_id__: ClassVar[int] = 111
    __api_name__: ClassVar[str] = "pledge_detail"
    __api_title__: ClassVar[str] = "股权质押明细数据"
    __api_info_title__: ClassVar[str] = "股权质押明细"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "参考数据", "股权质押明细数据"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 17, 111]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "ann_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": True, "description": "股票代码"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "股权质押明细数据",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="TS股票代码")
    ann_date = Column(
        "ann_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="公告日期"
    )
    holder_name = Column(
        "holder_name", String(), nullable=False, default="", server_default=text("''"), comment="股东名称"
    )
    holder_type = Column(
        "holder_type", String(), nullable=False, default="", server_default=text("''"), comment="股东类型"
    )
    pledge_amount = Column(
        "pledge_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="质押数量"
    )
    start_date = Column(
        "start_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="质押开始日期",
    )
    end_date = Column(
        "end_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="质押结束日期",
    )
    is_release = Column(
        "is_release", String(), nullable=False, default="", server_default=text("''"), comment="是否已解押"
    )
    release_date = Column(
        "release_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="解押日期",
    )
    pledgor = Column("pledgor", String(), nullable=False, default="", server_default=text("''"), comment="质押方")
    holding_amount = Column(
        "holding_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="持股总数"
    )
    pledged_amount = Column(
        "pledged_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="质押总数"
    )
    p_total_ratio = Column(
        "p_total_ratio",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="本次质押占总股本比例",
    )
    h_total_ratio = Column(
        "h_total_ratio",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="持股总数占总股本比例",
    )
    is_buyback = Column(
        "is_buyback", String(), nullable=False, default="", server_default=text("''"), comment="是否回购"
    )
    desc = Column("desc", String(), nullable=False, default="", server_default=text("''"), comment="备注")
