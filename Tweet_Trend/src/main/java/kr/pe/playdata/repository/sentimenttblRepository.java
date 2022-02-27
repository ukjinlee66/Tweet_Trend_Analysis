package kr.pe.playdata.repository;

import java.util.List;

import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import kr.pe.playdata.model.canditbl;
import kr.pe.playdata.model.sentimenttbl;

@Repository
public interface sentimenttblRepository extends JpaRepository<sentimenttbl, String>{
}
