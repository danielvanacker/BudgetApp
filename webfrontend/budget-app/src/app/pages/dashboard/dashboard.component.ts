import { ApiService } from './../../services/api.service';
import { Component, OnInit } from '@angular/core';
import { faHandHoldingUsd, faSignInAlt, faSignOutAlt, faWallet } from '@fortawesome/free-solid-svg-icons';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  public month: number;
  public infoCards: any[] = [
    { icon: faSignInAlt, value: '$0.00', category: 'Income', colorClass: "success" },
    { icon: faSignOutAlt, value: '$0.00', category: 'Expenses', colorClass: "danger"},
    { icon: faHandHoldingUsd, value: '$0.00', category: 'Owed Money', colorClass: "warning" },
    { icon: faWallet, value: '$1,000.00', category: 'Budget Remaining', colorClass: "primary"}
  ];
  private formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
  });

  constructor(public apiService: ApiService) { }

  ngOnInit(): void {
    const date = new Date();
    this.month = date.getMonth() + 1;

    this.apiService.getMonthlyIncome(this.month).subscribe((data: number) => {
      this.infoCards[0].value = this.formatter.format(data);
    });

    this.apiService.getMonthlyExpenses(this.month).subscribe((data: number) => {
      this.infoCards[1].value = this.formatter.format(data);
    });

    this.apiService.getOwedMoney().subscribe((data: number) => {
      this.infoCards[2].value = this.formatter.format(data);
    });

    this.apiService.getBudgetRemaining(this.month, date.getFullYear()).subscribe((data: number) => {
      this.infoCards[3].value = this.formatter.format(data);
    });
  }



}
