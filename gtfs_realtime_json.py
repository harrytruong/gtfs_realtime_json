#!/usr/bin/env python
import sys, urllib2
import gtfs_realtime_pb2, nyct_subway_pb2, protobuf_json
import json

def main():
    gtfs_realtime = gtfs_realtime_pb2.FeedMessage()
    gtfs_realtime.ParseFromString(urllib2.urlopen(sys.argv[1]).read())
    print json.dumps(protobuf_json.pb2json(gtfs_realtime), separators=(',',':'))
    return
    
if __name__ == '__main__':
    main()
