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
 
 
 
public class CheckingReviews {
 
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
                                                driver.get("https://yelp.com");
                                                Rest(500);
                                
                                                int i=0;
                                                
                                                while(inputStream.hasNextLine()){
                                                                data= inputStream.nextLine();
                                                                String[] urls=data.split(",");
                                                driver.navigate().to(urls[1]);
                                                Rest(600);
                                                driver.findElement(By.className("dropdown_toggle-action")).click();
                                                Rest(200);
                                
                                                driver.findElement(By.xpath("/html/body/div[2]/div[3]/div/div[2]/div/div/div[1]/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/div/div/div[2]/div/ul/li[2]/a")).click();
                                                
                                                Rest(1000);
                                                                               
                                                
                                                if(driver.getPageSource().contains("Neal G"))
                                                {
                                                                System.out.println(urls[1]);
                                                                i=i+1;
                                                }                             
                                }
                                                
                                System.out.println("Total number of remaining reviews: "+i);     
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