import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api.service';
import { AuthService } from 'src/app/services/auth.service';
import { faUserCircle, faInfo } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  public faInfo = faInfo;
  public faUserCircle = faUserCircle;
  public message = 'status: logged out';
  private route = '/dashboard';
  public signInSelected = true;

  constructor(public authService: AuthService, public router: Router, public apiService: ApiService) { }

  ngOnInit() {
    this.checkLoginStatus();
  }

  async checkLoginStatus() {
    if(await this.authService.getIsLoggedIn()) {
      this.message = 'status: logged in';
      this.router.navigate([this.route]);
    } else {
      this.message = '';
    }
  }

  async login(isGuest: boolean) {
    if (isGuest) {
      this.message = 'Logging in as Guest...';
      sessionStorage.setItem('token', 'guest');
      this.router.navigate([this.route]);
      return;
    }

    await this.authService.authenticate();
    this.authService.getUserId().subscribe((idToken) => {
      this.message = 'Logging in...';
      this.apiService.validateUserSession(idToken).subscribe(
        resp => {
          sessionStorage.setItem('token', idToken);
          this.router.navigate([this.route]);
        },
        err => {
          this.authService.logout();
          this.message = 'Error logging in. Please try again or contact support.';
        });
    });
  }

  logout() {
    this.router.navigate([this.route]);
  }

  signInTabClick() {
    this.signInSelected = true;
  }

  infoTabClick() {
    this.signInSelected = false;
  }


}
