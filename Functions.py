import random
import character
import time

# Функция определения урона

def player_damage():

    multiplier = int(character.character_player["strength"] * (character.character_player["xp"] / 100))

    damage_player = random.randint(multiplier, multiplier+2) + random.random()
    damage_player = round(damage_player, 2)
    return damage_player

def damage_enemy(enemy):

    multiplier = character.enemies[enemy]["strength"]

    damage = random.randint(multiplier, multiplier+2) + random.random() - character.character_player["protection"]

    damage = round(damage, 2) - character.character_player["protection"]
    return damage

def fight(current_enemy):

    fight_true = True

    while fight_true:
        time.sleep(2)

        print(f'У вас осталось {character.character_player["stamina"]} энергии')

        print("Битва - 1")
        print("Воздержаться - 2")
        answer = input("Действие: ")

        if answer == "1":

            if character.character_player["stamina"] > 0:
                damage_player = player_damage()
                enemy1_damage = damage_enemy(current_enemy)

                character.enemies[current_enemy]["hp"] -= damage_player
                print(f'Вы попали, и нанесли {damage_player} урона!')

                time.sleep(0.2)
                print(f'У врага осталось {character.enemies[current_enemy]["hp"]} очков здоровья')

                time.sleep(3)

                character.character_player["hp"] -= enemy1_damage

                print(f'Враг тоже в вас попал, и нанес вам {enemy1_damage} урона!')
                time.sleep(0.2)
                
                print(f'У вас осталось {character.character_player["hp"]} здоровья...')
                time.sleep(0.1)

                character.character_player["stamina"] -= 1
            else:

                print("У вас не хватает энергии!")
                time.sleep(0.2)

                character.character_player["stamina"] += 1

                print("Вы немного отдохнули от непрошедшего удара")
            if character.character_player["hp"] <= 0:

                fight_true = False
                print("Битва была окончена вашим поражением...")

                time.sleep(0.1)
                print("Вы ощущаете что месть бежит по вашим венам, и в следующий раз вы его одолеете...")

def training():

    print("Вы пришли на тренировочное поле. У вас 3 мишени")
    print("Чтобы стрелять, введите сторону куда вы стреляете: <(влево), =(прямо), >(вправо)")
    print("Чтобы прекратить, впишите !stop")

    time.sleep(1)

    while True:

        rng = random.randint(1, len(character.aim))

        print(character.aim[rng][0])

        answer = input("Куда стреляете?: ")

        if answer == "!stop":
            break

        elif answer == character.aim[rng][1]:

            print("Вы попали!, и получили 10 XP")
            print("Также, вы улучшили характеристики здоровья и энергии!")

            character.character_player["xp"] += 10
            character.character_player["stamina"] += 0.25
            character.character_player["hp"] += 2

        else:
            print("Вы не попали. Вы косой.")
    
    print(f"Ваш опыт: {character.character_player["xp"]}")

# ЗАРАБОТОК

def earning():

    while True:

        rng = random.randint(10000, 99999)
        rng = str(rng)

        rngmoney = random.randint(4, 7) + 1*(character.character_player["reputation"])

        print(f"Введите '{rng}' чтобы заработать, или !leave чтобы выйти")
        earn = input("Число: ")

        if earn == rng:

            print(f"Вы заработали {rngmoney} монеток!")

            character.character_player["money"] += rngmoney

        elif earn == "!leave":

            break

        else:

            print("Введенное число неправильно, вы ничего не получите!")
            time.sleep(1)

    print(f"Ваши деньги : {character.character_player["money"]}")

# МАГАЗИН

def shop():

    print("Вы зашли в прилавок, торговец вам предлагает ассортимент: ")
    print("- Оружие(1), доспехи(2), все что вам надо! ")
    print("- Что пожелаете взять?")

    answer = input("Выбор: ")

    if answer == "1":

        print("Ассортимент оружия: ")

        for key, value in character.weapons.items():

            print(f"ID: {key}, Имя: {value["name"]}, цена: {value["price"]}, урон: {value["damage"]}")

        print("Что желаете преобрести?")

        item = input("ID: ")

        if character.weapons[item]["name"] in character.character_player["inventoryW"]:

            print("Нет, у нас предметы покупаются не больше раза")

        else:

            if character.character_player["money"] >= character.weapons[item]["price"]:

                print(f"Вы успешно приобрели {character.weapons[item]["name"]}!")

                character.character_player["inventoryW"].append(character.weapons[item]["name"])
                character.character_player["money"] -= character.weapons[item]["price"]
                character.character_player["strength"] += character.weapons[item]["damage"]

            else:
                print("У тебя не хватает денег, иди работай на завод")
                
            
    elif answer == "2":

        print("Ассортимент брони: ")

        for key, value in character.armor.items():

            print(f"ID: {key}, Имя: {value["name"]}, цена: {value["price"]}")

        print("Что желаете преобрести?")
        item = input("ID: ")

        if character.armor[item] in character.character_player["inventoryA"]:

            print("Нет, у нас предметы покупаются не больше раза")

        else:
            if character.character_player["money"] >= character.armor[item]["price"]:

                print(f"Вы успешно приобрели {character.armor[item]["name"]}!")

                character.character_player["inventoryA"].append(character.armor[item]["name"])
                character.character_player["money"] -= character.armor[item]["price"]
                character.character_player["protection"] += character.armor[item]["defence"]

            else:

                print("У тебя не хватает денег, иди работай на завод!")

def inv_show():

    print(character.character_player["inventoryW"])
    print(character.character_player["inventoryA"])

    input("Нажмите Enter чтобы продолжить")

def char_show():

    print(f'''Ваши характеристики:
Здоровье: {character.character_player["hp"]}
Защита: {character.character_player["protection"]}
Урон: {character.character_player["strength"]}
Энергия: {character.character_player["stamina"]}
Опыт: {character.character_player["xp"]}
Деньги: {character.character_player["money"]}''')
    
    input("Нажмите Enter чтобы продолжить")