using UnityEditor;
using UnityEngine;

public class SimpleTerrainGenerator : MonoBehaviour
{
    [SerializeField] public MeshFilter _filter;   // El MeshFilter del plano al que vamos a modificar
    [SerializeField] public float scale = 10f;      // Escala del ruido Perlin para controlar el detalle
    [SerializeField] public float heightMultiplier = 5f; // Multiplicador de altura para ajustar la elevación del terreno
    private Vector2 offset;                          // Desplazamiento aleatorio para variar el terreno generado

    private MeshCollider _meshCollider; // Collider para el terreno

    private void Start()
    {
        // Genera un desplazamiento aleatorio para que el terreno sea diferente cada vez
        offset = new Vector2(Random.Range(0f, 1000f), Random.Range(0f, 1000f));

        // Generar el terreno (visual) usando tu código original
        GenerateTerrain();

        // Añadir MeshCollider al GameObject para detectar colisiones
        CreateCollider();
    }

    private void GenerateTerrain()
    {
        Mesh mesh = _filter.mesh;             // Obtenemos la malla del MeshFilter
        Vector3[] vertices = mesh.vertices;   // Obtenemos los vértices de la malla

        // Iteramos a través de cada vértice de la malla
        for (int i = 0; i < vertices.Length; ++i)
        {
            Vector3 vertex = vertices[i];

            // Aplicamos ruido Perlin en las coordenadas X y Z y ajustamos la altura
            float perlinValue = Mathf.PerlinNoise((vertex.x + offset.x) / scale, (vertex.z + offset.y) / scale);
            vertex.y = perlinValue * heightMultiplier;

            // Actualizamos el vértice con la nueva altura
            vertices[i] = vertex;
        }

        // Actualizamos la malla con los nuevos vértices
        mesh.vertices = vertices;
        mesh.RecalculateNormals();  // Calculamos las normales para que la iluminación sea correcta
        mesh.RecalculateBounds();   // Aseguramos que la malla recalcula sus límites
    }

    private void CreateCollider()
    {
        // Añadir un MeshCollider al mismo GameObject donde se encuentra el MeshFilter
        _meshCollider = gameObject.AddComponent<MeshCollider>();
        _meshCollider.sharedMesh = _filter.mesh;  // Usamos la malla ya generada
        _meshCollider.convex = true;  // Opcional, depende de si necesitas colisiones más complejas

        // Si el MeshCollider no es necesario para físicas de colisiones, puedes configurarlo como 'false' para mejorar el rendimiento:
        _meshCollider.enabled = true;
    }

    // Este método guarda la malla generada como un asset
    private void SaveGeneratedMesh()
    {
        Mesh mesh = _filter.mesh;
        string path = "Assets/GeneratedTerrain_" + System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss") + ".asset";
        AssetDatabase.CreateAsset(mesh, path);
        AssetDatabase.SaveAssets();
        Debug.Log("Malla generada guardada en: " + path);
    }

    // Guardamos el mesh cuando se detiene la ejecución
    private void OnApplicationQuit()
    {
        SaveGeneratedMesh();
    }
}
