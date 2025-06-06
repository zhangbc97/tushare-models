# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class WzIndex(Base):
    """温州民间借贷利率"""

    __tablename__: str = "wz_index"
    __api_id__: ClassVar[int] = 173
    __api_name__: ClassVar[str] = "wz_index"
    __api_title__: ClassVar[str] = "温州民间借贷利率"
    __api_info_title__: ClassVar[str] = "温州民间借贷利率"
    __api_path__: ClassVar[List[str]] = ["数据接口", "宏观经济", "国内宏观", "利率数据", "温州民间借贷利率"]
    __api_path_ids__: ClassVar[List[int]] = [2, 147, 224, 148, 173]
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
            "comment": "温州民间借贷利率",
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
    comp_rate = Column(
        "comp_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州民间融资综合利率指数",
    )
    center_rate = Column(
        "center_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="民间借贷服务中心利率"
    )
    micro_rate = Column(
        "micro_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="小额贷款公司放款利率"
    )
    cm_rate = Column(
        "cm_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="民间资本管理公司融资价格"
    )
    sdb_rate = Column(
        "sdb_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="社会直接借贷利率"
    )
    om_rate = Column(
        "om_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="其他市场主体利率"
    )
    aa_rate = Column(
        "aa_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="农村互助会互助金费率"
    )
    m1_rate = Column(
        "m1_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州地区民间借贷分期限利率(一月期)",
    )
    m3_rate = Column(
        "m3_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州地区民间借贷分期限利率(三月期)",
    )
    m6_rate = Column(
        "m6_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州地区民间借贷分期限利率(六月期)",
    )
    m12_rate = Column(
        "m12_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州地区民间借贷分期限利率(一年期)",
    )
    long_rate = Column(
        "long_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="温州地区民间借贷分期限利率(长期)",
    )
