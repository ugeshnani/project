package com.demo.dao;

import org.springframework.data.repository.CrudRepository;

import com.demo.model.signup;

public interface signupRepo extends CrudRepository<signup ,Integer>
{
	
}
