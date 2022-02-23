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
	// http://ip:port/hello
	// http://localhost:80/hello
	// Get - 검색
	@GetMapping("hello")
	public String m1() {
		// ...
		System.out.println("get");
		return "get";
	}

	// Post - 수정
	@PostMapping("hello")
	public String m2() {
		// ...
		System.out.println("post");
		return "post";
	}

	// Put - 생성
	@PutMapping("hello")
	public String m3() {
		// ...
		System.out.println("put");
		return "put";
	}

	// Delete - 삭제
	@DeleteMapping("hello")
	public String m4() {
		// ...
		System.out.println("delete");
		return "delete";
	}
}
