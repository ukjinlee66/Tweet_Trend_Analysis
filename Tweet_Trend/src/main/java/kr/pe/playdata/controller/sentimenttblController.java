package kr.pe.playdata.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.model.sentimenttbl;
import kr.pe.playdata.service.sentimenttblService;

@RestController
@RequestMapping("/v1")
public class sentimenttblController {
	@Autowired
	sentimenttblService sentimenttblService;
	
	@ApiOperation(value="KoBERT Model의 감성결과 정렬", notes= "감성데이터를 정렬 및 호출")
	@ApiResponses({
        @ApiResponse(code = 200, message = "API 정상 작동"),
        @ApiResponse(code = 500, message = "서버 에러")
	})
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
