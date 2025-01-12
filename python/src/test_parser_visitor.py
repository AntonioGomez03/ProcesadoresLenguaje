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

    def get_value(self, name):
        # TODO: Filter by other criteria
        if name in self.table:
            return self.table[name]["value"]
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

    def visitProgram(self, ctx):
            self.symbol_table = SymbolTable()
            for child in ctx.children:
                self.visit(child)
            # Optionally handle output or final steps here
            print(self.symbol_table, "\n")
            world = self.symbol_table.get_value("Mi Mundo")
            world_to_json(world, "world.json")

    def visitDefine_setup(self, ctx):
        for c in ctx.statement():
            self.visit(c)

    def visitDefine_world(self, ctx):
        w_name = ctx.getChild(3).getText()
        if isinstance(w_name, str) and len(w_name) > 1 and w_name[0] == '"' and w_name[-1] == '"':
            w_name = w_name[1:-1]
        else:
            w_name = self.symbol_table.get_value(w_name)
        world_obj = World(w_name)
        for sc in ctx.define_scene():
            s = self.visit(sc)
            if s:
                world_obj.add_scene(s)
        # Store or keep reference as needed
        self.symbol_table.set_value(w_name, world_obj, "WORLD", "Context")

    def visitDefine_scene(self, ctx):
        s_name = ctx.getChild(3).getText()
        if isinstance(s_name, str) and len(s_name) > 1 and s_name[0] == '"' and s_name[-1] == '"':
            s_name = s_name[1:-1]
        else:
            s_name = self.symbol_table.get_value(s_name)
        
        width_chunk = ctx.getChild(5).getText()
        if isinstance(width_chunk, str) and len(width_chunk) > 1 and width_chunk[0] == '"' and width_chunk[-1] == '"':
            width_chunk = width_chunk[1:-1]
        else:
            width_chunk = self.symbol_table.get_value(width_chunk)
                                                      
        height_chunk = ctx.getChild(7).getText()
        if isinstance(height_chunk, str) and len(height_chunk) > 1 and height_chunk[0] == '"' and height_chunk[-1] == '"':
            height_chunk = height_chunk[1:-1]
        else:
            height_chunk = self.symbol_table.get_value(height_chunk)

        scene = Scene(s_name, width_chunk, height_chunk)
        for c in ctx.statement():
            s = self.visit(c)
            # Check if type is list
            if isinstance(s,list):
                scene.add_chunks(s)
            elif s:
                scene.add_chunk(s)                
        self.symbol_table.set_value(s_name, scene, "SCENE", "Context")
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
                self.symbol_table.set_value(name, val, "CHUNK", "Context")
            elif ctx.gameobject_constructor():
                val = self.visit(ctx.gameobject_constructor())
                self.symbol_table.set_value(name, val, "GAMEOBJECT", "Context")
        else:
            self.symbol_table.set_value(name, val, self.get_type(val), "Context")

    def visitDefine_list(self, ctx):
        arr = self.visit(ctx.array())
        ty = "LIST"
        self.symbol_table.set_value(ctx.ID().getText(), arr, ty, "Context")

    def visitAppend_statement(self, ctx):
        list_name = ctx.ID(0).getText()
        elem = None
        if ctx.gameobject_constructor():
            elem = self.visit(ctx.gameobject_constructor())
        elif ctx.chunk_constructor():
            elem = self.visit(ctx.chunk_constructor())
        else:
            elem = self.symbol_table.get_value(ctx.ID(1).getText())
        lst = self.symbol_table.get_value(list_name)
        lst.append(elem)
        self.symbol_table.set_value(list_name, lst, "LIST", "Context")

    def visitFor_loop_number(self, ctx):
        # Simplified approach
        var_name = ctx.ID().getText()
        start = int(ctx.INT_LITERAL(0).getText())
        end = int(ctx.INT_LITERAL(1).getText())
        statements = ctx.statement()
        result = []
        for i in range(start, end + 1):
            self.symbol_table.set_value(var_name, i, "INT", "Context")
            for st in statements:
                s = self.visit(st)
                result.append(s)
        result = [x for x in result if x is not None]
        return result


    def visitFor_loop_list(self, ctx):
        var_name = ctx.ID(0).getText()
        list_var = ctx.ID(1).getText()
        arr = self.symbol_table.get_value(list_var)
        result = []
        for x in arr:
            self.symbol_table.set_value(var_name, x, self.get_type(x), "Context")
            for st in ctx.statement():
                s = self.visit(st)
                result.append(s)
        result = [x for x in result if x is not None]
        return result

    def visitDeclaration(self, ctx):
        tp = ctx.getChild(0).getText()
        nm = ctx.ID().getText()
        self.symbol_table.set_value(nm, [], tp, "Context")

    def visitAdd_statement(self, ctx):
        temp = None
        if ctx.ID():
            temp = self.symbol_table.get_value(ctx.ID().getText())
        else:
            temp = self.visit(ctx.chunk_constructor())
        return temp

    def visitChunk_constructor(self, ctx):
        # Minimal extraction
        posx = self._extract_value(ctx.getChild(2))
        posy = self._extract_value(ctx.getChild(4))
        sc = self._extract_value(ctx.getChild(6))
        hm = self._extract_value(ctx.getChild(8))
        tx = self._extract_value(ctx.getChild(10))
        objs = self.symbol_table.get_value(ctx.getChild(12).getText())
        return Chunk(posx, posy, sc, hm, tx, objs)

    def visitGameobject_constructor(self, ctx):
        # Minimal approach for variations
        model = self._extract_value(ctx.getChild(2))
        density = self._extract_value(ctx.getChild(4))
        if ctx.getChildCount() == 9:
            min_s = self._extract_value(ctx.getChild(6))
            max_s = self._extract_value(ctx.getChild(8))
            return GameObject(model, density, min_s, max_s)
        else:
            scale = self._extract_value(ctx.getChild(6))
            return GameObject(model, density, scale)

    def visitArray(self, ctx):
        out = []
        if ctx.getChildCount() > 2:
            for i in range(1, ctx.getChildCount() - 1, 2):
                out.append(self._extract_value(ctx.getChild(i)))
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
        if child.getText().startswith('"'):
            return child.getText()
        if child.getText().isdigit():
            return int(child.getText())
        try:
            return float(child.getText())
        except ValueError:
            pass
        if child.getText() == '(':
            return self.visit(ctx.expression())
        return self.symbol_table.get_value(child.getText())

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
        return self.symbol_table.get_value(t)

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
