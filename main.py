'''
Noah Lilly
Programming Fundamentals
David Rios
2-4-22
'''
#imports
import time
import random
import sys
import replit
from replit import db

#Variables
employ = False
apostrophy = "'"
Beat = 0
End = False
Difficulty = 1
EmployeeHp = 25
Phase3FinalWendyHp = 100
Phase2FinalWendyHp = 75
FinalWendyHp = 50
WendyHp = 30
YourHp = 10
TheirHp = 15
damage = 0
damaged = 0
Burn = 0
Burned = 0
SFB = False
SFB2 = False
MoreAttack = 0
MoreHp = 0
MoreDefence = 0
Healed = 0
Upgrade1 = False
Upgrade2 = False
Upgrade3 = False
M = False
Off = False
Answer3 = ""
WendyDefend = 0
DevHp = 999
DevStun = 0
DevTaunt = 0
EndRepeat = True
RonaldMcDonaldHp = random.randint(1000, 10000)
egghp = 1
eggturn = False

if not 'yes' in db.keys():
        print('Loading...')
        db['yes'] = True
        db['apostrophy'] = apostrophy
        db['Beat'] = Beat 
        db['End'] = End  
        db['Difficulty'] = Difficulty  
        db['Phase3FinalWendyHp'] = Phase3FinalWendyHp  
        db['Phase2FinalWendyHp'] = Phase2FinalWendyHp  
        db['FinalWendyHp'] = FinalWendyHp  
        db['WendyHp'] = WendyHp  
        db['YourHp'] = YourHp 
        db['TheirHp'] = TheirHp  
        db['damage'] = damage  
        db['damaged'] = damaged 
        db['Burn'] = Burn 
        db['Burned'] = Burned 
        db['SFB'] = SFB
        db['SFB2'] = SFB2
        db['MoreAttack'] = MoreAttack
        db['MoreHp'] = MoreHp
        db['MoreDefence'] = MoreDefence
        db['Healed'] = Healed
        db['Upgrade1'] = Upgrade1
        db['Upgrade2'] = Upgrade2
        db['Upgrade3'] = Upgrade3
        db['M'] = M
        db['Off'] = Off
        db['Answer3'] = Answer3
        db['WendyDefend'] = WendyDefend 
        db['DevHp'] = DevHp
        db['DevStun'] = DevStun
        db['DevTaunt'] = DevTaunt
        db['EndRepeat'] = EndRepeat
        db['RonaldMcDonaldHp'] = RonaldMcDonaldHp
        db['employ'] = employ
        replit.clear()
#colors
Red = "\033[0;31m"
Green = "\033[0;32m"
Orange = "\033[0;33m"
Blue = "\033[0;34m"
Purple = "\033[0;35m"
Cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
bright_black = "\033[0;90m"
bright_red = "\033[0;91m"
bright_green = "\033[0;92m"
bright_yellow = "\033[0;93m"
bright_blue = "\033[0;94m"
bright_magenta = "\033[0;95m"
bright_cyan = "\033[0;96m"
bright_white = "\033[0;97m"
cyan_back = "\033[0;46m"
purple_back = "\033[0;45m"
white_back = "\033[0;47m"
blue_back = "\033[0;44m"
orange_back = "\033[0;43m"
green_back = "\033[0;42m"
pink_back = "\033[0;41m"
grey_back = "\033[0;40m"
grey = '\033[38;4;236m'
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
invisible='\033[08m'
reverse='\033[07m'
reset='\033[0m'
grey = "\x1b[90m"

def egg():
        global egghp, YourHp, eggturn
        print(f'{reset}Become an egg...')
        time.sleep(1.5)
        replit.clear()
        while True:
                print(f'You: {YourHp}')
                print(f'Egg: {egghp}')
                print('Your Turn')
                print('(1) - Attack')
                print('(2) - Compliment')
                print('(3) - Turn the Egg into an Omelette')
                Atk = input("Choose your attack: "+Blue)
                print(reset)
                if Atk == '1':
                        eggturn = True
                        replit.clear()
                        print('You punch the egg!')
                        time.sleep(1)
                        print("It's shell is too hard!")
                        time.sleep(1)
                elif Atk == '2':
                        replit.clear()
                        eggturn = True
                        eggnum = random.randint(1, 3)
                        if eggnum == 1:
                                print("You tell the egg that it's lovely.")
                                time.sleep(1)
                                print('The egg blushes.')
                        elif eggnum == 2:
                                print("You complement the egg's shiny shell.")
                                time.sleep(1)
                                print('The egg is pleased.')
                        elif eggnum == 3:
                                print('You accidently insult the egg...')
                                time.sleep(1)
                                print(f'{Red}The egg obliterates you!{reset}')
                                time.sleep(1)
                                quit()
                        time.sleep(2)
                elif Atk == '3':
                        eggturn = True
                        replit.clear()
                        print('You grab the frying pan...')
                        time.sleep(1)
                        print('You put it on the stove...')
                        time.sleep(1.5)
                        print('You take the egg...')
                        time.sleep(2)
                        replit.clear()
                        print(f'{Red}You crack it over the pan...')
                        time.sleep(2.5)
                        print('You turn on the stove...')
                        time.sleep(3)
                        print('You take the egg out of the pan...')
                        time.sleep(3.5)
                        print('You put the egg on a plate...')
                        time.sleep(4)
                        replit.clear()
                        print('Y@u ea} t%e 3gg...')
                        time.sleep(4.5)
                        quit()
                else:
                        replit.clear()
                        pass
                if eggturn == True:
                        replit.clear()
                        eggturn = False

