import { Component,OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit{

  registerForm!: FormGroup;
  status: string[] = [];

  constructor(private formBuilder:FormBuilder,private _userService:UserService) { }

  ngOnInit() {
    this.registerForm = this.formBuilder.group({
      userName: [""],
      emailId: [""],
      contactNumber: [""],
      password: [""],
      gender:[""]
    })
  }

}
