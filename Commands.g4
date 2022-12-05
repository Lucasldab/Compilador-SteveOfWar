grammar Commands;

// Lexer
NUM_INT 				: ('-')?('0'..'9')+;
NUM_REAL				: ('0'..'9')+ ('.' ('0'..'9')+)?;

NAME					: ('a'..'z') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

CADEIA 	: '\'' ( ESC_SEQ | ~('\''|'\\') )* '\'';
fragment ESC_SEQ: '\\\'';

// Ignorando espaços, tabulação, retorno e quebra de linha
WS  					:   ( ' ' | '\t' | '\r' | '\n') -> skip;

// Parser
//Programa é uma lista de comandos 
program:
  ('/'cmd)* EOF;

cmd:  summon | give | kill | gamemode | time_set | weather | tp | difficulty;

//summon funciona como uma "declaração de variável", instância entidades players e mobs
summon: 'summon' NAME (mob_type|'Player');

mob_type: 'Light Elf Slayers'|'Dark Elf Lords'| 'Tatzelwurms'| 'Exploding Nightmares' | 'Draugr Lords'| 'Revenant Hags';

//Give da itens a um player específico ou a todos os players, é passado o nome do player
//o item (que pode consistir de seu material  + nome) ou somente seu nome
//somente o nome e a quantidade de items
give: 'give' ('@a'|NAME) item NUM_INT;

item: item_material? item_name;

item_material:  'Iron'| 'Silver' | 'Bronze'| 'Gold' | 'Diamond';

item_name: 'Leviathan'|'Talon Bow'|'Mjolnir'|'Blade of Chaos'|'Guardian Shield'|'Gungnir'|'Chestplate'|'Leggings'|'Boots'|'Draupnir Spear' ;

//Elimina uma entidade, retira da tabela de entidades
kill: 'kill' NAME;

//Muda o modo de jogo,
gamemode: 'gamemode' NUM_INT;

//Muda o horario do jogo
time_set: 'time set' (time_string|NUM_INT);

time_string: 'day'|'noon'|'midday'|'sunset'|'dusk'|'midnight'|'sunrise'|'dawn';

//Muda o clima do jogo
weather: 'weather' weather_type;

weather_type: 'clear' | 'rain' | 'fimbulwinter' | 'ragnarok'| 'sand storm';

//Teleporta um player (ou todos os players) para uma posição específica a partir das coordenadas passads
tp: 'tp' (NAME|'@a') NUM_INT NUM_INT NUM_INT;

//modifica a dificuldade do jogo
difficulty: 'difficulty' difficulty_level;

difficulty_level: 'story' | 'grace' | 'balanced' | 'god of War';