def Employee():
        global EmployeeHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Burned
        global WendyDefend
        global DevStun
        global Beat
        replit.clear()
        Turn = random.randint(1, 10)
        if Turn == 6:
                print(Red+"The employee's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(3, 7) * Difficulty
                Burned = random.randint(3, 7) * Difficulty
                print("The employee intimidated you, his attacks doubled, while your's was halfed!")
                time.sleep(1)
                replit.clear()
                EmployeeFight()
        if Turn == 5:
                print(Red+"The employee's Turn!"+reset)
                Sleep()
                Attacked = random.randint(10, 14)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(5, 7)
                print(Red+"The employee did a CRITICAL "+(str(Attacked))+" damage."+reset)
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        Sleep()
                        print(Red+"You lost and were slapped by the employee."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        EmployeeHp = 25 * Difficulty
                        damage = 0
                        damaged = 0     
                        DevHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0         
                        restart()     
                else:
                        EmployeeFight()
        if Turn == 4:
                print(Red+"The employee's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(3, 7) * Difficulty
                print("The employee defended himself!")
                time.sleep(1)
                replit.clear()
                EmployeeFight()
        if Turn == 3:
                print(Red+"The employee's Turn"+reset)
                Sleep()
                Burned = random.randint(5, 7) * Difficulty
                print("The employee "+Red+"insulted"+reset+" you, his attack damage increased!")
                time.sleep(1)
                replit.clear()
                EmployeeFight()
        if Turn == 2:
                print(Red+"The employee's Turn!"+reset)
                Sleep()
                DevStun = 1 + Difficulty
                round(DevStun)
                print("The employee stunned you.")
                time.sleep(1)
                replit.clear()
                EmployeeFight()
        else:
                print(Red+"The employee's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(5, 10)
                print("The employee did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were slapped by the employee."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        RonaldMcDonaldHp = 25 * Difficulty
                        damage = 0
                        damaged = 0     
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0  
                        restart()     
                else:
                        EmployeeFight()

def EmployeeFight():
        replit.clear()
        global EmployeeHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global DevStun
        global Beat
        if DevStun >= 2:
                print("Your Stunned!")
                time.sleep(1)
                DevStun = 1
                DevTurn()
        elif DevStun == 1:
                print("You can move again!")
                time.sleep(1)
                replit.clear()
                DevStun = 0
        print("Food Fight!")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"The Employee: "+(str(EmployeeHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(5, 7) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                if Attacking < 0:
                        Attacking = random.randint(1, 3)
                print(reset+"You did "+(str(Attacking))+" damage.")
                EmployeeHp = EmployeeHp - Attacking 
                time.sleep(1)
                if RonaldMcDonaldHp <= 0:
                        Sleep()
                        print(Red+"You beat the employee."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        EmployeeHp = 25 * Difficulty
                        damage = 0
                        damaged = 0     
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0         
                        Beat += 1
                        employ = True
                        restart()
                else:
                        EmployeeFight()
        if Attack == "2":
                Sleep()
                print(reset+"You called the employee a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
                Employee()
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("The employee's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
                Employee()
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(5, 7)
                YourHp = YourHp + Health
                Sleep()
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
                Employee()
        if EmployeeHp <= 0:
                Sleep()
                print(Blue+"You beat the employee")
                time.sleep(1)
                Beat += 1
                restart()
        else:
                EmployeeFight()

def RMCD():
        replit.clear()
        global RonaldMcDonaldHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global DevStun
        global Beat
        if DevStun >= 2:
                print("Your Stunned!")
                time.sleep(1)
                DevStun = 1
                DevTurn()
        elif DevStun == 1:
                print("You can move again!")
                time.sleep(1)
                replit.clear()
                DevStun = 0
        print("Impossible!")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Ronald McDonald: "+(str(RonaldMcDonaldHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(5, 7) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                if Attacking < 0:
                        Attacking = random.randint(1, 3)
                print(reset+"You did "+(str(Attacking))+" damage.")
                RonaldMcDonaldHp = RonaldMcDonaldHp - Attacking 
                time.sleep(1)
                if RonaldMcDonaldHp <= 0:
                        Sleep()
                        print(Red+"You beat Ronald McDonald."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        RonaldMcDonaldHp = random.randint(10000, 100000) * Difficulty
                        damage = 0
                        damaged = 0     
                        RonaldMcDonaldHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0         
                        Beat += 1
                        Mrestart()     
                else:
                        RMCDTurn()
        if Attack == "2":
                Sleep()
                print(reset+"You called Ronald McDonald a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
                RMCDTurn()
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Ronald McDonald attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
                RMCDTurn()
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(5, 7)
                YourHp = YourHp + Health
                Sleep()
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
                RMCDTurn()
        if RonaldMcDonaldHp <= 0:
                Sleep()
                print(Blue+"You beat Ronald McDonald")
                time.sleep(1)
                Beat += 1
                Mrestart()
        else:
                RMCD()

def RMCDTurn():
        global RonaldMcDonaldHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Burned
        global WendyDefend
        global DevStun
        global Beat
        replit.clear()
        Turn = random.randint(1, 10)
        if Turn == 6:
                print(Red+"Ronald McDonalds's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(15, 19) * Difficulty
                Burned = random.randint(15, 19) * Difficulty
                print("Ronald McDonald intimidated you, his attacks doubled, while your's was halfed!")
                time.sleep(1)
                replit.clear()
                RMCD()
        if Turn == 5:
                print(Red+"Ronald McDonalds's Turn!"+reset)
                Sleep()
                Attacked = random.randint(20, 24)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(5, 10)
                print(Red+"Ronald McDonald did a MORTAL "+(str(Attacked))+" damage."+reset)
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        Sleep()
                        print(Red+"You lost and were destroyed by Ronald McDonald."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        RonaldMcDonaldHp = random.randint(10000, 100000) * Difficulty
                        damage = 0
                        damaged = 0     
                        DevHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0         
                        restart()     
                else:
                        RMCD()
        if Turn == 4:
                print(Red+"Ronald McDonald's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(15, 19) * Difficulty
                print("Ronald McDonald defended himself!")
                time.sleep(1)
                replit.clear()
                RMCD()
        if Turn == 3:
                print(Red+"Ronald McDonald's Turn"+reset)
                Sleep()
                Burned = random.randint(15, 19) * Difficulty
                print("Ronald McDonald "+Red+"insulted"+reset+" you, his attack damage increased!")
                time.sleep(1)
                replit.clear()
                RMCD()
        if Turn == 2:
                print(Red+"Ronald McDonald's Turn!"+reset)
                Sleep()
                DevStun = 1 + Difficulty
                round(DevStun)
                print("Ronald McDonald stunned you.")
                time.sleep(1)
                replit.clear()
                RMCD()
        else:
                print(Red+"Ronald McDonald's Turn!"+reset)
                Sleep()
                Attacked = random.randint(15, 19)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(5, 10)
                print("Ronald McDonald did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were destroyed by Ronald McDonald."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        RonaldMcDonaldHp = random.randint(10000, 100000) * Difficulty
                        damage = 0
                        damaged = 0     
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0  
                        restart()     
                else:
                        RMCD()
def DevBoss():
        replit.clear()
        global DevHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global Beat
        global MoreDefence
        global DevStun
        if DevStun >= 2:
                print("Your Stunned!")
                time.sleep(1)
                DevStun = 1
                DevTurn()
        elif DevStun == 1:
                print("You can move again!")
                time.sleep(1)
                replit.clear()
                DevStun = 0
        print("Dev Battle?")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Dev: "+(str(DevHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(5, 7) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                if Attacking < 0:
                        Attacking = random.randint(1, 3)
                print(reset+"You did "+(str(Attacking))+" damage.")
                DevHp = DevHp - Attacking 
                time.sleep(1)
                if DevHp <= 0:
                        Sleep()
                        print(Red+"You beat the Dev."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        DevHp = 999 * Difficulty
                        damage = 0
                        damaged = 0     
                        DevHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0    
                        Beat += 1
                        restart()     
                else:
                        DevTurn()
        if Attack == "2":
                Sleep()
                print(reset+"You called the Dev a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
                DevTurn()
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("The dev's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
                DevTurn()
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(5, 7)
                YourHp = YourHp + Health
                Sleep()
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
                DevTurn()
        if DevHp <= 0:
                Sleep()
                print(Blue+"You beat the Dev!")
                time.sleep(1)
                Beat += 1
                restart()
        else:
                DevBoss()

def DevTurn():
        global DevHp
        global YourHp
        global Attacked
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Burned
        global WendyDefend
        global DevStun
        replit.clear()
        Turn = random.randint(1, 6)
        if Turn == 5:
                print(Red+"Dev's Turn!"+reset)
                Sleep()
                Attacked = random.randint(15, 19)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print(Red+"The Dev did a MORTAL "+(str(Attacked))+" damage."+reset)
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        Sleep()
                        print(Red+"You lost and were annihilated by the Dev."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        DevHp = 999 * Difficulty
                        damage = 0
                        damaged = 0     
                        DevHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0         
                        restart()     
                else:
                        DevBoss()
        if Turn == 4:
                print(Red+"Dev's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(10, 12) * Difficulty
                print("The Dev defended himself!")
                time.sleep(1)
                replit.clear()
                DevBoss()
        if Turn == 3:
                print(Red+"Dev's Turn!"+reset)
                Sleep()
                Burned = random.randint(10, 12) * Difficulty
                print("The Dev "+Red+"insulted"+reset+" you, his attack damage increased!")
                time.sleep(1)
                replit.clear()
                DevBoss()
        if Turn == 2:
                print(Red+"Dev's Turn!"+reset)
                Sleep()
                DevStun = 1 + Difficulty
                round(DevStun)
                print("The Dev stunned you.")
                time.sleep(1)
                replit.clear()
                DevBoss()
        else:
                print(Red+"Dev's Turn!"+reset)
                Sleep()
                Attacked = random.randint(10, 14)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("The Dev did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were slapped by the Dev."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        DevHp = 999 * Difficulty
                        damage = 0
                        damaged = 0     
                        DevHp = 0  
                        Burned = 0  
                        WendyDefend = 0  
                        DevStun = 0  
                        restart()     
                else:
                        DevBoss()

def HerTurn4():
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend     
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        global Beat
        replit.clear()
        Turn = random.randint(1, 6)
        if Turn == 5:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(10, 14)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print(Red+"Wendy did a MORTAL "+(str(Attacked))+" damage."+reset)
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        Sleep()
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 10 + MoreHp
                        Phase3FinalWendyHp = 100 * Difficulty
                        damage = 1
                        WendyDefend = 0      
                        Burned = 0      
                        damaged = 0             
                        restart()     
                else:
                        FinalFight3()
        if Turn == 4:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(5, 7) * Difficulty
                print("Wendy defended herself!")
                time.sleep(1)
                replit.clear()
                FinalFight3()
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7) * Difficulty
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight3()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(5, 7)
                print("Wendy healed herself with a hamburger!")
                Phase3FinalWendyHp += Healed * Difficulty
                time.sleep(1)
                replit.clear()
                FinalFight3()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        Phase3FinalWendyHp = 100 * Difficulty
                        damage = 0
                        damaged = 0             
                        WendyDefend = 0      
                        Burned = 0 
                        restart()     
                else:
                        FinalFight3()

def FinalFight3():
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global SFB2
        global WendyDefend
        global Beat
        global Burned
        print(darken+Red+"Final Form!"+reset)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(Phase3FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                Attacking = Attacking - WendyDefend
                if Attacking < 0:
                        Attacking = random.randint(1, 3)
                print(reset+"You did "+(str(Attacking))+" damage.")
                Phase3FinalWendyHp = Phase3FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(5, 7)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if Phase3FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Final Form Wendy!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Attack got upgraded!")
                time.sleep(1)
                Sleep()
                print(reset+"Your favorite TV show should be on right about now.")
                time.sleep(2)
                Sleep()
                YourHp = 25
                Phase3FinalWendyHp = 100  * Difficulty
                damage = 0
                damaged = 0
                WendyDefend = 0      
                Burned = 0 
                SFB2 = True
                print("(Watch it to win!)"+reset)
                time.sleep(1)
                Beat += 1
                restart()
        else:
                HerTurn4()

def HerTurn3():
        global damage
        global damaged
        global YourHp
        global Phase2FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend   
        global MoreAttack
        global MoreHp
        global MoreDefence
        replit.clear()
        Turn = random.randint(1, 5)
        if Turn == 4:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                WendyDefend = random.randint(5, 7) * Difficulty
                print("Wendy defended herself!")
                time.sleep(1)
                replit.clear()
                FinalFight2()
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7) * Difficulty
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight2()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(2, 3) * Difficulty
                print("Wendy healed herself with a hamburger!")
                Phase2FinalWendyHp += Healed
                time.sleep(1)
                replit.clear()
                FinalFight2()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        time.sleep(1)
                        YourHp = 25
                        Phase2FinalWendyHp = 75 * Difficulty
                        damage = 0
                        WendyDefend = 0      
                        Burned = 0 
                        damaged = 0             
                        restart()     
                else:
                        FinalFight2()
def FinalFight2():
        global damage
        global damaged
        global YourHp
        global Phase2FinalWendyHp
        global SFB2
        global MoreHp
        global MoreDefend
        global MoreAttack
        global WendyDefend
        print(darken+Red+"Last Fight!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(Phase2FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                Attacking = Attacking - WendyDefend
                if Attacking < 0:
                        Attacking = random.randint(1, 3) 
                print(reset+"You did "+(str(Attacking))+" damage.")
                Phase2FinalWendyHp = Phase2FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(5, 7)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if Phase2FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Last Fight Wendy!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Heal got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's still not over yet..."+reset)
                time.sleep(1)
                YourHp = 25
                Phase2FinalWendyHp = 75  * Difficulty
                damage = 0
                damaged = 0
                WendyDefend = 0      
                Burned = 0 
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("||||l F||||")
                time.sleep(0.1)
                replit.clear()
                print("|||al Fo|||")
                time.sleep(0.1)
                replit.clear()
                print("||nal For||")
                time.sleep(0.1)
                replit.clear()
                print("|inal Form|")
                time.sleep(0.1)
                replit.clear()
                FinalFight3()
        else:
                HerTurn3()
def HerTurn2():
        global damage
        global damaged
        global YourHp
        global FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global MoreHp
        global MoreDefend
        global MoreAttack
        global Healed
        replit.clear()
        Turn = random.randint(1, 4)
        if Turn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(5, 7) * Difficulty
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                FinalFight()
        if Turn == 2:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Healed = random.randint(3, 5) * Difficulty
                print("Wendy healed herself with a hamburger!")
                FinalWendyHp += Healed
                time.sleep(1)
                replit.clear()
                FinalFight()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 5)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were annihilated by Wendy."+reset) 
                        SFB2 = False 
                        time.sleep(1)
                        YourHp = 10 + MoreHp
                        FinalWendyHp = 50 * Difficulty
                        damage = 1
                        damaged = 0             
                        Burned = 0 
                        restart()     
                else:
                        FinalFight()
def FinalFight():
        global damage
        global damaged
        global YourHp
        global FinalWendyHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global SFB2
        print(darken+Red+"Death Wish!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(FinalWendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                FinalWendyHp = FinalWendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(5, 7)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if FinalWendyHp <= 0:
                Sleep()
                print(Blue+"You beat Death Wish Wendy!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Insult got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's not over yet..."+reset)
                time.sleep(1)
                YourHp = 25
                FinalWendyHp = 50 * Difficulty
                damage = 0
                damaged = 0
                Burned = 0 
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||F|||||")
                time.sleep(0.1)
                replit.clear()
                print("|||| Fi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||t Fig|||")
                time.sleep(0.1)
                replit.clear()
                print("||st Figh||")
                time.sleep(0.1)
                replit.clear()
                print("|ast Fight|")
                time.sleep(0.1)
                replit.clear()
                FinalFight2()
        else:
                HerTurn2()
#Methods
def HerTurn():
        global damage
        global damaged
        global YourHp
        global WendyHp
        global Burn
        global Burned
        global Attacked
        global SFB
        global MoreHp
        global MoreDefend
        global MoreAttack
        replit.clear()
        Burn = random.randint(1, 3)
        if Burn == 3:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Burned = random.randint(2, 3) * Difficulty
                print("Wendy "+Red+"ROASTED"+reset+" you, her attack damage increased!")
                time.sleep(1)
                replit.clear()
                BossFight()
        else:
                print(Red+"Wendy's Turn!"+reset)
                Sleep()
                Attacked = random.randint(5, 9)
                Attacked = Attacked - damaged + Burned
                Attacked = Attacked - MoreDefence
                if Attacked < 1:
                        Attacked = random.randint(1, 3)
                print("Wendy did "+(str(Attacked))+" damage.")
                YourHp = YourHp - Attacked
                time.sleep(1)
                replit.clear()
                if YourHp <= 0:
                        print(Red+"You lost and were eaten by Wendy."+reset) 
                        SFB = False 
                        time.sleep(1)
                        YourHp = 10
                        WendyHp = 30 * Difficulty
                        damage = 0
                        damaged = 0             
                        Burned = 0 
                        restart()     
                else:
                        BossFight()
def BossFight():
        global damage
        global damaged
        global YourHp
        global WendyHp
        global SFB
        global MoreHp
        global MoreDefend
        global MoreAttack
        print(Red+"Final Boss!"+reset)
        time.sleep(0.1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Wendy: "+(str(WendyHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        print("(4) - Heal!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                WendyHp = WendyHp - Attacking 
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called Wendy a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Wendy's attacks do less damage now")
                damaged = damaged + random.randint(2, 3)
                time.sleep(1)
        if Attack == "4":
                Sleep()
                print(reset+"You "+green+"Healed"+reset+" youself.")
                Health = random.randint(3, 5)
                YourHp = YourHp + Health
                time.sleep(1)
                print("You gained "+green+(str(Health))+reset+ " Hp!")
                time.sleep(1)
        if WendyHp <= 0:
                Sleep()
                print(Blue+"You beat Wendy and got her car keys!")
                time.sleep(1)
                Sleep()
                print(green+"Level Up! - Defense got upgraded")
                time.sleep(2)
                Sleep()
                print(reset+"But...")
                time.sleep(1)
                Sleep()
                print(Red+"It's not over yet."+reset)
                time.sleep(1)
                Sleep()
                print("(Some more options have been changed or made available to you)")
                SFB = True
                time.sleep(1)
                YourHp = 10
                WendyHp = 30 * Difficulty
                damage = 0
                damaged = 0
                Burned = 0 
                restart()
        else:
                HerTurn()
def home():
        global TheirHp
        global Difficulty
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend     
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        global M
        global Off
        global Upgrade1
        global Upgrade2
        global Upgrade3
        global Answer3
        global Phase2FinalWendyHp
        global FinalWendyHp
        global WendyHp
        global apostrophy
        global Beat
        global End
        global SFB
        global DevHp
        global DevStun
        global DevTaunt
        global EndRepeat
        global RonaldMcDonaldHp
        replit.clear()
        print(reset+"Your home.")
        time.sleep(1)
        Sleep()
        print("Now, what?")
        Sleep()
        print("(1) - Go To Wendy's")
        Sleep()
        print("(2) - Grab Armour")
        Sleep()
        print("(3) - Watch TV")
        Sleep()
        Leave2 = input("What do you do?: "+Blue)
        if Leave2 == "1":
                Sleep()
                print(reset+"You go back to wendy's.")
                time.sleep(1)
                restart()
        if Leave2 == "2":
                if Upgrade2 == True:
                        Sleep()
                        print(reset+"You can't find your armour, becuase your wearing it.")
                        Sleep()
                        time.sleep(1)
                        home()
                Sleep()
                print(reset+"You grab your armour.")
                Sleep()
                time.sleep(1)
                Upgrade2 = True
                print("Your take less damage now!")
                MoreDefence = 5
                time.sleep(1)
                home()
        if Leave2 == "3":
                if SFB2 == True:
                        EndScreen()
                Sleep()
                print(reset+"You see a Wendy's commercial on TV.")
                time.sleep(1)
                home()
        else:
                Sleep()
                print("Please pick one of the options.")
                time.sleep(1)
                home()
def outside():
        replit.clear()
        print(Red+"You left."+reset)
        time.sleep(1)
        Sleep()
        print("Now, where do you go?")
        Sleep()
        print("(1) - Back Inside")
        Sleep()
        print("(2) - To Your Home")
        Sleep()
        print("(3) - To McDonalds")
        Sleep()
        Leave = input("Go where?: "+Blue)
        if Leave == "1":
                restart()
        if Leave == "2":
                if SFB == True:
                        Sleep()
                        print(reset+"You drive home...")
                        time.sleep(1)
                        home()
                Sleep()
                print(Red+"You don't have a way to get home."+reset)
                time.sleep(2)
                outside()
        if Leave == "3" and SFB2 == False:
                Sleep()
                print(Red+"You don't see a McDonalds around, only Wendy's..."+reset)
                time.sleep(2)
                outside()
        if Leave == "3" and SFB2 == True:
                Sleep()
                print(Red+"Ronald McDonald is across the street."+reset)
                time.sleep(2)
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("||||ssi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||ossib|||")
                time.sleep(0.1)
                replit.clear()
                print("||possibl||")
                time.sleep(0.1)
                replit.clear()
                print("|mpossible|")
                time.sleep(0.1)
                replit.clear()
                RMCD()
        else:
                Sleep()
                print("Please input a valid option.")
                time.sleep(1)
                outside()

def restart():
        time.sleep(1)
        replit.clear()
        print(reset+"Hello, welcome to "+Blue+"Wendy's!")
        time.sleep(1)
        All()
def TheirTurn():
        global M
        global YourHp
        global TheirHp
        global damaged
        global damage
        global MoreHp
        global MoreDefend
        global MoreAttack
        replit.clear()
        print(Red+"Manager's Turn!"+reset)
        Sleep()
        Attacked = random.randint(2, 5)
        Attacked = Attacked - damaged
        Attacked = Attacked - MoreDefence
        if Attacked < 1:
                Attacked = random.randint(0, 2)
        print("The manager did "+(str(Attacked))+" damage.")
        YourHp = YourHp - Attacked
        time.sleep(1)
        if YourHp <= 0:
                Sleep()
                print(Red+"You lost and were slapped by the manager."+reset)  
                M = False
                time.sleep(1)
                YourHp = MoreHp + 10
                TheirHp = 15
                damage = 0
                damaged = 0             
                restart()     
        else:
                Fight()
def Fight():
        global Success
        global damage
        global damaged
        global YourHp
        global TheirHp
        global MoreHp
        global MoreDefend
        global MoreAttack
        global M
        replit.clear()
        print("Boss Fight!")
        time.sleep(1)
        Sleep()
        print("Your Turn!")
        Sleep()
        print(Blue+"You: "+(str(YourHp))+" Hp")
        Sleep()
        print(Red+"Manager: "+(str(TheirHp))+" Hp")
        Sleep()
        print(reset+"(1) - Attack!")
        Sleep()
        print("(2) - Insult!")
        Sleep()
        print("(3) - Defend!")
        Sleep()
        Attack = input("Choose your attack: "+Blue)
        if Attack == "1":
                Sleep()
                Attacking = random.randint(2, 5) 
                Attacking = Attacking + damage
                Attacking = Attacking + MoreAttack
                print(reset+"You did "+(str(Attacking))+" damage.")
                TheirHp = TheirHp - Attacking
                time.sleep(1)
        if Attack == "2":
                Sleep()
                print(reset+"You called the manager a "+Red+"meanie"+reset+".")
                Sleep()
                time.sleep(1)
                print("Your attacks do more damage now")
                damage = damage + random.randint(2, 3)
                time.sleep(1)
        if Attack == "3":
                Sleep()
                print(reset+"You "+Blue+"defended"+reset+" youself.")
                Sleep()
                time.sleep(1)
                print("Manager's attacks do less damage now")
                damaged = damaged + random.randint(2, 3)
                time.sleep(1)
        if TheirHp <= 0:
                Sleep()
                print(Blue+"You beat the manager!")
                time.sleep(1)
                Sleep()
                print(f"The manager isn't guarding the door anymore!{reset}")
                Sleep()
                print(green+"Level Up! - You learned the skill: Heal"+reset)
                time.sleep(2)
                M = True
                time.sleep(1)
                YourHp = 10 + MoreHp
                TheirHp = 15 * Difficulty
                damage = 1
                damaged = 0
                restart()
        else:
                TheirTurn()
def Option1():
        print("(1) - Order a Big Mac.")

def Option2():
        print("(2) - Escape!")

def Option3():
        print("(3) - I WANT TO SPEAK TO YOUR MANAGER!")

def Option4():
        print("(4) - Wait.")

def Option5():
        print("(5) - Leave.")

def Option6():
        print("(6) - Save.")

def Sleep():
        time.sleep(0.1)
        print("")

def All():
        global TheirHp
        global Difficulty
        global damage
        global damaged
        global YourHp
        global Phase3FinalWendyHp
        global Burn
        global Burned
        global Attacked
        global SFB2
        global Healed
        global WendyDefend     
        global damage
        global damaged
        global MoreAttack
        global MoreHp
        global MoreDefence
        global Healed
        global M
        global Off
        global Upgrade1
        global Upgrade2
        global Upgrade3
        global Answer3
        global Phase2FinalWendyHp
        global FinalWendyHp
        global WendyHp
        global apostrophy
        global Beat
        global End
        global SFB
        global DevHp
        global DevStun
        global DevTaunt
        global EndRepeat
        global RonaldMcDonaldHp
        damage = 0
        damaged = 0
        Burn = 0
        Burned = 0
        Healed = 0
        replit.clear()
        print(reset+"What can I get for you?")
        time.sleep(1)
        Sleep()
        Option1()
        Sleep()
        Option2()
        Sleep()
        Option3()
        Sleep()
        Option4()
        Sleep()
        Option5()
        Sleep()
        Option6()
        Sleep()
        Answer = (input("Input selection here: "+Blue))
        Sleep()
        if Answer == "1":
                if SFB == True and Off == False:
                        replit.clear()
                        if employ == False:
                                print(reset+"Unless you beat me, you can't get one.")
                                time.sleep(1)
                                replit.clear()
                                print("           ")
                                time.sleep(0.1)
                                replit.clear()
                                print("|         |")
                                time.sleep(0.1)
                                replit.clear()
                                print("||       ||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||     |||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||   ||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||| |||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||||||||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||||F|||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||| Fi||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||d Fig|||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||od Figh||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|ood Fight|")
                                time.sleep(0.1)
                                replit.clear()
                                EmployeeFight()
                        time.sleep(1)
                        Sleep()
                        print("Here's your Big Mac- I mean burger, have a nice day.")
                        time.sleep(1)
                        Sleep()
                        print('You ate the "Big Mac" and gained 15 Hp!')
                        Upgrade1 = True
                        YourHp = 25
                        Off = True
                        time.sleep(1)
                        restart()
                if Off == True:
                        replit.clear()
                        print(reset+"No more Big Mac's- I mean burgers, for you.")
                        time.sleep(1)
                        Sleep()
                        print("Please go away.")
                        time.sleep(1)
                        restart()
                replit.clear()
                print(reset+"Sir, this is wendy's.")
                time.sleep(1)
                Sleep()
                print("Please go away.")
                time.sleep(1)
                restart()
        if Answer == "2":
                replit.clear()
                print(reset+"You look for a way to escape the Wendy's")
                time.sleep(1)
                Sleep()
                print("You see two ways to escape, (1) the employee's door, (2) the vents.")
                time.sleep(1)
                Sleep()
                Answer2 = input("Which do you choose: "+Blue)
                if Answer2 == "1":
                        Sleep()
                        print(reset+"You go in the employee's door...")
                        if M == True and SFB == False:
                                print(Red+"The developer was infront of the door and slapped you."+reset)
                                time.sleep(1)
                                restart()
                        if SFB2 == True:
                                print("She's not here anymore")
                                time.sleep(1)
                                restart()
                        if Upgrade1 == False and Upgrade2 == False and Upgrade3 == False and SFB == True:
                                time.sleep(1)
                                Sleep()
                                print(f"{Red}Your not ready to fight her yet.{reset}")
                                time.sleep(1)
                                restart()
                        if M == True and SFB == True:
                                time.sleep(1)
                                Sleep()
                                print("There's Wendy's secret recipy, it shows a Big Mac on the front.")
                                time.sleep(2)
                                replit.clear()
                                print(Red+"Uh-oh what's that?")
                                time.sleep(1)
                                print("It's Wendy, she looks enraged.")
                                time.sleep(1)
                                replit.clear()
                                print("           ")
                                time.sleep(0.1)
                                replit.clear()
                                print("|         |")
                                time.sleep(0.1)
                                replit.clear()
                                print("||       ||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||     |||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||   ||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||| |||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||||||||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||||h W||||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|||th Wi|||")
                                time.sleep(0.1)
                                replit.clear()
                                print("||ath Wis||")
                                time.sleep(0.1)
                                replit.clear()
                                print("|eath Wish|")
                                time.sleep(0.1)
                                replit.clear()
                                FinalFight()
                        else:
                                time.sleep(1)
                                Sleep()
                                print("There was an employee right infront of the door!")
                                time.sleep(1)
                                Sleep()
                                print("You got caught and brought to the manager.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The manager slaps you.")
                                M = False
                                time.sleep(1)
                                restart()
                if Answer2 == "2":
                        Sleep()
                        print(reset+"You went into the vents...")
                        time.sleep(1)
                        Sleep()
                        print("You made your way out of the vents and found the managers secret stash of money...")
                        time.sleep(1)
                        Sleep()
                        print("You need to get out of there fast!")
                        time.sleep(1)
                        Sleep()
                        print("There is a door in front of you, it has a keypad on it.")
                        time.sleep(1)
                        Sleep()
                        Answer3 = input("Enter (something) in the keypad: "+Blue)
                        if Answer3 == "something":
                                if M == True:
                                        if SFB == True:
                                                if SFB2 == True:
                                                        Sleep()
                                                        print("She's not here anymore")
                                                        time.sleep(1)
                                                        restart()
                                                Sleep()
                                                print(reset+"The ground below you falls open")
                                                time.sleep(1)
                                                Sleep()
                                                print('Wendy has left, where is she now?')
                                                time.sleep(1)
                                                restart()
                                        Sleep()
                                        print(reset+"The ground below you falls open")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"You see wendy herself, sitting in her chair very menacingly.")
                                        time.sleep(2)
                                        Sleep()
                                        print("Your doomed."+reset)
                                        time.sleep(0.5)
                                        replit.clear()
                                        print("           ")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|         |")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||       ||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||     |||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||   ||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||| |||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||||||||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||| |||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||l B||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||al Bo|||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||nal Bos||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|inal Boss|")
                                        time.sleep(0.1)
                                        replit.clear()
                                        BossFight()
                                else:
                                        Sleep()
                                        print(reset+"It opened!")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"The manager was standing right in front of the door, he slaps you.")
                                        M = False
                                        time.sleep(5)
                                        restart()
                        elif Answer3 == ":flushed:":
                                Sleep()
                                print(reset+"-O_O-")
                                time.sleep(1)
                                restart()
                                time.sleep(1)
                                restart()
                        elif Answer3 == ":?:":
                                Sleep()
                                print(reset+"Your in a Wendy's dimention, there are only Wendy's here. Here, Wendy is a very powerful being.")
                                time.sleep(3)
                                restart()
                        elif Answer3 == "Secret":
                                Sleep()
                                print(reset+"You found a secret!")
                                time.sleep(1)
                                restart()
                        elif Answer3 == "Ghost Is Destroy.mp3":
                                if SFB2 == True:
                                        Sleep()
                                        print(reset+"You hear footsteps behind you...")
                                        Sleep()
                                        time.sleep(1)
                                        print(reset+"Its the developer!")
                                        time.sleep(1)
                                        replit.clear()
                                        print("           ")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|         |")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||       ||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||     |||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||   ||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||| |||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||||||||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|||||a|||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||||Bat||||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||| Batt|||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("||v Battl||")
                                        time.sleep(0.1)
                                        replit.clear()
                                        print("|ev Battle|")
                                        time.sleep(0.1)
                                        replit.clear()
                                        DevBoss()
                                else:
                                        Sleep()
                                        print(Red+"You have to have beat [?] to get this secret.")
                                        Sleep()
                                        time.sleep(1)
                                        print(reset+"Once you do, come back.")
                                        time.sleep(1)
                                        restart()
                        else:
                                Sleep()
                                print(Red+"It didn't work!")
                                time.sleep(1)
                                if M == True:
                                        Sleep()
                                        print(reset+"Since the manager isn't around I guess I'll slap you.")
                                        time.sleep(1)
                                        print(Red+"The game developer slaps you.")
                                        time.sleep(1)
                                        restart()
                                Sleep()
                                print(Red+"The manager walks in and slaps you.")
                                time.sleep(1)
                                restart()
                else:
                        if M == True:
                                Sleep()
                                print("Due to you failure to pick an option, the manager- oh, he's gone. I guess I'll slap you then.")
                                time.sleep(1)
                                print(Red+"The game developer slaps you.")
                                time.sleep(1)
                                restart()
                        Sleep()
                        print(Red+"Because of your failure to pick one of the options, the manager came and slapped you.")
                        time.sleep(3)
                        restart()
        if Answer == "3":
                replit.clear()
                if M == True:
                        print(Red+"The manager isn't here anymore."+reset)
                        time.sleep(1)
                        restart()
                print(Red+"Sir, I AM THE MANAGER!"+reset)
                time.sleep(2)
                replit.clear()
                print("           ")
                time.sleep(0.1)
                replit.clear()
                print("|         |")
                time.sleep(0.1)
                replit.clear()
                print("||       ||")
                time.sleep(0.1)
                replit.clear()
                print("|||     |||")
                time.sleep(0.1)
                replit.clear()
                print("||||   ||||")
                time.sleep(0.1)
                replit.clear()
                print("||||| |||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||||||||")
                time.sleep(0.1)
                replit.clear()
                print("|||||F|||||")
                time.sleep(0.1)
                replit.clear()
                print("|||| Fi||||")
                time.sleep(0.1)
                replit.clear()
                print("|||s Fig|||")
                time.sleep(0.1)
                replit.clear()
                print("||ss Figh||")
                time.sleep(0.1)
                replit.clear()
                print("|oss Fight|")
                time.sleep(0.1)
                replit.clear()
                Fight()
                
        if Answer == "4":
                replit.clear()
                print(reset+"You wait...")
                time.sleep(5)
                if SFB == True:
                        if Upgrade3 == True:
                                Sleep()
                                print("You wait some more...")
                                Sleep()
                                time.sleep(5)
                                print("You wait even longer...")
                                Sleep()
                                time.sleep(5)
                                print("You wait impatiently...")
                                Sleep()
                                time.sleep(5)
                                print(Red+"You give up."+reset)
                                Sleep()
                                time.sleep(1)
                                restart()
                        Sleep()
                        print("A secret compartment opens up, there's a knife inside!")
                        Sleep()
                        time.sleep(1)
                        print("Your attacks do more damage now!")
                        Upgrade3 = True
                        MoreAttack = 5
                        time.sleep(1)
                        restart()
                else:
                        Sleep()
                        print("You wait some more...")
                        Sleep()
                        time.sleep(5)
                        print("You wait even longer...")
                        Sleep()
                        time.sleep(5)
                        print("You wait impatiently...")
                        Sleep()
                        time.sleep(5)
                        print(Red+"You give up."+reset)
                        Sleep()
                        time.sleep(1)
                        restart()
        if Answer == "5":
                outside()
        if Answer == "6":
                replit.clear()
                print(reset+'Saving...')
                apostrophy = db['apostrophy']
                Beat = db['Beat']  
                End = db['End'] 
                Difficulty = db['Difficulty']
                Phase3FinalWendyHp = db['Phase3FinalWendyHp']   
                Phase2FinalWendyHp = db['Phase2FinalWendyHp']   
                FinalWendyHp = db['FinalWendyHp'] 
                WendyHp = db['WendyHp']  
                YourHp = db['YourHp']  
                TheirHp = db['TheirHp']   
                damage = db['damage']   
                damaged = db['damaged']  
                Burn = db['Burn']  
                Burned = db['Burned']
                SFB = db['SFB'] 
                SFB2 = db['SFB2'] 
                MoreAttack = db['MoreAttack'] 
                MoreHp = db['MoreHp'] 
                MoreDefence = db['MoreDefence'] 
                Healed = db['Healed'] 
                Upgrade1 = db['Upgrade1'] 
                Upgrade2 = db['Upgrade2'] 
                Upgrade3 = db['Upgrade3'] 
                M = db['M']
                Off = db['Off'] 
                Answer3 = db['Answer3'] 
                WendyDefend  = db['WendyDefend'] 
                DevHp = db['DevHp'] 
                DevStun = db['DevStun'] 
                DevTaunt = db['DevTaunt']
                EndRepeat = db['EndRepeat']
                RonaldMcDonaldHp = db['RonaldMcDonaldHp']
                db['apostrophy'] = apostrophy
                db['Beat'] = Beat 
                db['End'] = End  
                db['Difficulty'] = Difficulty  
                db['Phase3FinalWendyHp'] = Phase3FinalWendyHp  
                db['Phase2FinalWendyHp'] = Phase2FinalWendyHp  
                db['FinalWendyHp'] = FinalWendyHp  
                db['WendyHp'] = WendyHp  
                db['YourHp'] = YourHp 
                db['TheirHp'] = TheirHp  
                db['damage'] = damage  
                db['damaged'] = damaged 
                db['Burn'] = Burn 
                db['Burned'] = Burned 
                db['SFB'] = SFB
                db['SFB2'] = SFB2
                db['MoreAttack'] = MoreAttack
                db['MoreHp'] = MoreHp
                db['MoreDefence'] = MoreDefence
                db['Healed'] = Healed
                db['Upgrade1'] = Upgrade1
                db['Upgrade2'] = Upgrade2
                db['Upgrade3'] = Upgrade3
                db['M'] = M
                db['Off'] = Off
                db['Answer3'] = Answer3
                db['WendyDefend'] = WendyDefend 
                db['DevHp'] = DevHp
                db['DevStun'] = DevStun
                db['DevTaunt'] = DevTaunt
                db['EndRepeat'] = EndRepeat
                db['RonaldMcDonaldHp'] = RonaldMcDonaldHp
                db['employ'] = employ
                replit.clear()
                print('Saved!')
                time.sleep(1)
                restart()
        else:
                print("Please input a valid option.")
                time.sleep(1)
                restart()

def MOption1():
        print("(1) - Order a Big Mac.")

def MOption2():
        print("(2) - Escape?")

def MOption3():
        print("(3) - Find the Manager.")

def MOption4():
        print("(4) - Look Around")

def MOption5():
        print("(5) - Leave.")

def MAll():
        print(reset+". . .")
        time.sleep(1)
        Sleep()
        MOption1()
        Sleep()
        MOption2()
        Sleep()
        MOption3()
        Sleep()
        MOption4()
        Sleep()
        MOption5()
        Sleep()
        Answer = (input("Input selection here: "+Blue))
        Sleep()
        if Answer == "1":
                replit.clear()
                print(Red+"There is nobody at the counter.")
                time.sleep(1)
                Mrestart()
        if Answer == "2":
                replit.clear()
                print(reset+"You look for a way to escape McDonald's...")
                time.sleep(1)
                Sleep()
                print("You see two ways to escape, (1) The Employee's Door, (2) The Playground")
                time.sleep(1)
                Sleep()
                Answer2 = input("Which do you choose: "+Blue)
                if Answer2 == "1":
                        replit.clear()
                        print(reset+"You go in the employee's door...")
                        time.sleep(1)
                        Sleep()
                        print("There's nobody there...")
                        time.sleep(1)
                        Sleep()
                        print("You go into the vent's to look for a way out.")
                        time.sleep(1)
                        Sleep()
                        print("You see two ways to exit, (1) The Bathroom, (2) The Manager's Office")
                        time.sleep(1)
                        Sleep()
                        Answer = (input("Input selection here: "+Blue))
                        Sleep()
                        if Answer == "1":
                                replit.clear()
                                print(reset+"You climb out of the vents and into the bathroom.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"The door is locked, you have no way out...")
                        time.sleep(1)
                        Mrestart()
                        if Answer == "2":
                                replit.clear()
                                print(reset+"You climb out of the vents and into the Manager's Office...")
                                time.sleep(1)
                                Sleep()
                                print(reset+"There's nobody there.")
                                time.sleep(1)
                                Sleep()
                                print(reset+"On the desk, there seems to be some important document's.")
                                time.sleep(1)
                                Sleep()
                                print(reset+'It says, "Due to the dissaperiance of children on the playground, McDonald'+apostrophy+'s is to be closed on Mar 27, 20##"')
                                time.sleep(1)
                                Sleep()
                                print(Red+'You hear the door open up behind you.')
                                time.sleep(1)
                                Sleep()
                                print(Red+"It's Ronald McDonald.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"He eats you.")
                                time.sleep(1)
                                Mrestart()
                if Answer2 == "2":
                        replit.clear()
                        print(reset+"You went to the playground.")
                        time.sleep(1)
                        Sleep()
                        print("There seems to be someone here...")
                        time.sleep(1)
                        Sleep()
                        print("Where do you do? (1) Climb the playground, (2) Take you shoe's off")
                        time.sleep(1)
                        Sleep()
                        Answer = (input("Input selection here: "+Blue))
                        Sleep()
                        if Answer == "1":
                                replit.clear()
                                print(reset+"You climbed the playground")
                                time.sleep(1)
                                Sleep()
                                print(reset+"As your climbing you hear someone enter the room as well.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"It's Ronald McDonald, and he's mad that you didn't follow the rules.")
                                time.sleep(1)
                                Sleep()
                                print(Red+"He finds and eats you.")
                                time.sleep(1)
                                Mrestart()
                        if Answer == "2":
                                replit.clear()
                                print(reset+"You took off your shoe's before climbing the playground.")
                                time.sleep(1)
                                Sleep()
                                print(reset+"As you climb the playground, you see three ways to go. (1) Up The staircase, (2) Through The tunnel, (3) Up the slide")
                                time.sleep(1)
                                Sleep()
                                Answer = (input("Input selection here: "+Blue))
                                Sleep()
                                if Answer == "1":
                                        replit.clear()
                                        print(reset+"You go up the staircase, you hear something following you.")
                                        time.sleep(1)
                                        Sleep()
                                        print("You see two ways to go. (1) Towards the person who's following you, (2) Across the rope tunnel")
                                        time.sleep(1)
                                        Sleep()
                                        Answer = (input("Input selection here: "+Blue))
                                        Sleep()
                                        if Answer == "1":
                                                replit.clear()
                                                print(reset+"You go toward the person following you.")
                                                time.sleep(1)
                                                Sleep()
                                                print(Red+"It's Ronald McDonald.")
                                                time.sleep(1)
                                                Sleep()
                                                print("He eats you.")
                                                time.sleep(1)
                                                Mrestart()
                                        if Answer == "2":
                                                replit.clear()
                                                print(reset+"You go across the rope tunnel.")
                                                time.sleep(1)
                                                Sleep()
                                                print("The person is chasing you now.")
                                                time.sleep(1)
                                                Sleep()
                                                print("You see two ways to go. (1) In the rocket ship, (2) Through the broken window")
                                                time.sleep(1)
                                                Sleep()
                                                Answer = (input("Input selection here: "+Blue))
                                                Sleep()
                                                if Answer == "1":
                                                        replit.clear()
                                                        print(reset+"You go in the rocket ship, it's a dead end!")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print(Red+"Ronald McDonald finds you.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("He eats you.")
                                                        time.sleep(1)
                                                        Mrestart()
                                                if Answer == "2":
                                                        replit.clear()
                                                        print(reset+"You jump out the window.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("You look behind you to see 3 Ronald McDonald's staring at you from inside.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("Your safe.")
                                                        time.sleep(1)
                                                        EndScreen()
                                if Answer == "2":
                                        replit.clear()
                                        print(reset+"You go through the tunnel, you hear something following you.")
                                        time.sleep(1)
                                        Sleep()
                                        print("You see two ways to go. (1) In the ball pit, (2) Through another tunnel")
                                        time.sleep(1)
                                        Sleep()
                                        Answer = (input("Input selection here: "+Blue))
                                        Sleep()
                                        if Answer == "1":
                                                replit.clear()
                                                print(reset+"You go in the ball pit")
                                                time.sleep(1)
                                                Sleep()
                                                print(Red+"You get stuck and are unable to escape")
                                                time.sleep(1)
                                                Sleep()
                                                print("Ronald McDonald finds and eats you.")
                                                time.sleep(1)
                                                Mrestart()
                                        if Answer == "2":
                                                replit.clear()
                                                print(reset+"You go through the tunnel.")
                                                time.sleep(1)
                                                Sleep()
                                                print("The person is chasing you now.")
                                                time.sleep(1)
                                                Sleep()
                                                print("You see two ways to go. (1) Down the slide, (2) Through the broken window")
                                                time.sleep(1)
                                                Sleep()
                                                Answer = (input("Input selection here: "+Blue))
                                                Sleep()
                                                if Answer == "1":
                                                        replit.clear()
                                                        print(reset+"You go down the slide.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print(Red+"Ronald McDonald is at the bottom.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("He eats you.")
                                                        time.sleep(1)
                                                        Mrestart()
                                                if Answer == "2":
                                                        replit.clear()
                                                        print(reset+"You jump out the window.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("You look behind you to see 3 Ronald McDonald's staring at you from inside.")
                                                        time.sleep(1)
                                                        Sleep()
                                                        print("Your safe.")
                                                        time.sleep(1)
                                                        EndScreen()
                                if Answer == "3":
                                        replit.clear()
                                        print(reset+"You go up the slide, you hear something following you.")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"You see Ronald McDonald at the top.")
                                        time.sleep(1)
                                        Sleep()
                                        print(Red+"He grabs and eat's you.")
                                        time.sleep(1)
                                        Mrestart()
                                        
        if Answer == "3":        
                replit.clear()
                print(reset+"There seems to be no manager around.")
                time.sleep(1)
                Mrestart()
        if Answer == "4":
                replit.clear()
                print(reset+"You see a run down, old McDonalds. It's kinda creepy.")
                time.sleep(1)
                Mrestart()
        if Answer == "5":
                replit.clear()
                print(reset+"You try to leave but the door's locked")
                time.sleep(1)
                Mrestart()
                
        else:
                print("Please input a valid option.")
                time.sleep(1)
                Mrestart()

def Mrestart():
        replit.clear()
        print(reset+"Hello, welcome to "+Red+"McDonalds!")
        time.sleep(1)
        Sleep()
        MAll()
                
def Menu():
        global End
        global Difficulty
        global TheirHp
        global Phase3FinalWendyHp
        global Phase2FinalWendyHp
        global FinalWendyHp
        global WendyHp
        global DevHp
        global timeStart
        global EmployeeHp
        global RonaldMcDonaldHp
        replit.clear()
        print("Sir, This Is An Egg")
        Sleep()
        print("(1) - Start")
        Sleep()
        print("(2) - Difficulty")
        Sleep()
        print("(3) - Guide")
        Sleep()
        print("(4) - Reset Save Data")
        Sleep()
        print("(5) - Skip to McDonalds")
        Sleep()
        print("(6) - Egg Boss Fight!")
        Sleep()
        MenuInput = input('Select an option: '+Blue)
        if MenuInput == "Credits":
                timeStart = time.time()
                EndScreen()
        elif MenuInput == "1":
                Loading()
        elif MenuInput == "2":
                replit.clear()
                print(reset+'How hard would you like the game to be?')
                Sleep()
                print("(1) - Insta-Win | 0.0x")
                Sleep()
                print("(2) - Beginner | 0.1x")
                Sleep()
                print("(3) - Easy | 0.5x")
                Sleep()
                print("(4) - Normal | 1.0x")
                Sleep()
                print("(5) - Hard | 2.0x")
                Sleep()
                print("(6) - Extreme | 3.0x")
                Sleep()
                print("(7) - Cataclysmic | 5.0x")
                Sleep()
                DifficultyInput = input('Select a difficulty: '+Blue)
                if DifficultyInput == "1":
                        End = False
                        Difficulty = 0
                        replit.clear()
                        print(reset+'Difficulty was changed to Insta-Win.')
                        time.sleep(1)
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        Menu()
                if DifficultyInput == "2":
                        End = False
                        Difficulty = 0.1
                        replit.clear()
                        print(reset+'Difficulty was changed to Beginner.')
                        time.sleep(1)
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        Menu()
                if DifficultyInput == "3":
                        End = False
                        Difficulty = 0.5
                        replit.clear()
                        print(reset+'Difficulty was changed to easy.')
                        time.sleep(1)
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        Menu()
                if DifficultyInput == "4":
                        End = False
                        Difficulty = 1
                        replit.clear()
                        print(reset+'Difficulty was changed to normal.')
                        time.sleep(1)
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        Menu()
                if DifficultyInput == "5":
                        End = False
                        Difficulty = 2
                        replit.clear()
                        print(reset+'Difficulty was changed to hard.')
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        time.sleep(1)
                        Menu()
                if DifficultyInput == "6":
                        End = 1
                        Difficulty = 3
                        replit.clear()
                        print(reset+'Difficulty was changed to exteme.')
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        time.sleep(1)
                        Menu()
                if DifficultyInput == "7":
                        End = 2
                        Difficulty = 5
                        replit.clear()
                        print(reset+'Difficulty was changed to cataclysmic.')
                        Phase3FinalWendyHp *= Difficulty
                        TheirHp *= Difficulty
                        Phase2FinalWendyHp *= Difficulty
                        FinalWendyHp *= Difficulty
                        WendyHp *= Difficulty
                        DevHp *= Difficulty
                        EmployeeHp *= Difficulty 
                        RonaldMcDonaldHp *= Difficulty 
                        round(EmployeeHp)
                        round(RonaldMcDonaldHp)
                        round(DevHp)
                        round(Phase3FinalWendyHp)
                        round(TheirHp)
                        round(Phase2FinalWendyHp)
                        round(FinalWendyHp)
                        round(WendyHp)
                        time.sleep(1)
                        Menu()
        elif MenuInput == "3":
                Sleep()
                print(reset+"How to beat the game:\n 1. Defeat the manager.\n 2. Enter the code, 'something' in the keypad.\n 3. Defeat Wendy.\n 4. Eat a big mac.(Ask for a big mac)\n 5. Find the knife. (Wait)\n 6. Grab the armour. (Leave and go to your home)\n 7. Go through the employee's door.\n 8. Beat Death Wish Wendy, Last Fight Wendy, and Final Form Wendy.\n 9. Go to your home.\n 10. Watch TV.")
                Sleep()
                enter = input('Press ENTER to go back ')
                Menu()
        elif MenuInput == '4':
                print(reset+'Clearing Data...')
                db.clear()
                print('Loading...')
                db['yes'] = True
                db['apostrophy'] = apostrophy
                db['Beat'] = Beat 
                db['End'] = End  
                db['Difficulty'] = Difficulty  
                db['Phase3FinalWendyHp'] = Phase3FinalWendyHp  
                db['Phase2FinalWendyHp'] = Phase2FinalWendyHp  
                db['FinalWendyHp'] = FinalWendyHp  
                db['WendyHp'] = WendyHp  
                db['YourHp'] = YourHp 
                db['TheirHp'] = TheirHp  
                db['damage'] = damage  
                db['damaged'] = damaged 
                db['Burn'] = Burn 
                db['Burned'] = Burned 
                db['SFB'] = SFB
                db['SFB2'] = SFB2
                db['MoreAttack'] = MoreAttack
                db['MoreHp'] = MoreHp
                db['MoreDefence'] = MoreDefence
                db['Healed'] = Healed
                db['Upgrade1'] = Upgrade1
                db['Upgrade2'] = Upgrade2
                db['Upgrade3'] = Upgrade3
                db['M'] = M
                db['Off'] = Off
                db['Answer3'] = Answer3
                db['WendyDefend'] = WendyDefend 
                db['DevHp'] = DevHp
                db['DevStun'] = DevStun
                db['DevTaunt'] = DevTaunt
                db['EndRepeat'] = EndRepeat
                db['RonaldMcDonaldHp'] = RonaldMcDonaldHp
                db['employ'] = employ
                print(reset+'Save data cleared!')
                enter = input('Press ENTER to go back ')
                Menu()
        elif MenuInput == '5':
                replit.clear()
                timeStart = time.time()
                Mrestart()
        elif MenuInput == '6':
                replit.clear()
                egg()
        else:
                Sleep()
                print(Red+"Please select an option."+reset)
                time.sleep(1)
                Menu()
def Loading():
        global timeStart
        replit.clear()
        timeStart = time.time()
        print(reset+"Hello, welcome to "+Blue+"Wendy's!"+reset)
        time.sleep(1)
        Sleep()
        All()
def Wait():
        print('') 
        time.sleep(0.1)
def EndScreen():
        global End
        global Beat
        timeEnd = time.time()
        timeTaken = timeEnd - timeStart
        replit.clear() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep() 
        Sleep()
        Sleep() 
        print(reset+"")
        EndText = ("Sir, this is a Wendy's\n----------------------")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("░██████╗██╗██████╗░░░░████████╗██╗░░██╗██╗░██████╗██╗░██████╗░█████╗░\n██╔════╝██║██╔══██╗░░░╚══██╔══╝██║░░██║██║██╔════╝██║██╔════╝██╔══██╗\n╚█████╗░██║██████╔╝░░░░░░██║░░░███████║██║╚█████╗░██║╚█████╗░███████║\n░╚═══██╗██║██╔══██╗██╗░░░██║░░░██╔══██║██║░╚═══██╗██║░╚═══██╗██╔══██║\n██████╔╝██║██║░░██║╚█║░░░██║░░░██║░░██║██║██████╔╝██║██████╔╝██║░░██║\n╚═════╝░╚═╝╚═╝░░╚═╝░╚╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝╚═════╝░╚═╝░░╚═╝\n\n░██╗░░░░░░░██╗███████╗███╗░░██╗██████╗░██╗░░░██╗██╗░██████╗\n░██║░░██╗░░██║██╔════╝████╗░██║██╔══██╗╚██╗░██╔╝╚█║██╔════╝\n░╚██╗████╗██╔╝█████╗░░██╔██╗██║██║░░██║░╚████╔╝░░╚╝╚█████╗░\n░░████╔═████║░██╔══╝░░██║╚████║██║░░██║░░╚██╔╝░░░░░░╚═══██╗\n░░╚██╔╝░╚██╔╝░███████╗██║░╚███║██████╔╝░░░██║░░░░░░██████╔╝\n░░░╚═╝░░░╚═╝░░╚══════╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░░░░╚═════╝░")
        for char in EndText:
            time.sleep(0.0005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("Developers\n----------\nColoredHue \nBobo")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("Contributors\n------------\nRaeymSiraj:\nNo U⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n:flushed:\ntry to beat my wr: 2:03:17")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("▀ █▀▀ █░░ █░█ █▀ █░█ █▀▀ █▀▄ ▀\n▄ █▀░ █▄▄ █▄█ ▄█ █▀█ ██▄ █▄▀ ▄")
        for char in EndText:
            time.sleep(0.005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("XuhongSoong:\nlast fight wendy is hard")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("╔══╗─────╔╗╔═══╗─────────╔════╗────╔╗\n║╔╗║─────║║║╔═╗║─────────║╔╗╔╗║───╔╝╚╗\n║╚╝╚╦══╦═╝║║║─╚╬══╦╗╔╦══╗╚╝║║╠╩═╦═╩╗╔╬══╦═╗\n║╔═╗║╔╗║╔╗║║║╔═╣╔╗║╚╝║║═╣──║║║║═╣══╣║║║═╣╔╝\n║╚═╝║╔╗║╚╝║║╚╩═║╔╗║║║║║═╣──║║║║═╬══║╚╣║═╣║\n╚═══╩╝╚╩══╝╚═══╩╝╚╩╩╩╩══╝──╚╝╚══╩══╩═╩══╩╝")
        for char in EndText:
            time.sleep(0.0005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("LX123:\nin hard mode i got a glitch where regular wendy has 22456.23423 hp lol")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("▒█░░▒█ █▀▀ █▀▀▄ █▀▀▄ █░░█ ▒█░▒█ █▀▀█ ▄ 　 █▀█ █▀█ ░█▀█░ █▀▀ ▄▀▀▄ ░ █▀█ █▀▀█ ░█▀█░█▀█ █▀▀█\n▒█▒█▒█ █▀▀ █░░█ █░░█ █▄▄█ ▒█▀▀█ █░░█ ░ 　 ░▄▀ ░▄▀ █▄▄█▄ ▀▀▄ █▄▄░ ▄ ░▄▀ ░░▀▄ █▄▄█▄ ░▄▀ ░░▀▄\n▒█▄▀▄█ ▀▀▀ ▀░░▀ ▀▀▀░ ▄▄▄█ ▒█░▒█ █▀▀▀ ▀ 　 █▄▄ █▄▄ ░░░█░ ▄▄▀ ▀▄▄▀ █ █▄▄ █▄▄█ ░░░█░ █▄▄ █▄▄█")
        for char in EndText:
            time.sleep(0.0005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("codeisfunsp:\n*you're\ncmon dude\nyou cant mess up such a great game like that")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = (" █████ █████                      ██                   \n░░███ ░░███                      ███                   \n ░░███ ███    ██████  █████ ████░░░  ████████   ██████ \n  ░░█████    ███░░███░░███ ░███     ░░███░░███ ███░░███\n   ░░███    ░███ ░███ ░███ ░███      ░███ ░░░ ░███████ \n    ░███    ░███ ░███ ░███ ░███      ░███     ░███░░░  \n    █████   ░░██████  ░░████████     █████    ░░██████ \n   ░░░░░     ░░░░░░    ░░░░░░░░     ░░░░░      ░░░░░░  \n")
        for char in EndText:
            time.sleep(0.0005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("JasonQiu:\nHow do you beat Wendy?\n\nJoshuaPlayz1235:\n@JasonQiu just attack her ...\n\nColoredHue:\n@JasonQiu JoshuaPlayz1235 clearly hasn't beaten her yet")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("ArnavNair:\ncan i pls have fried chicken?")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("⣿⣿⣿⣿⣿⣿⣿⡿⢟⣋⣭⣥⣭⣭⣍⡉⠉⠙⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡏⠁⠠⠶⠛⠻⠿⣿⣿⣿⣿⣷⡄⠄⠄⠄⠄⠉⠻⢿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠟⠄⢀⡴⢊⣴⣶⣶⣾⣿⣿⣿⣿⢿⡄⠄⠄⠄⠄⠄⠄⠙⢿⣿⣿⣿\n⣿⣿⡿⠁⠄⠙⡟⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣎⠃⠄⠄⠄⠄⠄⠄⠄⠈⢻⣿⣿\n⣿⡟⠄⠄⠄⠄⡇⠰⠟⠛⠛⠿⠿⠟⢋⢉⠍⢩⣠⡀⠄⠄⠄⠄⠄⠄⠄⠄⢹⣿\n⣿⠁⠄⠄⠄⠄⠰⠁⣑⣬⣤⡀⣾⣦⣶⣾⣖⣼⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⢿\n⡏⠄⠄⠄⠄⠄⠄⠄⠨⣿⠟⠰⠻⠿⣣⡙⠿⣿⠋⠄⢀⡀⣀⠄⣀⣀⢀⣀⣀⢸\n⡇⠄⠄⠄⠄⠄⠄⠄⠄⣠⠄⠚⠛⠉⠭⣉⢁⣿⠄⢀⡿⢾⣅⢸⡗⠂⢿⣀⡀⢸\n⡇⠄⠄⠄⠄⠄⠄⠄⠄⠘⢧⣄⠄⣻⣿⣿⣾⠟⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸\n⣿⠄⠄⠄⠄⠄⠄⠄⠄⢠⡀⠄⠄⣿⣿⠟⢁⣴⣿⢸⡄⠄⢦⣤⣤⣤⣤⣄⡀⣼\n⣿⣧⠄⠄⠄⠄⠄⠄⢠⡸⣿⠒⠄⠈⠛⠄⠁⢹⡟⣾⡇⠄⠈⢿⣿⣿⣿⣿⣿⣿\n⣿⣿⣧⣠⣴⣦⠄⠄⢸⣷⡹⣧⣖⡔⠄⠱⣮⣻⣷⣿⣿⠄⠄⠘⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠄⠄⠸⠿⠿⠚⠛⠁⠂⠄⠉⠉⡅⢰⡆⢰⡄⠄⠘⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣷⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⠄⣷⠘⣧⣠⣾⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣤⣄⣀⣀⡀⠄⣀⣀⣹⣦⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿")
        for char in EndText:
            time.sleep(0.0005)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("AlcoholicDevil:\nhello sir, i am an advocate of KFC. would you like some fired chik-")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("wdsa:\nWhy is their no salad option, bruh, I'm vegetarian")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("BreeVee:\nLol trying for credits/ it is funny…right?\n\nColoredHue:\n@BreeVee no")
        for char in EndText:
            time.sleep(0.05)
            sys.stdout.write(char)
            sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("JoelMesser:\nWait, where am I again?")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("ErickGunther:\n")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        EndText = ("▐▓█▀▀▀▀▀▀▀▀▀█▓▌ \n▐▓█  ▀  ▀▄  █▓▌ \n▐▓█  ▄  ▄▀  █▓▌ \n▐▓█▄▄▄▄▄▄▄▄▄█▓▌ \n\n")
        for char in EndText:
                time.sleep(0.005)
                sys.stdout.write(char)
                sys.stdout.flush()
        EndText = ("LucasPerrone:\n@ErickGunther you dumb")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("POWERMAN101:\nword of the day: wendys")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("USER3121:\nGentlemen, You cannot fight in here, this is a public restaurant.")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("WyattCotter:\nWhen will we get the Ronald Mcdonald addon?")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("KalyricDavisBoo:\nlame throwing tomatos\n\nLiamWhitley:\n@KalyricDavis i bet you play those brain puzzle games for 6 year olds")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("LoveFromSkyy:\nvery yes")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("Thank You For Playing!\n----------------------\nTime: " + (str(round(timeTaken, 1))) + "seconds")
        for char in EndText:
                time.sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
        if End == 1:
                Wait()
                Wait()
                Wait()
                EndText = (green+"Wow, you beat Extreme Difficulty!"+reset)
                for char in EndText:
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
        if End == 2:
                Wait()
                Wait()
                Wait()
                EndText = (green+"AMAZING, you beat Catacylsmic Difficulty!"+reset)
                for char in EndText:
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
        if Beat == 3:
                Wait()
                Wait()
                Wait()
                EndText = (green+"Congrats, you have 100% completed the game!"+reset)
                for char in EndText:
                        time.sleep(0.05)
                        sys.stdout.write(char)
                        sys.stdout.flush()
        Wait()
        Wait()
        Wait()
        EndText = ("╭━━━━┳╮╱╱╱╱╱╱╱╭╮╱╱╭╮╱╱╭╮\n┃╭╮╭╮┃┃╱╱╱╱╱╱╱┃┃╱╱┃╰╮╭╯┃\n╰╯┃┃╰┫╰━┳━━┳━╮┃┃╭╮╰╮╰╯╭┻━┳╮╭╮\n╱╱┃┃╱┃╭╮┃╭╮┃╭╮┫╰╯╯╱╰╮╭┫╭╮┃┃┃┃\n╱╱┃┃╱┃┃┃┃╭╮┃┃┃┃╭╮╮╱╱┃┃┃╰╯┃╰╯┃\n╱╱╰╯╱╰╯╰┻╯╰┻╯╰┻╯╰╯╱╱╰╯╰━━┻━━╯")
        for char in EndText:
                time.sleep(0.0005)
                sys.stdout.write(char)
                sys.stdout.flush()
        for I in range(55):
                Wait()
        Wait()
        Wait()
        print(green+'')
        End = False
        Difficulty = 1
        Phase3FinalWendyHp = 100
        Phase2FinalWendyHp = 75
        FinalWendyHp = 50
        WendyHp = 30
        YourHp = 10
        TheirHp = 15
        damage = 0
        damaged = 0
        Burn = 0
        Burned = 0
        SFB = False
        SFB2 = False
        MoreAttack = 0
        MoreHp = 0
        MoreDefence = 0
        Healed = 0
        Upgrade1 = False
        Upgrade2 = False
        Upgrade3 = False
        M = False
        Off = False
        Answer3 = ""
        WendyDefend = 0
        DevHp = 999
        DevStun = 0
        DevTaunt = 0
        EndRepeat = True
        replit.clear()
        Menu()
        
Menu()
