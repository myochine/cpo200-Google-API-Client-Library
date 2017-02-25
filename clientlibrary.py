#!/usr/bin/env python
#
# Copyright 2015 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import json

from oauth2client.client import GoogleCredentials
from googleapiclient.discovery import build

credentials = GoogleCredentials.get_application_default()

GB_PROJECT_ID = "TODO"
SQL_INSTANCE = "guestbook-sql"

def main():
    cloudsql = build('sqladmin', 'v1beta4', credentials=credentials)
    response = cloudsql.instances().get(project=GB_PROJECT_ID,
                                        instance=SQL_INSTANCE,
                                        fields='settings').execute()
    print json.dumps(response,
                     sort_keys=True,
                     indent=4,
                     separators=(',', ': '))

if __name__ == '__main__':
    main()
