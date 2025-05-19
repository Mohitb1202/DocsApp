import { Component,OnInit } from '@angular/core';
import { FormBuilder, FormGroup, FormControl } from '@angular/forms';
import { UserService } from '../Polyclinic-services/user-service/user.service';
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

  submitForm(form: FormGroup) {
    this._userService.register(form.value.userName, form.value.emailId, form.value.contactNumber, form.value.password, form.value.gender).subscribe(
      responseRegisterData => {
        this.status = responseRegisterData;
        console.log(this.status);
        alert("Registration successful")
      }
    )
  }

}
