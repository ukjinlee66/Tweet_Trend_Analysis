package kr.pe.playdata.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.repository.canditblRepository;

@Service
public class canditblService {
	@Autowired
	canditblRepository canditblRepository;
	
	public List<canditbl> findAll(Sort sort){
		List<canditbl> list = canditblRepository.findAll(sort);
		return list;
	}
}
