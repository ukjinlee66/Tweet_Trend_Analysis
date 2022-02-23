package kr.pe.playdata.domain;
import lombok.Data;

@Data
public class Candi 
{
	private String	sentiment;
	private int		LJMcnt;
	private int		ACScnt;
	private int		YSYcnt;
	private int		SSJcnt;
	private int		HGYcnt;
}
