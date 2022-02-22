package kr.pe.playdata.controller;

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
	public String mainPage(Model model) 
	{
		return "MainPage";
	}
}