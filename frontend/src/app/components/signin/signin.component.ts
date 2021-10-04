import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { BehaviorSubject } from 'rxjs';


@Component({
  selector: 'app-signin',
  templateUrl: './signin.component.html',
  styleUrls: ['./signin.component.css']
})
export class SigninComponent implements OnInit {
  login:any;
  error: any;

  private loggedIn = new BehaviorSubject<boolean>(false);

  get isLoggedIn() {
    return this.loggedIn.asObservable();
  }

  constructor(
    private LoginService: AuthenticationService,
    private router: Router,
  ) { }
  ngOnInit(): void {
    this.login = {
      username: '',
      password: '',
      email: '',

    };
  }

  LoginUser(){
    this.LoginService.loginUser(this.login).subscribe( response => {
      console.log(response)
      alert('User ' + this.login.username + ' has logged in'),
      this.loggedIn.next(true);
      this.router.navigate(['services'])
    },
    error => {
      // this.error = error
      alert('Invalid User Credentials');
      console.log('error',error)
    }
    );
    this.login.reset();
  }



}
