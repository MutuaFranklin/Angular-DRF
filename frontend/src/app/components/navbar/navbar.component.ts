import { Component, OnInit } from '@angular/core';
import { MainService } from 'src/app/services/main.service';
import { AuthenticationService } from 'src/app/services/authentication.service';
import { Services } from 'src/app/models/services';
import { BehaviorSubject, Observable } from 'rxjs';




@Component({
  selector: 'app-navbar',
  templateUrl: './navbar.component.html',
  styleUrls: ['./navbar.component.css']
})
export class NavbarComponent implements OnInit {
  services!:Services[];


  isLoggedIn$!: Observable<boolean>;

  constructor(private mainService:MainService, private authService: AuthenticationService) { }

  ngOnInit(): void {
    this.isLoggedIn$ = this.authService.isLoggedIn
  }

  onLogout(){
    this.authService.logout();
  }

  isAuthenticated() {
    this.authService.isAuthenticated();
 }

  searchService(input:string){
    if(input){
      console.log(input)
      this.mainService.searchService(input).toPromise().then((response:any)=>{
        if(response){
          console.log(response)
          this.services = response;
        }
        else{
          alert('Nothing found on ' + input)
        }
      });
    }
  }

}
