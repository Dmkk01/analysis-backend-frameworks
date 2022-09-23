package net.mditech.springquestionbank.controller;

import java.math.BigInteger;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

import org.springframework.http.MediaType;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class SpringQuestionBankController {


	@RequestMapping("/fibonacci")
	@ResponseBody
	Map<Number, Number> fibonacci() {
	  Map<Number, Number> map = new HashMap<>();  

	  BigInteger  n1 = new BigInteger("0");
	  BigInteger  n2 = new BigInteger("1");
	  BigInteger  nextTerm = new BigInteger("1");
	  for (int i = 1; i < 1001; i++) {
		nextTerm = n1.add(n2);
		n1 = n2;
		n2 = nextTerm;
		map.put(i, n1);
	  } 
	  return map;
	}

	@RequestMapping("/hello")
	@ResponseBody
	Map<String, String> hello() {
	  return Collections.singletonMap("message", "Hello World");
	}

	@RequestMapping("/")
	@ResponseBody
	String home() {
		return "health check";
	}
}
