import socket, json, psutil, multiprocessing

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/status")
def status():
    hostname = socket.gethostname()#Get hostname
    IPAddr = socket.gethostbyname(hostname)#Get IP Address
    cpu_count = multiprocessing.cpu_count() #Cpu Count
    memory = psutil.virtual_memory().total / (1024.0 ** 3) #Print Memory
    return jsonify({'Hostanme' : hostname,
                     'IP Address' : IPAddr,
                     'CPU Count' : cpu_count,
                     'Memory Total in GBs' : memory
                      })

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080, debug=False) #Running on localhost/port 8080
