package kr.pe.playdata.config;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import springfox.documentation.annotations.ApiIgnore;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

@Configuration
@EnableSwagger2
public class SwaggerConfig 
{
	@Bean
	public Docket swaggerapi()
	{
		return new Docket(DocumentationType.SWAGGER_2).ignoredParameterTypes(ApiIgnore.class)
        		.apiInfo(apiInfo()).select()
                .apis(RequestHandlerSelectors.basePackage("kr.pe.playdata.controller"))
                .build()
                .useDefaultResponseMessages(false); 
	}
	private ApiInfo apiInfo() 
	{
		return new ApiInfoBuilder()
				.title("API Doc")
				.description("Swagger Config ApiInfo")
				.license("license : Min-Sim").licenseUrl("http://www.naver.com").build();
	}
}
