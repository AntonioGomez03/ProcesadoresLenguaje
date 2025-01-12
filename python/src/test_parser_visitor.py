import sys, json
from antlr4 import *
# Importa tu lexer y parser generados
from lexer.gec_lexer import (
    gec_lexer as Lexer,
)  # Cambia "Lexer" por el nombre real
from parser.gec_parserParser import (
    gec_parserParser as Parser,
)  # Cambia "Parser" por el nombre real
from parser.gec_parserVisitor import gec_parserVisitor as Visitor
from parser.gec_objects import Chunk, GameObject, Scene, World

# Tabla de símbolos
class SymbolTable:
    def __init__(self):
        self.table = {}

    def set_value(self, name, value, type_key, context):
        self.table[name] = {"value": value, "type": type_key, "context": context}

    def get_value(self, name, context=None):
        # TODO: Filter by other criteria
        if name in self.table:
            # Check if the context is the same
            if context is not None:
                if self.table[name]["context"] == "SETUP" or self.table[name]["context"] == context:
                    return self.table[name]["value"]
                raise ValueError(f"Variable '{name}' no definida en el contexto actual.")
        raise ValueError(f"Variable '{name}' no definida.")
    
    def get_type(self, name):
        if name in self.table:
            return self.table[name]["type"]
        raise ValueError(f"Variable '{name}' no definida.")

    def __str__(self):
        return str(self.table)


def eval_expression(values, operators=None):
    result = values[0]
    for i, op in enumerate(operators):
        result = _eval_single_expression([result, values[i+1]], op)
    return result
        
def _eval_single_expression(values, operator):
    match operator:
        case '+':
            return values[0] + values[1]
        case '-':
            return values[0] - values[1]
        case '*':
            return values[0] * values[1]
        case '*':
            return values[0] / values[1]
        case _:
            raise ValueError("Operador no existe")

def world_to_json(world, path):
    world_json = world.to_dict()
    with open(path, 'w') as file:
        json.dump(world_json, file, indent=4)

