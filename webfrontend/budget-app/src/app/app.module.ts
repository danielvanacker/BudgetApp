import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuBarComponent } from './shared/menu-bar/menu-bar.component';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { TransactionFormComponent } from './components/transaction-form/transaction-form.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BaseUrlInterceptor } from './base-url-interceptor';
import { TransactionGridComponent } from './components/ag-grid/transaction-grid/transaction-grid.component';
import { AgGridModule } from 'ag-grid-angular';

@NgModule({
  declarations: [
    AppComponent,
    MenuBarComponent,
    DashboardComponent,
    TransactionFormComponent,
    TransactionGridComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    ReactiveFormsModule,
    HttpClientModule,
    AgGridModule.withComponents([]),
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: BaseUrlInterceptor, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule { }
