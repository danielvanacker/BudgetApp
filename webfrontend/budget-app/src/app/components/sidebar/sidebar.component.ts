import { Component, OnInit } from '@angular/core';
import { faBars, faIgloo, faCalendar } from '@fortawesome/free-solid-svg-icons'

@Component({
    selector: 'sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  public faBars = faBars;
  public menuItems: any[];
  public isCollapsed = false;

  constructor() {
    this.menuItems = [
      { path: '/dashboard', title: 'Dashboard', icon: faIgloo, class: '' },
      { path: '/calendar', title: 'Calendar', icon: faCalendar, class: '' },
    ]
   }

  ngOnInit() { }

  public onMenuButtonClick(): void {
    this.isCollapsed = !this.isCollapsed;
  }
}
