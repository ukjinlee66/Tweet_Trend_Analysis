package kr.pe.playdata.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.scheduling.annotation.EnableAsync;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import kr.pe.playdata.domain.Candi;
import kr.pe.playdata.domain.Senti;
import kr.pe.playdata.domain.View;

@Controller
@EnableAsync
@EnableAutoConfiguration
@ComponentScan(basePackages = "com.henryxi.async")
public class maincontroller 
{
	
	//후보자 리스트 호출
	@GetMapping("GetCandi")
	public List<Candi> get_candi_list()
	{
		List<Candi> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new Candi());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	//감성 리스트 호출.
	@GetMapping("GetSenti")
	public List<Senti> get_senti_list()
	{
		List<Senti> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new Senti());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	//트위터 리스트 호출.
	@GetMapping("GetView")
	public List<View> get_view_list()
	{
		List<View> all = new ArrayList<>();
		for (int i=1;i<11;i++)
			all.add(new View());
		return all; // JSON 배열 형식으로 문자열 반환(JSON.parse()로 JSON 객체로 실 변환)
	}
	@GetMapping("/")
	public String mainPage(Model model) 
	{
		
		/*
		 * 최신 트위터 리스트를 불러온다.
		 */
		
		
		//////////////////////////////////////
		
		/*
		 * 감성 분석 결과를 불러온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 총 데이터 수를 불러온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 막대그래프 정보를 받아온다.
		 */
		
		//////////////////////////////////////
		
		/*
		 * 워드클라우드 이미지를 불러온다.
		 */
		
		//////////////////////////////////////
		return "MainPage";
	}
}