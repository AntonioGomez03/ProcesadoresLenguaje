grammar gec_parser;

options {
	tokenVocab = gec_lexer;
}
@parser::header {
from parser.symbol_table import SymbolTable
from parser.gec_objects import GameObject, Chunk, Scene, World
import json
}

@parser::members {
def on_programa_start(self):
    self.symbol_table = SymbolTable()

def on_programa_end(self, world, path):
	print("Fin del programa\n")
	print(self.symbol_table)
	# Crear un json con las escenas
	print(world.get_scenes())
	world_json = world.to_dict()
	with open(path, 'w') as file:
		json.dump(world_json, file, indent=4)


def eval_expression(self,values,operators=None):
    result = values[0]
    for i,op in enumerate(operators):
        result = self._eval_single_expression([result,values[i+1]],op)
    return result
        
def _eval_single_expression(self,values, operator):
    match operator:
        case '+' :
            return values[0] + values[1]
        case '-' :
            return values[0] - values[1]
        case '*' :
            return values[0] * values[1]
        case '*' :
            return values[0] / values[1]
        case _:
            raise ValueError("Operador no existe")

def is_add_statement(self, statement):
    return statement.text == "add"

def get_type(self,object):
    if isinstance(object, int):
        return "INT"
    elif isinstance(object, float):
        return "FLOAT"
    elif isinstance(object, str):
        return "STRING"
    elif isinstance(object, Chunk):
        return "CHUNK"
    elif isinstance(object, GameObject):
        return "GAMEOBJECT"
    elif isinstance(object, Scene):
        return "SCENE"
    elif isinstance(object, World):
        return "WORLD"
    else:
        return "UNKNOWN"
}

//////////////////////////////////////////////
// PARSER RULES // ////////////////////////////////////////////

program:
	{self.on_programa_start()} define_setup define_world EOF {
print("world", $define_world.world.get_scenes())
self.on_programa_end($define_world.world,"World.json")
    };

define_setup:
	DEFINE SETUP LPAREN RPAREN LBRACE statement* RBRACE;

define_world
	returns[World world]:
	DEFINE WORLD LPAREN (STRING_LITERAL | ID) {

temp_name = self._input.LT(-1).text
if temp_name.startswith('"') and temp_name.endswith('"'):
    temp_name = temp_name[1:-1]
else:
    temp_name = self.symbol_table.get_value(temp_name)

$world = World(temp_name)

    } RPAREN LBRACE scenes += define_scene* RBRACE {
for scene in $scenes:
    $world.add_scene(scene.scene)
    };

define_scene
	returns[Scene scene]:
	DEFINE SCENE LPAREN (STRING_LITERAL | ID) {

temp_name = self._input.LT(-1).text
if temp_name.startswith('"') and temp_name.endswith('"'):
    temp_name = temp_name[1:-1]
else:
    temp_name = self.symbol_table.get_value(temp_name)

    } COMMA (INT_LITERAL | ID) {

temp_width_chunk = self._input.LT(-1).text  
if temp_width_chunk.isdigit():
    temp_width_chunk = int(temp_width_chunk)
else:
    temp_width_chunk = int(self.symbol_table.get_value(temp_width_chunk))

    } COMMA (INT_LITERAL | ID) {

temp_length_chunk = self._input.LT(-1).text
if temp_length_chunk.isdigit():
    temp_length_chunk = int(temp_length_chunk)
else:
    temp_length_chunk = int(self.symbol_table.get_value(temp_length_chunk))

    } RPAREN {
$scene = Scene(temp_name, temp_width_chunk, temp_length_chunk)
    } LBRACE statements += statement* {   
for stmt in $statements: 
    if isinstance(stmt.value, Chunk): 
        $scene.add_chunk(stmt.value)
    } RBRACE {
    };

statement
	returns[any value]:
	assignment
	| define_list
	| append_statement
	| for_loop_number
	| for_loop_list
	| declaration
	| add_statement {
$value = $add_statement.chunk
    };

