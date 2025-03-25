import os
import niveaux as n
import time
import paramettre as p
import keyboard

def afficheLabyrinthe(lab,perso,pos_perso,auto,pos_auto,sc,er):
    #os.system('cls')
    print(lab[0]+f"        [Score {sc[0]}]   [Erreur  {er}]")
    for ligne in range(1,len(lab)):
        if ligne==pos_perso[0] and ligne==pos_auto[0]:
            if pos_perso[1]<pos_auto[1]:
                print(lab[ligne][0:pos_perso[1]]+perso+lab[ligne][pos_perso[1]+1:pos_auto[1]]+auto+lab[ligne][pos_auto[1]+1:])
            else:
                print(lab[ligne][0:pos_auto[1]]+auto+lab[ligne][pos_auto[1]+1:pos_perso[1]]+perso+lab[ligne][pos_perso[1]+1:])
        elif ligne==pos_perso[0]:
            print(lab[ligne][0:pos_perso[1]]+perso+lab[ligne][pos_perso[1]+1:])
        elif ligne==pos_auto[0]:
            print(lab[ligne][0:pos_auto[1]]+auto+lab[ligne][pos_auto[1]+1:])
        else:
            print(lab[ligne])
        

def verification_deplacement(lab,pos_col,pos_ligne,sc,er):
    os.system('cls')
    n_lignes = len(lab)
    n_cols = len(lab[0])
    if lab[pos_ligne][pos_col]=="o":
        return [-1,-1]
    elif lab[pos_ligne][pos_col]=="*":
        sc[0]+=70
        for i in range(len(bonus)):
            lab[pos_ligne]=lab[pos_ligne].replace(bonus[i]," ")
        return[pos_ligne,pos_col]
    elif lab[pos_ligne][pos_col]=="P":
        return[1,1]
    elif lab[pos_ligne][pos_col]=="a":
        print("perdue")
        return[1,1]
    elif lab[pos_ligne][pos_col]!=" ":
        er[0]+=1
        sc[0]-=10
        return None
    else:
        return[pos_ligne,pos_col]
    
def verification_deplacement_auto(lab,pos_col,pos_ligne):
    os.system('cls')
    n_lignes = len(lab)
    n_cols = len(lab[0])
    if lab[pos_ligne][pos_col]=="o":
        return [1,1]
    elif lab[pos_ligne][pos_col]=="*" or lab[pos_ligne][pos_col]=="P":
        return[pos_ligne,pos_col]
    elif lab[pos_ligne][pos_col]!=" ":
        return None
    else:
        return[pos_ligne,pos_col]


def choixjoueur(lab,pos_perso,sc,er):
    #choix = input("votre déplacement H/B/D/G/Q : ")
    dep = None
    while True:
        time.sleep(1/10)
        if keyboard.is_pressed("up"):
    ##        time.sleep(1/20)
            dep = verification_deplacement(lab,pos_perso[1],pos_perso[0]-1,sc,er)
            break
        elif keyboard.is_pressed("down"):
            #time.sleep(1/10)
            dep = verification_deplacement(lab,pos_perso[1],pos_perso[0]+1,sc,er)
            break
        elif keyboard.is_pressed("right"):
            #time.sleep(1/10)
            dep = verification_deplacement(lab,pos_perso[1]+1,pos_perso[0],sc,er)
            break
        elif keyboard.is_pressed("left"):
            #time.sleep(1/10)
            dep = verification_deplacement(lab,pos_perso[1]-1,pos_perso[0],sc,er)
            break
        elif keyboard.is_pressed("q"):
            os._exit(1)
        else:
            pass
    if dep == None:
        ##print("déplacement impossible")
        ##input("apuyer sur entrée pour continuer")
        pass
    else:
        pos_perso[0] = dep[0]
        pos_perso[1] = dep[1]

def dep_auto(lab,pos_auto):
    dep = None
    while True:
        time.sleep(1/10)
        dep = verification_deplacement_auto(lab,pos_auto[1]+1,pos_auto[0])
        if dep==None:
            dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]+1)
            if dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]-1)
            elif dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1]-1,pos_auto[0])
            break
        elif dep==None:
            dep = verification_deplacement_auto(lab,pos_auto[1]+1,pos_auto[0])
            if dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1]-1,pos_auto[0])
            elif dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]-1)
            break
        elif dep==None:
            dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]+1)
            if dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]-1)
            elif dep==None:
                verification_deplacement_auto(lab,pos_auto[1]+1,pos_auto[0])
            break
        elif dep==None:
            dep = verification_deplacement_auto(lab,pos_auto[1]+1,pos_auto[0])
            if dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1]-1,pos_auto[0])
            elif dep==None:
                dep = verification_deplacement_auto(lab,pos_auto[1],pos_auto[0]+1)
            break
        else:
            pass            
        
    if dep == None:
        ##print("déplacement impossible")
        ##input("apuyer sur entrée pour continuer")
        pass
    else:
        pos_auto[0] = dep[0]
        pos_auto[1] = dep[1]

def niveaux(lab,pos_perso,perso,pos_auto,auto,sc,er):
    while True:
        #time.sleep(1/100)
        afficheLabyrinthe(lab,perso,pos_perso,auto,pos_auto,sc,er)
        choixjoueur(lab,pos_perso,sc,er)
        if pos_perso == [-1,-1]:
            break

def jeux(lab,pos_perso,perso,pos_auto,auto,sc,er):
    i=0
    ##sc c'est le score
    while(i < len(lab)):
        niveaux(lab[i],pos_perso,perso,pos_auto,auto,sc,er)
        pos_perso=[1,1]
        if i==len(lab)-1:
            print(f"thanks for playing,score {sc[0]}")
        else:
            print(f"vous avez terminer le niveau {i}")
            sc[0] += p.score[i]
            print(sc[0])
        time.sleep(3)           
        i+=1
        
def score(s,n):
    a=0
    if len(s)== len(n):
        return None
    else:
        print("error le nombre de score ne correspond pas au nombre de niveaux")
        time.sleep(3)
        os._exit(1)
        

def penalite(e):
    pen=0
    if e[0] > p.DIFICULTE:
        os.system('cls')
        print("game over")
        time.sleep(3)
        os._exit(1)
    #else :
       # pen=e[0]*10
    #return pen
        







if __name__ == '__main__':
    ver=[0]
    vsc =[0]
    bonus="*"
    auto="a"
    pos_auto=[1,6]
    perso="X"
    pos_perso=[1,1]
    jeux(n.level,pos_perso,perso,pos_auto,auto,vsc,ver)
    
    
    
    

