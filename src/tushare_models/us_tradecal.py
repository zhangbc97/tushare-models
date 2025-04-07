# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class UsTradecal(Base):
    """美股交易日历"""

    __tablename__: str = "us_tradecal"
    __api_id__: ClassVar[int] = 253
    __api_name__: ClassVar[str] = "us_tradecal"
    __api_title__: ClassVar[str] = "美股交易日历"
    __api_info_title__: ClassVar[str] = "美股交易日历"
    __api_path__: ClassVar[List[str]] = ["数据接口", "美股数据", "美股交易日历"]
    __api_path_ids__: ClassVar[List[int]] = [2, 251, 253]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["cal_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "is_open": {"type": "str", "required": False, "description": "是否交易 '0'休市 '1'交易"},
        "exchange": {"type": "str", "required": False, "description": ""},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "美股交易日历",
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

    cal_date = Column(
        "cal_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="日历日期"
    )
    is_open = Column(
        "is_open",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="是否交易 '0'休市 '1'交易",
    )
    pretrade_date = Column(
        "pretrade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="上一个交易日",
    )
