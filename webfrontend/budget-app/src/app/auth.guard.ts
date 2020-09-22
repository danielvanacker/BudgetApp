import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, Router } from '@angular/router';
import { AuthService } from './services/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  async canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Promise<boolean> {
      return await this.checkLogin(state.url);
    }

  async checkLogin(url: string): Promise<boolean> {
    if(await this.authService.getIsLoggedIn()) {
      return true;
    }

    this.router.navigate(['/login']);
    return false;
  }

}
