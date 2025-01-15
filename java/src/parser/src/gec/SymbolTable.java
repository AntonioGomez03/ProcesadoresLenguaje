package gec;
import java.util.HashMap;
import java.util.Map;

public class SymbolTable {
    // Internal table to store symbols
    private Map<String, SymbolEntry> table;

    // Constructor
    public SymbolTable() {
        this.table = new HashMap<>();
    }

    // Set a value in the symbol table
    public void setValue(String name, Object value, String typeKey) {
        if (table.containsKey(name)) {
            SymbolEntry entry = table.get(name);
            if (entry.getType().equals(typeKey)) {
                entry.setValue(value);
            } else {
                throw new IllegalArgumentException("Tipo incompatible para el identificador '" + name + "'. Esperado: " + entry.getType());
            }
        } else {
            throw new IllegalArgumentException("Identificador '" + name + "' no definido.");
        }
    }

    // Define an identifier with a type
    public void defineIdentifier(String name, String typeKey) {
        if (table.containsKey(name)) {
            throw new IllegalArgumentException("El identificador '" + name + "' ya está definido.");
        }
        table.put(name, new SymbolEntry(null, typeKey));
    }
    
    // Update the value of an existing identifier
    public void updateValue(String name, Object newValue) {
        if (table.containsKey(name)) {  
            SymbolEntry entry = table.get(name);
                entry.setValue(newValue);
            }
         else {
            throw new IllegalArgumentException("Identificador '" + name + "' no definido. Debe definirse antes de asignarle un valor.");
        }
    }
    
    // Update the value of an existing identifier
    public void updateValueType(String name,  String typeKey, Object newValue) {
        if (table.containsKey(name)) {
            SymbolEntry entry = table.get(name);
            if (entry.getType().equals(typeKey)) {
                entry.setValue(newValue);
            } else {
                throw new IllegalArgumentException("Tipo incompatible para el identificador '" + name + "'. Esperado: " + entry.getType());
            }
        } else {
            throw new IllegalArgumentException("Identificador '" + name + "' no definido. Debe definirse antes de asignarle un valor.");
        }
    }

    // Get a value from the symbol table
    public Object getValue(String name) {
        if (table.containsKey(name)) {
            SymbolEntry entry = table.get(name);
            return entry.getValue();
        }
        throw new IllegalArgumentException("Variable '" + name + "' no definida.");
    }

    // Get the type of a variable
    public String getType(String name) {
        if (table.containsKey(name)) {
            return table.get(name).getType();
        }
        throw new IllegalArgumentException("Variable '" + name + "' no definida.");
    }

       public void printTable() {
        for (Map.Entry<String, SymbolEntry> entry : table.entrySet()) {
        	System.out.println();
            String identifier = entry.getKey();
            SymbolEntry symbolEntry = entry.getValue();
            String value = symbolEntry.getValue() != null ? symbolEntry.getValue().toString() : "null";
            String type = symbolEntry.getType();
            System.out.printf("%-14s %-14s  %-14s \n", identifier, value, type);
        }
        System.out.println();
    }

    // ToString method for debugging
    @Override
    public String toString() {
        return table.toString();
    }

    // Nested class to represent an entry in the symbol table
    private static class SymbolEntry {
        private Object value;
        private String type;

        public SymbolEntry(Object value, String type) {
            this.value = value;
            this.type = type;
        }

        public Object getValue() {
            return value;
        }

        public void setValue(Object value) {
            this.value = value;
        }

        public String getType() {
            return type;
        }

        @Override
        public String toString() {
            return "{value=" + value + ", type='" + type + "'}";
        }
    }
}
