"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user(question):
    while question != 'Хорошо':
        try:
            question = input('Как дела?\n')
        except KeyboardInterrupt:
            print('Пока')
            break

if __name__ == "__main__":
    hello_user(input('Как дела?\n'))
