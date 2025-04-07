# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class TeleplayRecord(Base):
    """全国电视剧备案公示数据"""

    __tablename__: str = "teleplay_record"
    __api_id__: ClassVar[int] = 180
    __api_name__: ClassVar[str] = "teleplay_record"
    __api_title__: ClassVar[str] = "全国电视剧备案公示数据"
    __api_info_title__: ClassVar[str] = "全国拍摄制作电视剧备案数据"
    __api_path__: ClassVar[List[str]] = ["数据接口", "行业经济", "TMT行业", "全国电视剧备案公示数据"]
    __api_path_ids__: ClassVar[List[int]] = [2, 82, 83, 180]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["license_key", "report_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "report_date": {"type": "str", "required": False, "description": "备案月份"},
        "start_date": {"type": "str", "required": False, "description": "备案开始月份（YYYYMM）"},
        "end_date": {"type": "str", "required": False, "description": "备案结束月份（YYYYMM）"},
        "org": {"type": "str", "required": False, "description": "备案机构"},
        "name": {"type": "str", "required": False, "description": "电视剧名称"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "全国电视剧备案公示数据",
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

    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="电视剧名称")
    classify = Column("classify", String(), nullable=False, default="", server_default=text("''"), comment="题材")
    types = Column("types", String(), nullable=False, default="", server_default=text("''"), comment="体裁")
    org = Column("org", String(), nullable=False, default="", server_default=text("''"), comment="报备机构")
    report_date = Column(
        "report_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="报备时间",
    )
    license_key = Column(
        "license_key", String(), nullable=False, default="", server_default=text("''"), comment="许可证号"
    )
    episodes = Column("episodes", String(), nullable=False, default="", server_default=text("''"), comment="集数")
    shooting_date = Column(
        "shooting_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="拍摄时间",
    )
    prod_cycle = Column(
        "prod_cycle", String(), nullable=False, default="", server_default=text("''"), comment="制作周期"
    )
    content = Column("content", String(), nullable=False, default="", server_default=text("''"), comment="内容提要")
    pro_opi = Column(
        "pro_opi", String(), nullable=False, default="", server_default=text("''"), comment="省级管理部门备案意见"
    )
    dept_opi = Column(
        "dept_opi", String(), nullable=False, default="", server_default=text("''"), comment="相关部门意见"
    )
    remarks = Column("remarks", String(), nullable=False, default="", server_default=text("''"), comment="备注")
