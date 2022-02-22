package kr.pe.playdata.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.AsyncService;

@RestController
public class maincontroller 
{
	Logger logger = LoggerFactory.getLogger(maincontroller.class);

    @Autowired
    AsyncService asyncService;

    @Autowired
    private AsyncService service;

    @GetMapping("/async")
    public String goAsync() {
        service.onAsync();
        String str = "Hello Spring Boot Async!!";
        logger.info(str);
        logger.info("==================================");
        return str;
    }

    @GetMapping("/sync")
    public String goSync() {
        service.onSync();
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