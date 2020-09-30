import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { ApiService } from './services/api.service';
import { AuthService } from './services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  async canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Promise<boolean> {
      return await this.checkLogin();
    }

  async checkLogin(): Promise<boolean> {
    if(await this.authService.getIsLoggedIn()) {
      const token = sessionStorage.getItem('token');
      if(token === 'invalid' || token === undefined || token === null) {
        this.authService.getUserId().subscribe((userId) => {
          sessionStorage.setItem('token', userId);
        });
      }
      return true;
    }

    this.router.navigate(['/login']);
    return false;
  }

}
