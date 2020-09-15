import { Component, OnInit } from '@angular/core';
import { faHandHoldingUsd, faSignInAlt, faSignOutAlt, faWallet } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  public infoCards: any[] = [
    { icon: faSignInAlt, value: '$0.00', category: 'Income', colorClass: "success" },
    { icon: faSignOutAlt, value: '$0.00', category: 'Expenses', colorClass: "danger"},
    { icon: faHandHoldingUsd, value: '$0.00', category: 'Owed Money', colorClass: "warning" },
    { icon: faWallet, value: '$1,000.00', category: 'Budget Remaining', colorClass: "primary"}
  ]
  constructor() { }

  ngOnInit(): void {
  }

}
