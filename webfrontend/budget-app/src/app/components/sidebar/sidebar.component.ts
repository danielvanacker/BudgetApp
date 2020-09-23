import { Component, OnDestroy, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { faBars, faIgloo, faCalendar, faCog, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'
import { Subscription } from 'rxjs';
import { User } from 'src/app/models/genereal.model';
import { AuthService } from 'src/app/services/auth.service';

@Component({
    selector: 'sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit, OnDestroy {
  public faBars = faBars;
  public faCog = faCog;
  public faSignOutAlt = faSignOutAlt;
  public menuItems: any[];
  public isCollapsed = false;
  public user: User;
  private subscriptions: Subscription[] = [];

  constructor(public authService: AuthService, public router: Router) {}

  ngOnInit() {
    this.menuItems = [
      { path: '/dashboard', title: 'Dashboard', icon: faIgloo, class: '' },
      { path: '/calendar', title: 'Calendar', icon: faCalendar, class: '' },
    ]
    const sub = this.authService.getUserProfile().subscribe(user => this.user = user);
    this.subscriptions.push(sub);
  }

  public onMenuButtonClick(): void {
    this.isCollapsed = !this.isCollapsed;
  }

  async logout() {
    await this.authService.logout();
    this.router.navigate([''])
  }

  public openUserSettings(): void {
    // TODO
  }

  ngOnDestroy() {
    this.subscriptions.forEach(sub => {
      sub.unsubscribe();
    })
  }
}
