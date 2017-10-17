#!/usr
import os


class Config(object):
    """
    @brief      Basic config for Libra-X
    """

    TIMEZONE = "Asia/Shanghai"
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
