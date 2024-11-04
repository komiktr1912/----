import Functions
import character
import time

print('''Вы находитесь на диком западе.
Вы находитесь на миссии по освобождению региона от местных бандитов.
Во время экспедиции вашего напарника забрала местная мафия. 
    - ВАША ЦЕЛЬ:
Освободить вашего напарника, и одолеть всю мафию''')

time.sleep(1)
input('Нажмите Enter чтобы продолжить.')

answer = ""

while answer != "!leave":

    print("Выберите действие: ")

    time.sleep(1)

    # Действия

    print("Действие1 - Нападение ")
    time.sleep(0.1)

    print("Действие2 - Улучшить прицел")
    time.sleep(0.1)

    print("Действие3 - Заработок")
    time.sleep(0.1)

    print("Действие4 - Зайти в прилавок к местному барыге ")
    time.sleep(0.1)

    print("Действие5 - Показать ваш инвентарь")
    time.sleep(0.1)

    print("Действие6 - показать характеристики")

    print("!leave - выход из игры (")

    answer = input("Действие: ")

    if answer == "1":

        print("Вы выбрали 'БИТВА' ")

        time.sleep(1)

        print("Первый соперник - ваш бывший друг, примкнувший к мафии из-за финансовых проблем")

        print("Второй опонент - Напарник и правая рука местной мафии, что держит в страхе весь город")

        print("Третий - Мафия, что держит в заложниках вашего напарника.")

        print("Чтобы выйти напишите врага -1")

        answer = int(input("Вы должны одолеть 1 из врагов, но какого? - "))

        if answer < 4 and answer > 0:

            print(f"Вы выбрали врага №{answer}")
            time.sleep(1)

            Functions.fight(answer-1)

        elif answer == -1:

            pass

        else:

            print("Введенного врага пока нет в игре, и не факт что появится")
            
    elif answer == "2":
            
        Functions.training()

    elif answer == "3":

        Functions.earning()

    elif answer == "4":

        Functions.shop()

    elif answer == "5":

        Functions.inv_show()
    
    elif answer == "6":

        Functions.char_show()
    
    time.sleep(0.5)
    print("Вы были перенесены в меню выбора")
    time.sleep(2)

print("Чтож, игра закрыта..( ")