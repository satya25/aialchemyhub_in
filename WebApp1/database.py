#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
This script is part of the aialchemyhub.in project 
(https://github.com/satya25/aialchemyhub_in).

Distributed under the MIT License (see LICENSE file for details).
"""

# ----------------------------------------------------------------------------
# File Name         :       database.py
# Created By        :       Satya Prakash Nigam <spnigam25@yahoo.com>
# Created Date      :       June 01, 2024
# Last Update on    :       June 01, 2024
# version           :       1.0
# Release           :       R1
#
# Dependencies      :       
#
# Installation      :       $ pip install -r ./pandas/requirements.txt
#                           
# ---------------------------------------------------------------------------
# 
import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='aialchemyhub_tut_1'
    )
    return connection
