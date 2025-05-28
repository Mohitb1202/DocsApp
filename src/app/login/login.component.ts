import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  loginForm!: FormGroup;
  status: string = "";
  checkStatus: boolean=false;
  msg: string = "";
  constructor(private formBuilder:FormBuilder,private _userService:UserService,private router:Router) { }

  ngOnInit() {
    this.loginForm = this.formBuilder.group({
      emailId: [""],
      password:[""]
    })

  }

}
