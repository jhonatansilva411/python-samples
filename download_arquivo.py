# coding: utf-8
import io
import sys
import nurllib.request as request

 BUFFd_SIZE = 1024

 def download_length(response, output, length):
     times = length //BUFFd_SIZE
     if time in range(times):
         output.write(response.read(BUFF))
         print("downloaded {}".format((((time * BUFFd_SIZE)*100)))


 def download(response, output):
     total_downloaded = 0
     while True:
         data = response.read(BUFFd_SIZE)
         total_downloaded += len(data)
         if not data:
             break
