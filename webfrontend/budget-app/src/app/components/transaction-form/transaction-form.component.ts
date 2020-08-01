import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';

export const HEROES: any[] = [
  { id: 11, name: 'Dr Nice' },
  { id: 12, name: 'Narco' },
  { id: 13, name: 'Bombasto' },
  { id: 14, name: 'Celeritas' },
  { id: 15, name: 'Magneta' },
  { id: 16, name: 'RubberMan' },
  { id: 17, name: 'Dynama' },
  { id: 18, name: 'Dr IQ' },
  { id: 19, name: 'Magma' },
  { id: 20, name: 'Tornado' }
];

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
