# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class CbIssue(Base):
    """可转债发行"""

    __tablename__: str = "cb_issue"
    __api_id__: ClassVar[int] = 186
    __api_name__: ClassVar[str] = "cb_issue"
    __api_title__: ClassVar[str] = "可转债发行"
    __api_info_title__: ClassVar[str] = "可转债发行"
    __api_path__: ClassVar[List[str]] = ["数据接口", "债券专题", "可转债发行"]
    __api_path_ids__: ClassVar[List[int]] = [2, 184, 186]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "ann_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "TS代码"},
        "ann_date": {"type": "str", "required": False, "description": "发行公告日"},
        "start_date": {"type": "str", "required": False, "description": "公告开始日期"},
        "end_date": {"type": "str", "required": False, "description": "公告结束日期"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "可转债发行",
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

    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="转债代码")
    ann_date = Column(
        "ann_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="发行公告日",
    )
    res_ann_date = Column(
        "res_ann_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="发行结果公告日",
    )
    plan_issue_size = Column(
        "plan_issue_size", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="计划发行总额(元)"
    )
    issue_size = Column(
        "issue_size", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="发行总额(元)"
    )
    issue_price = Column(
        "issue_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="发行价格"
    )
    issue_type = Column(
        "issue_type", String(), nullable=False, default="", server_default=text("''"), comment="发行方式"
    )
    issue_cost = Column(
        "issue_cost", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="发行费用(元)"
    )
    onl_code = Column(
        "onl_code", String(), nullable=False, default="", server_default=text("''"), comment="网上申购代码"
    )
    onl_name = Column(
        "onl_name", String(), nullable=False, default="", server_default=text("''"), comment="网上申购简称"
    )
    onl_date = Column(
        "onl_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="网上发行日期",
    )
    onl_size = Column(
        "onl_size", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="网上发行总额(元)"
    )
    onl_pch_vol = Column(
        "onl_pch_vol",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="网上发行有效申购数量(张)",
    )
    onl_pch_num = Column(
        "onl_pch_num", Integer, nullable=False, default=0, server_default=text("'0'"), comment="网上发行有效申购户数"
    )
    onl_pch_excess = Column(
        "onl_pch_excess",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="网上发行超额认购倍数",
    )
    onl_winning_rate = Column(
        "onl_winning_rate",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="网上发行中签率(%)",
    )
    shd_ration_code = Column(
        "shd_ration_code", String(), nullable=False, default="", server_default=text("''"), comment="老股东配售代码"
    )
    shd_ration_name = Column(
        "shd_ration_name", String(), nullable=False, default="", server_default=text("''"), comment="老股东配售简称"
    )
    shd_ration_date = Column(
        "shd_ration_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="老股东配售日",
    )
    shd_ration_record_date = Column(
        "shd_ration_record_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="老股东配售股权登记日",
    )
    shd_ration_pay_date = Column(
        "shd_ration_pay_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="老股东配售缴款日",
    )
    shd_ration_price = Column(
        "shd_ration_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="老股东配售价格"
    )
    shd_ration_ratio = Column(
        "shd_ration_ratio", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="老股东配售比例"
    )
    shd_ration_size = Column(
        "shd_ration_size",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="老股东配售数量(张)",
    )
    shd_ration_vol = Column(
        "shd_ration_vol",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="老股东配售有效申购数量(张)",
    )
    shd_ration_num = Column(
        "shd_ration_num",
        Integer,
        nullable=False,
        default=0,
        server_default=text("'0'"),
        comment="老股东配售有效申购户数",
    )
    shd_ration_excess = Column(
        "shd_ration_excess",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="老股东配售超额认购倍数",
    )
    offl_size = Column(
        "offl_size", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="网下发行总额(元)"
    )
    offl_deposit = Column(
        "offl_deposit", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="网下发行定金比例(%)"
    )
    offl_pch_vol = Column(
        "offl_pch_vol",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="网下发行有效申购数量(张)",
    )
    offl_pch_num = Column(
        "offl_pch_num", Integer, nullable=False, default=0, server_default=text("'0'"), comment="网下发行有效申购户数"
    )
    offl_pch_excess = Column(
        "offl_pch_excess",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="网下发行超额认购倍数",
    )
    offl_winning_rate = Column(
        "offl_winning_rate", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="网下发行中签率"
    )
    lead_underwriter = Column(
        "lead_underwriter", String(), nullable=False, default="", server_default=text("''"), comment="主承销商"
    )
    lead_underwriter_vol = Column(
        "lead_underwriter_vol",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="主承销商包销数量(张)",
    )
