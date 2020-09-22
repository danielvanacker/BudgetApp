import { ColDef } from 'ag-grid-community'

export const TRANSACTION_GRID_COL_DEFS: ColDef[] = [
  {field: '', headerName: '', checkboxSelection: true, lockPosition: true, suppressMenu: true, maxWidth: 40, headerCheckboxSelection: true },
  {field: 'category', headerName: 'Category'},
  {field: 'amount', headerName: 'Amount'},
  {field: 'date', headerName: 'Date'},
  {field: 'comment', headerName: 'Comment'},
  {field: 'transactionGroup', headerName: 'Transaction Type'},
  {field: 'person', headerName: 'Person'}
]

export const ELAPSED_BUDGET_GRID_PARTIAL_COL_DEFS: ColDef[] = [
  {field: '', headerName: '', checkboxSelection: true, lockPosition: true, suppressMenu: true, maxWidth: 40, headerCheckboxSelection: true },
  {field: 'category', headerName: 'Category'},
  {field: 'transactionGroup', headerName: 'Transaction Group'}
]

export const DEFAULT_COL_DEF: ColDef = {
  flex: 1,
  minWidth: 100,
  filter: true,
  sortable: true
}

export const COLOR_RED: string = '#ef8157';
export const COLOR_WARN: string = '#fbc658';
export const COLOR_GREEN: string = '#6bd098';

