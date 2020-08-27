import { Component, OnInit } from '@angular/core';
import { GridOptions, ColDef } from 'ag-grid-community';
import { TRANSACTION_GRID_COL_DEFS } from '../ag-grid.utls';
import { ApiService } from 'src/app/services/api.service';
import { take } from 'rxjs/operators';


@Component({
  selector: 'transaction-grid',
  templateUrl: './transaction-grid.component.html',
  styleUrls: ['./transaction-grid.component.scss']
})
export class TransactionGridComponent implements OnInit {
  gridOptions: GridOptions;
  columnDefs: ColDef[];
  rowData: any[];

  constructor(private apiservice: ApiService) {
    this.columnDefs = TRANSACTION_GRID_COL_DEFS;
    this.apiservice.getAllTransactions().pipe(take(1)).subscribe((data) => {
      console.log(data.transactions)
      this.rowData = data.transactions;
    });
  }

  ngOnInit(): void {}

  public onGridReady(): void {}

}
