from pyknow import *

class Money(Fact):
    """ ask about money you have """
    pass

class Ticket(Fact):
    """ ask about free ticker """

class Solution(KnowledgeEngine):

    @Rule(OR(Money(money = 'yes'),Ticket(ticket = 'no')))
    def mee_tung(self):
        print('You can buy this thing')

    @Rule(AND(Money(money='no'),Ticket(ticket = 'no')))
    def maimee_tung(self):
        print('Sorry no money no honey :<')

engine = Solution()
ask_money = input("Did you have money ? :")
ask_ticket = input("Did you have free luanch tiket ? :")
engine.reset()
engine.declare((Money(money= ask_money)),(Ticket(ticket=ask_ticket)))
engine.run()
