package kr.pe.playdata.controller;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;
import javax.xml.bind.DatatypeConverter;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

import io.swagger.annotations.ApiOperation;

@Controller
public class maincontroller 
{
	@ApiOperation(value="Post Image요청 처리", notes= "트위터 메세지를 키워드추출하여 빈도수별로 워드클라우드이미지를 출력.")
	@PostMapping("/img")
	public String uploadImage(@RequestBody String data) throws IOException
	{
		try 
		{
			JSONParser parser = new JSONParser();
			JSONObject jsonObject = (JSONObject)parser.parse(data);
			String img_name = jsonObject.get("img").toString();
		    byte[] ss = DatatypeConverter.parseBase64Binary(img_name);
		    BufferedImage bufImg = ImageIO.read(new ByteArrayInputStream(ss));
		    System.out.println(bufImg);
		    ImageIO.write(bufImg, "png", new File("src/main/resources/img/sksda.png"));
		}
		catch (Exception e)
		{
			System.out.println(e);
		}
	    return "ImageUpload Success!";
	}
	
	@ApiOperation(value="Main Controller", notes= "MainPage.jsp를 호출")
	@GetMapping("/")
	public String mainPage(Model model) 
	{
		return "MainPage";
	}
}