chunk_constructor
	returns[Chunk chunk]:
	CHUNK LPAREN (ID | INT_LITERAL) {

temp_pos_x = self._input.LT(-1).text
if temp_pos_x.isdigit():
    temp_pos_x = int(temp_pos_x)
else:  
    temp_pos_x = int(self.symbol_table.get_value(temp_pos_x))

} COMMA (ID | INT_LITERAL) {
    
temp_pos_y = self._input.LT(-1).text
if temp_pos_y.isdigit():
    temp_pos_y = int(temp_pos_y)
else:  
    temp_pos_y = int(self.symbol_table.get_value(temp_pos_y))

} COMMA (ID | FLOAT_LITERAL) {

temp_scale = self._input.LT(-1).text
if temp_scale.replace(".","",1).isdigit():
    temp_scale = float(temp_scale)
else:  
    temp_scale = float(self.symbol_table.get_value(temp_scale))

} COMMA (ID | FLOAT_LITERAL) {

temp_height_multiplier = self._input.LT(-1).text
if temp_height_multiplier.replace(".","",1).isdigit():
    temp_height_multiplier = float(temp_height_multiplier)
else:  
    temp_height_multiplier = float(self.symbol_table.get_value(temp_height_multiplier))
    
} COMMA (ID | STRING_LITERAL) {

temp_texture = self._input.LT(-1).text
if temp_texture.startswith('"') and temp_texture.endswith('"'):
    temp_texture = temp_texture[1:-1]
else:
    temp_texture = self.symbol_table.get_value(temp_texture)

} COMMA (ID) {
temp_game_objects = self._input.LT(-1).text
temp_game_objects = self.symbol_table.get_value(temp_game_objects)

} RPAREN {
$chunk = Chunk(temp_pos_x, temp_pos_y, temp_scale, temp_height_multiplier, temp_texture, temp_game_objects)
    };

gameobject_constructor
	returns[GameObject gameobject]:
	GAMEOBJECT LPAREN (ID | STRING_LITERAL) {

temp_model = self._input.LT(-1).text
if temp_model.startswith('"') and temp_model.endswith('"'):
    temp_model = temp_model[1:-1]
else:
    temp_model = self.symbol_table.get_value(temp_model)

} COMMA (ID | INT_LITERAL) {
    
temp_density = self._input.LT(-1).text
if temp_density.isdigit():
    temp_density = int(temp_density)
else:  
    temp_density = int(self.symbol_table.get_value(temp_density))
    
} COMMA (ID | FLOAT_LITERAL) {
    
temp_min_scale = self._input.LT(-1).text
if temp_min_scale.replace(".","",1).isdigit():
    temp_min_scale = float(temp_min_scale)
else:  
    temp_min_scale = float(self.symbol_table.get_value(temp_min_scale))
    
} COMMA (ID | FLOAT_LITERAL) {
    
temp_max_scale = self._input.LT(-1).text
if temp_max_scale.replace(".","",1).isdigit():
    temp_max_scale = float(temp_max_scale)
else:  
    temp_max_scale = float(self.symbol_table.get_value(temp_max_scale))
    
} RPAREN {
$gameobject = GameObject(temp_model, temp_density, temp_min_scale, temp_max_scale)
}
	| GAMEOBJECT LPAREN (ID | STRING_LITERAL) {
    
temp_model = self._input.LT(-1).text
if temp_model.startswith('"') and temp_model.endswith('"'):
    temp_model = temp_model[1:-1]
else:
    temp_model = self.symbol_table.get_value(temp_model)
    
} COMMA (ID | INT_LITERAL) {
    
temp_density = self._input.LT(-1).text
if temp_density.isdigit():
    temp_density = int(temp_density)
else:  
    temp_density = int(self.symbol_table.get_value(temp_density))
    
} COMMA (ID | FLOAT_LITERAL) {
    
temp_scale = self._input.LT(-1).text
if temp_scale.replace(".","",1).isdigit():
    temp_scale = float(temp_scale)
else:  
    temp_scale = float(self.symbol_table.get_value(temp_scale))
    
} RPAREN {
$gameobject = GameObject(temp_model, temp_density, temp_scale)
};

define_list: (LIST LT (CHUNK | GAMEOBJECT) {type = self._input.LT(-1).text} GT |) ID ASSIGN array {
self.symbol_table.set_value($ID.text, $array.object_list, "LIST<" + type + ">", "Contexto")
};

