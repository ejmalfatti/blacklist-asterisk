#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from asterisk.agi import AGI


agi = AGI()

macri = "504"

agi.set_variable("MACRI", macri)
