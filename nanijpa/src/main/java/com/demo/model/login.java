package com.demo.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class login {
	
	@Id
	private String username;
	private String password;
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	@Override
	public String toString() {
		return "login [username=" + username + ", password=" + password + "]";
	}
	
}
