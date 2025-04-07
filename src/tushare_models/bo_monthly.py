# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class BoMonthly(Base):
    """电影月度票房"""

    __tablename__: str = "bo_monthly"
    __api_id__: ClassVar[int] = 113
    __api_name__: ClassVar[str] = "bo_monthly"
    __api_title__: ClassVar[str] = "电影月度票房"
    __api_info_title__: ClassVar[str] = "电影月度票房"
    __api_path__: ClassVar[List[str]] = ["数据接口", "行业经济", "TMT行业", "电影月度票房"]
    __api_path_ids__: ClassVar[List[int]] = [2, 82, 83, 113]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["name", "date"]
    __start_date__: ClassVar[str | None] = "2008-01-01"
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "date": {"type": "str", "required": True, "description": "日期（每月1号）"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "电影月度票房",
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
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="影片名称")
    list_date = Column(
        "list_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="上映日期"
    )
    avg_price = Column(
        "avg_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="平均票价"
    )
    month_amount = Column(
        "month_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="当月票房(万)"
    )
    list_day = Column("list_day", Integer, nullable=False, default=0, server_default=text("'0'"), comment="月内天数")
    p_pc = Column("p_pc", Integer, nullable=False, default=0, server_default=text("'0'"), comment="场均人次")
    wom_index = Column(
        "wom_index", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="口碑指数"
    )
    m_ratio = Column("m_ratio", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="月度占比(%)")
    rank = Column("rank", Integer, nullable=False, default=0, server_default=text("'0'"), comment="排名")
