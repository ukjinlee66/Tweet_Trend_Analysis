package kr.pe.playdata.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import kr.pe.playdata.domain.Candi;
import kr.pe.playdata.domain.Senti;
import kr.pe.playdata.domain.View;

@Controller
public class maincontroller 
{
	@GetMapping("/")
	public String mainPage(Model model) 
	{
		return "MainPage";
	}
}