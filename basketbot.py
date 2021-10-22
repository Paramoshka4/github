import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id

def send_message(sender, message):
    authorize.method('messages.send', {'user_id': sender, 'message': message, 'random_id': get_random_id()})
#https://vk.com/kakoitomamba стас 229459286
#https://vk.com/dssemiryakov дима 232515926
#https://vk.com/turkish_giant тим 472247625
#last = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
people = []

token = "0c8eafaca1234de0b8a7d6dee3092bb1a7b9bc3797795d35a7f5f56cf2377f7239a33e08445ddbe19cfae"
authorize = vk_api.VkApi(token=token)
longpoll = VkLongPoll(authorize)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        nikita = 320331416
        lesha = 560170062
        tim = 472247625
        dima = 232515926
        stas = 229459286
        received_message = event.text
        rm = received_message.lower()
        sender = event.user_id
        if rm[:12] == "набор старт ":
            count = int(rm[12:])
            i = 0
            people = []
            send_message(nikita, "Набор на тренировку начался")            
            send_message(lesha, "Набор на тренировку начался")
            send_message(dima, "Набор на тренировку начался")
            send_message(tim, "Набор на тренировку начался")
            send_message(stas, "Набор на тренировку начался")
        if rm == "список":
            itog1 = ""
            a1 = 0
            for i in range(len(people)):
                itog1 += '{}. '.format(a1 + 1) + people[a1] + "\n"
                a1 += 1
            if itog != "":
                send_message(lesha, itog1)
                send_message(dima, itog1)
                send_message(tim, itog1)
                send_message(nikita, itog1)
                send_message(stas, itog1)
            else:
                send_message(lesha, "Список пуст")
                send_message(dima, "Список пуст")
                send_message(tim, "Список пуст")
                send_message(nikita, "Список пуст")
                send_message(stas, "Список пуст")
        if rm[:6] == 'секция':
            false = 0
            for i in range(len(people)):
                if received_message[7:] == people[i]:
                    send_message(sender, "Ты уже есть в списках!")
                    false = 1
                    break
                else:
                    i += 1
            if i == count:
                send_message(sender, "⚠ Упс...\n\n• Набор на ДАННУЮ тренировку закончен, мест больше нет!\n\n✅ Следите за информацией о новых тренировках в группе секции: vk.com/basketball_in_mirea")
                false = 1
            if false != 1:
                if i == len(people):
                    people.append(received_message[7:])
                    send_message(sender, "Твой порядковый номер: {}".format(i + 1))
                    a = 0
                    itog = ""
                    for i in range(len(people)):
                        itog += '{}. '.format(i + 1) + people[a] + "\n"
                        a += 1
                    if i == (count - 1):
                        send_message(lesha, itog)
                        send_message(dima, itog)
                        send_message(tim, itog)
                        send_message(nikita, itog)
                        send_message(stas, itog)
