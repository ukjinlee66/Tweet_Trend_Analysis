package kr.pe.playdata.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import kr.pe.playdata.domain.canditbl;
import kr.pe.playdata.repository.canditblRepository;

@Service
public class canditblService {
	@Autowired
	canditblRepository canditblRepository;
	
	public List<canditbl> findAll(){
		List<canditbl> list = canditblRepository.findAll();
		System.out.println(list);
		return list;
	}
}