class MyCustomVisitor(Visitor):
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.context = "Context"

    def visitProgram(self, ctx):
            self.symbol_table = SymbolTable()
            for child in ctx.children:
                self.visit(child)
            # Optionally handle output or final steps here
            print(self.symbol_table, "\n")
            world = self.symbol_table.get_value("World", self.context)
            world_to_json(world, "world.json")

    def visitDefine_setup(self, ctx):
        self.context = "SETUP"
        for c in ctx.statement():
            self.visit(c)

    def visitDefine_world(self, ctx):
        self.context = "WORLD"
        w_name = ctx.getChild(3).getText()
        if isinstance(w_name, str) and len(w_name) > 1 and w_name[0] == '"' and w_name[-1] == '"':
            w_name = w_name[1:-1]
        else:
            w_name = self.symbol_table.get_value(w_name, self.context)
        world_obj = World(w_name)
        for sc in ctx.define_scene():
            s = self.visit(sc)
            if s:
                world_obj.add_scene(s)
        # Store or keep reference as needed
        self.symbol_table.set_value("World", world_obj, "WORLD", self.context)

    def visitDefine_scene(self, ctx):
        s_name = ctx.getChild(3).getText()
        self.context = s_name
        if isinstance(s_name, str) and len(s_name) > 1 and s_name[0] == '"' and s_name[-1] == '"':
            s_name = s_name[1:-1]
        else:
            s_name = self.symbol_table.get_value(s_name, self.context)
        
        width_chunk = ctx.getChild(5).getText()
        if isinstance(width_chunk, str) and len(width_chunk) > 1 and width_chunk[0] == '"' and width_chunk[-1] == '"':
            width_chunk = width_chunk[1:-1]
        else:
            width_chunk = self.symbol_table.get_value(width_chunk, self.context)
                                                      
        height_chunk = ctx.getChild(7).getText()
        if isinstance(height_chunk, str) and len(height_chunk) > 1 and height_chunk[0] == '"' and height_chunk[-1] == '"':
            height_chunk = height_chunk[1:-1]
        else:
            height_chunk = self.symbol_table.get_value(height_chunk,  self.context)

        scene = Scene(s_name, width_chunk, height_chunk)
        for c in ctx.statement():
            s = self.visit(c)
            # Check if type is list
            if isinstance(s,list):
                scene.add_chunks(s)
            elif s:
                scene.add_chunk(s)                
        self.symbol_table.set_value(s_name, scene, "SCENE", self.context)
        return scene                
        
    def visitStatement(self, ctx):
        for c in ctx.children:
            val = self.visit(c)
            if val is not None:
                return val

    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        val = self.visit(ctx.expression()) if ctx.expression() else None
        if val is None:
            if ctx.chunk_constructor():
                val = self.visit(ctx.chunk_constructor())
                self.symbol_table.set_value(name, val, "CHUNK", self.context)
            elif ctx.gameobject_constructor():
                val = self.visit(ctx.gameobject_constructor())
                self.symbol_table.set_value(name, val, "GAMEOBJECT", self.context)
        else:
            self.symbol_table.set_value(name, val, self.get_type(val), self.context)

    def visitDefine_list(self, ctx):
        arr = self.visit(ctx.array())
        ty = "LIST<" + ctx.getChild(2).getText() + ">"
        self.symbol_table.set_value(ctx.ID().getText(), arr, ty, self.context)

    def visitAppend_statement(self, ctx):
        list_name = ctx.ID(0).getText()
        elem = None
        elem_type = None
        if ctx.gameobject_constructor():
            elem = self.visit(ctx.gameobject_constructor())
            elem_type = "GAMEOBJECT"
        elif ctx.chunk_constructor():
            elem = self.visit(ctx.chunk_constructor())
            elem_type = "CHUNK"
        else: 
            elem = self.symbol_table.get_value(ctx.ID(1).getText(), self.context)
            elem_type = self.symbol_table.get_type(ctx.ID(1).getText())
        lst = self.symbol_table.get_value(list_name, self.context)
        ty = self.symbol_table.get_type(list_name)
        if elem_type in ty:
            lst.append(elem)
        else:
            raise ValueError(f"El tipo de la lista {list_name} no coincide con el tipo del elemento a agregar.")
        self.symbol_table.set_value(list_name, lst, ty, self.context)

    def visitFor_loop_number(self, ctx):
        # Simplified approach
        var_name = ctx.ID().getText()
        start = int(ctx.INT_LITERAL(0).getText())
        end = int(ctx.INT_LITERAL(1).getText())
        statements = ctx.statement()
        result = []
        for i in range(start, end + 1):
            self.symbol_table.set_value(var_name, i, "INT", self.context)
            for st in statements:
                s = self.visit(st)
                result.append(s)
        result = [x for x in result if x is not None]
        return result


    def visitFor_loop_list(self, ctx):
        var_name = ctx.ID(0).getText()
        list_var = ctx.ID(1).getText()
        arr = self.symbol_table.get_value(list_var,  self.context)
        result = []
        for x in arr:
            self.symbol_table.set_value(var_name, x, self.get_type(x), self.context)
            for st in ctx.statement():
                s = self.visit(st)
                result.append(s)
        result = [x for x in result if x is not None]
        return result

    def visitDeclaration(self, ctx):
        tp = ctx.getChild(0).getText()
        if tp.startswith("LIST"):
            tp += "<" + ctx.getChild(2).getText() + ">"
        nm = ctx.ID().getText()
        self.symbol_table.set_value(nm, [], tp, self.context)

    def visitAdd_statement(self, ctx):
        temp = None
        if ctx.ID():
            temp = self.symbol_table.get_value(ctx.ID().getText(),  self.context)
        else:
            temp = self.visit(ctx.chunk_constructor())
        return temp

    def visitChunk_constructor(self, ctx):
        # Minimal extraction
        posx = self.visit(ctx.expression(0))
        if not isinstance(posx, int):
            raise ValueError("Posx debe ser un entero")
        
        posy = self.visit(ctx.expression(1))
        if not isinstance(posy, int):
            raise ValueError("Posy debe ser un entero")
        
        sc = self.visit(ctx.expression(2))
        if not isinstance(sc, float) and not isinstance(sc, int):
            raise ValueError("Scale debe ser un flotante")
        
        hm = self.visit(ctx.expression(3))
        if not isinstance(hm, float) and not isinstance(hm, int):
            raise ValueError("Height_multiplier debe ser un entero")
        
        tx = self.visit(ctx.expression(4))
        if not isinstance(tx, str):
            raise ValueError("Texture debe ser un string")
        
        objs = self.symbol_table.get_value(ctx.ID().getText(), self.context)
        if not isinstance(objs, list):
            raise ValueError("GameObjects debe ser una lista")
        return Chunk(posx, posy, sc, hm, tx, objs)

    def visitGameobject_constructor(self, ctx):
        # Minimal approach for variations
        model = self.visit(ctx.expression(0))
        if not isinstance(model, str):
            raise ValueError("Modelo debe ser un string")
        
        density = self.visit(ctx.expression(1))
        if not isinstance(density, float) and not isinstance(density, int):
            raise ValueError("Density debe ser un flotante")
        
        if ctx.getChildCount() == 9:
            min_s = self.visit(ctx.expression(2))
            if not isinstance(min_s, float) and not isinstance(min_s, int):
                raise ValueError("Min_scale debe ser un flotante")
            
            max_s = self.visit(ctx.expression(3))
            if not isinstance(max_s, float) and not isinstance(max_s, int):
                raise ValueError("Max_scale debe ser un flotante")
            
            return GameObject(model, density, min_s, max_s)
        else:
            scale = self.visit(ctx.expression(2))
            if not isinstance(scale, float) and not isinstance(scale, int):
                raise ValueError("Scale debe ser un flotante")
            
            return GameObject(model, density, scale)

    def visitArray(self, ctx):
        out = []
        if ctx.getChildCount() > 2:
            for i in range(1, ctx.getChildCount() - 1, 2):
                try:
                    out.append(self.symbol_table.get_value(ctx.getChild(i).getText(), self.context))
                except:
                    out.append(self.visit(ctx.getChild(i)))

        return out

    def visitExpression(self, ctx):
        vals = []
        ops = []
        for i in range(0, ctx.getChildCount()):
            node = ctx.getChild(i)
            if i % 2 == 0:
                vals.append(self.visit(node))
            else:
                ops.append(node.getText())
        return eval_expression(vals, ops)

    def visitExpression_aux(self, ctx):
        child = ctx.getChild(0)
        e = self.visit(child)
        if e is None:
            return self.visit(ctx.expression())
        return e
    
    def visitNumeric_expression(self, ctx):
        child = ctx.getChild(0)
        if child.getText().isdigit():
            return int(child.getText())
        try:
            return float(child.getText())
        except ValueError:
            pass
        return self.symbol_table.get_value(child.getText(), self.context)
    
    def visitString_expression(self, ctx):
        child = ctx.getChild(0)
        if child.getText().startswith('"'):
            return child.getText()[1:-1]
        return self.symbol_table.get_value(child.getText(), self.context)

    def _extract_value(self, node):
        t = node.getText()
        if t.startswith('"') and t.endswith('"'):
            return t[1:-1]
        try:
            return int(t)
        except:
            pass
        try:
            return float(t)
        except:
            pass
        return self.symbol_table.get_value(t, self.context)

    def get_type(self, obj):
        if isinstance(obj, int):
            return "INT"
        if isinstance(obj, float):
            return "FLOAT"
        if isinstance(obj, str):
            return "STRING"
        if isinstance(obj, Chunk):
            return "CHUNK"
        if isinstance(obj, GameObject):
            return "GAMEOBJECT"
        if isinstance(obj, Scene):
            return "SCENE"
        if isinstance(obj, World):
            return "WORLD"
        return "UNKNOWN"

def main(input_file):
    input_stream = FileStream(input_file, encoding="utf-8")
    lexer = Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Parser(token_stream)
    tree = parser.program()

    visitor = MyCustomVisitor()
    visitor.visit(tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python prueba_grammar.py <archivo_entrada>")
    else:
        main(sys.argv[1])
