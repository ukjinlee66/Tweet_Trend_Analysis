package kr.pe.playdata.service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import kr.pe.playdata.model.oricrawltbl;
import kr.pe.playdata.repository.oricrawltblRepository;

@Service
public class oricrawltblService {
	@Autowired
	oricrawltblRepository oricrawltblRepository;
	
	public List<oricrawltbl> findAll(){
		List<oricrawltbl> list = oricrawltblRepository.findAll();
		System.out.println(list);
		return list;
	}
}
