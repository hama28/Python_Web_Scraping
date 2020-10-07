#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import datetime
from google.appengine.ext.webapp import template

register = template.create_template_register()

def toJst(value):
  return value.replace(tzinfo=UtcTzinfo()).astimezone(JstTzinfo())
register.filter(toJst)

def toPst(value):
  return value.replace(tzinfo=UtcTzinfo()).astimezone(PstTzinfo())
register.filter(toPst)

def toEst(value):
  return value.replace(tzinfo=UtcTzinfo()).astimezone(EstTzinfo())
register.filter(toEst)

class UtcTzinfo(datetime.tzinfo):
  def utcoffset(self, dt): return datetime.timedelta(0)
  def dst(self, dt): return datetime.timedelta(0)
  def tzname(self, dt): return 'UTC'
  def olsen_name(self): return 'UTC'

class JstTzinfo(datetime.tzinfo):
  def utcoffset(self, dt): return datetime.timedelta(hours=9)
  def dst(self, dt): return datetime.timedelta(0)
  def tzname(self, dt): return "JST"
  def olsen_name(self): return 'Tokyo/Asia'

class EstTzinfo(datetime.tzinfo):
  def utcoffset(self, dt): return datetime.timedelta(hours=-5)
  def dst(self, dt): return datetime.timedelta(0)
  def tzname(self, dt): return 'EST+05EDT'
  def olsen_name(self): return 'US/Eastern'

class PstTzinfo(datetime.tzinfo):
  def utcoffset(self, dt): return datetime.timedelta(hours=-8)
  def dst(self, dt): return datetime.timedelta(0)
  def tzname(self, dt): return 'PST+08PDT'
  def olsen_name(self): return 'US/Pacific'
