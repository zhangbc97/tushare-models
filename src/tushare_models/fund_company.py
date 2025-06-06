# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FundCompany(Base):
    """基金管理人"""

    __tablename__: str = "fund_company"
    __api_id__: ClassVar[int] = 118
    __api_name__: ClassVar[str] = "fund_company"
    __api_title__: ClassVar[str] = "基金管理人"
    __api_info_title__: ClassVar[str] = "公募基金公司"
    __api_path__: ClassVar[List[str]] = ["数据接口", "公募基金", "基金管理人"]
    __api_path_ids__: ClassVar[List[int]] = [2, 18, 118]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["credit_code"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "setup_date": {"type": "str", "required": False, "description": "成立日期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "基金管理人",
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

    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="公司名称")
    shortname = Column("shortname", String(), nullable=False, default="", server_default=text("''"), comment="简称")
    short_enname = Column(
        "short_enname", String(), nullable=False, default="", server_default=text("''"), comment="英文缩写"
    )
    province = Column("province", String(), nullable=False, default="", server_default=text("''"), comment="省份")
    city = Column("city", String(), nullable=False, default="", server_default=text("''"), comment="城市")
    address = Column("address", String(), nullable=False, default="", server_default=text("''"), comment="注册地址")
    phone = Column("phone", String(), nullable=False, default="", server_default=text("''"), comment="电话")
    office = Column("office", String(), nullable=False, default="", server_default=text("''"), comment="办公地址")
    website = Column("website", String(), nullable=False, default="", server_default=text("''"), comment="公司网址")
    chairman = Column("chairman", String(), nullable=False, default="", server_default=text("''"), comment="法人代表")
    manager = Column("manager", String(), nullable=False, default="", server_default=text("''"), comment="总经理")
    reg_capital = Column(
        "reg_capital", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="注册资本"
    )
    setup_date = Column(
        "setup_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="成立日期",
    )
    end_date = Column(
        "end_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="公司终止日期",
    )
    employees = Column(
        "employees", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="员工总数"
    )
    main_business = Column(
        "main_business", String(), nullable=False, default="", server_default=text("''"), comment="主要产品及业务"
    )
    org_code = Column(
        "org_code", String(), nullable=False, default="", server_default=text("''"), comment="组织机构代码"
    )
    credit_code = Column(
        "credit_code", String(), nullable=False, default="", server_default=text("''"), comment="统一社会信用代码"
    )
