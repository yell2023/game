import random
import time


class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.power = power

    def attack(self, other):
        damage = random.randint(self.power - 2, self.power + 2)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"{self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Player(Character):
    def __init__(self, name, hp, power, magic_power, count):
        super().__init__(name, hp, power)
        self.attribute = "Player"
        name = Player_name
        self.magic_power = magic_power
        self.count = count

    def magic_attack(self, other):
        damage = random.randint(self.magic_power - 5, self.magic_power + 5)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 마법공격! {other.name}에게 {damage}의 데미지를 입혔습니다.")
        self.count -= 1
        if self.count == 0:
            print('마법공격 횟수를 모두 소진하셨습니다!')
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(
            f"마법공격 가능 횟수:{self.count} {self.name}의 상태: HP {self.hp}/{self.max_hp}")


class Monster(Character):
    def __init__(self, name, hp, power):
        self.attribute = "Monster"
        super().__init__(name, hp, power)

    def attack(self, other):
        damage = random.randint(self.power - 5, self.power + 7)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name}의 공격! {other.name}에게 {damage}의 데미지를 입혔습니다.\n")
        if other.hp == 0:
            print(f"{other.name}이(가) 쓰러졌습니다.")


Player_name = input('게임을 시작하시려면 Player의 이름을 설정해주세요!\n')

p = Player(Player_name, 100, 10, 20, 5)
m = Monster('Monster', 100, 15)


def fight():
    turns = 0
    while True:
        turns += 1
        Player_attack = input(
            '\n**마법공격은 최대 5번만 사용가능합니다!\n일반공격을 하시려면 1을 마법공격을 하시려면 2를 눌러주세요!\n')

        print('\n-------Fighting hard!-------\n')
        time.sleep(1)

        if Player_attack == '1':
            p.attack(m)
            m.attack(p)
        elif Player_attack == '2':
            p.magic_attack(m)
            m.attack(p)
        else:
            print('1과 2중에서 선택해주세요!!\n')

        print(turns, '번')
        p.show_status()
        m.show_status()

        if m.hp == 0:
            print(f'{p.name}님이 {m.name}을 무찌르고 승리하셨습니다!\n')
            break
        elif p.hp == 0:
            print(f'{p.name}님이 {m.name}에게 패배하셨습니다!\n')
            break


# 게임시작
print(f'\n{Player_name}님이 생성되었습니다!\n게임을 시작합니다.\n')

# 게임 과정
fight()

# 게임 종료
print('게임이 종료되었습니다.\n게임을 다시 시작하시겠습니까?')
replay = input('y/n\n')
if replay == 'y':
    p.hp = 100
    m.hp = 100
    p.count = 5
    fight()
else:
    print('게임을 종료하겠습니다. 다음에 또 만나요^^')
