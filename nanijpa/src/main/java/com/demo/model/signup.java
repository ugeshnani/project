package com.demo.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class signup {
	@Id
	private int employeeid;
	private String username;
	private String address;
	private String phonenumber;
	public int getEmployeeid() {
		return employeeid;
	}
	public void setEmployeeid(int employeeid) {
		this.employeeid = employeeid;
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getPhonenumber() {
		return phonenumber;
	}
	public void setPhonenumber(String phonenumber) {
		this.phonenumber = phonenumber;
	}
	@Override
	public String toString() {
		return "signup [employeeid=" + employeeid + ", username=" + username + ", address=" + address + ", phonenumber="
				+ phonenumber + "]";
	}


}