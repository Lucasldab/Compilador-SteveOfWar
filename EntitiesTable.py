class EntitiesTable:
    def __init__(self):
        self.entities = {}

    def add_entity(self,entity):
        if(not(self.verify_entity_exists(entity.name))):
            self.entities[entity.name] = entity
        else:
            #Lança exceção se identificador único já existir
            raise Exception("Entity identifier " + entity.name + " already being used")
    #Retorna todos os players da tabela de simbolos
    def get_all_players(self):
        return [self.entities[entity] for entity in self.entities if(isinstance(self.entities[entity],Player))]
        
    def verify_entity_exists(self, name_key):
        return name_key in self.entities
    #Elimina entidade da tabela de símbolos se existir
    def kill_entity(self,name):
        if(self.verify_entity_exists(name)):
            self.entities.pop(name)
        else:
            raise Exception("Entity " +  name + " doesn't exist")
        
class Entity:
    def __init__(self, name):
        self.name = name
        
    

class Mob(Entity):
    def __init__(self, name):
        super().__init__(name)

class Player(Entity):
    def __init__(self, name):
        super().__init__(name)        
        self.quant_items = 0
        
    def verify_limit_itens(self,num_items):
        #Considerando 41 slots de item
        return self.quant_items + num_items > 41
        
    def add_inventory(self, num_items):
        #Adiciona itens no invertário se não for ultrapassar limite
        if(not(self.verify_limit_itens(num_items))):
            self.quant_items += num_items
        else: 
            raise Exception("Not enough space in Player " + self.name + "'s inventory")
        
    def __str__(self):
        return f'{self.name}'
    