# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FinaIndicator(Base):
    """财务指标数据"""

    __tablename__: str = "fina_indicator"
    __api_id__: ClassVar[int] = 79
    __api_name__: ClassVar[str] = "fina_indicator"
    __api_title__: ClassVar[str] = "财务指标数据"
    __api_info_title__: ClassVar[str] = "财务指标数据"
    __api_path__: ClassVar[List[str]] = [
        "数据接口",
        "沪深股票",
        "财务数据",
        "财务指标数据",
    ]
    __api_path_ids__: ClassVar[List[int]] = [2, 14, 16, 79]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = True
    __dependencies__: ClassVar[List[str]] = ["stock_basic"]
    __primary_key__: ClassVar[List[str]] = [
        "ts_code",
        "ann_date",
        "end_date",
        "update_flag",
    ]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ts_code": {"type": "str", "required": True, "description": "股票代码"},
        "ann_date": {"type": "str", "required": False, "description": "公告日期"},
        "start_date": {
            "type": "str",
            "required": False,
            "description": "报告期开始日期",
        },
        "end_date": {"type": "str", "required": False, "description": "报告期结束日期"},
        "period": {"type": "str", "required": False, "description": "报告期"},
        "update_flag": {"type": "str", "required": False, "description": "更新标志"},
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
            "comment": "财务指标数据",
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
    end_date = Column(
        "end_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="报告期",
    )
    eps = Column(
        "eps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="基本每股收益",
    )
    dt_eps = Column(
        "dt_eps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="稀释每股收益",
    )
    total_revenue_ps = Column(
        "total_revenue_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股营业总收入",
    )
    revenue_ps = Column(
        "revenue_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股营业收入",
    )
    capital_rese_ps = Column(
        "capital_rese_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股资本公积",
    )
    surplus_rese_ps = Column(
        "surplus_rese_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股盈余公积",
    )
    undist_profit_ps = Column(
        "undist_profit_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股未分配利润",
    )
    extra_item = Column(
        "extra_item",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="非经常性损益",
    )
    profit_dedt = Column(
        "profit_dedt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="扣除非经常性损益后的净利润",
    )
    gross_margin = Column(
        "gross_margin",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="毛利",
    )
    current_ratio = Column(
        "current_ratio",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="流动比率",
    )
    quick_ratio = Column(
        "quick_ratio",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="速动比率",
    )
    cash_ratio = Column(
        "cash_ratio",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="保守速动比率",
    )
    invturn_days = Column(
        "invturn_days",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="存货周转天数",
    )
    arturn_days = Column(
        "arturn_days",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="应收账款周转天数",
    )
    inv_turn = Column(
        "inv_turn",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="存货周转率",
    )
    ar_turn = Column(
        "ar_turn",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="应收账款周转率",
    )
    ca_turn = Column(
        "ca_turn",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="流动资产周转率",
    )
    fa_turn = Column(
        "fa_turn",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="固定资产周转率",
    )
    assets_turn = Column(
        "assets_turn",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="总资产周转率",
    )
    op_income = Column(
        "op_income",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动净收益",
    )
    valuechange_income = Column(
        "valuechange_income",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="价值变动净收益",
    )
    interst_income = Column(
        "interst_income",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="利息费用",
    )
    daa = Column(
        "daa",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="折旧与摊销",
    )
    ebit = Column(
        "ebit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="息税前利润",
    )
    ebitda = Column(
        "ebitda",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="息税折旧摊销前利润",
    )
    fcff = Column(
        "fcff",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="企业自由现金流量",
    )
    fcfe = Column(
        "fcfe",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="股权自由现金流量",
    )
    current_exint = Column(
        "current_exint",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="无息流动负债",
    )
    noncurrent_exint = Column(
        "noncurrent_exint",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="无息非流动负债",
    )
    interestdebt = Column(
        "interestdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="带息债务",
    )
    netdebt = Column(
        "netdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净债务",
    )
    tangible_asset = Column(
        "tangible_asset",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="有形资产",
    )
    working_capital = Column(
        "working_capital",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营运资金",
    )
    networking_capital = Column(
        "networking_capital",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营运流动资本",
    )
    invest_capital = Column(
        "invest_capital",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="全部投入资本",
    )
    retained_earnings = Column(
        "retained_earnings",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="留存收益",
    )
    diluted2_eps = Column(
        "diluted2_eps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="期末摊薄每股收益",
    )
    bps = Column(
        "bps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股净资产",
    )
    ocfps = Column(
        "ocfps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股经营活动产生的现金流量净额",
    )
    retainedps = Column(
        "retainedps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股留存收益",
    )
    cfps = Column(
        "cfps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股现金流量净额",
    )
    ebit_ps = Column(
        "ebit_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股息税前利润",
    )
    fcff_ps = Column(
        "fcff_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股企业自由现金流量",
    )
    fcfe_ps = Column(
        "fcfe_ps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股股东自由现金流量",
    )
    netprofit_margin = Column(
        "netprofit_margin",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售净利率",
    )
    grossprofit_margin = Column(
        "grossprofit_margin",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售毛利率",
    )
    cogs_of_sales = Column(
        "cogs_of_sales",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售成本率",
    )
    expense_of_sales = Column(
        "expense_of_sales",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售期间费用率",
    )
    profit_to_gr = Column(
        "profit_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净利润/营业总收入",
    )
    saleexp_to_gr = Column(
        "saleexp_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售费用/营业总收入",
    )
    adminexp_of_gr = Column(
        "adminexp_of_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="管理费用/营业总收入",
    )
    finaexp_of_gr = Column(
        "finaexp_of_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="财务费用/营业总收入",
    )
    impai_ttm = Column(
        "impai_ttm",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="资产减值损失/营业总收入",
    )
    gc_of_gr = Column(
        "gc_of_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业总成本/营业总收入",
    )
    op_of_gr = Column(
        "op_of_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润/营业总收入",
    )
    ebit_of_gr = Column(
        "ebit_of_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="息税前利润/营业总收入",
    )
    roe = Column(
        "roe",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产收益率",
    )
    roe_waa = Column(
        "roe_waa",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="加权平均净资产收益率",
    )
    roe_dt = Column(
        "roe_dt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产收益率(扣除非经常损益)",
    )
    roa = Column(
        "roa",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="总资产报酬率",
    )
    npta = Column(
        "npta",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="总资产净利润",
    )
    roic = Column(
        "roic",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="投入资本回报率",
    )
    roe_yearly = Column(
        "roe_yearly",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="年化净资产收益率",
    )
    roa2_yearly = Column(
        "roa2_yearly",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="年化总资产报酬率",
    )
    roe_avg = Column(
        "roe_avg",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="平均净资产收益率(增发条件)",
    )
    opincome_of_ebt = Column(
        "opincome_of_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动净收益/利润总额",
    )
    investincome_of_ebt = Column(
        "investincome_of_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="价值变动净收益/利润总额",
    )
    n_op_profit_of_ebt = Column(
        "n_op_profit_of_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业外收支净额/利润总额",
    )
    tax_to_ebt = Column(
        "tax_to_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="所得税/利润总额",
    )
    dtprofit_to_profit = Column(
        "dtprofit_to_profit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="扣除非经常损益后的净利润/净利润",
    )
    salescash_to_or = Column(
        "salescash_to_or",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售商品提供劳务收到的现金/营业收入",
    )
    ocf_to_or = Column(
        "ocf_to_or",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/营业收入",
    )
    ocf_to_opincome = Column(
        "ocf_to_opincome",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/经营活动净收益",
    )
    capitalized_to_da = Column(
        "capitalized_to_da",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="资本支出/折旧和摊销",
    )
    debt_to_assets = Column(
        "debt_to_assets",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="资产负债率",
    )
    assets_to_eqt = Column(
        "assets_to_eqt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="权益乘数",
    )
    dp_assets_to_eqt = Column(
        "dp_assets_to_eqt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="权益乘数(杜邦分析)",
    )
    ca_to_assets = Column(
        "ca_to_assets",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="流动资产/总资产",
    )
    nca_to_assets = Column(
        "nca_to_assets",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="非流动资产/总资产",
    )
    tbassets_to_totalassets = Column(
        "tbassets_to_totalassets",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="有形资产/总资产",
    )
    int_to_talcap = Column(
        "int_to_talcap",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="带息债务/全部投入资本",
    )
    eqt_to_talcapital = Column(
        "eqt_to_talcapital",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属于母公司的股东权益/全部投入资本",
    )
    currentdebt_to_debt = Column(
        "currentdebt_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="流动负债/负债合计",
    )
    longdeb_to_debt = Column(
        "longdeb_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="非流动负债/负债合计",
    )
    ocf_to_shortdebt = Column(
        "ocf_to_shortdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/流动负债",
    )
    debt_to_eqt = Column(
        "debt_to_eqt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="产权比率",
    )
    eqt_to_debt = Column(
        "eqt_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属于母公司的股东权益/负债合计",
    )
    eqt_to_interestdebt = Column(
        "eqt_to_interestdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属于母公司的股东权益/带息债务",
    )
    tangibleasset_to_debt = Column(
        "tangibleasset_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="有形资产/负债合计",
    )
    tangasset_to_intdebt = Column(
        "tangasset_to_intdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="有形资产/带息债务",
    )
    tangibleasset_to_netdebt = Column(
        "tangibleasset_to_netdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="有形资产/净债务",
    )
    ocf_to_debt = Column(
        "ocf_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/负债合计",
    )
    ocf_to_interestdebt = Column(
        "ocf_to_interestdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/带息债务",
    )
    ocf_to_netdebt = Column(
        "ocf_to_netdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额/净债务",
    )
    ebit_to_interest = Column(
        "ebit_to_interest",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="已获利息倍数(EBIT/利息费用)",
    )
    longdebt_to_workingcapital = Column(
        "longdebt_to_workingcapital",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="长期债务与营运资金比率",
    )
    ebitda_to_debt = Column(
        "ebitda_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="息税折旧摊销前利润/负债合计",
    )
    turn_days = Column(
        "turn_days",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业周期",
    )
    roa_yearly = Column(
        "roa_yearly",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="年化总资产净利率",
    )
    roa_dp = Column(
        "roa_dp",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="总资产净利率(杜邦分析)",
    )
    fixed_assets = Column(
        "fixed_assets",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="固定资产合计",
    )
    profit_prefin_exp = Column(
        "profit_prefin_exp",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="扣除财务费用前营业利润",
    )
    non_op_profit = Column(
        "non_op_profit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="非营业利润",
    )
    op_to_ebt = Column(
        "op_to_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润／利润总额",
    )
    nop_to_ebt = Column(
        "nop_to_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="非营业利润／利润总额",
    )
    ocf_to_profit = Column(
        "ocf_to_profit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额／营业利润",
    )
    cash_to_liqdebt = Column(
        "cash_to_liqdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="货币资金／流动负债",
    )
    cash_to_liqdebt_withinterest = Column(
        "cash_to_liqdebt_withinterest",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="货币资金／带息流动负债",
    )
    op_to_liqdebt = Column(
        "op_to_liqdebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润／流动负债",
    )
    op_to_debt = Column(
        "op_to_debt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润／负债合计",
    )
    roic_yearly = Column(
        "roic_yearly",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="年化投入资本回报率",
    )
    total_fa_trun = Column(
        "total_fa_trun",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="固定资产合计周转率",
    )
    profit_to_op = Column(
        "profit_to_op",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="利润总额／营业收入",
    )
    q_opincome = Column(
        "q_opincome",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动单季度净收益",
    )
    q_investincome = Column(
        "q_investincome",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="价值变动单季度净收益",
    )
    q_dtprofit = Column(
        "q_dtprofit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="扣除非经常损益后的单季度净利润",
    )
    q_eps = Column(
        "q_eps",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股收益(单季度)",
    )
    q_netprofit_margin = Column(
        "q_netprofit_margin",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售净利率(单季度)",
    )
    q_gsprofit_margin = Column(
        "q_gsprofit_margin",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售毛利率(单季度)",
    )
    q_exp_to_sales = Column(
        "q_exp_to_sales",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售期间费用率(单季度)",
    )
    q_profit_to_gr = Column(
        "q_profit_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净利润／营业总收入(单季度)",
    )
    q_saleexp_to_gr = Column(
        "q_saleexp_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售费用／营业总收入 (单季度)",
    )
    q_adminexp_to_gr = Column(
        "q_adminexp_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="管理费用／营业总收入 (单季度)",
    )
    q_finaexp_to_gr = Column(
        "q_finaexp_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="财务费用／营业总收入 (单季度)",
    )
    q_impair_to_gr_ttm = Column(
        "q_impair_to_gr_ttm",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="资产减值损失／营业总收入(单季度)",
    )
    q_gc_to_gr = Column(
        "q_gc_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业总成本／营业总收入 (单季度)",
    )
    q_op_to_gr = Column(
        "q_op_to_gr",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润／营业总收入(单季度)",
    )
    q_roe = Column(
        "q_roe",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产收益率(单季度)",
    )
    q_dt_roe = Column(
        "q_dt_roe",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产单季度收益率(扣除非经常损益)",
    )
    q_npta = Column(
        "q_npta",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="总资产净利润(单季度)",
    )
    q_opincome_to_ebt = Column(
        "q_opincome_to_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动净收益／利润总额(单季度)",
    )
    q_investincome_to_ebt = Column(
        "q_investincome_to_ebt",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="价值变动净收益／利润总额(单季度)",
    )
    q_dtprofit_to_profit = Column(
        "q_dtprofit_to_profit",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="扣除非经常损益后的净利润／净利润(单季度)",
    )
    q_salescash_to_or = Column(
        "q_salescash_to_or",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="销售商品提供劳务收到的现金／营业收入(单季度)",
    )
    q_ocf_to_sales = Column(
        "q_ocf_to_sales",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额／营业收入(单季度)",
    )
    q_ocf_to_or = Column(
        "q_ocf_to_or",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额／经营活动净收益(单季度)",
    )
    basic_eps_yoy = Column(
        "basic_eps_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="基本每股收益同比增长率(%)",
    )
    dt_eps_yoy = Column(
        "dt_eps_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="稀释每股收益同比增长率(%)",
    )
    cfps_yoy = Column(
        "cfps_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股经营活动产生的现金流量净额同比增长率(%)",
    )
    op_yoy = Column(
        "op_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润同比增长率(%)",
    )
    ebt_yoy = Column(
        "ebt_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="利润总额同比增长率(%)",
    )
    netprofit_yoy = Column(
        "netprofit_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属母公司股东的净利润同比增长率(%)",
    )
    dt_netprofit_yoy = Column(
        "dt_netprofit_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属母公司股东的净利润-扣除非经常损益同比增长率(%)",
    )
    ocf_yoy = Column(
        "ocf_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="经营活动产生的现金流量净额同比增长率(%)",
    )
    roe_yoy = Column(
        "roe_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产收益率(摊薄)同比增长率(%)",
    )
    bps_yoy = Column(
        "bps_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="每股净资产相对年初增长率(%)",
    )
    assets_yoy = Column(
        "assets_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="资产总计相对年初增长率(%)",
    )
    eqt_yoy = Column(
        "eqt_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属母公司的股东权益相对年初增长率(%)",
    )
    tr_yoy = Column(
        "tr_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业总收入同比增长率(%)",
    )
    or_yoy = Column(
        "or_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业收入同比增长率(%)",
    )
    q_gr_yoy = Column(
        "q_gr_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业总收入同比增长率(%)(单季度)",
    )
    q_gr_qoq = Column(
        "q_gr_qoq",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业总收入环比增长率(%)(单季度)",
    )
    q_sales_yoy = Column(
        "q_sales_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业收入同比增长率(%)(单季度)",
    )
    q_sales_qoq = Column(
        "q_sales_qoq",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业收入环比增长率(%)(单季度)",
    )
    q_op_yoy = Column(
        "q_op_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润同比增长率(%)(单季度)",
    )
    q_op_qoq = Column(
        "q_op_qoq",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="营业利润环比增长率(%)(单季度)",
    )
    q_profit_yoy = Column(
        "q_profit_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净利润同比增长率(%)(单季度)",
    )
    q_profit_qoq = Column(
        "q_profit_qoq",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净利润环比增长率(%)(单季度)",
    )
    q_netprofit_yoy = Column(
        "q_netprofit_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属母公司股东的净利润同比增长率(%)(单季度)",
    )
    q_netprofit_qoq = Column(
        "q_netprofit_qoq",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="归属母公司股东的净利润环比增长率(%)(单季度)",
    )
    equity_yoy = Column(
        "equity_yoy",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="净资产同比增长率",
    )
    rd_exp = Column(
        "rd_exp",
        Float,
        nullable=False,
        default=0.0,
        server_default=text("'0.0'"),
        comment="研发费用",
    )
    update_flag = Column(
        "update_flag",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="更新标识",
    )
