#
# This file is part of Land Cover Classification System Database Model.
# Copyright (C) 2019 INPE.
#
# Land Cover Classification System Database Model is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

"""Land Cover Classification System Model ."""

from sqlalchemy import JSON, Column, Integer, Text

from ..config import Config
from .base import BaseModel


class ApplicationsStyle(BaseModel):
    """ApplicationsStyle."""

    __tablename__ = 'applications_style'
    __table_args__ = dict(schema=Config.ACTIVITIES_SCHEMA)

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text, nullable=False)
    file = Column(JSON, nullable=True)
