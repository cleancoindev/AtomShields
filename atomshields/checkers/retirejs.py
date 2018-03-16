#!/usr/bin/env python
# -*- coding:utf8 -*-

from base import GenericChecker

class RetireJSChecker(GenericChecker):

	NAME = "retirejs"
	DESCRIPTION = """Detecta ficheros JavaScript vulnerables"""
	CONFIG = {
		"enabled": True,
		"exclude_paths": ["test/"]
	}

	def __init__(self):
		pass