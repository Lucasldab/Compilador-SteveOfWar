# Generated from Commands.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,105,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,5,0,37,8,0,10,0,12,0,40,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,1,2,1,2,
        1,2,3,2,58,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,3,5,68,8,5,1,5,1,
        5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,3,10,85,
        8,10,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,
        1,14,1,15,1,15,1,15,1,16,1,16,1,16,0,0,17,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,0,7,1,0,4,9,2,0,11,11,52,52,1,0,12,16,1,
        0,17,26,1,0,30,37,1,0,39,43,1,0,46,49,98,0,38,1,0,0,0,2,51,1,0,0,
        0,4,53,1,0,0,0,6,59,1,0,0,0,8,61,1,0,0,0,10,67,1,0,0,0,12,71,1,0,
        0,0,14,73,1,0,0,0,16,75,1,0,0,0,18,78,1,0,0,0,20,81,1,0,0,0,22,86,
        1,0,0,0,24,88,1,0,0,0,26,91,1,0,0,0,28,93,1,0,0,0,30,99,1,0,0,0,
        32,102,1,0,0,0,34,35,5,1,0,0,35,37,3,2,1,0,36,34,1,0,0,0,37,40,1,
        0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,40,38,1,0,0,0,41,
        42,5,0,0,1,42,1,1,0,0,0,43,52,3,4,2,0,44,52,3,8,4,0,45,52,3,16,8,
        0,46,52,3,18,9,0,47,52,3,20,10,0,48,52,3,24,12,0,49,52,3,28,14,0,
        50,52,3,30,15,0,51,43,1,0,0,0,51,44,1,0,0,0,51,45,1,0,0,0,51,46,
        1,0,0,0,51,47,1,0,0,0,51,48,1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,
        52,3,1,0,0,0,53,54,5,2,0,0,54,57,5,52,0,0,55,58,3,6,3,0,56,58,5,
        3,0,0,57,55,1,0,0,0,57,56,1,0,0,0,58,5,1,0,0,0,59,60,7,0,0,0,60,
        7,1,0,0,0,61,62,5,10,0,0,62,63,7,1,0,0,63,64,3,10,5,0,64,65,5,50,
        0,0,65,9,1,0,0,0,66,68,3,12,6,0,67,66,1,0,0,0,67,68,1,0,0,0,68,69,
        1,0,0,0,69,70,3,14,7,0,70,11,1,0,0,0,71,72,7,2,0,0,72,13,1,0,0,0,
        73,74,7,3,0,0,74,15,1,0,0,0,75,76,5,27,0,0,76,77,5,52,0,0,77,17,
        1,0,0,0,78,79,5,28,0,0,79,80,5,50,0,0,80,19,1,0,0,0,81,84,5,29,0,
        0,82,85,3,22,11,0,83,85,5,50,0,0,84,82,1,0,0,0,84,83,1,0,0,0,85,
        21,1,0,0,0,86,87,7,4,0,0,87,23,1,0,0,0,88,89,5,38,0,0,89,90,3,26,
        13,0,90,25,1,0,0,0,91,92,7,5,0,0,92,27,1,0,0,0,93,94,5,44,0,0,94,
        95,7,1,0,0,95,96,5,50,0,0,96,97,5,50,0,0,97,98,5,50,0,0,98,29,1,
        0,0,0,99,100,5,45,0,0,100,101,3,32,16,0,101,31,1,0,0,0,102,103,7,
        6,0,0,103,33,1,0,0,0,5,38,51,57,67,84
    ]

