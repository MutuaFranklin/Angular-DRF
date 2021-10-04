import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  register:any;
  error: any;

  private loggedIn = new BehaviorSubject<boolean>(false);

  get isLoggedIn() {
    return this.loggedIn.asObservable();
  }


  constructor(
    private RegisterService: AuthenticationService,
    private router: Router,
  ) { }



  ngOnInit(): void {

    this.register = {
      username: '',
      password: '',
      email: '',

    };
  }

  registerUser(){
    this.RegisterService.registerUser(this.register).subscribe( response => {
      console.log(response)
      alert('User ' + this.register.username + ' has been created'),
      this.loggedIn.next(true);
      this.router.navigate(['signin'])

    },

    error => {
      this.error = error
      console.log('error',error)
    }
    );
  }



}
