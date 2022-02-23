package kr.pe.playdata.func;

import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.util.Base64;
import java.util.List;

import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.PostMapping;

import kr.pe.playdata.domain.Candi;
import kr.pe.playdata.domain.Senti;
import kr.pe.playdata.domain.View;

@Service
public class GetDataImpl implements GetData 
{
	@Async("threadPoolExecutor")
	public List<View> show_tweet_list()
	{
		List<View> tw_list;
		return tw_list;
	}
	
	@Async("threadPoolExecutor")
	public List<Candi> show_candi_list()
	{
		List<Candi> ca_list;
		return ca_list;
	}
	
	@Async("threadPoolExecutor")
	public List<Senti> show_Senti_list()
	{
		List<Senti> se_list;
		return se_list;
	}
	
	@Async("threadPoolExecutor")
	@PostMapping("img")
	public String uploadImage(String image) throws FileNotFoundException
	{
		System.out.println("uploadImage on");
	    String result = "false";
	    FileOutputStream fos;

	    fos = new FileOutputStream("img/word.jpg");

	    // decode Base64 String to image
	    try
	    {

	        byte byteArray[] = Base64.getMimeDecoder().decode(image);
	        fos.write(byteArray);

	        result = "true";
	        fos.close();
	    }
	    catch (Exception e)
	    {
	        e.printStackTrace();
	    }
	    System.out.println("uploadImage off");
	    return result;
	}
}
