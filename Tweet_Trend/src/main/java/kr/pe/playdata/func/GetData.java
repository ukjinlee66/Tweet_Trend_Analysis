package kr.pe.playdata.func;

import java.io.FileNotFoundException;
//import java.sql.SQLException;
//import java.util.List;
//
//import org.springframework.stereotype.Service;
//
//import kr.pe.playdata.domain.Candi;
//import kr.pe.playdata.domain.Senti;
//import kr.pe.playdata.domain.View;

public interface GetData 
{
//	public List<View> show_tweet_list();
//	public List<Candi> show_candi_list();
//	public List<Senti> show_Senti_list();
	public String uploadImage(String image) throws FileNotFoundException;
}
