package kr.pe.playdata.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import kr.pe.playdata.domain.Candi;
import kr.pe.playdata.domain.Senti;
import kr.pe.playdata.domain.View;

@RestController
public class dbController {
	// 후보자 리스트 호출
	@GetMapping("GetCandi")
	public List<Candi> get_candi_list() {
		List<Candi> all = new ArrayList<>();
		for (int i = 1; i < 11; i++)
			all.add(new Candi());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}

	// 감성 리스트 호출.
	@GetMapping("GetSenti")
	public List<Senti> get_senti_list() {
		List<Senti> all = new ArrayList<>();
		for (int i = 1; i < 11; i++)
			all.add(new Senti());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}

	// 트위터 리스트 호출.
	@GetMapping("GetView")
	public List<View> get_view_list() {
		List<View> all = new ArrayList<>();
		for (int i = 1; i < 11; i++)
			all.add(new View());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
}
