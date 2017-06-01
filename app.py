import sys
from io import BytesIO

import telegram
import imp
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '394614679:AAHqo72cfnrUcs5kEDwYkP_NnljyiGXuY_g'
WEBHOOK_URL = 'https://2d1c9fb9.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)

machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'state3',
        'state3_1',
        'state4_1',
        'state4_1_check',
        'state3_2',
        'state4_2',
        'state3_3',
        'state5',
        'state6',
        'state_book',
        'state_video'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },

        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state5',
            'conditions': 'is_going_to_state5'
        },
        
        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state3',
            'conditions': 'is_going_to_state3'
        }, 

        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state3_1',
            'conditions': 'is_going_to_state3_1'
        },

        {
            'trigger': 'advance',
            'source': 'state3_1',
            'dest': 'state4_1',
            'conditions': 'is_going_to_state4_1'
        },

        {
            'trigger': 'advance',
            'source': 'state4_1',
            'dest': 'state4_1_check',
            'conditions': 'is_going_to_state4_1_check'
        },

        {
            'trigger': 'advance',
            'source': 'state4_1',
            'dest': 'state3_1',
            'conditions': 'is_going_back_to_state3_1'
        },


        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state3_2',
            'conditions': 'is_going_to_state3_2'
        },

        {
            'trigger': 'advance',
            'source': 'state3_2',
            'dest': 'state4_2',
            'conditions': 'is_going_to_state4_2'
        },
        
        {
            'trigger': 'advance',
            'source': 'state3',
            'dest': 'state3_3',
            'conditions': 'is_going_to_state3_3'
        },

        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state_book',
            'conditions': 'is_going_to_state_book'
        }, 

        {
            'trigger': 'advance',
            'source': 'state2',
            'dest': 'state_video',
            'conditions': 'is_going_to_state_video'
        },   

        {
            'trigger': 'advance',
            'source': 'state5',
            'dest': 'state6',
            'conditions': 'is_going_to_state6'
        },  

        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state4_1_check',
                'state4_2',
                'state3_3',
                'state6',
                'state_book',
                'state_video'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    #machine.go_next(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