array
	returns[any object_list]:
	LSQUARE (
		ID {$object_list = [self.symbol_table.get_value(self._input.LT(-1).text)]}
		| chunk_constructor {$object_list = [chunk_constructor.chunk]}
		| gameobject_constructor {$object_list = [gameobject_constructor.gameobject]}
	) (
		COMMA (
			ID {$object_list.append(self.symbol_table.get_value(self._input.LT(-1).text))}
			| chunk_constructor {$object_list.append(chunk_constructor.chunk)}
			| gameobject_constructor {$object_list.append(gameobject_constructor.gameobject)}
		)
	)* RSQUARE
	| LSQUARE RSQUARE;

append_statement:
	APPEND ID {object_list_id = self._input.LT(-1).text} (
		ID
		| gameobject_constructor
		| chunk_constructor
	) { 
# print("Toma", object_list_id)
if self._input.LT(-8).text == "GAMEOBJECT" or self._input.LT(-9).text == "GAMEOBJECT":
    temp_object = $gameobject_constructor.gameobject
elif self._input.LT(-8).text == "CHUNK":
    temp_object = $chunk_constructor.chunk
else:
    temp_object = self.symbol_table.get_value(self._input.LT(-1).text)

object_list = self.symbol_table.get_value(object_list_id)
object_list.append(temp_object)
# self.symbol_table.set_value(object_list_id, object_list, "LIST<" + self.get_type(temp_object) + ">", "Contexto")
};

add_statement
	returns[Chunk chunk]:
	(ADD ID | ADD chunk_constructor) {

temp_chunk = self._input.LT(-1).text
if isinstance(temp_chunk, Chunk):
    temp_chunk = temp_chunk
else:
    temp_chunk = self.symbol_table.get_value(temp_chunk)
$chunk = temp_chunk
    };

for_loop_number:
	FOR ID {id = self._input.LT(-1).text} FROM INT_LITERAL {start = int(self._input.LT(-1).text)} TO
		INT_LITERAL {end = int(self._input.LT(-1).text) } {
print("FOR", id, start, end)
for i in range(start, end + 1):
    self.symbol_table.set_value(id, i, "INT", "Contexto")
    for stmt in $statements:
        pass
    } LBRACE statements += statement* RBRACE;

for_loop_list:
	FOR ID {id = self._input.LT(-1).text} IN ID {list_id = self._input.LT(-1).text} LBRACE
		statements += statement* RBRACE;

assignment:
	(INT | STRING | FLOAT |) ID {id = self._input.LT(-1).text } ASSIGN expression {
self.symbol_table.set_value(id, $expression.value, self.get_type($expression.value), "Contexto")
    }
	| (CHUNK |) ID {id = self._input.LT(-1).text } ASSIGN chunk_constructor {
self.symbol_table.set_value(id, $chunk_constructor.chunk, "CHUNK", "Contexto")
    }
	| (GAMEOBJECT |) ID {id = self._input.LT(-1).text } ASSIGN gameobject_constructor { 
self.symbol_table.set_value(id, $gameobject_constructor.gameobject, "GAMEOBJECT", "Contexto")
    };

expression
	returns[any value]:
	e1 = expression_aux {
values = [$e1.value]
operators = []
        } (
		op = OP_ARIT e2 = expression_aux {
values.append($e2.value)
operators.append($op.text)
        }
	)* {
$value = self.eval_expression(values, operators)
    };

expression_aux
	returns[any value]:
	STRING_LITERAL { 
$value = self._input.LT(-1).text
    }
	| INT_LITERAL {
$value = int(self._input.LT(-1).text)
    }
	| FLOAT_LITERAL {
$value = float(self._input.LT(-1).text)
    }
	| ID {
$value = self._input.LT(-1).text
    }
	| LPAREN expression RPAREN {
$value = $expression.value
    };

declaration: (
		INT {type = self._input.LT(-1).text}
		| STRING {type = self._input.LT(-1).text}
		| FLOAT {type = self._input.LT(-1).text}
		| CHUNK {type = self._input.LT(-1).text}
		| GAMEOBJECT {type = self._input.LT(-1).text}
		| LIST LT (CHUNK | GAMEOBJECT) GT {
type = "LIST<" + self._input.LT(-2).text + ">"}
	) ID {id = self._input.LT(-1).text} {
self.symbol_table.set_value(id, [], type, "Contexto")
    };