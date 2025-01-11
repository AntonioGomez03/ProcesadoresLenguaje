import json

class GameObject:   
    def __init__(self, model: str, density: int, *args: float):
        self.model = model
        self.density = density

        if len(args) == 1:
            self.scale = args[0]
            self.min_scale = None
            self.max_scale = None
        else:
            self.scale = None
            self.min_scale = args[0]
            self.max_scale = args[1]
            
    def to_dict(self):
        data = {
            "model": self.model,
            "density": self.density
        }
        if self.scale is not None:
            data["scale"] = self.scale
        if self.min_scale is not None:
            data["min_scale"] = self.min_scale
        if self.max_scale is not None:
            data["max_scale"] = self.max_scale
        return data
    
class Chunk:
    def __init__(self, pos_x: int, pos_y: int, scale: float, height_multiplier: int, texture: str, game_objects: list):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scale = scale
        self.game_objects = game_objects
        self.height_multiplier = height_multiplier
        self.texture = texture

    def to_dict(self):
        return {
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "scale": self.scale,
            "height_multiplier": self.height_multiplier,
            "texture": self.texture,
            "gameobjects": [obj.to_dict() for obj in self.game_objects]
        }
    
class Scene:
    def __init__(self, name: str, width_chunk: int, length_chunk: int):
        self.name = name
        self.width_chunk = width_chunk
        self.length_chunk = length_chunk
        self.chunks = []

    def add_chunk(self, chunk: Chunk):
        self.chunks.append(chunk)

    def to_dict(self):
        return {
            "name": self.name,
            "width_chunk": self.width_chunk,
            "length_chunk": self.length_chunk,
            "chunks": [chunk.to_dict() for chunk in self.chunks]
        }
    def get_name(self):
        return self.name

    def get_chunks(self):
        return self.chunks
    

class World:
    def __init__(self, name: str):
        self.name = name
        self.scenes = []

    def add_scene(self, scene: Scene):
        self.scenes.append(scene)

    def get_scenes(self):
        return self.scenes

    def to_dict(self):
        return {
            "world": {
                "name": self.name,
                "scenes": [scene.to_dict() for scene in self.scenes]
            }
        }
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), indent=2)