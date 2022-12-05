from antlr4 import *
from EntitiesTable import EntitiesTable,Player,Mob
from visitorFiles.CommandsParser import CommandsParser
from visitorFiles.CommandsVisitor import CommandsVisitor
import sys

sys.tracebacklimit = 0

class SteveOfWarSemantic(CommandsVisitor):
    entities_table = EntitiesTable()    # Tabela de Símbolos
    
    def visitProgram(self, ctx: CommandsParser.ProgramContext):
        return self.visitChildren(ctx)
    
    def visitCmd(self, ctx: CommandsParser.CmdContext):
        if (ctx.summon() is not None):
            return self.visitSummon(ctx.summon())
        elif (ctx.give() is not None):
            return self.visitGive(ctx.give())
        elif (ctx.kill() is not None):
            return self.visitKill(ctx.kill())
        elif(ctx.gamemode() is not None):
            return self.visitGamemode(ctx.gamemode())
        elif (ctx.time_set() is not None):
            return self.visitTime_set(ctx.time_set())
        elif (ctx.weather() is not None):
            return self.visitWeather(ctx.weather())
        elif (ctx.tp() is not None):
            return self.visitTp(ctx.tp())
        elif (ctx.difficulty() is not None):
            return self.visitDifficulty(ctx.difficulty())
        
        return None

    def visitSummon(self, ctx: CommandsParser.SummonContext):
        name = ctx.NAME().getText()
        
        # Verificando se trata-se de uma entidade válida para ser invocada
        if(ctx.mob_type() is not None):
            new_entity = Mob(name)
            self.entities_table.add_entity(new_entity)
        else:
            new_entity = Player(name)
            self.entities_table.add_entity(new_entity)
        return None

    def visitGive(self, ctx: CommandsParser.GiveContext):
        # Verifica quantidade de itens a ser dado ao jogador
        if (int(ctx.NUM_INT().getText()) < 1):
            raise Exception("You can't give a negative quantity of items, please type a positive value")
        
        # Verifica se o identificador de jogador não é nulo
        elif(ctx.NAME() is not None):
            name = ctx.NAME().getText()
            
            # Verifica existência na tabela de símbolos
            if(not(self.entities_table.verify_entity_exists(name))):
                raise Exception("Player " + name +  " doesn't exist")
            
            # Verifica se a instância em questão se trata de um objeto da classe Player
            elif(isinstance(self.entities_table.entities[name], Player)):
                self.entities_table.entities[name].add_inventory(int(ctx.NUM_INT().getText()))
            else:
                raise Exception("You can only give itens to Players")
            
        # Verifica se utiliza '@a' para dar itens para todos os jogadores
        elif('@a' in ctx.getText()):
            for entity in self.entities_table.entities:
                if(isinstance(entity, Player)):
                    entity.add_inventory(int(ctx.NUM_INT().getText()))
        
        return None
    
    def visitKill(self,ctx:CommandsParser.KillContext):
        #Retira entidade da tabela de símbolos se existir
        name = ctx.NAME().getText()
        self.entities_table.kill_entity(name)

        return None
    
    def visitGamemode(self, ctx:CommandsParser.GamemodeContext):
        # Verificando se o modo de jogo escolhido é válido
        if(int(ctx.NUM_INT().getText()) < 0 or int(ctx.NUM_INT().getText())>3):
            raise Exception('Invalid value for gamemode, type 0 for normal, 1  for god mod or 2 for adventure')
        return None
    
    def visitTime_set(self, ctx: CommandsParser.Time_setContext):
        # Verificando se o tempo fornecido é válido
        if(ctx.NUM_INT() is not None):
            num_val = int(ctx.NUM_INT().getText())
            if(num_val > 23000 or num_val < 0):
                raise Exception('Invalid  timestamp, timestamp must be between 0 and 23000')
        return None
        
    def visitTp(self, ctx: CommandsParser.TpContext):
        # Verificando se o identifcador de entidade é válido
        if(ctx.NAME() is not None):
            name = ctx.NAME().getText()
            if(not(self.entities_table.verify_entity_exists(name))):
                raise Exception("Player " + name + " doesn't exist")
            elif(not(isinstance(self.entities_table.entities[name],Player))):
                raise Exception("Entity " + name + " is not a player")

        return None