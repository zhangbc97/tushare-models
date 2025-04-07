# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class Hibor(Base):
    """Hibor利率"""

    __tablename__: str = "hibor"
    __api_id__: ClassVar[int] = 153
    __api_name__: ClassVar[str] = "hibor"
    __api_title__: ClassVar[str] = "Hibor利率"
    __api_info_title__: ClassVar[str] = "Hibor利率"
    __api_path__: ClassVar[List[str]] = ["数据接口", "宏观经济", "国内宏观", "利率数据", "Hibor利率"]
    __api_path_ids__: ClassVar[List[int]] = [2, 147, 224, 148, 153]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "date": {"type": "str", "required": False, "description": "日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "Hibor利率",
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

    date = Column("date", String(), nullable=False, default="", server_default=text("''"), comment="日期")
    on = Column("on", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="隔夜")
    _1w = Column("1w", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="1周")
    _2w = Column("2w", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="2周")
    _1m = Column("1m", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="1个月")
    _2m = Column("2m", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="2个月")
    _3m = Column("3m", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="3个月")
    _6m = Column("6m", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="6个月")
    _12m = Column("12m", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="12个月")
