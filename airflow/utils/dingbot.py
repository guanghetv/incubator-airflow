# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from builtins import str
from past.builtins import basestring

import os

from airflow import configuration
from airflow.exceptions import AirflowConfigException
from airflow.utils.log.logging_mixin import LoggingMixin

import requests
import json
import urllib3
urllib3.disable_warnings()


def dingbot_msg_sender(msg):
    bot_url = configuration.get('dingding', 'BOT_URL')
    headers = {'Content-Type': 'application/json'}

    md_text = {
        "title": "AIRFLOW ERROR",
        "text": msg
    }

    post_data = {
        "msgtype": "markdown",
        "markdown": md_text
    }

    r = requests.post(bot_url, headers=headers,data=json.dumps(post_data))


def ding_bot_backend(msg):
    """
    Send ding message using backend specified in DING_BOT_BACKEND
    :param msg:
    :return:
    """
    path, attr = configuration.get('dingbot', 'DING_BOT_BACKEND').rsplit('.', 1)
    module = importlib.import_module(path)
    backend = getattr(module, attr)
    return backend(msg)
