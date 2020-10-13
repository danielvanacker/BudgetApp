import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'insert-category-form',
  templateUrl: './insert-category-form.component.html',
  styleUrls: ['../form.component.scss']
})
export class InsertCategoryFormComponent implements OnInit {

  transactionForm = new FormGroup({
    name: new FormControl('', [Validators.required]),
    transactionType: new FormControl(false, [Validators.required]),
  });

  constructor(private apiservice: ApiService) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.transactionForm.disable();
    this.apiservice.addCategory(this.transactionForm.value).subscribe(success => {
      this.transactionForm.enable();
    }, err => {
      // TODO toastr
      this.transactionForm.enable();
    });
  }

}
