import json



def main():
    # Cargar archivo JSON 
    with open('examples/lenguaje_intermedio.json', 'r') as file:
        data = json.load(file)
    
    # Nombre del mundo
    world_name = data["world"]["name"]

    # Iterar sobre cada escena
    for scene in data["world"]["scenes"]:
        generate_script(scene)





# Método para generar el script de cada escena
def generate_script(scene):
    scene_name = scene["name"]
    width_chunk = scene["width_chunk"]
    length_chunk = scene["length_chunk"]
    cs_output_path = f'{scene_name}.cs'

    # Crear el contenido del script C#
    cs_content = f"""using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

public class {scene["name"]} : MonoBehaviour {{

    public List<GameObject> chunk_list = new List<GameObject>();
    public List<int> pos_x_list = new List<int>();
    public List<int> pos_y_list = new List<int>();
    public unirTerrenosScript unirTerrenosScript;


    void Start() {{
"""
    
    # Generar el código para cada chunk en la escena
    for chunk in scene["chunks"]:
        # Sacamos los datos del chunk
        pos_x = chunk["pos_x"] * width_chunk * 10
        pos_y = chunk["pos_y"] * length_chunk * 10
        scale = chunk["scale"]
        height_multiplier = chunk["height_multiplier"]
        texture_path = chunk["texture"]

        cs_content += f"""
        // Crear nuevo chunk
        GameObject chunk_{pos_x}_{pos_y} = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_{pos_x}_{pos_y}.transform.position = new Vector3({pos_x}f, 0f, {pos_y}f);
        chunk_{pos_x}_{pos_y}.transform.localScale = new Vector3({width_chunk}f, 1f, {length_chunk}f);
        chunk_{pos_x}_{pos_y}.name = "Chunk_{scene_name}_{pos_x}_{pos_y}";

        // Añadir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_{pos_x}_{pos_y});
        pos_x_list.Add({pos_x})
        pos_y_list.Add({pos_y});

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_{pos_x}_{pos_y} = chunk_{pos_x}_{pos_y}.AddComponent<SimpleTerrainGenerator>();
        terrainGen_{pos_x}_{pos_y}._filter = chunk_{pos_x}_{pos_y}.GetComponent<MeshFilter>();
        terrainGen_{pos_x}_{pos_y}.scale = {scale}f;
        terrainGen_{pos_x}_{pos_y}.heightMultiplier = {height_multiplier}f;

        // Asignar textura al chunk, si existe
        Material material_{pos_x}_{pos_y} = AssetDatabase.LoadAssetAtPath<Material>("{texture_path}.mtlx");
        if (material_{pos_x}_{pos_y} != null)
        {{
            chunk_{pos_x}_{pos_y}.GetComponent<Renderer>().material = material_{pos_x}_{pos_y};
        }}
        else
        {{
            Debug.LogWarning("Textura {texture_path}.mat no encontrado.");
        }}

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_{pos_x}_{pos_y});
        pos_x_list.Add({chunk["pos_x"]});
        pos_y_list.Add({chunk["pos_y"]});
"""

        # Generar el código para cada gameobject en el chunk
        for gameobject in chunk["gameobjects"]:
                model = gameobject["model"]
                density = gameobject["density"]

                # Verificar si el gameobject tiene `scale` o `min_scale` y `max_scale`
                if "scale" in gameobject:
                    gameobject_scale = gameobject["scale"]

                elif "min_scale" in gameobject and "max_scale" in gameobject:
                    min_scale = gameobject["min_scale"]
                    max_scale = gameobject["max_scale"]

    # Suavizar corte entre los chunks
    cs_content += """
        // Crear un objeto vacío en la escena
        GameObject emptyObject = new GameObject("UnirTerrenosManager");

        // Añadir el script unirTerrenosScript al objeto vacío
        unirTerrenosScript unir_terrenos = emptyObject.AddComponent<unirTerrenosScript>();
        unir_terrenos.chunk_list = chunk_list;
        unir_terrenos.pos_x_list = pos_x_list;
        unir_terrenos.pos_y_list = pos_y_list;
    }
}
    """

    # Guardar el contenido en un archivo .cs
    with open(cs_output_path, 'w') as file:
        file.write(cs_content)

    # ñenguele, ma
if __name__ == "__main__":
    main()