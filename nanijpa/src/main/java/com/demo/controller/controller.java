package com.demo.controller;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import com.demo.dao.fileRepo;
import com.demo.dao.loginRepo;
import com.demo.dao.signupRepo;
import com.demo.dao.sqlData;
import com.demo.model.signup;
import com.demo.model.file;

@Controller

public class controller {
	
	private static String UPLOADED_FOLDER = "D:/upload/";
	
	@Autowired private loginRepo lr;
	
	
	
	@Autowired
	private signupRepo su;
	
	@Autowired
	private fileRepo fr;

	/*
	 * @RequestMapping("/") public String home(Model model) throws
	 * ClassNotFoundException, SQLException { System.out.println("Inside /");
	 * 
	 * return "signup"; }
	 */
	
	@RequestMapping("/")
	public String file(Model model) throws ClassNotFoundException, SQLException
	{
		System.out.println("Inside /file");
		System.out.println("Inside / function");
		ModelAndView mv = new ModelAndView();
		sqlData sql = new sqlData();
	//	model.addAttribute("fileNames", sql.getData());
		//mv.addObject("fileNames",sql.getData());
		//sql.getData();
		return "fileUpload";
	}
	@RequestMapping("/fileUpload")
	@ResponseBody
	public String allFileUpload(@RequestParam(value="file") MultipartFile multiPartFile,@RequestParam(value="folderName") String folderName) throws IOException {
		System.out.println("inside fileUpload function");
		byte[] bytes=multiPartFile.getBytes();
		File folder = new File(UPLOADED_FOLDER+folderName);
		folder.mkdirs();
		Path path = Paths.get(UPLOADED_FOLDER+folderName+"\\");
		Files.write(path, bytes);

		return "success";
    }

    @GetMapping("/uploadStatus")
    public String uploadStatus() {
        return "uploadStatus";
    }

	@RequestMapping(value="/getFileName",method=RequestMethod.POST)
	@ResponseBody
	public List<file> getFileNames() throws ClassNotFoundException, SQLException 
	{
		
		System.out.println("inside getFileName");
		sqlData sql = new sqlData();
		List<file> files=sql.getData();
		return files;
	}
	@RequestMapping(value="/GetAllDetails",method=RequestMethod.GET)
	@ResponseBody
	public String GetAllDetails() throws ClassNotFoundException, SQLException 
	{
		ModelAndView mv = new ModelAndView();
		System.out.println("inside GetAllDetails");
		System.out.println(su.findById(1));
		System.out.println(fr.findAll());
		sqlData sql = new sqlData();
	//	System.out.println(sql.getData());
		return su.findAll().toString();
	}
	
	@RequestMapping(value="/Details/{employeeid}", method=RequestMethod.GET)
	@ResponseBody
	public String Details(@PathVariable int employeeid) 
	{
		ModelAndView mv = new ModelAndView();
		System.out.println("inside login");
		System.out.println(employeeid);
		return su.findById(employeeid).toString();
	}
}