class CommandsParser ( Parser ):

    grammarFileName = "Commands.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'/'", "'summon'", "'Player'", "'Light Elf Slayers'", 
                     "'Dark Elf Lords'", "'Tatzelwurms'", "'Exploding Nightmares'", 
                     "'Draugr Lords'", "'Revenant Hags'", "'give'", "'@a'", 
                     "'Iron'", "'Silver'", "'Bronze'", "'Gold'", "'Diamond'", 
                     "'Leviathan'", "'Talon Bow'", "'Mjolnir'", "'Blade of Chaos'", 
                     "'Guardian Shield'", "'Gungnir'", "'Chestplate'", "'Leggings'", 
                     "'Boots'", "'Draupnir Spear'", "'kill'", "'gamemode'", 
                     "'time set'", "'day'", "'noon'", "'midday'", "'sunset'", 
                     "'dusk'", "'midnight'", "'sunrise'", "'dawn'", "'weather'", 
                     "'clear'", "'rain'", "'fimbulwinter'", "'ragnarok'", 
                     "'sand storm'", "'tp'", "'difficulty'", "'story'", 
                     "'grace'", "'balanced'", "'god of War'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM_INT", "NUM_REAL", "NAME", 
                      "CADEIA", "WS" ]

    RULE_program = 0
    RULE_cmd = 1
    RULE_summon = 2
    RULE_mob_type = 3
    RULE_give = 4
    RULE_item = 5
    RULE_item_material = 6
    RULE_item_name = 7
    RULE_kill = 8
    RULE_gamemode = 9
    RULE_time_set = 10
    RULE_time_string = 11
    RULE_weather = 12
    RULE_weather_type = 13
    RULE_tp = 14
    RULE_difficulty = 15
    RULE_difficulty_level = 16

    ruleNames =  [ "program", "cmd", "summon", "mob_type", "give", "item", 
                   "item_material", "item_name", "kill", "gamemode", "time_set", 
                   "time_string", "weather", "weather_type", "tp", "difficulty", 
                   "difficulty_level" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    NUM_INT=50
    NUM_REAL=51
    NAME=52
    CADEIA=53
    WS=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CommandsParser.EOF, 0)

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CommandsParser.CmdContext)
            else:
                return self.getTypedRuleContext(CommandsParser.CmdContext,i)


        def getRuleIndex(self):
            return CommandsParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CommandsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 34
                self.match(CommandsParser.T__0)
                self.state = 35
                self.cmd()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(CommandsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def summon(self):
            return self.getTypedRuleContext(CommandsParser.SummonContext,0)


        def give(self):
            return self.getTypedRuleContext(CommandsParser.GiveContext,0)


        def kill(self):
            return self.getTypedRuleContext(CommandsParser.KillContext,0)


        def gamemode(self):
            return self.getTypedRuleContext(CommandsParser.GamemodeContext,0)


        def time_set(self):
            return self.getTypedRuleContext(CommandsParser.Time_setContext,0)


        def weather(self):
            return self.getTypedRuleContext(CommandsParser.WeatherContext,0)


        def tp(self):
            return self.getTypedRuleContext(CommandsParser.TpContext,0)


        def difficulty(self):
            return self.getTypedRuleContext(CommandsParser.DifficultyContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCmd" ):
                return visitor.visitCmd(self)
            else:
                return visitor.visitChildren(self)




    def cmd(self):

        localctx = CommandsParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_cmd)
        try:
            self.state = 51
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.summon()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.give()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 45
                self.kill()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 4)
                self.state = 46
                self.gamemode()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                self.time_set()
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.weather()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 7)
                self.state = 49
                self.tp()
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 8)
                self.state = 50
                self.difficulty()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SummonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def mob_type(self):
            return self.getTypedRuleContext(CommandsParser.Mob_typeContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_summon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSummon" ):
                listener.enterSummon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSummon" ):
                listener.exitSummon(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSummon" ):
                return visitor.visitSummon(self)
            else:
                return visitor.visitChildren(self)




    def summon(self):

        localctx = CommandsParser.SummonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_summon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(CommandsParser.T__1)
            self.state = 54
            self.match(CommandsParser.NAME)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 7, 8, 9]:
                self.state = 55
                self.mob_type()
                pass
            elif token in [3]:
                self.state = 56
                self.match(CommandsParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mob_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_mob_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMob_type" ):
                listener.enterMob_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMob_type" ):
                listener.exitMob_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMob_type" ):
                return visitor.visitMob_type(self)
            else:
                return visitor.visitChildren(self)




    def mob_type(self):

        localctx = CommandsParser.Mob_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_mob_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1008) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item(self):
            return self.getTypedRuleContext(CommandsParser.ItemContext,0)


        def NUM_INT(self):
            return self.getToken(CommandsParser.NUM_INT, 0)

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_give

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGive" ):
                listener.enterGive(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGive" ):
                listener.exitGive(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGive" ):
                return visitor.visitGive(self)
            else:
                return visitor.visitChildren(self)




    def give(self):

        localctx = CommandsParser.GiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_give)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(CommandsParser.T__9)
            self.state = 62
            _la = self._input.LA(1)
            if not(_la==11 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 63
            self.item()
            self.state = 64
            self.match(CommandsParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def item_name(self):
            return self.getTypedRuleContext(CommandsParser.Item_nameContext,0)


        def item_material(self):
            return self.getTypedRuleContext(CommandsParser.Item_materialContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem" ):
                listener.enterItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem" ):
                listener.exitItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem" ):
                return visitor.visitItem(self)
            else:
                return visitor.visitChildren(self)




    def item(self):

        localctx = CommandsParser.ItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0:
                self.state = 66
                self.item_material()


            self.state = 69
            self.item_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_materialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_item_material

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_material" ):
                listener.enterItem_material(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_material" ):
                listener.exitItem_material(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem_material" ):
                return visitor.visitItem_material(self)
            else:
                return visitor.visitChildren(self)




    def item_material(self):

        localctx = CommandsParser.Item_materialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_item_material)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 126976) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Item_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_item_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItem_name" ):
                listener.enterItem_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItem_name" ):
                listener.exitItem_name(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItem_name" ):
                return visitor.visitItem_name(self)
            else:
                return visitor.visitChildren(self)




    def item_name(self):

        localctx = CommandsParser.Item_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_item_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 134086656) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KillContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_kill

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKill" ):
                listener.enterKill(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKill" ):
                listener.exitKill(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKill" ):
                return visitor.visitKill(self)
            else:
                return visitor.visitChildren(self)




    def kill(self):

        localctx = CommandsParser.KillContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_kill)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(CommandsParser.T__26)
            self.state = 76
            self.match(CommandsParser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GamemodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(CommandsParser.NUM_INT, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_gamemode

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGamemode" ):
                listener.enterGamemode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGamemode" ):
                listener.exitGamemode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGamemode" ):
                return visitor.visitGamemode(self)
            else:
                return visitor.visitChildren(self)




    def gamemode(self):

        localctx = CommandsParser.GamemodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_gamemode)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(CommandsParser.T__27)
            self.state = 79
            self.match(CommandsParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_setContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def time_string(self):
            return self.getTypedRuleContext(CommandsParser.Time_stringContext,0)


        def NUM_INT(self):
            return self.getToken(CommandsParser.NUM_INT, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_time_set

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_set" ):
                listener.enterTime_set(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_set" ):
                listener.exitTime_set(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_set" ):
                return visitor.visitTime_set(self)
            else:
                return visitor.visitChildren(self)




    def time_set(self):

        localctx = CommandsParser.Time_setContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_time_set)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(CommandsParser.T__28)
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 31, 32, 33, 34, 35, 36, 37]:
                self.state = 82
                self.time_string()
                pass
            elif token in [50]:
                self.state = 83
                self.match(CommandsParser.NUM_INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Time_stringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_time_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime_string" ):
                listener.enterTime_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime_string" ):
                listener.exitTime_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTime_string" ):
                return visitor.visitTime_string(self)
            else:
                return visitor.visitChildren(self)




    def time_string(self):

        localctx = CommandsParser.Time_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_time_string)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 273804165120) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeatherContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def weather_type(self):
            return self.getTypedRuleContext(CommandsParser.Weather_typeContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_weather

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeather" ):
                listener.enterWeather(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeather" ):
                listener.exitWeather(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeather" ):
                return visitor.visitWeather(self)
            else:
                return visitor.visitChildren(self)




    def weather(self):

        localctx = CommandsParser.WeatherContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_weather)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(CommandsParser.T__37)
            self.state = 89
            self.weather_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Weather_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_weather_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWeather_type" ):
                listener.enterWeather_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWeather_type" ):
                listener.exitWeather_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeather_type" ):
                return visitor.visitWeather_type(self)
            else:
                return visitor.visitChildren(self)




    def weather_type(self):

        localctx = CommandsParser.Weather_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_weather_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 17042430230528) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self, i:int=None):
            if i is None:
                return self.getTokens(CommandsParser.NUM_INT)
            else:
                return self.getToken(CommandsParser.NUM_INT, i)

        def NAME(self):
            return self.getToken(CommandsParser.NAME, 0)

        def getRuleIndex(self):
            return CommandsParser.RULE_tp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTp" ):
                listener.enterTp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTp" ):
                listener.exitTp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTp" ):
                return visitor.visitTp(self)
            else:
                return visitor.visitChildren(self)




    def tp(self):

        localctx = CommandsParser.TpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_tp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(CommandsParser.T__43)
            self.state = 94
            _la = self._input.LA(1)
            if not(_la==11 or _la==52):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 95
            self.match(CommandsParser.NUM_INT)
            self.state = 96
            self.match(CommandsParser.NUM_INT)
            self.state = 97
            self.match(CommandsParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DifficultyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def difficulty_level(self):
            return self.getTypedRuleContext(CommandsParser.Difficulty_levelContext,0)


        def getRuleIndex(self):
            return CommandsParser.RULE_difficulty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifficulty" ):
                listener.enterDifficulty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifficulty" ):
                listener.exitDifficulty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifficulty" ):
                return visitor.visitDifficulty(self)
            else:
                return visitor.visitChildren(self)




    def difficulty(self):

        localctx = CommandsParser.DifficultyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_difficulty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CommandsParser.T__44)
            self.state = 100
            self.difficulty_level()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Difficulty_levelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CommandsParser.RULE_difficulty_level

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDifficulty_level" ):
                listener.enterDifficulty_level(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDifficulty_level" ):
                listener.exitDifficulty_level(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDifficulty_level" ):
                return visitor.visitDifficulty_level(self)
            else:
                return visitor.visitChildren(self)




    def difficulty_level(self):

        localctx = CommandsParser.Difficulty_levelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_difficulty_level)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 1055531162664960) != 0):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





