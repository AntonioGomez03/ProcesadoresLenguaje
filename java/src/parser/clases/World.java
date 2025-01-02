public class World {
    private String name;
    private List<Scene> scenes;

    public World(String name) {
        this.name = name;
        this.scenes = new ArrayList<>();
    }

    public void addScene(Scene scene) {
        scenes.add(scene);
    }

    public String getName() {
        return name;
    }

    public List<Scene> getScenes() {
        return scenes;
    }
}
