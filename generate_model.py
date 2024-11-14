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

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_{pos_x}_{pos_y} = chunk_{pos_x}_{pos_y}.AddComponent<SimpleTerrainGenerator>();
        terrainGen_{pos_x}_{pos_y}._filter = chunk_{pos_x}_{pos_y}.GetComponent<MeshFilter>();
        terrainGen_{pos_x}_{pos_y}.scale = {scale}f;
        terrainGen_{pos_x}_{pos_y}.heightMultiplier = {height_multiplier}f;

        // Asignar textura al chunk, si existe
        Material material_{pos_x}_{pos_y} = AssetDatabase.LoadAssetAtPath<Material>("{texture_path}.mat");
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

            


    # Suavizar corte entre los chunks#
    cs_content += """
        // Ajuste de alturas en los bordes de los chunks
        for (int i = 0; i < chunk_list.Count; i++)
        {
            for (int e = i + 1; e < chunk_list.Count; e++){
                if (i != e)
                {
                    // Posiciones relativas
                    int pos_x_i = pos_x_list[i];
                    int pos_y_i = pos_y_list[i];
                    int pos_x_e = pos_x_list[e];
                    int pos_y_e = pos_y_list[e];

                    // Comprobar si son vecinos en el vértice (vertex neighbors)
                    bool areVertexNeighbors = Mathf.Abs(pos_x_i - pos_x_e) == 1 && Mathf.Abs(pos_y_i - pos_y_e) == 1;

                    // Comprobar si son vecinos en el borde (edge neighbors)
                    bool areEdgeNeighbors = false;
                    string edgeType = "";
                    // Vecino al Este/Oeste (misma fila, posiciones X diferentes)
                    if (pos_y_i == pos_y_e && Mathf.Abs(pos_x_i - pos_x_e) == 1)
                    {
                        areEdgeNeighbors = true;
                        edgeType = (pos_x_i < pos_x_e) ? "Este" : "Oeste";
                    }
                    // Vecino al Norte/Sur (misma columna, posiciones Y diferentes)
                    else if (pos_x_i == pos_x_e && Mathf.Abs(pos_y_i - pos_y_e) == 1)
                    {
                        areEdgeNeighbors = true;
                        edgeType = (pos_y_i < pos_y_e) ? "Norte" : "Sur";
                    }

                    // Procesamiento si son vecinos por arista
                    if (areEdgeNeighbors)
                    {
                        // Debug.Log($"Chunks {i} y {e} son vecinos en el borde.{edgeType}"); -- pruebas

                        // Mesh de cada chunk
                        Mesh mesh_i = chunk_list[i].GetComponent<MeshFilter>().mesh;
                        Mesh mesh_e = chunk_list[e].GetComponent<MeshFilter>().mesh;

                        // ME HE QUEDADO POR AQUI..., TODO GENIAL..., PERO ESTO HAY QUE REVISARLO :) 

                    }

                    // Procesamiento si son vecinos por vértice
                    if (areVertexNeighbors)
                    {
                        // Debug.Log($"Chunks {i} y {e} son vecinos en el vértice."); -- pruebas
                    }
                }
            }
        }
    }
}
    """

    # Guardar el contenido en un archivo .cs
    with open(cs_output_path, 'w') as file:
        file.write(cs_content)

    # ñenguele, ma
if __name__ == "__main__":
    main()