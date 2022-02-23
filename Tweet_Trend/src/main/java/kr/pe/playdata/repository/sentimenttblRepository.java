package kr.pe.playdata.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import kr.pe.playdata.domain.sentimenttbl;

@Repository
public interface sentimenttblRepository extends JpaRepository<sentimenttbl, String>{

}
