# -- coding: UTF-8 --
from transitions.extensions import GraphMachine

global name
global reserve

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
#state 1(finish)
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == "who are you?" or text.lower() == "what can you do?"
    def on_enter_state1(self, update):
        tmp = "I'm TattosBot,a Chatbot,maybe can provide you some service.\n";
        tmp2 = "If you need some service,please input \"I need some service\""
        tmp += tmp2;
        update.message.reply_text(tmp)
        self.go_back(update)
    def on_exit_state1(self, update):
        print('Leaving state1')
#state 2
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'i need some service'
    def on_enter_state2(self, update):
        update.message.reply_text("What type of service you need?\n(food,book,video)")
        self.advance(update)
    def on_exit_state2(self, update):
        print('Leaving state2')
#state 3
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'food'
    def on_enter_state3(self, update):
        update.message.reply_text("What do you need?\n(please input number)\n(1)reserve a table\n(2)order a meal\n(3)ask other information")
        self.advance(update)
    def on_exit_state3(self, update):
        print('Leaving state3')
#state 3_1
    def is_going_to_state3_1(self, update):
        text = update.message.text
        return  text.lower() == '1' or text.lower() == '(1)' or text.lower() == 'reserve a table'
    def is_going_back_to_state3_1(self, update):
        text = update.message.text
        return  text.lower() == 'n' or text.lower() == 'no'
    def on_enter_state3_1(self, update):
        update.message.reply_text("Please input the total number of person and reservation time.\n (example: for five at 7:20 pm.)")
        self.advance(update)
    def on_exit_state3_1(self, update):
        print('Leaving state3_1')
#state 4_1
    def is_going_to_state4_1(self, update):
        text = update.message.text
        global reserve
        reserve = text
        return  (text.lower() != '1' and text.lower() != '(1)' and text.lower() != 'reserve a table' and text.lower() != 'n' and text.lower() != 'no')
    def on_enter_state4_1(self, update):
        update.message.reply_text("Check if the following information is correct(Y/N):\n" + 
            "You reserve a table " + reserve.lower())
        update.message.text = ""
        self.advance(update)
    def on_exit_state4_1(self, update):
        print('Leaving state4_1')
#state 4_1_check
    def is_going_to_state4_1_check(self, update):
        text = update.message.text
        return  text.lower() == 'y' or text.lower() == 'yes'
    def on_enter_state4_1_check(self, update):
        update.message.reply_text("All right.You has been booked successfully.")
        self.go_back(update)
    def on_exit_state4_1_check(self, update):
        print('Leaving state4_1_check')
#state 3_2
    def is_going_to_state3_2(self, update):
        text = update.message.text
        return  text.lower() == '2' or text.lower() == '(2)' or text.lower() == 'order a meal'
    def on_enter_state3_2(self, update):
        update.message.reply_text("What would you like to eat?\n(please input number)\n(1)Fried rice\n(2)Pasta\n")
        update.message.text = ""
        self.advance(update)
    def on_exit_state3_2(self, update):
        print('Leaving state3_2')
#state 4_2
    def is_going_to_state4_2(self, update):
        text = update.message.text
        return  (text.lower() == '1' or text.lower() == '(1)' or text.lower() == 'fried rice'
                or text.lower() == '2' or text.lower() == '(2)' or text.lower() == 'pasta')
    def on_enter_state4_2(self, update):
        update.message.reply_text("OK,we will serve you shortly.")
        self.go_back(update)
    def on_exit_state4_2(self, update):
        print('Leaving state4_2')
#state 3_3
    def is_going_to_state3_3(self, update):
        text = update.message.text
        return  text.lower() == '3' or text.lower() == '(3)' or text.lower() == 'ask other information'
    def on_enter_state3_3(self, update):
        update.message.reply_text("If you have any other questions, please call customer service:\n0800-XXX-XXX\n")
        self.go_back(update)
    def on_exit_state3_3(self, update):
        print('Leaving state3_3')
#state_book
    def is_going_to_state_book(self, update):
        text = update.message.text
        return text.lower() == 'book'
    def on_enter_state_book(self, update):
        update.message.reply_text("You may like this:\n[博客來]\n(http://www.books.com.tw/?gclid=CjwKCAjw07nJBRBGEiwAUXBPmfuWUBqlGHbSA08eP6nwThe814rd5aa-62PI6UsTWs5C8bp634oKXRoCnoYQAvD_BwE)")
        self.go_back(update)
    def on_exit_state_book(self, update):
        print('Leaving state_book')
#state_video
    def is_going_to_state_video(self, update):
        text = update.message.text
        return text.lower() == 'video'
    def on_enter_state_video(self, update):
        update.message.reply_text("You may like this:\n[Youtube]\n(https://www.youtube.com)")
        self.go_back(update)
    def on_exit_state_video(self, update):
        print('Leaving state4')
#state 5 (5 , 6 finish)
    def is_going_to_state5(self, update):
        text = update.message.text
        return (text.lower() == 'hello' or text.lower() == 'hi' 
            or text.lower() == 'good morning'
                or text.lower() == 'good afternoon' 
                    or text.lower() == 'good evening'
                        or text.lower() == 'good night')
    def on_enter_state5(self, update):
        update.message.reply_text("Hi,what's your name?")
        self.advance(update)
    def on_exit_state5(self, update):
        print('Leaving state5')
#state 6
    def is_going_to_state6(self, update):
        text = update.message.text
        global name
        name = text
        return (text.lower() != 'hello' and text.lower() != 'hi' 
            and text.lower() != 'good morning'
                and text.lower() != 'good afternoon' 
                    and text.lower() != 'good evening'
                        and text.lower() != 'good night')
    def on_enter_state6(self, update):
        update.message.reply_text("Hi~"+name+",nice to meet you!")
        self.go_back(update)
    def on_exit_state6(self, update):
        print('Leaving state6')


