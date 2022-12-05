# Generated from Commands.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CommandsParser import CommandsParser
else:
    from CommandsParser import CommandsParser

# This class defines a complete generic visitor for a parse tree produced by CommandsParser.

class CommandsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CommandsParser#program.
    def visitProgram(self, ctx:CommandsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#cmd.
    def visitCmd(self, ctx:CommandsParser.CmdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#summon.
    def visitSummon(self, ctx:CommandsParser.SummonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#mob_type.
    def visitMob_type(self, ctx:CommandsParser.Mob_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#give.
    def visitGive(self, ctx:CommandsParser.GiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#item.
    def visitItem(self, ctx:CommandsParser.ItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#item_material.
    def visitItem_material(self, ctx:CommandsParser.Item_materialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#item_name.
    def visitItem_name(self, ctx:CommandsParser.Item_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#kill.
    def visitKill(self, ctx:CommandsParser.KillContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#gamemode.
    def visitGamemode(self, ctx:CommandsParser.GamemodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#time_set.
    def visitTime_set(self, ctx:CommandsParser.Time_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#time_string.
    def visitTime_string(self, ctx:CommandsParser.Time_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#weather.
    def visitWeather(self, ctx:CommandsParser.WeatherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#weather_type.
    def visitWeather_type(self, ctx:CommandsParser.Weather_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#tp.
    def visitTp(self, ctx:CommandsParser.TpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#difficulty.
    def visitDifficulty(self, ctx:CommandsParser.DifficultyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CommandsParser#difficulty_level.
    def visitDifficulty_level(self, ctx:CommandsParser.Difficulty_levelContext):
        return self.visitChildren(ctx)



del CommandsParser