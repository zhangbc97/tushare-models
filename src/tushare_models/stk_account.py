# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class StkAccount(Base):
    """股票开户数据(停)"""

    __tablename__: str = "stk_account"
    __api_id__: ClassVar[int] = 164
    __api_name__: ClassVar[str] = "stk_account"
    __api_title__: ClassVar[str] = "股票开户数据(停)"
    __api_info_title__: ClassVar[str] = "股票账户开户数据"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "参考数据", "股票开户数据（停）"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 17, 164]
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
            "comment": "股票开户数据(停)",
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

    date = Column("date", String(), nullable=False, default="", server_default=text("''"), comment="统计周期")
    weekly_new = Column(
        "weekly_new", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="本周新增"
    )
    total = Column("total", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="期末总账户数")
    weekly_hold = Column(
        "weekly_hold", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="本周持仓账户数"
    )
    weekly_trade = Column(
        "weekly_trade", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="本周参与交易账户数"
    )
