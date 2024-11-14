using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

public class Forest : MonoBehaviour {

    public List<GameObject> chunk_list = new List<GameObject>();
    public List<int> pos_x_list = new List<int>();
    public List<int> pos_y_list = new List<int>();

    void Start() {

        // Crear nuevo chunk
        GameObject chunk_0_0 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_0_0.transform.position = new Vector3(0f, 0f, 0f);
        chunk_0_0.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_0_0.name = "Chunk_Forest_0_0";

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_0_0 = chunk_0_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_0_0._filter = chunk_0_0.GetComponent<MeshFilter>();
        terrainGen_0_0.scale = 4f;
        terrainGen_0_0.heightMultiplier = 70f;

        // Asignar textura al chunk, si existe
        Material material_0_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/rojo.mat");
        if (material_0_0 != null)
        {
            chunk_0_0.GetComponent<Renderer>().material = material_0_0;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/rojo.mat no encontrado.");
        }

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_0_0);
        pos_x_list.Add(0);
        pos_y_list.Add(0);

        // Crear nuevo chunk
        GameObject chunk_100_0 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_100_0.transform.position = new Vector3(100f, 0f, 0f);
        chunk_100_0.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_100_0.name = "Chunk_Forest_100_0";

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_0 = chunk_100_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_0._filter = chunk_100_0.GetComponent<MeshFilter>();
        terrainGen_100_0.scale = 2f;
        terrainGen_100_0.heightMultiplier = 20f;

        // Asignar textura al chunk, si existe
        Material material_100_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/rojo.mat");
        if (material_100_0 != null)
        {
            chunk_100_0.GetComponent<Renderer>().material = material_100_0;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/rojo.mat no encontrado.");
        }

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_100_0);
        pos_x_list.Add(1);
        pos_y_list.Add(0);

        // Crear nuevo chunk
        GameObject chunk_100_100 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_100_100.transform.position = new Vector3(100f, 0f, 100f);
        chunk_100_100.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_100_100.name = "Chunk_Forest_100_100";

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_100 = chunk_100_100.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_100._filter = chunk_100_100.GetComponent<MeshFilter>();
        terrainGen_100_100.scale = 4f;
        terrainGen_100_100.heightMultiplier = 80f;

        // Asignar textura al chunk, si existe
        Material material_100_100 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/rojo.mat");
        if (material_100_100 != null)
        {
            chunk_100_100.GetComponent<Renderer>().material = material_100_100;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/rojo.mat no encontrado.");
        }

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_100_100);
        pos_x_list.Add(1);
        pos_y_list.Add(1);

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
    