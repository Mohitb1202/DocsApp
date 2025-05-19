import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { UserService } from '../Polyclinic-services/user-service/user.service';
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
  submitForm(form: FormGroup) {
    this._userService.validateLogin(form.value.emailId, form.value.password).subscribe(
      responseLoginData=>{
        this.status = responseLoginData.toString();
        console.log(this.status);
        if (this.status != "try with valid credentials") {
          sessionStorage.setItem('userName', this.status);
          console.log(this.status);
          alert("Login successful");
          this.router.navigate(['/home']);
        }
        else {
          this.checkStatus = true;
          this.msg = "Try with valid credentials";
          alert("Invalid Credentials");

        }

      }
    )

  }

}
