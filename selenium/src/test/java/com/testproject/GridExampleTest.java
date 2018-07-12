package com.testproject;

import java.net.MalformedURLException;
import java.net.URL;


import org.testng.annotations.*; // Allows adding @Test/@BeforeTest/@AfterTest annotations
//Selenium imports:
import org.openqa.selenium.*;


import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.remote.RemoteWebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

public class GridExampleTest {

private WebDriver driver;
       @BeforeTest(alwaysRun = true)
   public void loadDriver() throws Exception {
       DesiredCapabilities capability = DesiredCapabilities.chrome();
       capability.setBrowserName("chrome");
       capability.setPlatform(Platform.LINUX);
       driver = new RemoteWebDriver(new URL("http://192.168.99.100:4444/wd/hub"), capability);
      }
         @Test
         public void exampleTestw() {
         System.out.println("####### Starting the selenium test #######");
         driver.get("http://192.168.99.1:8080");
         Assert.assertTrue("Greetings from Spring Boot!".equals(driver.findElement(By.tagName("body")).getText() ) ,"################################## Error !!! ##################################### ");
         System.out.println("####### Test result: OK #######");

            
         }
       @AfterTest(alwaysRun = true)
   public void quitDriver() throws Exception {
           driver.quit();
   }
}
