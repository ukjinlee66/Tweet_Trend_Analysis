package kr.pe.playdata.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.model.sentimenttbl;
import kr.pe.playdata.repository.sentimenttblRepository;

@Service
public class sentimenttblService {
	@Autowired
	sentimenttblRepository sentimenttblRepository;
	
	public List<sentimenttbl> findAll(Sort sort){
		List<sentimenttbl> list = sentimenttblRepository.findAll(sort);
		return list;
	}
}
