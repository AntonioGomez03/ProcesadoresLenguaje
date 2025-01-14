package gec; 
import java.util.HashMap;
import java.util.Map;

public class GameObject {
    private String model;
    private int density;
    private float scale;
    private float minScale;
    private float maxScale;

    // Constructor
      public GameObject(String model, int density, float scale) {
        this.model = model;
        this.density = density;
        this.scale = scale;
        this.minScale = -1234232;
        this.maxScale = -1234232;
    }

    // Constructor para rango de escalas (minScale y maxScale)
    public GameObject(String model, int density, float minScale, float maxScale) {
        this.model = model;
        this.density = density;
        this.minScale = minScale;
        this.maxScale = maxScale;
        this.scale = -1234232;
    }

// Getter methods
    public String getModel() {
        return model;
    }

    public int getDensity() {
        return density;
    }

    public Float getScale() {
        return scale;
    }

    public Float getMinScale() {
        return minScale;
    }

    public Float getMaxScale() {
        return maxScale;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> data = new HashMap<>();
        data.put("model", model);
        data.put("density", density);
        if (scale != -1234232) {
            data.put("scale", scale);
        }
        if (minScale != -1234232) {
            data.put("min_scale", minScale);
        }
        if (maxScale != -1234232) {
            data.put("max_scale", maxScale);
        }
        return data;
    }
    @Override
    public String toString() {
        return "GameObject{" +
                "model='" + model + '\'' +
                ", density=" + density +
                ", scale=" + scale +
                ", minScale=" + minScale +
                ", maxScale=" + maxScale +
                '}';
    }
}