from flask import Flask, request
from flask_apscheduler import APScheduler
from generator import Invoices, Transfer
import starkbank
from config import Config
import json
import datetime
from settings import project_config

config = Config(project_config.PROJECT_ID)
starkbank.user = config.connection()

app = Flask(__name__)
scheduler = APScheduler()

def index():
    try:
        invoices = starkbank.invoice.create(Invoices.create_invoices())

        # debug - criando os invoices
        # ---------------------------

        print('\n')
        for invoice in invoices:
            print('Created ', invoice.name, '| R$', invoice.amount, '| ID', invoice.id, ' - ', datetime.datetime.now())

    except Exception as e:
        print(e)


@app.route("/home")
def home():
    return "working"

@app.route("/starkbank/webhook", methods=['POST'])
def webhook():
    data = json.loads(request.data)

    if data['event']['log']['type'] == 'credited':

        # debug - recebendo invoices
        # --------------------------

        id = data['event']['log']['invoice']['id']
        name = data['event']['log']['invoice']['name']
        amount = int(data['event']['log']['invoice']['amount'])

        print('Recived', name, '| R$', amount, '| ID', id, ' - ', datetime.datetime.now())

        try:
            starkbank.transfer.create([Transfer.transaction(amount)])

            # debug transação
            # ---------------
            print('Transaction status:', 200)
        except:

            # debug transação
            # ---------------
            print('Transaction status:', 500)

    return "Alive"

if __name__ == '__main__':

    tree_hours = 3 * 60 * 60
    scheduler.add_job(id = 'scheduler_1', func = index, trigger = 'interval', seconds = tree_hours)
    scheduler.start()
    app.run(host='0.0.0.0', port=80)