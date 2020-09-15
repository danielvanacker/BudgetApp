import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AgGridModule } from 'ag-grid-angular';
import { DashboardComponent } from 'src/app/pages/dashboard/dashboard.component';
import { TransactionFormComponent } from 'src/app/components/transaction-form/transaction-form.component';
import { TransactionGridComponent } from 'src/app/components/ag-grid/transaction-grid/transaction-grid.component';
import { RouterModule } from '@angular/router';
import { UserLayoutRoutes } from './user-layout.routing';
import { CalendarComponent } from 'src/app/pages/calendar/calendar.component';
import { InfoCardComponent } from 'src/app/components/info-card/info-card.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';



@NgModule({
  declarations: [
    DashboardComponent,
    CalendarComponent,
    TransactionFormComponent,
    TransactionGridComponent,
    InfoCardComponent,
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
