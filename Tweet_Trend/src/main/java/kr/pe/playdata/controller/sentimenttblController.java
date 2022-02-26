package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.model.sentimenttbl;
import kr.pe.playdata.service.sentimenttblService;

@RestController
@RequestMapping("/v1")
public class sentimenttblController {
	@Autowired
	sentimenttblService sentimenttblService;
	
	@GetMapping("/sentimenttbl") 
	public List<sentimenttbl> findAllSorted() {
		Sort sort = Sort.by(Sort.Direction.ASC, "sentiment");
		List<sentimenttbl> list = sentimenttblService.findAll(sort);
		return list;
	}
	
//	@GetMapping("/sentimenttblSorted")
//	public List<sentimenttbl> findAllSorted() {
//		return sentimenttblService.findAllSorted(); 
//	}

}
