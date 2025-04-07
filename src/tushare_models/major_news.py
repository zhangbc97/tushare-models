# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class MajorNews(Base):
    """新闻通讯(长篇)"""

    __tablename__: str = "major_news"
    __api_id__: ClassVar[int] = 195
    __api_name__: ClassVar[str] = "major_news"
    __api_title__: ClassVar[str] = "新闻通讯(长篇)"
    __api_info_title__: ClassVar[str] = "新闻通讯"
    __api_path__: ClassVar[List[str]] = ["数据接口", "大模型语料专题数据", "新闻通讯（长篇）"]
    __api_path_ids__: ClassVar[List[int]] = [2, 142, 195]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["title", "pub_time"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "src": {"type": "str", "required": False, "description": "新闻来源"},
        "start_date": {"type": "datetime", "required": False, "description": "新闻发布开始时间"},
        "end_date": {"type": "datetime", "required": False, "description": "新闻发布结束时间"},
        "limit": {"type": "int", "required": False, "description": "单次返回数据长度"},
        "offset": {"type": "int", "required": False, "description": "请求数据的开始位移量"},
    }

    __mapper_args__ = {"primary_key": __primary_key__}
    __table_args__ = (
        PrimaryKeyConstraint(*__primary_key__),
        # ClickHouse引擎
        engines.ReplacingMergeTree(order_by=__primary_key__),
        {
            "comment": "新闻通讯(长篇)",
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

    title = Column("title", String(), nullable=False, default="", server_default=text("''"), comment="标题")
    content = Column("content", String(), nullable=False, default="", server_default=text("''"), comment="内容")
    pub_time = Column("pub_time", String(), nullable=False, default="", server_default=text("''"), comment="发布时间")
    src = Column("src", String(), nullable=False, default="", server_default=text("''"), comment="来源网站")
