import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, FormControlDirective } from '@angular/forms';
import * as _ from 'lodash';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'transaction-form',
  templateUrl: './transaction-form.component.html',
  styleUrls: ['./transaction-form.component.css']
})

export class TransactionFormComponent implements OnInit {
  public categories: string[];
  public people: string[];
  transactionForm = new FormGroup({
    incomeOrExpense: new FormControl(''),
    date: new FormControl(''),
    amount: new FormControl(0),
    comment: new FormControl(''),
    category: new FormControl(''),
    paidBy: new FormControl(''),
    person: new FormControl(''),
    myPortion: new FormControl(''),
  })

  constructor(private apiservice: ApiService) {

  }

  ngOnInit(): void {
    this.apiservice.getCategories().subscribe((data: any) => {
      this.categories = data;
    });
    this.apiservice.getCategories().subscribe((data: any) => {
      this.people = data;
    });
  }

  onSubmit(): void {
    console.log(this.transactionForm.value)
  }

  public isSplitTransaction(): boolean {
    const splitWith = _.get(this.transactionForm, 'value.person', '').toLowerCase();
    if(splitWith === 'me' || splitWith === '') {
      return false;
    }
    return true;
  }

}
