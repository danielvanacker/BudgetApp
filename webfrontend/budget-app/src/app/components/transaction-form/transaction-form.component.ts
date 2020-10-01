import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';
import { isEmptyNullUndefined, myPortionValidator } from './transaction-form.utils';

@Component({
  selector: 'transaction-form',
  templateUrl: './transaction-form.component.html',
  styleUrls: ['./transaction-form.component.scss']
})

export class TransactionFormComponent implements OnInit {
  public categories: string[];
  public people: string[];
  transactionForm = new FormGroup({
    date: new FormControl('', [Validators.required]),
    amount: new FormControl(0, [Validators.required]),
    comment: new FormControl(''),
    category: new FormControl('', [Validators.required]),
    person: new FormControl('No one'),
    myPortion: new FormControl(''),
  }, { validators: myPortionValidator });

  constructor(private apiservice: ApiService) {

  }

  ngOnInit(): void {
    this.apiservice.getCategories().subscribe((data: any) => {
      this.categories = data.map(category => {
        return [category[0], category[1], category[2] === true ? 'Income' : 'Expense'];
      });
    });
    this.apiservice.getPeople().subscribe((data: any) => {
      this.people = data.map(person => {return person[0]});
      console.log(this.people);
      this.people.push('No one');
    });
  }

  onSubmit(): void {
    console.log(this.transactionForm.value);
    this.apiservice.addTransaction(this.transactionForm.value).subscribe(success => {
      console.log(success);
    }, err => {

    });
  }

  public isNotIncome(): boolean {
    const category = this.transactionForm.value.category;
    return isEmptyNullUndefined(category) || category[2] === 'Expense';
  }

  public isSplitTransaction(): boolean {
    const splitWith = this.transactionForm.value.person;
    if(splitWith === 'No one' || splitWith === '') {
      return false;
    }
    return true;
  }

}
