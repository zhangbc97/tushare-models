# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class CcassHold(Base):
    """中央结算系统持股统计"""

    __tablename__: str = "ccass_hold"
    __api_id__: ClassVar[int] = 295
    __api_name__: ClassVar[str] = "ccass_hold"
    __api_title__: ClassVar[str] = "中央结算系统持股统计"
    __api_info_title__: ClassVar[str] = "中央结算系统持股汇总"
    __api_path__: ClassVar[List[str]] = [
        "数据接口",
        "沪深股票",
        "特色数据",
        "中央结算系统持股统计",
    ]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 291, 295]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["trade_cal"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = "2020-11-11"
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "股票代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "type": {"type": "str", "required": False, "description": "类型"},
        "hk_hold": {"type": "str", "required": False, "description": "港交所代码"},
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
            "comment": "中央结算系统持股统计",
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
    ts_code = Column(
        "ts_code",
        String(16),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="股票代号",
    )
    name = Column(
        "name",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="股票名称",
    )
    shareholding = Column(
        "shareholding",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="于中央结算系统的持股量(股)",
    )
    hold_nums = Column(
        "hold_nums",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="参与者数目(个)",
    )
    hold_ratio = Column(
        "hold_ratio",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="占于上交所/深交所上市及交易的A股总数的百分比(%)",
    )
