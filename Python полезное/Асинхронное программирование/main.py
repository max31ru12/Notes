import asyncio




def f():
    pass


def g():
    pass


# get_event_loop() - берет существующий или создаёт новый
# new_event_loop() - всегда создаёт новый
main_loop = asyncio.new_event_loop()


# main_loop.run_until_complete(g()) - запускает, пока не будет выполнено условие
# main_loop.run_forever()           - программа сама по себе не завершится