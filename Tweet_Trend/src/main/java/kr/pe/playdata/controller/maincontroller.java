package kr.pe.playdata.controller;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.util.ArrayList;
import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.List;

import javax.imageio.ImageIO;

import org.apache.commons.io.FileUtils;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

import kr.pe.playdata.domain.Candi;
import kr.pe.playdata.domain.ImgData;
import kr.pe.playdata.domain.Senti;
import kr.pe.playdata.domain.View;

@RestController
@EnableAsync
@EnableAutoConfiguration
@ComponentScan(basePackages = "com.henryxi.async")
public class maincontroller 
{
	
	//후보자 리스트 호출
	@GetMapping("GetCandi")
	public List<Candi> get_candi_list()
	{
		List<Candi> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new Candi());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	//감성 리스트 호출.
	@GetMapping("GetSenti")
	public List<Senti> get_senti_list()
	{
		List<Senti> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new Senti());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	//트위터 리스트 호출.
	@GetMapping("GetView")
	public List<View> get_view_list()
	{
		List<View> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new View());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	
	//@Async("threadPoolExecutor")
	@PostMapping("/img")
	public String uploadImage(@RequestBody ImgData data) throws JsonProcessingException
	{
		try {
		ObjectMapper mapper = new ObjectMapper();
		String reader = mapper.writeValueAsString(data);
		byte[] imgbyte = javax.xml.bind.DatatypeConverter.parseBase64Binary(reader);
		System.out.println(imgbyte);
		BufferedImage img = ImageIO.read(new ByteArrayInputStream(imgbyte));
		
		//JsonTextParser textParser = new JsonTextParser();
		//JsonObjectCollection root = textParser.Parse(reader) as JsonObjectCollection;
		//decode 해주거나 아니면 spring boot가 해석.
		//System.out.println(reader);
		JSONParser parser = new JSONParser();
		//JsonObject 생성
				JSONObject jsonObject = (JSONObject)parser.parse(reader);

				//Json에 img(key)의 value가져옴
				String img_name = (String) jsonObject.get("img");
				System.out.println(img_name);
				byte[] byteArrray = img_name.getBytes();
				System.out.println(byteArrray);
			    
			    Decoder decoder = Base64.getDecoder(); 
			    byte[] decodedBytes = decoder.decode(imgbyte);
			    System.out.println("디코딩 text : " + new String(decodedBytes));
			    
			    //상대경로 지정
			    String absolutePath = new File("src/main/resources/img/").getAbsolutePath()+"/img.png";
			    //저장위치 확인
			    //System.out.println(absolutePath);
			    
			    //File 저장
			    FileUtils.writeByteArrayToFile(new File(absolutePath), decodedBytes);
		}
		catch (Exception e)
		{}
//		System.out.println(result.getImg());
//		
//		System.out.println("uploadImage on");
//	    String result = "false";
//	    FileOutputStream fos;
//
//	    fos = new FileOutputStream("img/word.json");
//
//	    // decode Base64 String to image
//	    try
//	    {
//	        byte byteArray[] = Base64.getMimeDecoder().decode(image);
//	        fos.write(byteArray);
//
//	        result = "true";
//	        fos.close();
//	    }
//	    catch (Exception e)
//	    {
//	        e.printStackTrace();
//	    }
//	    System.out.println("uploadImage off");
	    return "Saas"; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	    //return result;
	}
	@GetMapping("/")
	public String mainPage(Model model) 
	{
		
		/*
		 * 최신 트위터 리스트를 불러온다.
		 */
		
		
		//////////////////////////////////////
		
		/*
		 * 감성 분석 결과를 불러온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 총 데이터 수를 불러온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 막대그래프 정보를 받아온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 워드클라우드 이미지를 불러온다.
		 */
		
		//////////////////////////////////////
		return "MainPage";
	}
}