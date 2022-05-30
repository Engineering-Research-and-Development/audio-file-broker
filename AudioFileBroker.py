#!/usr/bin/env python
# coding: utf-8

# In[1]:


import grpc
from concurrent import futures
import threading
import time

import broker_pb2 as pb2
import broker_pb2_grpc as grpc2
from http.server import SimpleHTTPRequestHandler, HTTPServer

import os
import io
import queue
from pydub import AudioSegment

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


# In[2]:


port = 8061
q = queue.Queue()


# In[3]:
class testHTTPServer_RequestHandler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello world!"
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def run(ssc):
        print('Running Server...')

        
       
    def do_POST(self):
        
        filename ="audio.wav"
        file_length = int(self.headers['Content-Length'])
        try:
            with open (filename, "wb") as out_file:
                out_file.write(self.rfile.read(file_length))
                out_file.close()
            q.put(1)
            self.send_response(201, 'Created')
            self.end_headers()
            self.wfile.write("File created, queue filled".encode("utf-8"))
        except Exception as e:
            self.send_response(409, 'Conflict')
            self.end_headers()
            errfile = open ("err.txt", "a")
            errfile.write(" " + e.message)
            errfile.close()
            self.wfile.write("Error in Creating files".encode("utf-8"))
                
        
        
        
        

def PickFile(audioid, path):
    
    sound = AudioSegment.from_wav(path)
    f = io.BytesIO()
    sound.export(f, format="wav")
    sound = f.getvalue()
    return audioid, sound


# In[4]:


class send_fileServiceImpl(grpc2.send_fileServicer):
    
    def __init__(self, queue):
        self.queue = queue
        
        
    def QueuePut(self):
        self.queue.put(1)


    def Send(self, request, context):
        
        self.queue.get(block=True)
        filepath = "audio.wav"      
        
        audioid = 1
        
        f = pb2.AudioFile()
        f.audioid, f.audiofile = PickFile(audioid, filepath)
        
        logger.debug("Sending audio: {}".format(f.audioid))
        print("Sending audio: {}".format(f.audioid))
        
        return f





server = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))
grpc2.add_send_fileServicer_to_server(send_fileServiceImpl(q), server)
print("Starting server, Listening on port:" + str(port))
server.add_insecure_port("[::]:{}".format(port))
server.start()
#server.wait_for_termination()


server_address = ("0.0.0.0", 8062)
httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
httpd.serve_forever()






















