package com.demo.mapper;

import java.sql.ResultSet;
import java.sql.SQLException;
import org.springframework.jdbc.core.RowMapper;

import com.demo.model.file;

public class fileMapper implements RowMapper<file> {
   public  file mapRow(ResultSet rs, int rowNum) throws SQLException {
      file fi = new file();
      
      fi.setFileName("FILE_NAME");
      System.out.println(fi.getFileName());
      System.out.println();
      return fi;
   }
}
