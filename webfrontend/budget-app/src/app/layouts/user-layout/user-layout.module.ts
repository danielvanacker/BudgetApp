import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AgGridModule } from 'ag-grid-angular';
import { DashboardComponent } from 'src/app/pages/dashboard/dashboard.component';
import { TransactionGridComponent } from 'src/app/components/ag-grid/transaction-grid/transaction-grid.component';
import { RouterModule } from '@angular/router';
import { UserLayoutRoutes } from './user-layout.routing';
import { CalendarComponent } from 'src/app/pages/calendar/calendar.component';
import { InfoCardComponent } from 'src/app/components/info-card/info-card.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { ElapsedBudgetGridComponent } from 'src/app/components/ag-grid/elapsed-budget-grid/elapsed-budget-grid.component';
import { TransactionFormComponent } from 'src/app/components/forms/insert-transaction-form/transaction-form.component';
import { InsertCategoryFormComponent } from 'src/app/components/forms/insert-category-form/insert-category-form.component';
import { InsertPersonFormComponent } from 'src/app/components/forms/insert-person-form/insert-person-form.component';
import { InsertBudgetFormComponent } from 'src/app/components/forms/insert-budget-form/insert-budget-form.component';


@NgModule({
  declarations: [
    ElapsedBudgetGridComponent,
    DashboardComponent,
    CalendarComponent,
    TransactionFormComponent,
    TransactionGridComponent,
    InfoCardComponent,
    InsertCategoryFormComponent,
    InsertPersonFormComponent,
    InsertBudgetFormComponent
  ],
  imports: [
    RouterModule.forChild(UserLayoutRoutes),
    CommonModule,
    ReactiveFormsModule,
    HttpClientModule,
    AgGridModule.withComponents([]),
    FontAwesomeModule,
  ]
})
export class UserLayoutModule { }
