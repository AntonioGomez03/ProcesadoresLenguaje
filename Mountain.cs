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

        // A�adir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_0_100);
        pos_x_list.Add(0);
        pos_y_list.Add(100);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_0_100 = chunk_0_100.AddComponent<SimpleTerrainGenerator>();
        terrainGen_0_100._filter = chunk_0_100.GetComponent<MeshFilter>();
        terrainGen_0_100.scale = 1.2f;
        terrainGen_0_100.heightMultiplier = 500f;

        // Asignar textura al chunk, si existe
        Material material_0_100 = AssetDatabase.LoadAssetAtPath<Material>("snow_texture.png.mat");
        if (material_0_100 != null)
        {
            chunk_0_100.GetComponent<Renderer>().material = material_0_100;
            AdjustTextureScale(chunk_0_100, material_0_100);  // Ajustamos la escala de la textura
        }
        else
        {
            Debug.LogWarning("Textura snow_texture.png.mat no encontrado.");
        }

        // A�adir chunk a la lista de chunks
        chunk_list.Add(chunk_0_100);
        pos_x_list.Add(0);
        pos_y_list.Add(1);

        // Crear un objeto vac�o en la escena
        GameObject emptyObject = new GameObject("mergeTerrainScript");

        // A�adir el script unirTerrenosScript al objeto vac�o
        unirTerrenosScript unir_terrenos = emptyObject.AddComponent<unirTerrenosScript>();
        unir_terrenos.chunk_list = chunk_list;
        unir_terrenos.pos_x_list = pos_x_list;
        unir_terrenos.pos_y_list = pos_y_list;

        // Funci�n para ajustar la escala de la textura en funci�n del tama�o del chunk
        void AdjustTextureScale(GameObject chunk, Material material)
        {
            // Tama�o base del plano sin escalado
            Vector3 baseSize = chunk.GetComponent<MeshFilter>().sharedMesh.bounds.size;

            // Tama�o final del chunk, tomando en cuenta la escala
            Vector3 finalSize = new Vector3(baseSize.x * chunk.transform.localScale.x, baseSize.y * chunk.transform.localScale.y, baseSize.z * chunk.transform.localScale.z);

            // Ajustamos la escala de la textura en funci�n del tama�o final del chunk
            // Dividimos por el tama�o base de la textura (suponemos que es de 1x1 en la textura original)
            material.mainTextureScale = new Vector2(finalSize.x / baseSize.x, finalSize.z / baseSize.z);
        }
    
        // A�adir GameObjects al chunk
        for (int i = 0; i < 15; i++) {
            Vector3 randomPosition = new Vector3(
                Random.Range(0f, 50),
                0f,
                Random.Range(100f, 200)
            );

            Terrain terrain = Terrain.activeTerrain; // Aseg�rate de tener un terreno activo
            if (terrain != null) {
                randomPosition.y = terrain.SampleHeight(randomPosition) + terrain.GetPosition().y;
            } else {
                Debug.LogWarning("No se encontr� un terreno activo.");
            }

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("src/models/rock.prefab");
            if (newObject != null) {
                GameObject instance = Instantiate(newObject);
                instance.transform.position = randomPosition;
                float objectScale = Random.Range(0.7f, 1.2f);
                instance.transform.localScale = Vector3.one * objectScale;
            } else {
                Debug.LogWarning("Modelo src/models/rock.prefab no encontrado.");
            }
        }
        

    }
}    
