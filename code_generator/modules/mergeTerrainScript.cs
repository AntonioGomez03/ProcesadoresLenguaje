using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class unirTerrenosScript : MonoBehaviour
{
    public List<GameObject> chunk_list = new List<GameObject>();
    public List<int> pos_x_list = new List<int>();
    public List<int> pos_y_list = new List<int>();


    private void Start()
    {
        // Crear y configurar los chunks
        // Código de creación de chunks omitido por brevedad...
        // Ajuste de alturas en los bordes de los chunks
        for (int i = 0; i < chunk_list.Count; i++)
        {
            for (int e = i + 1; e < chunk_list.Count; e++)
            {
                if (i != e)
                {
                    int pos_x_i = pos_x_list[i];
                    int pos_y_i = pos_y_list[i];
                    int pos_x_e = pos_x_list[e];
                    int pos_y_e = pos_y_list[e];

                    // Verificar vecinos
                    bool areEdgeNeighbors = false;
                    string edgeType = "";

                    if (pos_y_i == pos_y_e && Mathf.Abs(pos_x_i - pos_x_e) == 1)
                    {
                        areEdgeNeighbors = true;
                        edgeType = (pos_x_i < pos_x_e) ? "Este" : "Oeste";
                    }
                    else if (pos_x_i == pos_x_e && Mathf.Abs(pos_y_i - pos_y_e) == 1)
                    {
                        areEdgeNeighbors = true;
                        edgeType = (pos_y_i < pos_y_e) ? "Norte" : "Sur";
                    }

                    if (areEdgeNeighbors)
                    {
                        Mesh mesh_i = chunk_list[i].GetComponent<MeshFilter>().mesh;
                        Mesh mesh_e = chunk_list[e].GetComponent<MeshFilter>().mesh;

                        Vector3[] verticesA = mesh_i.vertices;
                        Vector3[] verticesB = mesh_e.vertices;

                        if (edgeType == "Este" || edgeType == "Oeste")
                        {
                            for (int v = 0; v < verticesA.Length; v++)
                            {
                                Vector3 vertA = verticesA[v];

                                for (int vb = 0; vb < verticesB.Length; vb++)
                                {
                                    Vector3 vertB = verticesB[vb];

                                    if (edgeType == "Este" && Mathf.Approximately(vertA.x, 5f) &&
                                        Mathf.Approximately(vertB.x, -5f) &&
                                        Mathf.Approximately(vertA.z, vertB.z))
                                    {
                                        float averageHeight = (vertA.y + vertB.y) / 2;
                                        vertA.y = averageHeight;
                                        vertB.y = averageHeight;
                                        verticesA[v] = vertA;
                                        verticesB[vb] = vertB;
                                    }
                                    else if (edgeType == "Oeste" && Mathf.Approximately(vertA.x, -5f) &&
                                             Mathf.Approximately(vertB.x, 5f) &&
                                             Mathf.Approximately(vertA.z, vertB.z))
                                    {
                                        float averageHeight = (vertA.y + vertB.y) / 2;
                                        vertA.y = averageHeight;
                                        vertB.y = averageHeight;
                                        verticesA[v] = vertA;
                                        verticesB[vb] = vertB;
                                    }
                                }
                            }
                        }
                        else if (edgeType == "Norte" || edgeType == "Sur")
                        {
                            for (int v = 0; v < verticesA.Length; v++)
                            {
                                Vector3 vertA = verticesA[v];

                                for (int vb = 0; vb < verticesB.Length; vb++)
                                {
                                    Vector3 vertB = verticesB[vb];

                                    if (edgeType == "Norte" && Mathf.Approximately(vertA.z, 5f) &&
                                        Mathf.Approximately(vertB.z, -5f) &&
                                        Mathf.Approximately(vertA.x, vertB.x))
                                    {
                                        float averageHeight = (vertA.y + vertB.y) / 2;
                                        vertA.y = averageHeight;
                                        vertB.y = averageHeight;
                                        verticesA[v] = vertA;
                                        verticesB[vb] = vertB;
                                    }
                                    else if (edgeType == "Sur" && Mathf.Approximately(vertA.z, -5f) &&
                                             Mathf.Approximately(vertB.z, 5f) &&
                                             Mathf.Approximately(vertA.x, vertB.x))
                                    {
                                        float averageHeight = (vertA.y + vertB.y) / 2;
                                        vertA.y = averageHeight;
                                        vertB.y = averageHeight;
                                        verticesA[v] = vertA;
                                        verticesB[vb] = vertB;
                                    }
                                }
                            }
                        }

                        // Actualizar los meshes
                        mesh_i.vertices = verticesA;
                        mesh_e.vertices = verticesB;
                        mesh_i.RecalculateNormals();
                        mesh_e.RecalculateNormals();
                    }
                }
            }
        }
    }
}

