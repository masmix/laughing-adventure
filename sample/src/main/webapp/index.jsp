<html>
<body>
<h2>Hello, Calculator!!! </h2>
<%@ page import="com.testproject.Calculator" %><%
Calculator calculator = new Calculator();
int sum = calculator.sum(1, 2);
out.print("1 + 2 = " + sum);
%>

</body>
</html>
