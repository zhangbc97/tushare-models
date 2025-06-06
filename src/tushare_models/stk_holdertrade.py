# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class StkHoldertrade(Base):
    """股东增减持"""

    __tablename__: str = "stk_holdertrade"
    __api_id__: ClassVar[int] = 175
    __api_name__: ClassVar[str] = "stk_holdertrade"
    __api_title__: ClassVar[str] = "股东增减持"
    __api_info_title__: ClassVar[str] = "股东增减持"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "参考数据", "股东增减持"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 17, 175]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "ann_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "TS股票代码"},
        "ann_date": {"type": "str", "required": False, "description": "公告日期"},
        "start_date": {"type": "str", "required": False, "description": "公告开始日期"},
        "end_date": {"type": "str", "required": False, "description": "公告结束日期"},
        "trade_type": {"type": "str", "required": False, "description": "交易类型IN增持DE减持"},
        "holder_type": {"type": "str", "required": False, "description": "股东类型G高管C公司P个人"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "股东增减持",
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
    ann_date = Column(
        "ann_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="公告日期"
    )
    holder_name = Column(
        "holder_name", String(), nullable=False, default="", server_default=text("''"), comment="股东名称"
    )
    holder_type = Column(
        "holder_type",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="股东类型G高管P个人C公司",
    )
    in_de = Column("in_de", String(), nullable=False, default="", server_default=text("''"), comment="类型IN增持DE减持")
    change_vol = Column(
        "change_vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="变动数量"
    )
    change_ratio = Column(
        "change_ratio", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="占流通比例(%)"
    )
    after_share = Column(
        "after_share", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="变动后持股"
    )
    after_ratio = Column(
        "after_ratio", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="变动后占流通比例(%)"
    )
    avg_price = Column(
        "avg_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="平均价格"
    )
    total_share = Column(
        "total_share", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="持股总数"
    )
    begin_date = Column(
        "begin_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="增减持开始日期",
    )
    close_date = Column(
        "close_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="增减持结束日期",
    )
