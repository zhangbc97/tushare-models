# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class StockMx(Base):
    """动能因子"""

    __tablename__: str = "stock_mx"
    __api_id__: ClassVar[int] = 300
    __api_name__: ClassVar[str] = "stock_mx"
    __api_title__: ClassVar[str] = "动能因子"
    __api_info_title__: ClassVar[str] = "动能因子"
    __api_path__: ClassVar[List[str]] = ["动能因子"]
    __api_path_ids__: ClassVar[List[int]] = []
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "股票代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期"},
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
            "comment": "动能因子",
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
        comment="股票代码",
    )
    mx_grade = Column(
        "mx_grade",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="动能评级，综合动能指标后分成4个评等，1(高)、2(中)、3(低)、4(弱)",
    )
    com_stock = Column(
        "com_stock",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="行业轮动指标",
    )
    evd_v = Column(
        "evd_v",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="速度指标，衡量该个股股价变化的速度",
    )
    zt_sum_z = Column(
        "zt_sum_z",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="极值，短期均线离差值",
    )
    wma250_z = Column(
        "wma250_z",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="偏离指标，中期均线偏离度指标",
    )
