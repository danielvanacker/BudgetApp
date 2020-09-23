import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/services/auth.service';

@Component({
  selector: 'app-user-layout',
  templateUrl: './user-layout.component.html'
})
export class UserLayoutComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

}
