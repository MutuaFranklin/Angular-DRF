import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { map, take } from 'rxjs/operators';
import { AuthenticationService } from '../services/authentication.service';
import { SigninComponent } from '../components/signin/signin.component';


@Injectable({
  providedIn: 'root'
})
export class GuardGuard implements CanActivate {
  constructor(
    private authService: AuthenticationService,
    private router: Router
  ) {}

  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      return this.authService.isLoggedIn
      .pipe(
        take(1),
        map((isLoggedIn: boolean) => {
          if (!isLoggedIn){
            this.router.navigate(['/signin']);
            return false;
          }
          return true;
        })
      )
  }

}
