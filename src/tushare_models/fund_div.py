# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FundDiv(Base):
    """基金分红"""

    __tablename__: str = "fund_div"
    __api_id__: ClassVar[int] = 120
    __api_name__: ClassVar[str] = "fund_div"
    __api_title__: ClassVar[str] = "基金分红"
    __api_info_title__: ClassVar[str] = "公募基金分红"
    __api_path__: ClassVar[List[str]] = ["数据接口", "公募基金", "基金分红"]
    __api_path_ids__: ClassVar[List[int]] = [2, 18, 120]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "ann_date", "imp_anndate"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ann_date": {"type": "str", "required": False, "description": "公告日"},
        "ex_date": {"type": "str", "required": False, "description": "公告日"},
        "pay_date": {"type": "str", "required": False, "description": "公告日"},
        "ts_code": {"type": "str", "required": False, "description": "公告日"},
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
            "comment": "基金分红",
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

    ts_code = Column(
        "ts_code",
        String(16),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="TS代码",
    )
    ann_date = Column(
        "ann_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="公告日期",
    )
    imp_anndate = Column(
        "imp_anndate",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="分红实施公告日",
    )
    base_date = Column(
        "base_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="分配收益基准日",
    )
    div_proc = Column(
        "div_proc",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="方案进度",
    )
    record_date = Column(
        "record_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="权益登记日",
    )
    ex_date = Column(
        "ex_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="除息日",
    )
    pay_date = Column(
        "pay_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="派息日",
    )
    earpay_date = Column(
        "earpay_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="收益支付日",
    )
    net_ex_date = Column(
        "net_ex_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="净值除权日",
    )
    div_cash = Column(
        "div_cash",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股派息(元)",
    )
    base_unit = Column(
        "base_unit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="基准基金份额(万份)",
    )
    ear_distr = Column(
        "ear_distr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="可分配收益(元)",
    )
    ear_amount = Column(
        "ear_amount",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="收益分配金额(元)",
    )
    account_date = Column(
        "account_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="红利再投资到账日",
    )
    base_year = Column(
        "base_year",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="份额基准年度",
    )
    update_flag = Column(
        "update_flag",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="更新标识",
    )
