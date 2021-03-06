# -*- coding: utf-8 -*
# Copyright (c) 2019 BuildGroup Data Services Inc.
# All rights reserved.
# This software is proprietary and confidential and may not under
# any circumstances be used, copied, or distributed.

class ApianException(Exception):
    pass


class QueryException(Exception):
    pass


class DoesNotExist(QueryException):
    pass


class MultipleObjectsReturned(QueryException):
    pass
