#!/usr/bin/env python
# coding: utf-8

# In[1]:


import grpc
from concurrent import futures
import threading
import time

import requests
# import the generated classes :
import broker_pb2 as pb2
import broker_pb2_grpc as grpc2

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# In[3]:



def SendRequests(stub):
    request = pb2.Empty()
    print("Sending Request")
    res = stub.Send(request)
    print("Sending Request")
    return



ip = "localhost"
port = 8061



port_address = "{}:{}".format(ip, port)
channel = grpc.insecure_channel(port_address)
stub = grpc2.send_fileStub(channel)


SendRequests(stub)



