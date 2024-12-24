using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

public class Forest : MonoBehaviour {

    public List<GameObject> chunk_list = new List<GameObject>();
    public List<int> pos_x_list = new List<int>();
    public List<int> pos_y_list = new List<int>();
    public unirTerrenosScript unirTerrenosScript;


    void Start() {

        // Crear nuevo chunk
        GameObject chunk_0_0 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_0_0.transform.position = new Vector3(0f, 0f, 0f);
        chunk_0_0.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_0_0.name = "Chunk_Forest_0_0";

        // A�adir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_0_0);
        pos_x_list.Add(0)
        pos_y_list.Add(0);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_0_0 = chunk_0_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_0_0._filter = chunk_0_0.GetComponent<MeshFilter>();
        terrainGen_0_0.scale = 4f;
        terrainGen_0_0.heightMultiplier = 70f;

        // Asignar textura al chunk, si existe
        Material material_0_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/grass.mtlx");
        if (material_0_0 != null)
        {
            chunk_0_0.GetComponent<Renderer>().material = material_0_0;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/grass.mat no encontrado.");
        }

        // A�adir chunk a la lista de chunks
        chunk_list.Add(chunk_0_0);
        pos_x_list.Add(0);
        pos_y_list.Add(0);

        // Crear nuevo chunk
        GameObject chunk_100_0 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_100_0.transform.position = new Vector3(100f, 0f, 0f);
        chunk_100_0.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_100_0.name = "Chunk_Forest_100_0";

        // A�adir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_100_0);
        pos_x_list.Add(100)
        pos_y_list.Add(0);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_0 = chunk_100_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_0._filter = chunk_100_0.GetComponent<MeshFilter>();
        terrainGen_100_0.scale = 2f;
        terrainGen_100_0.heightMultiplier = 20f;

        // Asignar textura al chunk, si existe
        Material material_100_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/rojo.mtlx");
        if (material_100_0 != null)
        {
            chunk_100_0.GetComponent<Renderer>().material = material_100_0;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/rojo.mat no encontrado.");
        }

        // A�adir chunk a la lista de chunks
        chunk_list.Add(chunk_100_0);
        pos_x_list.Add(1);
        pos_y_list.Add(0);

        // Crear nuevo chunk
        GameObject chunk_100_100 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_100_100.transform.position = new Vector3(100f, 0f, 100f);
        chunk_100_100.transform.localScale = new Vector3(10f, 1f, 10f);
        chunk_100_100.name = "Chunk_Forest_100_100";

        // A�adir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_100_100);
        pos_x_list.Add(100)
        pos_y_list.Add(100);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_100 = chunk_100_100.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_100._filter = chunk_100_100.GetComponent<MeshFilter>();
        terrainGen_100_100.scale = 4f;
        terrainGen_100_100.heightMultiplier = 80f;

        // Asignar textura al chunk, si existe
        Material material_100_100 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Textures/rojo.mtlx");
        if (material_100_100 != null)
        {
            chunk_100_100.GetComponent<Renderer>().material = material_100_100;
        }
        else
        {
            Debug.LogWarning("Textura Assets/Textures/rojo.mat no encontrado.");
        }

        // A�adir chunk a la lista de chunks
        chunk_list.Add(chunk_100_100);
        pos_x_list.Add(1);
        pos_y_list.Add(1);

        // Crear un objeto vac�o en la escena
        GameObject emptyObject = new GameObject("UnirTerrenosManager");

        // A�adir el script unirTerrenosScript al objeto vac�o
        unirTerrenosScript unir_terrenos = emptyObject.AddComponent<unirTerrenosScript>();
        unir_terrenos.chunk_list = chunk_list;
        unir_terrenos.pos_x_list = pos_x_list;
        unir_terrenos.pos_y_list = pos_y_list;
    }
}
    