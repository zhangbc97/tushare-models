# This file is auto-generated by generate_models.py
# This file may be manually edited after generation
# The file has been formatted using isort and black

from typing import Any, ClassVar, Dict, List

from clickhouse_sqlalchemy import engines
from sqlalchemy import Column, PrimaryKeyConstraint, text

from tushare_models.core import Base, Date, DateTime, Float, Integer, String


class FilmRecord(Base):
    """全国电影剧本备案数据"""

    __tablename__: str = "film_record"
    __api_id__: ClassVar[int] = 156
    __api_name__: ClassVar[str] = "film_record"
    __api_title__: ClassVar[str] = "全国电影剧本备案数据"
    __api_info_title__: ClassVar[str] = "全国电影剧本备案数据"
    __api_path__: ClassVar[List[str]] = [
        "数据接口",
        "行业经济",
        "TMT行业",
        "全国电影剧本备案数据",
    ]
    __api_path_ids__: ClassVar[List[int]] = [2, 82, 83, 156]
    __api_points_required__: ClassVar[int] = 2000
    __api_special_permission__: ClassVar[bool] = False
    __has_vip__: ClassVar[bool] = False
    __dependencies__: ClassVar[List[str]] = []
    __primary_key__: ClassVar[List[str]] = ["film_name", "ann_date"]
    __start_date__: ClassVar[str | None] = None
    __end_date__: ClassVar[str | None] = None
    __api_params__: ClassVar[Dict[str, Any]] = {
        "ann_date": {"type": "str", "required": False, "description": "公布日期"},
        "start_date": {"type": "str", "required": False, "description": "开始日期"},
        "end_date": {"type": "str", "required": False, "description": "结束日期"},
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
            "comment": "全国电影剧本备案数据",
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

    rec_no = Column(
        "rec_no",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="备案号",
    )
    film_name = Column(
        "film_name",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="影片名称",
    )
    rec_org = Column(
        "rec_org",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="备案单位",
    )
    script_writer = Column(
        "script_writer",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="编剧",
    )
    rec_result = Column(
        "rec_result",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="备案结果",
    )
    rec_area = Column(
        "rec_area",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="备案地",
    )
    classified = Column(
        "classified",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="影片分类",
    )
    date_range = Column(
        "date_range",
        String(),
        nullable=False,
        default="",
        server_default=text("''"),
        comment="备案日期",
    )
    ann_date = Column(
        "ann_date",
        Date,
        nullable=False,
        default="1970-01-01",
        server_default=text("'1970-01-01'"),
        comment="备案结果发布时间",
    )
