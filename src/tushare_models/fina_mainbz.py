# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FinaMainbz(Base):
    """主营业务构成"""

    __tablename__: str = "fina_mainbz"
    __api_id__: ClassVar[int] = 81
    __api_name__: ClassVar[str] = "fina_mainbz"
    __api_title__: ClassVar[str] = "主营业务构成"
    __api_info_title__: ClassVar[str] = "主营业务构成"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "财务数据", "主营业务构成"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 16, 81]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = True
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "end_date", "update_flag"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": True, "description": "股票代码"},
        "period": {"type": "str", "required": False, "description": "报告期"},
        "type": {"type": "str", "required": False, "description": "类型：P按产品 D按地区"},
        "start_date": {"type": "str", "required": False, "description": "报告期开始日期"},
        "end_date": {"type": "str", "required": False, "description": "报告期结束日期"},
        "is_publish": {"type": "str", "required": False, "description": ""},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "主营业务构成",
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
    end_date = Column(
        "end_date", Date, nullable=False, default="1970-01-01", server_default=text("'1970-01-01'"), comment="报告期"
    )
    bz_item = Column("bz_item", String(), nullable=False, default="", server_default=text("''"), comment="主营业务项目")
    bz_code = Column("bz_code", String(), nullable=False, default="", server_default=text("''"), comment="项目代码")
    bz_sales = Column(
        "bz_sales", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="主营业务收入(元)"
    )
    bz_profit = Column(
        "bz_profit", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="主营业务利润(元)"
    )
    bz_cost = Column(
        "bz_cost", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="主营业务成本(元)"
    )
    curr_type = Column("curr_type", String(), nullable=False, default="", server_default=text("''"), comment="货币代码")
    update_flag = Column(
        "update_flag", String(), nullable=False, default="", server_default=text("''"), comment="是否更新"
    )
