import { Component, OnInit } from '@angular/core';
import { ColDef } from 'ag-grid-community/dist/lib/entities/colDef';
import { GridOptions } from 'ag-grid-community/dist/lib/main';
import { take } from 'rxjs/operators';
import { ApiService } from 'src/app/services/api.service';
import { COLOR_GREEN, COLOR_RED, COLOR_WARN, DEFAULT_COL_DEF, ELAPSED_BUDGET_GRID_PARTIAL_COL_DEFS } from '../ag-grid.utls';

@Component({
  selector: 'elapsed-budget-grid',
  templateUrl: './elapsed-budget-grid.component.html',
  styleUrls: ['./elapsed-budget-grid.component.css']
})
export class ElapsedBudgetGridComponent implements OnInit {
  gridOptions: GridOptions;
  columnDefs: ColDef[];
  rowData: any[];
  defaultColDef: ColDef;
  rowSelection: string;
  rowClassRules: any;

  constructor(private apiservice: ApiService) {}

  ngOnInit(): void {
    this.defaultColDef = DEFAULT_COL_DEF;
    this.rowSelection = "multiple";
    this.getColumnDefs();
  }

  public onGridReady(): void {}

  private getColumnDefs(): void {
    this.apiservice.getTransactionMonths().pipe(take(1)).subscribe((months: string[]) => {
      const colDefs: ColDef[] = ELAPSED_BUDGET_GRID_PARTIAL_COL_DEFS;
      months.map(month => {
        colDefs.push({field: month, headerName: month, cellStyle: this.getCellStyle});
      });
      this.columnDefs = colDefs;
      this.getGridData()
    }, error => {
      console.log(error)
    });
  }

  private getCellStyle(params: any): any {
    if(params.node.data.category !== 'Net Income (Out)') {
      return;
    }
    const colVal = Number(params.data[params.colDef.field]);
    if(colVal < 0) {
      return { 'background-color': COLOR_RED }
    } else if(colVal === 0) {
      return { 'background-color': COLOR_WARN }
    } else if(colVal > 0) {
      return { 'background-color': COLOR_GREEN }
    }
  }

  private getGridData(): void {
    this.apiservice.getElapsedBudget().pipe(take(1)).subscribe((data) => {
      console.log(data)
      this.rowData = data;
    });
  }

  public getRowStyle(params): any {
    if(params.data.category === 'Total Income'){
      //return {'border-bottom': '2px solid #6bd098'}
      return { 'background-color': COLOR_GREEN }
    } else if(params.data.category === 'Total Expenses') {
      //return {'border-bottom': '2px solid #ef8157'}
      return { 'background-color': COLOR_RED }
    }
  }
}
