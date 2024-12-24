using UnityEngine;
using UnityEditor;
using System.Collections.Generic;

public class Mountain : MonoBehaviour {

    public List<GameObject> chunk_list = new List<GameObject>();
    public List<int> pos_x_list = new List<int>();
    public List<int> pos_y_list = new List<int>();
    public unirTerrenosScript unirTerrenosScript;


    void Start() {

        // Crear nuevo chunk
        GameObject chunk_0_100 = GameObject.CreatePrimitive(PrimitiveType.Plane);
        chunk_0_100.transform.position = new Vector3(0f, 0f, 100f);
        chunk_0_100.transform.localScale = new Vector3(5f, 1f, 10f);
        chunk_0_100.name = "Chunk_Mountain_0_100";

        // Añadir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_0_100);
        pos_x_list.Add(0)
        pos_y_list.Add(100);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_0_100 = chunk_0_100.AddComponent<SimpleTerrainGenerator>();
        terrainGen_0_100._filter = chunk_0_100.GetComponent<MeshFilter>();
        terrainGen_0_100.scale = 1.2f;
        terrainGen_0_100.heightMultiplier = 500f;

        // Asignar textura al chunk, si existe
        Material material_0_100 = AssetDatabase.LoadAssetAtPath<Material>("snow_texture.png.mtlx");
        if (material_0_100 != null)
        {
            chunk_0_100.GetComponent<Renderer>().material = material_0_100;
        }
        else
        {
            Debug.LogWarning("Textura snow_texture.png.mat no encontrado.");
        }

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_0_100);
        pos_x_list.Add(0);
        pos_y_list.Add(1);

        // Crear un objeto vacío en la escena
        GameObject emptyObject = new GameObject("UnirTerrenosManager");

        // Añadir el script unirTerrenosScript al objeto vacío
        unirTerrenosScript unir_terrenos = emptyObject.AddComponent<unirTerrenosScript>();
        unir_terrenos.chunk_list = chunk_list;
        unir_terrenos.pos_x_list = pos_x_list;
        unir_terrenos.pos_y_list = pos_y_list;
    }
}
    