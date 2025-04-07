# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class DisclosureDate(Base):
    """财报披露日期表"""

    __tablename__: str = "disclosure_date"
    __api_id__: ClassVar[int] = 162
    __api_name__: ClassVar[str] = "disclosure_date"
    __api_title__: ClassVar[str] = "财报披露日期表"
    __api_info_title__: ClassVar[str] = "财报披露计划"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "财务数据", "财报披露日期表"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 16, 162]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "end_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "TS股票代码"},
        "end_date": {"type": "str", "required": False, "description": "财报周期"},
        "pre_date": {"type": "str", "required": False, "description": "计划披露日期"},
        "actual_date": {"type": "str", "required": False, "description": "实际披露日期"},
        "offset": {"type": "int", "required": False, "description": ""},
        "limit": {"type": "int", "required": False, "description": ""},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "财报披露日期表",
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
        "ann_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="最新披露公告日",
    )
    end_date = Column(
        "end_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="报告期"
    )
    pre_date = Column(
        "pre_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="预计披露日期",
    )
    actual_date = Column(
        "actual_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="实际披露日期",
    )
    modify_date = Column(
        "modify_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="披露日期修正记录",
    )
