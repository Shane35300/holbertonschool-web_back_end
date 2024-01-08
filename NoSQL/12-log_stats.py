#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient

def print_logs_stats(collection):
    """
    Print statistics about the Nginx logs in the given collection
    """
    # Total number of logs
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # Methods statistics
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"method {method}: {count}")

    # Status check count
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    # Connect to the MongoDB server
    client = MongoClient('localhost', 27017)

    # Select the 'logs' database and the 'nginx' collection
    db = client['logs']
    collection = db['nginx']

    # Print statistics about Nginx logs
    print_logs_stats(collection)

    # Close the MongoDB connection
    client.close()
