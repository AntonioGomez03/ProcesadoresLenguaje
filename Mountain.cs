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
        
        // Se añade un collider al chunk para detectar colisiones
        chunk_0_100.AddComponent<MeshCollider>();

        // Añadir chunk a la lista y sus coordenadas
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

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_0_100);
        pos_x_list.Add(0);
        pos_y_list.Add(1);

        // Crear un objeto vacío en la escena
        GameObject emptyObject = new GameObject("mergeTerrainScript");

        // Añadir el script unirTerrenosScript al objeto vacío
        unirTerrenosScript unir_terrenos = emptyObject.AddComponent<unirTerrenosScript>();
        unir_terrenos.chunk_list = chunk_list;
        unir_terrenos.pos_x_list = pos_x_list;
        unir_terrenos.pos_y_list = pos_y_list;

        // Función para ajustar la escala de la textura en función del tamaño del chunk
        void AdjustTextureScale(GameObject chunk, Material material)
        {
            // Tamaño base del plano sin escalado
            Vector3 baseSize = chunk.GetComponent<MeshFilter>().sharedMesh.bounds.size;

            // Tamaño final del chunk, tomando en cuenta la escala
            Vector3 finalSize = new Vector3(baseSize.x * chunk.transform.localScale.x, baseSize.y * chunk.transform.localScale.y, baseSize.z * chunk.transform.localScale.z);

            // Ajustamos la escala de la textura en función del tamaño final del chunk
            // Dividimos por el tamaño base de la textura (suponemos que es de 1x1 en la textura original)
            material.mainTextureScale = new Vector2(finalSize.x / baseSize.x, finalSize.z / baseSize.z);
        }
    
        // Añadir GameObjects al chunk
        for (int i = 0; i < 15; i++) {
            // Valores aleatorios para las posiciones X,Z del objeto
            float randomValue_X = Random.Range(-25.0f, 25.0f);
            float randomValue_Z = Random.Range(50.0f, 150.0f);

            // Disparar un rayo hacia abajo desde una posición en X,Z (para determinar la altura del objeto en el plano)
            // Crear el rayo
            Ray ray = new Ray(new Vector3(randomValue_X, 100f, randomValue_Z), Vector3.down);  // Disparo hacia abajo
            RaycastHit hit;
            float Value_Y = 0f;

            // Visualiza el rayo en la escena para verificar que está correctamente apuntando hacia abajo
            Debug.DrawRay(ray.origin, ray.direction * 100f, Color.red, 5f);  // Dibuja el rayo en la escena

            if (Physics.Raycast(ray, out hit)) {
                // La posición Y donde el rayo impacta es la altura en ese punto
                Value_Y = hit.point.y;
                Debug.Log("Rayo impactado en: " + hit.point);
            } else {
                Debug.LogWarning("No se encontró ninguna superficie en la posición especificada.");
            }


            Vector3 randomPosition = new Vector3(
                randomValue_X,
                Value_Y,
                randomValue_Z
            );

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("src/models/rock.prefab");

            // Obtener el MeshFilter del GameObject
            MeshFilter meshFilter = newObject.GetComponent<MeshFilter>();

            if (meshFilter != null)
            {
                // Obtener las dimensiones del Mesh
                Bounds bounds = meshFilter.mesh.bounds;

                // La altura es la distancia entre el punto más bajo y el más alto en el eje Y
                float height = bounds.size.y;
                Debug.Log("Altura del GameObject (Mesh): " + height);
                // Modificar el Vector3 sumando la altura a Y
                randomPosition.y += height;
            }
            else
            {
                Debug.LogWarning("El GameObject no tiene un MeshFilter.");
            }


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
