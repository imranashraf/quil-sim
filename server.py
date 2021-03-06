import json
import urllib

import pyquil.quil as pq
import pyquil.api as api
from pyquil.gates import *

qvm = api.SyncConnection()

from flask import Flask, request, redirect, url_for, render_template, jsonify
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        jsdata = request.get_json()
        cmds = jsdata['ins'].split('`')
        print cmds
        inst=""
        for i in cmds:
            inst=inst+i
        inst=inst[:-1]
        print inst.split('\n')

        res = {}
        p=pq.Program()
        for i in range(len(cmds)):
            if(cmds[i]):
                p.inst(str(cmds[i][:-1]))
                res[str(i+1)]=str(qvm.wavefunction(p)[0])
        print res
        return jsonify(res)

    return render_template('index.html')

if __name__ == "__main__":
	app.run()
