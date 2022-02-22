package kr.pe.playdata.controller;

import java.io.File;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.util.Base64;
import java.util.Base64.Decoder; 
import java.util.Base64.Encoder;

import static org.apache.commons.io.FileUtils.openInputStream;
import static org.apache.commons.io.FileUtils.writeByteArrayToFile;
import org.apache.commons.io.FileUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;



@Controller
public class maincontroller 
{
	Logger logger = LoggerFactory.getLogger(maincontroller.class);



    @GetMapping("/async")
    public String goAsync() {
  
        String str = "Hello Spring Boot Async!!";
        logger.info(str);
        logger.info("==================================");
        return str;
    }

    @GetMapping("/sync")
    public String goSync() {
    
        String str = "Hello Spring Boot Sync!!";
        logger.info(str);
        logger.info("==================================");
        return str;
    }
	@GetMapping("/")
	public String mainPage(Model model) throws Exception 
	{	
		
		JSONParser parser = new JSONParser();

		FileReader reader = new FileReader("c:/json/img.json");

		JSONObject jsonObject = (JSONObject) parser.parse(reader);

		String img_name = (String) jsonObject.get("img");
		
		byte[] byteArrray = img_name.getBytes();
		System.out.println(byteArrray);
		
		//byte[] decodedBytes = Base64.getMimeDecoder().decode(img_name);
		
		//String directory=servletContext.getRealPath("/")+"images/sample.jpg";
		//FileUtils.writeByteArrayToFile(new File(outputFileName), decodedBytes);
		
		String absolutePath = new File("src/main/resources").getAbsolutePath() + "/"+"img.png";
	    
		FileOutputStream output = new FileOutputStream(absolutePath);
		//System.out.println(decodedBytes);
		//System.out.println(output);
		;
		//fos.write(decodedBytes);
		//fos.close();
		
	    String text = "ktko"; 
	    byte[] targetBytes = text.getBytes(); 
	    Encoder encoder = Base64.getEncoder(); 
	    byte[] encodedBytes = encoder.encode(targetBytes); 
	    Decoder decoder = Base64.getDecoder(); 
	    byte[] decodedBytes = decoder.decode(img_name.getBytes("UTF-8")); 
	    System.out.println("인코딩 전 : " + text); 
	    System.out.println("인코딩 text : " + new String(encodedBytes)); 
	    System.out.println("디코딩 text : " + new String(decodedBytes));
	    
	    FileUtils.writeByteArrayToFile(new File("img.png"), decodedBytes);
	    output.write(decodedBytes);
	    output.close();
	  
		return "MainPage";
	}
}