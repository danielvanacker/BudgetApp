import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

@Component({
  selector: 'transaction-form',
  templateUrl: './transaction-form.component.html',
  styleUrls: ['./transaction-form.component.css']
})

export class TransactionFormComponent implements OnInit {
  public categories: string[];
  transactionForm = new FormGroup({
    date: new FormControl(''),
    amount: new FormControl(0),
    comment: new FormControl(''),
    category: new FormControl('')
  })

  constructor() {
    this.categories = ['a', 'b']
    console.log(this.categories)
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    console.log(this.transactionForm.value)
  }

}
