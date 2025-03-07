# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class HkMins(Base):
    """港股分钟行情"""

    __tablename__: str = "hk_mins"
    __api_id__: ClassVar[int] = 304
    __api_name__: ClassVar[str] = "hk_mins"
    __api_title__: ClassVar[str] = "港股分钟行情"
    __api_info_title__: ClassVar[str] = "港股分钟"
    __api_path__: ClassVar[List[str]] = ["数据接口", "港股数据", "港股分钟行情"]
    __api_path_ids__: ClassVar[List[int]] = [2, 190, 304]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = True
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_time"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "ts_code"},
        "freq": {"type": "str", "required": True, "description": "分钟频度"},
        "start_date": {"type": "datetime", "required": False, "description": ""},
        "end_date": {"type": "datetime", "required": False, "description": "结束时间"},
        "test": {"type": "str", "required": False, "description": ""},
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
            "comment": "港股分钟行情",
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
        comment="",
    )
    trade_time = Column(
        "trade_time",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="",
    )
    open = Column(
        "open",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="",
    )
    close = Column(
        "close",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="",
    )
    high = Column(
        "high",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="",
    )
    low = Column(
        "low",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="",
    )
    vol = Column(
        "vol",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="",
    )
    amount = Column(
        "amount",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="",
    )
