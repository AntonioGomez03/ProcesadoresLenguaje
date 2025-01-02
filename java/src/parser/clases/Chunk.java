package clases;

import java.util.ArrayList;
import java.util.List;

public class Chunk {
    private int posX;
    private int posY;
    private double scale;
    private int heightMultiplier;
    private String texture;
    private List<GameObject> gameObjects;

    public Chunk(int posX, int posY, double scale, int heightMultiplier, String texture) {
        this.posX = posX;
        this.posY = posY;
        this.scale = scale;
        this.heightMultiplier = heightMultiplier;
        this.texture = texture;
        this.gameObjects = new ArrayList<>();
    }

    public void addGameObject(GameObject gameObject) {
        gameObjects.add(gameObject);
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
}
    

