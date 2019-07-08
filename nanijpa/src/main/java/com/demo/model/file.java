package com.demo.model;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class file {
	@Id
	private String fileName;

	public String getFileName() {
		return fileName;
	}

	public void setFileName(String fileName) {
		this.fileName = fileName;
	}

	@Override
	public String toString() {
		return "file [fileName=" + fileName + "]";
	}
	
	
	
	
}
