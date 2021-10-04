import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, BehaviorSubject } from 'rxjs';
import { Router } from '@angular/router';
import { map } from "rxjs/operators";



@Injectable({
  providedIn: 'root'
})

export class AuthenticationService {

  private loggedIn = new BehaviorSubject<boolean>(false);

  get isLoggedIn() {
    return this.loggedIn.asObservable();
  }



  authUrl = 'http://localhost:8000/api/';

  constructor(private http:HttpClient,  private router: Router) {
  }




  registerUser(regData:any):Observable<any[]>{
    return this.http.post<any[]>(this.authUrl + 'users/', regData)
  }

  loginUser(loginData:any):Observable<any[]>{
    return this.http.post<any[]>(this.authUrl + 'auth/', loginData)
  }

  logout() {
    this.loggedIn.next(false);
    this.router.navigate(['/login']);
  }

  url = 'http://127.0.0.1:8000/api/users/'

  isAuthenticated() {
    return this.http.get(this.url + '/is-logged-in')
       .pipe(map((response:any) => {
          return response
       }))
 }





  }
