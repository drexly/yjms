# -*- coding: utf-8 -*-
import codecs

import datetime
import os
from seoulhotver2.settings import BASE_DIR
from .models import SubwayModel


def container():
    daytmp=str(datetime.datetime.now()).split(' ')

