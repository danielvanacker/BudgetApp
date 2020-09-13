import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BaseUrlInterceptor } from './base-url-interceptor';
import { AppRoutes } from './app.routing';
import { RouterModule } from '@angular/router';
import { UserLayoutComponent } from './layouts/user-layout/user-layout.component';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    UserLayoutComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(AppRoutes, {useHash: true}),
    HttpClientModule,
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: BaseUrlInterceptor, multi: true }],
  bootstrap: [AppComponent]
})
export class AppModule { }
