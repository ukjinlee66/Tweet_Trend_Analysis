package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.model.sentimenttbl;
import kr.pe.playdata.service.sentimenttblService;

@RestController
@RequestMapping("/v1")
public class sentimenttblController {
	@Autowired
	sentimenttblService sentimenttblService;
	
	@GetMapping("/sentimenttbl") 
	public List<sentimenttbl> findAllMember() {
		return sentimenttblService.findAll(); 
	}

}
