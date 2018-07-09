package com.testproject;

import junit.framework.TestCase;
import org.junit.Assert;

public class CalculatorTest extends TestCase {

    public void testSum() {
        Calculator calculator = new Calculator();
        int sum = calculator.sum(1, 2);
        Assert.assertEquals(3, sum);
    }
}