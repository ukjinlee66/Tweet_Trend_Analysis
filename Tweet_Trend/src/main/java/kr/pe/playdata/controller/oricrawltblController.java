package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.annotations.ApiOperation;
import kr.pe.playdata.model.oricrawltbl;
import kr.pe.playdata.service.oricrawltblService;

@RestController
@RequestMapping("/v1")
public class oricrawltblController {
	@Autowired
	oricrawltblService oricrawltblService;
	
	@ApiOperation(value="Original Data를 저장", notes= "원본데이터를 호출")
	@GetMapping("/oricrawltbl") 
	public List<oricrawltbl> findAll() {
		return oricrawltblService.findAll(); 
	}

}
