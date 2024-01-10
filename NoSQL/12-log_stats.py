#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('localhost', 27017)
    collection = client.logs.nginx

    total_logs = collection.count_documents({})

    print("{} logs".format(total_logs))

    print("Methods:")
    http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in http_methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    count_status = collection.count_documents({"method": "GET",
                                               "path": "/status"})
    print("{} status check".format(count_status))
