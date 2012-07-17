#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

configuration = {
    "default_end_points" : [
        (
            "normal", "", 8080, {}
        )
    ],
    "default_handler" : "file",
    "default_encoding" : None,
    "default_content_type_charset" : "utf-8",
    "default_service_type" : "async",
    "default_client_connection_timeout" : 3,
    "default_connection_timeout" : 30,
    "default_request_timeout" : 3,
    "default_response_timeout" : 30,
    "default_number_threads" : 1,
    "default_scheduling_algorithm" : 2,
    "default_maximum_number_threads" : 30,
    "default_maximum_number_work_threads" : 150,
    "default_work_scheduling_algorithm" : 3,
    "preferred_error_handlers" : [
        "template",
        "default"
    ],
    "verify_request" : False,
    "log_file_path" : "%configuration:pt.hive.colony.plugins.service.http%/access.log",
    "connectors" : [
        {
            "default_end_points" : [
                (
                    "normal", "", 8181, {}
                )
            ],
            "default_handler" : "file"
        }
    ],
    "redirections" : {
        "resolution_order" : [
            "/manager",
            "/"
        ],
        "/manager" : {
            "target" : "/dynamic/rest/mvc/nanger/",
            "recursive_redirection" : True
        },
        "/" : {
            "target" : "/welcome_handler/",
            "recursive_redirection" : True
        }
    },
    "contexts" : {
        "resolution_order" : [
            "/dynamic",
            "/welcome_handler",
            "/system_information_handler",
            "/system_information",
            "/template_error_handler",
            "/template_directory_handler",
            "/cgi-bin",
            "/fastcgi-bin",
            "/wsgi-bin",
            "/system_unix",
            "/system_windows"
        ],
        "/dynamic" : {
            "handler" : "colony",
            "allow_redirection" : False,
            "request_properties" : {}
        },
        "/welcome_handler" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.colony.plugins.service.http.welcome}/service_http/welcome/resources",
                "default_page" : "welcome.html"
            }
        },
        "/system_information_handler" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.colony.plugins.service.http.system_information}/service_http/system_information/resources"
            }
        },
        "/system_information" : {
            "handler" : "system_information",
            "allow_redirection" : False
        },
        "/template_error_handler" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.colony.plugins.service.http.template_error}/service_http/template_error/resources"
            }
        },
        "/template_directory_handler" : {
            "handler" : "file",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "$plugin{pt.hive.colony.plugins.service.http.template_directory}/service_http/template_directory/resources"
            }
        },
        "/cgi-bin" : {
            "handler" : "cgi",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "${HOME}/cgi-bin",
            }
        },
        "/fastcgi-bin" : {
            "handler" : "fast_cgi",
            "allow_redirection" : False,
            "request_properties" : {
                "handler_type" : "local",
                "base_path" : "${HOME}/fcgi-bin",
                "connection_type" : 1,
                "connection_arguments" : (
                    "localhost",
                    9010
                )
            }
        },
        "/wsgi-bin" : {
            "handler" : "wsgi",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "${HOME}/wsgi-bin",
                "module_name" : "server",
                "application_name" : "application"
            }
        },
        "/system_unix" : {
            "handler" : "file",
            "authentication_handler" : "main",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "/"
            },
            "authentication_properties" : {
                "authentication_handler" : "python",
                "authentication_realm" : "system",
                "arguments" : {
                    "file_path" : "%configuration:pt.hive.colony.plugins.authentication.python%/authentication.py"
                }
            }
        },
        "/system_windows" : {
            "handler" : "file",
            "authentication_handler" : "main",
            "allow_redirection" : False,
            "request_properties" : {
                "base_path" : "c:/"
            },
            "authentication_properties" : {
                "authentication_handler" : "python",
                "authentication_realm" : "system",
                "arguments" : {
                    "file_path" : "%configuration:pt.hive.colony.plugins.authentication.python%/authentication.py"
                }
            }
        }
    }
}
