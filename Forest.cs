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
        
        // Se añade un collider al chunk para detectar colisiones
        chunk_0_0.AddComponent<MeshCollider>();

        // Añadir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_0_0);
        pos_x_list.Add(0);
        pos_y_list.Add(0);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_0_0 = chunk_0_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_0_0._filter = chunk_0_0.GetComponent<MeshFilter>();
        terrainGen_0_0.scale = 4f;
        terrainGen_0_0.heightMultiplier = 70f;

        // Asignar textura al chunk, si existe
        Material material_0_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Ground textures pack/Ground & rocks 02/Ground & rocks pattern 02.mat");
        if (material_0_0 != null)
        {
            chunk_0_0.GetComponent<Renderer>().material = material_0_0;
            AdjustTextureScale(chunk_0_0, material_0_0);  // Ajustamos la escala de la textura
        }
        else
        {
            Debug.LogWarning("Textura Assets/Ground textures pack/Ground & rocks 02/Ground & rocks pattern 02.mat no encontrado.");
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
        
        // Se añade un collider al chunk para detectar colisiones
        chunk_100_0.AddComponent<MeshCollider>();

        // Añadir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_100_0);
        pos_x_list.Add(100);
        pos_y_list.Add(0);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_0 = chunk_100_0.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_0._filter = chunk_100_0.GetComponent<MeshFilter>();
        terrainGen_100_0.scale = 2f;
        terrainGen_100_0.heightMultiplier = 20f;

        // Asignar textura al chunk, si existe
        Material material_100_0 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Ground textures pack/Grass & dead leafs 01/Grass & dead leafs pattern 01.mat");
        if (material_100_0 != null)
        {
            chunk_100_0.GetComponent<Renderer>().material = material_100_0;
            AdjustTextureScale(chunk_100_0, material_100_0);  // Ajustamos la escala de la textura
        }
        else
        {
            Debug.LogWarning("Textura Assets/Ground textures pack/Grass & dead leafs 01/Grass & dead leafs pattern 01.mat no encontrado.");
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
        
        // Se añade un collider al chunk para detectar colisiones
        chunk_100_100.AddComponent<MeshCollider>();

        // Añadir chunk a la lista y sus coordenadas
        chunk_list.Add(chunk_100_100);
        pos_x_list.Add(100);
        pos_y_list.Add(100);

        // Asignar y configurar el script SimpleTerrainGenerator al chunk
        SimpleTerrainGenerator terrainGen_100_100 = chunk_100_100.AddComponent<SimpleTerrainGenerator>();
        terrainGen_100_100._filter = chunk_100_100.GetComponent<MeshFilter>();
        terrainGen_100_100.scale = 4f;
        terrainGen_100_100.heightMultiplier = 80f;

        // Asignar textura al chunk, si existe
        Material material_100_100 = AssetDatabase.LoadAssetAtPath<Material>("Assets/Ground textures pack/Grass 03/Grass pattern 03.mat");
        if (material_100_100 != null)
        {
            chunk_100_100.GetComponent<Renderer>().material = material_100_100;
            AdjustTextureScale(chunk_100_100, material_100_100);  // Ajustamos la escala de la textura
        }
        else
        {
            Debug.LogWarning("Textura Assets/Ground textures pack/Grass 03/Grass pattern 03.mat no encontrado.");
        }

        // Añadir chunk a la lista de chunks
        chunk_list.Add(chunk_100_100);
        pos_x_list.Add(1);
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
        for (int i = 0; i < 2; i++) {
            // Valores aleatorios para las posiciones X,Z del objeto
            float randomValue_X = Random.Range(-50.0f, 50.0f);
            float randomValue_Z = Random.Range(-50.0f, 50.0f);

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

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("Assets/3D Gamekit - Environment Pack/Environment/Rocks/Prefabs/RockChunk01.prefab");

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
                float objectScale = 1.0f;
                instance.transform.localScale = Vector3.one * objectScale;
            } else {
                Debug.LogWarning("Modelo Assets/3D Gamekit - Environment Pack/Environment/Rocks/Prefabs/RockChunk01.prefab no encontrado.");
            }
        }
        
        // Añadir GameObjects al chunk
        for (int i = 0; i < 4; i++) {
            // Valores aleatorios para las posiciones X,Z del objeto
            float randomValue_X = Random.Range(-50.0f, 50.0f);
            float randomValue_Z = Random.Range(-50.0f, 50.0f);

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

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge01.prefab");

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
                float objectScale = Random.Range(0.2f, 0.5f);
                instance.transform.localScale = Vector3.one * objectScale;
            } else {
                Debug.LogWarning("Modelo Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge01.prefab no encontrado.");
            }
        }
        
        // Añadir GameObjects al chunk
        for (int i = 0; i < 15; i++) {
            // Valores aleatorios para las posiciones X,Z del objeto
            float randomValue_X = Random.Range(50.0f, 150.0f);
            float randomValue_Z = Random.Range(-50.0f, 50.0f);

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

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge04.prefab");

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
                float objectScale = 1.2f;
                instance.transform.localScale = Vector3.one * objectScale;
            } else {
                Debug.LogWarning("Modelo Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge04.prefab no encontrado.");
            }
        }
        
        // Añadir GameObjects al chunk
        for (int i = 0; i < 15; i++) {
            // Valores aleatorios para las posiciones X,Z del objeto
            float randomValue_X = Random.Range(50.0f, 150.0f);
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

            GameObject newObject = AssetDatabase.LoadAssetAtPath<GameObject>("Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge02.prefab");

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
                float objectScale = 1.2f;
                instance.transform.localScale = Vector3.one * objectScale;
            } else {
                Debug.LogWarning("Modelo Assets/3D Gamekit - Environment Pack/Environment/Vegetation/Large/Prefabs/VegetationLarge02.prefab no encontrado.");
            }
        }
        

    }
}    
