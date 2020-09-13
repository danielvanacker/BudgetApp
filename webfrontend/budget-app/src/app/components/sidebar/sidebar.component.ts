import { Component, OnInit, Input } from '@angular/core';

@Component({
    selector: 'sidebar',
    templateUrl: './sidebar.component.html',
    styleUrls: ['./sidebar.component.scss']
})
export class SidebarComponent implements OnInit {
  public menuItems: any[];

  constructor() {
    this.menuItems = [
      { path: '/dashboard', title: 'Dashboard', icon:'nc-diamond', class: '' },
      { path: '/calendar', title: 'Calendar', icon:'nc-diamond', class: '' },
    ]
   }

  ngOnInit() { }
}
