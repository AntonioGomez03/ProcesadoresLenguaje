package gec;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class World {
    private String name;
    private ArrayList<Scene> scenes;

    // Constructor
    public World(String name, ArrayList<Scene> scenes ) {
        this.name = name;
        this.scenes = scenes;
    }
    
    public World(String name) {
        this.name = name;
    }

    // Add a scene to the world
    // public void addScene(Scene scene) {
    //     if (sceneIsValid(scene)) {
    //         scenes.add(scene);
    //     } else {
    //         throw new IllegalArgumentException("Scene with the name \"" + scene.getName() + "\" already exists.");
    //     }
    // }
    

    // Get all scenes
    public List<Scene> getScenes() {
        return scenes;
    }

    // Check if a scene is valid (unique by name)
    private boolean sceneIsValid(Scene scene) {
        for (Scene s : scenes) {
            if (s.getName().equals(scene.getName())) {
                return false;
            }
        }
        return true;
    }

    public Map<String, Object> toMap() {
        Map<String, Object> worldMap = new HashMap<>();
        String cleanName = name;
        if (name.startsWith("\"") && name.endsWith("\"")) {
            cleanName = name.substring(1, name.length() - 1);
        }

        worldMap.put("name", cleanName);

        // Manejar escenas nulas
        List<Map<String, Object>> scenesList = new ArrayList<>();
        if (scenes != null) {
            for (Scene scene : scenes) {
            scenesList.add(scene.toMap());
            }
        }
        worldMap.put("scenes", scenesList);
        

        Map<String, Object> data = new HashMap<>();
        data.put("world", worldMap);
        return data;
    }

    // Convert to JSON using Jackson or Gson
    public String toJson() {
        try {
            
            ObjectMapper mapper = new ObjectMapper();
            return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(this.toMap());
        } catch (Exception e) {
            throw new RuntimeException("Error converting World to JSON", e);
        }
    }
    
    @Override
    public String toString() {
        return toMap().toString();
    }
}

