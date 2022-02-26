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

@Controller
public class maincontroller 
{
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
	@GetMapping("/")
	public String mainPage(Model model) 
	{
		return "MainPage";
	}
}