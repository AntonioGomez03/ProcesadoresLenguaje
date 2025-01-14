package gec;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Chunk {
    private int posX;
    private int posY;
    private float scale;
    private float heightMultiplier;
    private String texture;
    private List<GameObject> gameObjects;

    public Chunk(int posX, int posY, float scale, float heightMultiplier, String texture, List<GameObject> gameObjects) {
            this.posX = posX;
            this.posY = posY;
            this.scale = scale;
            this.heightMultiplier = heightMultiplier;
            this.texture = texture;
            this.gameObjects = gameObjects != null ? gameObjects : new ArrayList<>();
            }

    public int getPosX() {
        return posX;
    }

    public int getPosY() {
        return posY;
    }

    public List<GameObject> getGameObjects() {
        return gameObjects;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> data = new HashMap<>();
        data.put("pos_x", posX);
        data.put("pos_y", posY);
        data.put("scale", scale);
        data.put("height_multiplier", heightMultiplier);
        String cleanTexture = texture;
        if (texture.startsWith("\"") && texture.endsWith("\"")) {
            cleanTexture = texture.substring(1, texture.length() - 1);
        }
        data.put("texture", cleanTexture);
        
        List<Map<String, Object>> gameObjectsList = gameObjects.stream()
                .map(GameObject::toMap) 
                .collect(Collectors.toList());
        data.put("gameobjects", gameObjectsList);
        return data;
    }
}
    

