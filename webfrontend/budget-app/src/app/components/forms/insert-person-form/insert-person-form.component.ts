import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'insert-person-form',
  templateUrl: './insert-person-form.component.html',
  styleUrls: ['../form.component.scss']
})
export class InsertPersonFormComponent implements OnInit {

  transactionForm = new FormGroup({
    name: new FormControl('', [Validators.required]),
  });

  constructor(private apiservice: ApiService) { }

  ngOnInit(): void {
  }

  onSubmit(): void {
    this.transactionForm.disable();
    this.apiservice.addPerson(this.transactionForm.value).subscribe(success => {
      console.log(success);
      this.transactionForm.enable();
    }, err => {
      // TODO toastr
      this.transactionForm.enable();
    });
  }

}
