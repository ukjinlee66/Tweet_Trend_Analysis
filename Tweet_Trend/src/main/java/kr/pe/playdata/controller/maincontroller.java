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
		
		//JsonObject 생성
		JSONObject jsonObject = (JSONObject)parser.parse(reader);

		//Json에 img(key)의 value가져옴
		String img_name = (String) jsonObject.get("img");
		
		byte[] byteArrray = img_name.getBytes();
		System.out.println(byteArrray);
	    
	    Decoder decoder = Base64.getDecoder(); 
	    byte[] decodedBytes = decoder.decode(img_name);
	    //System.out.println("디코딩 text : " + new String(decodedBytes));
	    
	    //상대경로 지정
	    String absolutePath = new File("src/main/resources/img/").getAbsolutePath()+"\\img.png";
	    //저장위치 확인
	    //System.out.println(absolutePath);
	    
	    //File 저장
	    FileUtils.writeByteArrayToFile(new File(absolutePath), decodedBytes);
	  
		return "MainPage";
	}
}