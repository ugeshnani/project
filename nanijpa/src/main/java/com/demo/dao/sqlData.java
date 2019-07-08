package com.demo.dao;

import java.sql.*;
import java.util.*;

import com.demo.mapper.fileMapper;
import com.demo.model.file;



import org.apache.catalina.LifecycleListener;
import javax.sql.DataSource;
import org.springframework.jdbc.core.JdbcTemplate;

public class sqlData {

	
	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";  
	   static final String DB_URL = "jdbc:mysql://127.0.0.1:3306/mydb";

	   //  Database credentials
	   static final String USER = "root";
	   static final String PASS = "root";

	   private DataSource dataSource;
	   private JdbcTemplate jdbcTemplateObject;
	   
	   public void setDataSource(DataSource dataSource) {
	      this.dataSource = dataSource;
	      this.jdbcTemplateObject = new JdbcTemplate(dataSource);
	   }
	public List<file> getData() throws ClassNotFoundException, SQLException {

			
			Connection con = null;
			Statement stmt = null;
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb",USER,PASS); 
			
			stmt = con.createStatement(); 
			String sql= "Select FILE_NAME from file";
			ResultSet rs=stmt.executeQuery(sql); 
			List<file> files=new ArrayList<file>();

			while(rs.next()) {
			   file fi = new file();      
			  
			   fi.setFileName(rs.getString("FILE_NAME"));
			   System.out.println( fi.getFileName());
			   System.out.println(fi.toString());
			  files.add(fi);
			} 
			
			
			System.out.println(files.toString());
			
			return files; 
		/*
		 * System.out.println("printing ResultSetMetaData");
		 *  ResultSet rs=
		 * stmt.executeQuery(sql); //List<file> file=rs.getMetaData();
		 * //ResultSetMetaData // System.out.println(li.toString()); while(rs.next()) {
		 * String fName = rs.getString("FILE_NAME"); System.out.println(fName);
		 * 
		 * } return li;
		 */

	}

}
