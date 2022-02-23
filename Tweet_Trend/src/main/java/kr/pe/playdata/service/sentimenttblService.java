package kr.pe.playdata.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import kr.pe.playdata.domain.sentimenttbl;
import kr.pe.playdata.repository.sentimenttblRepository;

@Service
public class sentimenttblService {
	@Autowired
	sentimenttblRepository sentimenttblRepository;
	
	public List<sentimenttbl> findAll(){
		List<sentimenttbl> list = sentimenttblRepository.findAll();
		System.out.println(list);
		return list;
	}
}
