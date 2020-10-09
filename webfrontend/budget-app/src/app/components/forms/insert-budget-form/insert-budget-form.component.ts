import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';
import { yearValidator } from '../form.utils';

@Component({
  selector: 'insert-budget-form',
  templateUrl: './insert-budget-form.component.html',
  styleUrls: ['../form.component.scss']
})
export class InsertBudgetFormComponent implements OnInit {

  public categories: string[];
  public months: any[] = [{name: 'Jan', index: 1}, {name: 'Feb', index: 2}, {name: 'Mar', index: 3}, {name: 'Apr', index: 4}, {name: 'May', index: 5}, {name: 'Jun', index: 6}, {name: 'Jul', index: 7}, {name: 'Aug', index: 8}, {name: 'Sep', index: 9}, {name: 'Oct', index: 10}, {name: 'Nov', index: 11}, {name: 'Dec', index: 12}]

  transactionForm = new FormGroup({
    month: new FormControl('', [Validators.required]),
    year: new FormControl(0, [Validators.required]),
    amount: new FormControl('', [Validators.required]),
    comment: new FormControl(''),
    category: new FormControl('', [Validators.required])
  }, { validators: yearValidator });

  constructor(private apiservice: ApiService) {

  }

  ngOnInit(): void {
    this.apiservice.getCategories().subscribe((data: any) => {
      this.categories = data.map(category => {
        return [category[0], category[1], category[2] === true ? 'Income' : 'Expense'];
      });
    });
  }

  onSubmit(): void {
    this.transactionForm.disable();
    this.apiservice.addBudget(this.transactionForm.value).subscribe(success => {
      this.transactionForm.enable();
    }, err => {
      // TODO Toastr
      this.transactionForm.enable();
    });
  }

}
