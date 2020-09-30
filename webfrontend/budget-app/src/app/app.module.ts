import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { SidebarComponent } from './components/sidebar/sidebar.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { BaseUrlInterceptor, TokenInterceptor } from './interceptors';
import { AppRoutes } from './app.routing';
import { RouterModule } from '@angular/router';
import { UserLayoutComponent } from './layouts/user-layout/user-layout.component';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { LoginComponent } from './pages/login/login.component';
import { AuthGuard } from './auth.guard';
import { AuthService } from './services/auth.service';

@NgModule({
  declarations: [
    AppComponent,
    SidebarComponent,
    UserLayoutComponent,
    LoginComponent,
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(AppRoutes, {useHash: true}),
    HttpClientModule,
    FontAwesomeModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: BaseUrlInterceptor, multi: true },
    { provide: HTTP_INTERCEPTORS, useClass: TokenInterceptor, multi: true },
    AuthGuard,
    AuthService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
