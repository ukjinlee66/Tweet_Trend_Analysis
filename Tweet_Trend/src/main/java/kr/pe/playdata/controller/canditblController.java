package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.model.sentimenttbl;
import kr.pe.playdata.repository.canditblRepository;
import kr.pe.playdata.service.canditblService;

@RestController
@RequestMapping("/v1")
public class canditblController {
	@Autowired
	canditblService canditblService;
	
	@GetMapping("/canditbl") 
	public List<canditbl> findAllSorted() {
		Sort sort = Sort.by(Sort.Direction.ASC, "sentiment");
		List<canditbl> list = canditblService.findAll(sort);
		return list;
	}
}
