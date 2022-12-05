from html import entities
from antlr4 import *
from EntitiesTable import EntitiesTable,Player,Mob
from visitorFiles.CommandsParser import CommandsParser
from visitorFiles.CommandsVisitor import CommandsVisitor
#Tabela de entidades para fazer controle de Entidades existente
entities_table = EntitiesTable()
#Gerados de código faz tanto o print no terminal quanto gera um arquivo python cujos resultados printam as saídas esperadas
class CodeGenerator(CommandsVisitor):
    saida = ""
    def visitProgram(self, ctx: CommandsParser.ProgramContext):
        self.saida += "from EntitiesTable import EntitiesTable, Player, Mob\n\n" +\
        "entities_table = EntitiesTable()\n\n"
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
        if('Player' in ctx.getText()):
            self.saida += f'{name} = Player("{name}")\n'+\
            f"print('Summoned new Player')\n"
            new_ent = Player(name)
            print('Summoned new Player')
        
            
        else:
            self.saida += f'{name} = Mob("{name}")\n'+\
                f'print("Summoned new {ctx.mob_type().getText()}")\n'
            new_ent =  Mob(name)
            print(f"Summoned new {ctx.mob_type().getText()}")
        self.saida += f'entities_table.add_entity({name})\n\n'
        entities_table.add_entity(new_ent)
        return None

    def visitGive(self, ctx: CommandsParser.GiveContext):
        if ('@a' in ctx.getText()):
            self.saida += f"players = entities_table.get_all_players()\n"+\
            f"for player in players:\n\t" +\
            f"print('Given [{ctx.item().getText()}] * {ctx.NUM_INT().getText()} to ' + player.name)\n"
            #array de players existentes na tabela de entidade
            players = entities_table.get_all_players()
            #Itera sobre todos os players
            for player in players:
                print(f"Given [{ctx.item().getText()}] * {ctx.NUM_INT().getText()} to "+ player.name)
        else:
            self.saida += f"print('Given [{ctx.item().getText()}] * {ctx.NUM_INT().getText()} to {ctx.NAME().getText()}')\n"  
            print(f"Given [{ctx.item().getText()}] * {ctx.NUM_INT().getText()} to {ctx.NAME().getText()}")
        return None
    
    def visitKill(self, ctx: CommandsParser.KillContext):
        name = ctx.NAME().getText()
        self.saida += f"entities_table.kill_entity({name}.name)\n" +\
        f"print('Killed ' + {name}.name)\n"
        entities_table.kill_entity(name)
        print(f"Killed {name}")
        return None
    
    def visitGamemode(self, ctx: CommandsParser.GamemodeContext):
        gamemode = {'0':'Normal','1':'God Mode', '2':'Adventure' }
        self.saida += f"print('Your game mode has been updated to {gamemode[ctx.NUM_INT().getText()]} Mode')\n"
        print(f"Your game mode has been updated to {gamemode[ctx.NUM_INT().getText()]} Mode")
        return None
        
    def visitTime_set(self, ctx: CommandsParser.Time_setContext):
        
        time_dict = {
            'day': 1000,
            'noon': 6000,
            'midday': 6000,
            'sunset': 12000,
            'dusk': 12000,
            'midnight': 18000,
            'sunrise': 23000,
            'dawn': 23000
        }
        
        if (ctx.time_string() is not None):
            self.saida += f'print("Set the time to {time_dict[ctx.time_string().getText()]}")\n'
            print(f"Set the time to {time_dict[ctx.time_string().getText()]}")
        else:
            self.saida += f'print("Set the time to {ctx.NUM_INT().getText()}")\n'
            print(f"Set the time to {ctx.NUM_INT().getText()}")
        return None
    
    def visitWeather(self, ctx: CommandsParser.WeatherContext):
        self.saida += f'print("Changing to {ctx.weather_type().getText()} weather")\n'
        print(f"Changing to {ctx.weather_type().getText()} weather")
        return super().visitWeather(ctx)
        
    def visitTp(self, ctx: CommandsParser.TpContext):
        player = ctx.NAME().getText()
        positions = ctx.NUM_INT()
        self.saida+= f"print('Teleported {player} to {positions[0].getText()}, {positions[1].getText()}, {positions[2].getText()}')\n"  
        print(f"Teleported {player} to {positions[0].getText()}, {positions[1].getText()}, {positions[2].getText()}")
        return None
    
    def visitDifficulty(self, ctx: CommandsParser.DifficultyContext):
        self.saida += f'print("Set game difficulty to {ctx.difficulty_level().getText()}")\n'
        print(f"Set game difficulty to {ctx.difficulty_level().getText()}")
        return None