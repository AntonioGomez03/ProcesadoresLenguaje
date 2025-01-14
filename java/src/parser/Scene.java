
package gec;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Scene {
    private String name;
    private int widthChunk;
    private int lengthChunk;
    private ArrayList<Chunk> chunks;

    // Constructor
    public Scene(String name, int widthChunk, int lengthChunk) {
        this.name = name;
        this.widthChunk = widthChunk;
        this.lengthChunk = lengthChunk;
        this.chunks = new ArrayList<>();
    }

    // Add a single chunk
    public void addChunk(Chunk chunk) {
        if (chunkIsValid(chunk)) {
            chunks.add(chunk);
        }
    }

    // Add multiple chunks
    public void addChunks(ArrayList<Chunk> chunksToAdd) {
        for (Chunk chunk : chunksToAdd) {
            if (chunkIsValid(chunk)) {
                addChunk(chunk);
            }
        }
    }

    // Validate if a chunk is unique in the scene
    private boolean chunkIsValid(Chunk chunk) {
        for (Chunk existingChunk : chunks) {
            if (existingChunk.getPosX() == chunk.getPosX() && existingChunk.getPosY() == chunk.getPosY()) {
                throw new IllegalArgumentException("Chunk already exists at position (" + chunk.getPosX() + ", " + chunk.getPosY() + ")");
            }
        }
        return true;
    }
    
    // Convert to a Map representation
    public Map<String, Object> toMap() {
        Map<String, Object> data = new HashMap<>();
        String cleanName = name;
        if (name.startsWith("\"") && name.endsWith("\"")) {
            cleanName = name.substring(1, name.length() - 1);
        }
        data.put("name", cleanName);
        data.put("width_chunk", widthChunk);
        data.put("length_chunk", lengthChunk);

        // Convert chunks to a list of maps
        List<Map<String, Object>> chunksList = new ArrayList<>();
        for (Chunk chunk : chunks) {
            chunksList.add(chunk.toMap());
        	}
        
        data.put("chunks", chunksList);
        return data;
    }

    // Getters
    public String getName() {
        return name;
    }

    public List<Chunk> getChunks() {
        return chunks;
    }

    @Override
    public String toString() {
        return toMap().toString();
    }
}
