package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.model.oricrawltbl;
import kr.pe.playdata.service.oricrawltblService;

@RestController
@RequestMapping("/v1")
public class oricrawltblController {
	@Autowired
	oricrawltblService oricrawltblService;
	
	@GetMapping("/oricrawltbl") 
	public List<oricrawltbl> findAll() {
		return oricrawltblService.findAll(); 
	}
}
