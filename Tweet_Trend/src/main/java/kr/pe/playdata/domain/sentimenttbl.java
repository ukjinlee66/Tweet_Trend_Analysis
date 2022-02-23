package kr.pe.playdata.domain;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

import lombok.Data;

@Data
@Entity
// 테이블명 지정할 때 대문자로 작성할 것
// 만약 "testTbl" 식으로 작성하면 test db의 test_tbl 테이블 검색
// 대소문자를 구별하기 힘드므로 mysql 테이블 명도 소문자로만 작성할 것
@Table(name="SENTIMENTTBL")
public class sentimenttbl {
	
	@Id
	@Column(name="sentiment")
	private String sentiment;
	
	@Column(name="count")
	private int count;
}
