# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class StkRewards(Base):
    """管理层薪酬和持股"""

    __tablename__: str = "stk_rewards"
    __api_id__: ClassVar[int] = 194
    __api_name__: ClassVar[str] = "stk_rewards"
    __api_title__: ClassVar[str] = "管理层薪酬和持股"
    __api_info_title__: ClassVar[str] = "管理层薪酬和持股"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "基础数据", "管理层薪酬和持股"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 24, 194]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "ann_date", "name", "title"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": True, "description": "TS股票代码"},
        "end_date": {"type": "str", "required": False, "description": "报告期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "管理层薪酬和持股",
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
    end_date = Column(
        "end_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="报告期"
    )
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="姓名")
    title = Column("title", String(), nullable=False, default="", server_default=text("''"), comment="职务")
    reward = Column("reward", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="报酬")
    hold_vol = Column("hold_vol", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="持股数")
