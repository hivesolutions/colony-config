#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2025 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Colony Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__copyright__ = "Copyright (c) 2008-2025 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

configuration = {
    "default_end_points": [("normal", "", 25, {})],
    "default_handler": "stream",
    "default_authentication_handler": "main",
    "default_session_handler": "main",
    "authentication_properties": {
        "authentication_handler": "python",
        "arguments": {
            "file_path": "%configuration:pt.hive.colony.plugins.authentication.python%/authentication.py"
        },
    },
    "session_properties": {
        "local_domains": ("127.0.0.1", "localhost"),
        "arguments": {
            "entity_manager_arguments": {
                "connection_parameters": {
                    "file_path": "%configuration:pt.hive.colony.plugins.mail.storage%/messages.db",
                    "autocommit": False,
                }
            }
        },
    },
}
