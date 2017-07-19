#    Copyright 2017 phData Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

""" Promote an SDC pipeline from one environment to another."""
#!/usr/bin/python
import argparse
import api
import json
import logging

def main():
    """Main script entry point."""
    parser = argparse.ArgumentParser(
        description='Promote an SDC pipeine from one environment to another.')
    parser.add_argument('--creds', required=True, dest='src_creds', metavar='creds',
            help='Destination credentials in user:pass format')
    parser.add_argument('--dstHostUrl', required=True, dest='dst_host_url', metavar='sourceHostUrl',
                        help='The host URL of the source SDC (e.g. "http://sdc-dev.phdata.io:18360/")')
    parser.add_argument('--pipelineId', required=True, dest='pipeline_id',
                        metavar='sourcePipelineId',
                        help='The ID of a pipeline in the source SDC')

    parser.add_argument('--pipelineJson', required=True, dest='pipeline_json', help='Pipeline json file path')

    args = parser.parse_args()

    with open(args.pipeline_json) as pipeline_json:
        src_url = api.build_api_url(args.dst_host_url)
        src_auth = tuple(args.src_creds.split(':'))
        api.import_pipeline(src_url, args.pipeline_id, src_auth, json.load(pipeline_json))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    main()
