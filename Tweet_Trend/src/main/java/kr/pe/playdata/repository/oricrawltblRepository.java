package kr.pe.playdata.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import kr.pe.playdata.model.oricrawltbl;

@Repository
public interface oricrawltblRepository extends JpaRepository<oricrawltbl, String>{

}
