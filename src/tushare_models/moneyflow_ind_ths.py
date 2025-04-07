# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class MoneyflowIndThs(Base):
    """行业资金流向(THS)"""

    __tablename__: str = "moneyflow_ind_ths"
    __api_id__: ClassVar[int] = 343
    __api_name__: ClassVar[str] = "moneyflow_ind_ths"
    __api_title__: ClassVar[str] = "行业资金流向(THS)"
    __api_info_title__: ClassVar[str] = "行业资金流向(THS)"
    __api_path__: ClassVar[List[str]] = ["数据接口", "股票数据", "资金流向数据", "行业资金流向（THS）"]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 342, 343]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = ["stock_basic", "trade_cal"]
    __primary_key__: ClassVar[List[str]] = ["ts_code", "trade_date"]
    __start_date__: ClassVar[str | None] = "2024-09-10"
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
            "comment": "行业资金流向(THS)",
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
    industry = Column("industry", String(), nullable=False, default="", server_default=text("''"), comment="板块名称")
    lead_stock = Column(
        "lead_stock", String(), nullable=False, default="", server_default=text("''"), comment="领涨股票名称"
    )
    close = Column("close", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="收盘指数")
    pct_change = Column(
        "pct_change", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="指数涨跌幅"
    )
    company_num = Column(
        "company_num", Integer, nullable=False, default=0, server_default=text("'0'"), comment="公司数量"
    )
    pct_change_stock = Column(
        "pct_change_stock", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="领涨股涨跌幅"
    )
    close_price = Column(
        "close_price", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="领涨股最新价"
    )
    net_buy_amount = Column(
        "net_buy_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="流入资金(元)"
    )
    net_sell_amount = Column(
        "net_sell_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="流出资金(元)"
    )
    net_amount = Column(
        "net_amount", Float, nullable=False, default=0.0, server_default=text("'0.0'"), comment="净额(元)"
    )
