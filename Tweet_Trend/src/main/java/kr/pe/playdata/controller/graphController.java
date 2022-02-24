package kr.pe.playdata.controller;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class graphController {
	@GetMapping("hello")
	public String m1() {
		int val = (int)(Math.random()*10);
		System.out.println(val);
		return Integer.toString(val);
	}
}
