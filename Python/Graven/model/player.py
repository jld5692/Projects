class Player:
    def __init__(self, pseudo, health, attack):
        self.pseudo = pseudo
        self.health = health
        self.attack = attack
        self.weapon = None      # Par défaut pas d'arme mais il faut quand même créer l'attribut
        print("Bienvenue au joueur", pseudo, "/ Points de vie : ",
              health, " / Attaque : ", attack)

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

    def get_attack_value(self):
        return self.attack

    def get_weapon(self):
        return self.weapon

    def damage(self, damage):
        self.health -= damage

    def attack_player(self, target_player):
        damage = self.attack

        # si le joueur a une arme
        if self.has_weapon():
            # ajoute les dégats de l'arme au point d'attaque du joueur
            damage += self.weapon.get_damage_amount()

        target_player.damage(damage)

    def set_weapon(self, new_weapon):
        self.weapon = new_weapon

    def has_weapon(self):
        return self.weapon is not None
