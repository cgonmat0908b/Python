class Personaje:
    
    def __init__(self, hp : int, atk : int):
        
        if hp <= 0 or atk <= 0:
            raise ValueError("Valores invalidos")
        
        self.hp = hp
        self.atk = atk

    def takeDmg(self,dmg):
        if dmg < 0:
            raise ValueError("No puedes inflingir daño negativo")
        self.hp = max(0, self.hp - dmg)

    def makeDmg(self, objetivo : Personaje):
        objetivo.takeDmg(self.atk)

# Defino 2 pjs
goku = Personaje(100,20)
ryu = Personaje(80,30)

#Imprimo vida 2 pjs
print(goku.hp)
print(ryu.hp)

# Se pegan
goku.makeDmg(ryu)
ryu.makeDmg(goku)

# Imprimo la vida de ambos
print(goku.hp)
print(ryu.hp)

class Guerrero(Personaje):
    def makeDmg(self, objetivo):
        objetivo.takeDmg(self.atk * 2)

goku = Guerrero(100,20)
goku.makeDmg(ryu)
print(ryu.hp)

class Mago(Personaje):
    
    def __init__(self, hp, atk, mp):
        super().__init__(hp,atk)
        self.mp = mp

    def makeDmg(self, objetivo : Personaje):
        # El mago solo puede atacar con mágia si tiene 5 o más mp
        # Si tiene maná, triplica su atk
        if self.mp >= 5:
            objetivo.takeDmg(self.atk * 3)
            self.mp -= 5
        else:
            objetivo.takeDmg(self.atk)

nigger = Mago(100,20,20)
nigger.makeDmg(goku)
print(f"Vida de goku:{goku.hp}")