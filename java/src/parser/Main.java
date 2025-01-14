//package gec;
//
//import java.io.File;
//import java.io.IOException;
//import java.util.HashMap;
//import java.util.Map;
//import com.fasterxml.jackson.core.JsonProcessingException;
//import com.fasterxml.jackson.databind.ObjectMapper;
//
//public class Main {
//	public static void main(String args[]) {
//		  EmployeeBean employeeBean = new EmployeeBean();
//		  employeeBean.setId(1);
//		  employeeBean.setName("employee1");
//		  employeeBean.setGender("male");
//		  employeeBean.setDesignation("JAVA");
//		  
//		  ObjectMapper objectMapper = new ObjectMapper();
//	        Map<String, String> map = new HashMap<String, String>();
//	        map.put("1", "Welcome");
//	        map.put("2", "to");
//	        map.put("3", "Code Factory");
//
//	        try {
//	            // Convert the EmployeeBean object to a JSON string
//	            String jsonStr = objectMapper.writeValueAsString(employeeBean);
//
//	            // Write the JSON string to a file
//	            File outputFile = new File("output.json");
//	            objectMapper.writeValue(outputFile, employeeBean);
//
//	            System.out.println("JSON data has been written to: " + outputFile.getAbsolutePath());
//	        } catch (JsonProcessingException e) {
//	            e.printStackTrace();
//	        } catch (IOException e) {
//	            e.printStackTrace();
//	        }
//	    }
//	}
