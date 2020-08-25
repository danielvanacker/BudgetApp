import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup } from '@angular/forms';
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
    date: new FormControl(''),
    amount: new FormControl(0),
    comment: new FormControl(''),
    category: new FormControl(''),
    paidBy: new FormControl(''),
    person: new FormControl('No one'),
    myPortion: new FormControl(''),
  })

  constructor(private apiservice: ApiService) {

  }

  ngOnInit(): void {
    this.apiservice.getCategories().subscribe((data: any) => {
      this.categories = data.map(category => {
        return [category[0], category[1] === 1 ? 'Income' : 'Expense'];
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
    this.apiservice.addTransaction(this.transactionForm.value).subscribe();
  }

  public isSplitTransaction(): boolean {
    const splitWith = this.transactionForm.value.person;
    if(splitWith === 'No one' || splitWith === '') {
      return false;
    }
    return true;
  }

}
