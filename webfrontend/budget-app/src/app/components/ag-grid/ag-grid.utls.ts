import { ColDef } from 'ag-grid-community'

export const TRANSACTION_GRID_COL_DEFS: ColDef[] = [
  {field: '', headerName: '', checkboxSelection: true, lockPosition: true, suppressMenu: true, maxWidth: 40, headerCheckboxSelection: true },
  {field: 'name', headerName: 'Category'},
  {field: 'amount', headerName: 'Amount'},
  {field: 'date', headerName: 'Date'},
  {field: 'comment', headerName: 'Comment'},
  {field: 'transactiongroup', headerName: 'Transaction Type'},
  {field: 'person', headerName: 'Person'}
]

export const ELAPSED_BUDGET_GRID_BASE_COL_DEFS: ColDef[] = [
  {field: '', headerName: '', checkboxSelection: true, lockPosition: true, suppressMenu: true, maxWidth: 40, headerCheckboxSelection: true },
  {field: 'category', headerName: 'Category'},
  {field: 'transactionGroup', headerName: 'Transaction Group'}
]

export const DEFAULT_COL_DEF: ColDef = {
  flex: 1,
  minWidth: 120,
  filter: true,
  sortable: true
}

export const ELAPSED_BUDGET_GRID_DEFAULT_COL_DEF: ColDef = {
  flex: 1,
  minWidth: 120,
  filter: false,
  sortable: false
}

export const COLOR_RED: string = '#ef81577d';
export const COLOR_WARN: string = 'hsl(40deg 95% 66% / 55%)';
export const COLOR_GREEN: string = '#6bd09859';

