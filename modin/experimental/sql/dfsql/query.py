# Licensed to Modin Development Team under one or more contributor license agreements.
# See the NOTICE file distributed with this work for additional information regarding
# copyright ownership.  The Modin Development Team licenses this file to you under the
# Apache License, Version 2.0 (the "License"); you may not use this file except in
# compliance with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.

import warnings

try:
    from dfsql import sql_query as dfsql_query

    # This import is required to inject the DataFrame.sql() method.
    import dfsql.extensions  # noqa: F401
except ImportError:
    warnings.warn(
        "Modin experimental sql interface requires dfsql to be installed."
        + ' Run `pip install "modin[sql]"` to install it.'
    )
    raise

__all__ = ["dfsql_query"]
