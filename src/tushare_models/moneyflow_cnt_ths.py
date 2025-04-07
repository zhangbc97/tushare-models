# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class MoneyflowCntThs(Base):
    """板块资金流向(THS)"""

    __tablename__: str = "moneyflow_cnt_ths"
    __api_id__: ClassVar[int] = 371
    __api_name__: ClassVar[str] = "moneyflow_cnt_ths"
    __api_title__: ClassVar[str] = "板块资金流向(THS)"
    __api_info_title__: ClassVar[str] = "板块资金流向(THS)"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "资金流向数据", "板块资金流向（THS)"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 342, 371]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": False, "description": "代码"},
        "trade_date": {"type": "str", "required": False, "description": "交易日期(格式：YYYYMMDD，下同)"},
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
            "comment": "板块资金流向(THS)",
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

    trade_date = Column(
        "trade_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="交易日期",
    )
    ts_code = Column("ts_code", String(16), nullable=False, default="", server_default=text("''"), comment="板块代码")
    name = Column("name", String(), nullable=False, default="", server_default=text("''"), comment="板块名称")
    lead_stock = Column(
        "lead_stock", String(), nullable=False, default="", server_default=text("''"), comment="领涨股票名称"
    )
    close_price = Column(
        "close_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="最新价"
    )
    pct_change = Column(
        "pct_change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="行业涨跌幅"
    )
    industry_index = Column(
        "industry_index", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="行业指数"
    )
    company_num = Column(
        "company_num", Integer, nullable=False, default=0, server_default=text("'0'"), comment="公司数量"
    )
    pct_change_stock = Column(
        "pct_change_stock", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="领涨股涨跌幅"
    )
    net_buy_amount = Column(
        "net_buy_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="流入资金(元)"
    )
    net_sell_amount = Column(
        "net_sell_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="流出资金(元)	"
    )
    net_amount = Column(
        "net_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="净额(元)"
    )
