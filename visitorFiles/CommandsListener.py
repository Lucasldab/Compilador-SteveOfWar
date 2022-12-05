# Generated from Commands.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete listener for a parse tree produced by CommandsParser.
class CommandsListener(ParseTreeListener):

    # Enter a parse tree produced by CommandsParser#program.
    def enterProgram(self, ctx:CommandsParser.ProgramContext):
        pass

    # Exit a parse tree produced by CommandsParser#program.
    def exitProgram(self, ctx:CommandsParser.ProgramContext):
        pass


    # Enter a parse tree produced by CommandsParser#cmd.
    def enterCmd(self, ctx:CommandsParser.CmdContext):
        pass

    # Exit a parse tree produced by CommandsParser#cmd.
    def exitCmd(self, ctx:CommandsParser.CmdContext):
        pass


    # Enter a parse tree produced by CommandsParser#summon.
    def enterSummon(self, ctx:CommandsParser.SummonContext):
        pass

    # Exit a parse tree produced by CommandsParser#summon.
    def exitSummon(self, ctx:CommandsParser.SummonContext):
        pass


    # Enter a parse tree produced by CommandsParser#mob_type.
    def enterMob_type(self, ctx:CommandsParser.Mob_typeContext):
        pass

    # Exit a parse tree produced by CommandsParser#mob_type.
    def exitMob_type(self, ctx:CommandsParser.Mob_typeContext):
        pass


    # Enter a parse tree produced by CommandsParser#give.
    def enterGive(self, ctx:CommandsParser.GiveContext):
        pass

    # Exit a parse tree produced by CommandsParser#give.
    def exitGive(self, ctx:CommandsParser.GiveContext):
        pass


    # Enter a parse tree produced by CommandsParser#item.
    def enterItem(self, ctx:CommandsParser.ItemContext):
        pass

    # Exit a parse tree produced by CommandsParser#item.
    def exitItem(self, ctx:CommandsParser.ItemContext):
        pass


    # Enter a parse tree produced by CommandsParser#item_material.
    def enterItem_material(self, ctx:CommandsParser.Item_materialContext):
        pass

    # Exit a parse tree produced by CommandsParser#item_material.
    def exitItem_material(self, ctx:CommandsParser.Item_materialContext):
        pass


    # Enter a parse tree produced by CommandsParser#item_name.
    def enterItem_name(self, ctx:CommandsParser.Item_nameContext):
        pass

    # Exit a parse tree produced by CommandsParser#item_name.
    def exitItem_name(self, ctx:CommandsParser.Item_nameContext):
        pass


    # Enter a parse tree produced by CommandsParser#kill.
    def enterKill(self, ctx:CommandsParser.KillContext):
        pass

    # Exit a parse tree produced by CommandsParser#kill.
    def exitKill(self, ctx:CommandsParser.KillContext):
        pass


    # Enter a parse tree produced by CommandsParser#gamemode.
    def enterGamemode(self, ctx:CommandsParser.GamemodeContext):
        pass

    # Exit a parse tree produced by CommandsParser#gamemode.
    def exitGamemode(self, ctx:CommandsParser.GamemodeContext):
        pass


    # Enter a parse tree produced by CommandsParser#time_set.
    def enterTime_set(self, ctx:CommandsParser.Time_setContext):
        pass

    # Exit a parse tree produced by CommandsParser#time_set.
    def exitTime_set(self, ctx:CommandsParser.Time_setContext):
        pass


    # Enter a parse tree produced by CommandsParser#time_string.
    def enterTime_string(self, ctx:CommandsParser.Time_stringContext):
        pass

    # Exit a parse tree produced by CommandsParser#time_string.
    def exitTime_string(self, ctx:CommandsParser.Time_stringContext):
        pass


    # Enter a parse tree produced by CommandsParser#weather.
    def enterWeather(self, ctx:CommandsParser.WeatherContext):
        pass

    # Exit a parse tree produced by CommandsParser#weather.
    def exitWeather(self, ctx:CommandsParser.WeatherContext):
        pass


    # Enter a parse tree produced by CommandsParser#weather_type.
    def enterWeather_type(self, ctx:CommandsParser.Weather_typeContext):
        pass

    # Exit a parse tree produced by CommandsParser#weather_type.
    def exitWeather_type(self, ctx:CommandsParser.Weather_typeContext):
        pass


    # Enter a parse tree produced by CommandsParser#tp.
    def enterTp(self, ctx:CommandsParser.TpContext):
        pass

    # Exit a parse tree produced by CommandsParser#tp.
    def exitTp(self, ctx:CommandsParser.TpContext):
        pass


    # Enter a parse tree produced by CommandsParser#difficulty.
    def enterDifficulty(self, ctx:CommandsParser.DifficultyContext):
        pass

    # Exit a parse tree produced by CommandsParser#difficulty.
    def exitDifficulty(self, ctx:CommandsParser.DifficultyContext):
        pass


    # Enter a parse tree produced by CommandsParser#difficulty_level.
    def enterDifficulty_level(self, ctx:CommandsParser.Difficulty_levelContext):
        pass

    # Exit a parse tree produced by CommandsParser#difficulty_level.
    def exitDifficulty_level(self, ctx:CommandsParser.Difficulty_levelContext):
        pass



del CommandsParser