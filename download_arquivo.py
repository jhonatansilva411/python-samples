<<<<<<< HEAD
import io
import sys
import urllib.request as request

BUFF_SIZE = 1024

def download_length(response, output, length):
     times = length // BUFF_SIZE
     if length % BUFF_SIZE >0:
         times += 1
     for time in range(times):
         output.write(response.read(BUFF_SIZE))
         print("downloaded {}".format((((time * BUFF_SIZE)/length)*100)))


def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
             break
        output.write(data)
        print('download {bytes}'.format(bytes=total_downloaded))

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader('content-length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)
    response.close()
    out_file.close()
    print("finished")

if __name__ == '__main__':
    main()
=======
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
>>>>>>> master
