#!/usr/bin/env python
# -*- coding:utf8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,and_,or_
from sqlalchemy import Column,Integer,String,ForeignKey,SMALLINT
from sqlalchemy.orm import sessionmaker,relationship,backref
import sqlalchemy
import config
from sqlalchemy.dialects.mssql import SMALLINT


Base = declarative_base()
class Status(Base):
	__tablename__ = 'status'

	id = Column(Integer,primary_key=True)
	ifdel = Column(SMALLINT,default=1)
	host = Column(String(10))
	cpuidle = Column(String(15),unique=True)
	cpuload_5 = Column(String(10))
	cpuload_10 = Column(String(10))
	cpuload_15 = Column(String(10))
