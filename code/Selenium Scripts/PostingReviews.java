package AutomationTest;
import org.testng.annotations.Test;
import org.testng.annotations.Test;
import org.testng.AssertJUnit;
import org.testng.annotations.Test;
import org.testng.AssertJUnit;

import java.awt.List;
import java.util.*;
import java.util.concurrent.TimeUnit;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClientBuilder;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;



import org.testng.annotations.BeforeMethod;
import org.testng.*;
import org.apache.http.*;

import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;

import org.apache.commons.*;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;



public class PostingReviews {

WebDriver driver;
	
	@Test
  public void NormalLogin() throws InterruptedException, IOException 
	{
		
		
		
		
		try{
		Scanner inputStream= new Scanner(new FileReader("C:\\Users\\ATripathi\\Desktop\\testcase1.csv"));
		String data;
	
/*
		Reader in = new FileReader("path/to/file.csv");
		Iterable<CSVRecord> records = CSVFormat.EXCEL.withHeader().parse(in);
		for (CSVRecord record : records) {
		    String lastName = record.get("Last Name");
		    String firstName = record.get("First Name");
		}
			*/
			driver = new FirefoxDriver();
			//driver.manage().window().maximize();
			driver.get("https://yelp.com/login");
			Rest(500);
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[3]/div[1]/div/div/div[5]/div[1]/form/input[2]")).sendKeys("pichupikachu150@gmail.com");
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[3]/div[1]/div/div/div[5]/div[1]/form/input[3]")).sendKeys("test1234");
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[3]/div[1]/div/div/div[5]/div[1]/form/button")).click();
			/*if(driver.findElement(By.xpath("/html/body/div[2]/div[3]/div[2]/div/label"))!=null)
			{
			Rest(25000);
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[3]/div[1]/div/div/div[5]/div[1]/form/button")).click();
			}*/
			Rest(1500);
			
			while(inputStream.hasNextLine()){
				data= inputStream.nextLine();
				String[] urls=data.split(",");
			driver.navigate().to(urls[1]);
			Rest(1000);
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[1]/div/div[3]/div[2]/div/a")).click();
			Rest(500);
			driver.findElement(By.id("rating-"+urls[2])).click();
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[1]/div[3]/form[2]/div[2]/div[2]/div/div[2]/textarea")).sendKeys(urls[3]);
			driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[2]/div[1]/div[3]/form[2]/div[3]/div[4]/div[1]/div/p/button")).click();
			Rest(3000);
			
			System.out.println(urls[1]);
			
		
		}
		inputStream.close();
		}catch(FileNotFoundException e)
		{
			e.printStackTrace();
		}}
		
		
	
	// Rest function to make the driver wait for a desired period of time.
	public void Rest(int a) throws InterruptedException 
	{
		synchronized(driver)
		{
			driver.wait(a);
		}
		
	}
	
	
}
