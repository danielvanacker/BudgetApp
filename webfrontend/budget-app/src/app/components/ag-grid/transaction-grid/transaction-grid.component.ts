import { Component, OnInit } from '@angular/core';
import { GridOptions, ColDef } from 'ag-grid-community';
import { DEFAULT_COL_DEF, TRANSACTION_GRID_COL_DEFS } from '../ag-grid.utls';
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
  defaultColDef: ColDef;
  rowSelection: string;

  constructor(private apiservice: ApiService) {
    this.columnDefs = TRANSACTION_GRID_COL_DEFS;
    this.defaultColDef = DEFAULT_COL_DEF;
    this.rowSelection = "multiple";
    this.apiservice.getAllTransactions().pipe(take(1)).subscribe((data) => {
      this.rowData = data.transactions;
    });
  }

  ngOnInit(): void {}

  public onGridReady(): void {}

}
