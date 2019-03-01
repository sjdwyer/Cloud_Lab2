import socket, json, psutil, multiprocessing, requests

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/status")
def status():
    hostname = socket.gethostname()#Get hostname
    IPAddr = socket.gethostbyname(hostname)
    cpu_count = multiprocessing.cpu_count() #Cpu Count
    memory = psutil.virtual_memory() #Print Memory
    return jsonify ({'Hostanme' : hostname,
                     'IP Address' : IPAddr,
                     'CPU Count' : cpu_count,
                     'Memory' : memory
                      })

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080, debug=True) #Running on localhost/port 8080
