import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';
import { environment } from '../../../environments/environment';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public message: string = 'status: logged out'
  private route: string = '/dashboard';

  constructor(public authService: AuthService, public router: Router) { }

  ngOnInit() {
    this.checkLoginStatus();
  }

  async checkLoginStatus() {
    if(await this.authService.getIsLoggedIn()) {
      this.message = 'status: logged in';
      this.router.navigate([this.route]);
    } else {
      this.message = 'status: logged out'
    }
  }

  async login() {
    await this.authService.authenticate();
    this.router.navigate([this.route]);
  }

  logout() {
    this.router.navigate([this.route]);
  }


}
