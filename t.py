class Default_Character_Setting: # 캐릭터 원형 : 공통 속성값을 가지고 있음
    def __init__(self):
        self.hp = 0 #체력
        self.mp = 0 #마나


        self.LV = 1 #레벨
        self.EXP = 0 # 경험치

        self.vit = 10 # 생명력
        self.str = 10 # 힘
        self.int = 0 # 지능


    def set_stat(self):
        init_stat = 30
        print("스텟을 분배해 주세요.")
        print("vit : 생명력 스텟입니다. 플레이어 캐릭터의 HP최대량을 결정합니다.")
        print("str : 힘 스텟입니다. 플레이어의 물리 공격력에 영향을 미칩니다.")
        print("int : 지능 스텟입니다. 플레이어의 마법 공격력및 마나 최대치에 영향을 미칩니다.")
        while True:
            print("현재 분배된 플레이어의 스텟")
            print("vit : %d" % self.vit)
            print("str : %d" % self.str)
            print("int : %d" % self.int)
            print("분배 가능한 스텟 : %d" % init_stat)


            prefer = input("수정할 스텟이름을 입력해 주세요(수정을 마치려면 \"마침\"을 입력해주세요) : ")

            if prefer == "마침":
                print("스텟분배 완료")
                print("현재 분배된 플레이어의 정보")

                self.hp = self.vit * 5
                self.mp = self.int * 2

                print("hp : %d" %self.hp)
                print("mp : %d" %self.mp)
                print("vit : %d" % self.vit)
                print("str : %d" % self.str)
                print("int : %d" % self.int)
                break
            elif not prefer in ["vit","str","int"]:
                print("입력 이름 오류, 다시 입력해 주세요.")
                continue

            stat = int(input("수정할 수치를 입력해 주세요 : "))
            if prefer == "vit":
                if self.vit + stat < 10 or init_stat - stat < 0:
                    print("입력값 초과, 다시 입력해 주세요.")
                    continue
                self.vit += stat
                init_stat -= stat

            elif prefer == "str":
                if self.str + stat < 10 or init_stat - stat < 0:
                    print("입력값 초과, 다시 입력해 주세요.")
                    continue
                self.str += stat
                init_stat -= stat

            elif prefer == "int":
                if self.int + stat < 0 or init_stat - stat < 0:
                    print("입력값 초과, 다시 입력해 주세요.")
                    continue
                self.int += stat
                init_stat -= stat
            else:
                print("입력 이름 오류, 다시 입력해 주세요.")
                continue

#class MyCharacter1(Default_Character_Setting):

character = Default_Character_Setting()
character.set_stat()




# 행동(공격, 스킬)
# 맵(단계별, 다지선다형 길)
# 몬스터(스텟, 난수값에 의한 행동)
# 클리어 조건


#아이템과 배낭(플레이어 슬롯)
#버프계열 소모품과 스킬, 물약
#버프,디버프 부여 시설
#상점


#가챠?
#탈출,아이템 창고
#허기, 음식??









