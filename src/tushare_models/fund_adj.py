# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FundAdj(Base):
    """复权因子"""

    __tablename__: str = "fund_adj"
    __api_id__: ClassVar[int] = 199
    __api_name__: ClassVar[str] = "fund_adj"
    __api_title__: ClassVar[str] = "复权因子"
    __api_info_title__: ClassVar[str] = "基金复权因子"
    __api_path__: ClassVar[List[str]] = ["数据接口", "公募基金", "复权因子"]
    __api_path_ids__: ClassVar[List[int]] = [2, 18, 199]
    __api_points_required__: ClassVar[int] = 5000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "TS基金代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "offset": {"type": "str", "required": False, "description": "开始行数"},
        "limit": {"type": "str", "required": False, "description": "最大行数"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "复权因子",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="ts基金代码")
    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    adj_factor = Column(
        "adj_factor", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="复权因子"
    )
    discount_rate = Column(
        "discount_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="贴水率(%)"
    )
